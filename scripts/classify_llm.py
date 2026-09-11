# -*- coding: utf-8 -*-
"""LLM 逐卡判读的**生产管线**：出题 → 收卷 → 校验 → 出表。

用法：
    python scripts/classify_llm.py packets [--per 25]     # 生成判读包
    python scripts/classify_llm.py collect                # 收卷 + 校验 + 写 classification.json
    python scripts/classify_llm.py check                  # 只校验，不改文件
    python scripts/classify_llm.py merge <文件> ...        # 把某个判读输出并进来

判读输出格式（每张卡一行，四栏）：
    sk-0123 | A5 | 中心主张：…… | 原文依据：……
    sk-0456 | SPLIT | 中心主张：A / B | 原文依据：……
    sk-0789 | NONE  | 中心主张：原文无判断 | 原文依据：……

**为什么强制「中心主张 + 原文依据」**：这是外部评审给的要求
（「最终分类必须提交中心主张＋原文证据＋适用判据」），也是关键词方法做不到的事。
收卷时会做一条硬校验：**「原文依据」必须真的出现在该卡的原文摘录或转述里**——
对不上就判为编造，计入失败清单，不许入库。
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from taxonomy import load_spec  # noqa: E402

WORK = ROOT / "local_working_copy" / "llm-classify"
WORK.mkdir(parents=True, exist_ok=True)
RESULT = ROOT / "classification.json"
SPEC_FOR_JUDGE = ROOT / "docs" / "audit" / "SPEC-FOR-JUDGE.md"

LINE_RE = re.compile(r"^(sk-\d{4})\s*\|\s*(\S+)\s*\|\s*中心主张：(.*?)\s*\|\s*原文依据：(.*?)\s*$")


def cards() -> list[dict]:
    return json.load(open(ROOT / "web" / "data.json", encoding="utf-8"))["cards"]


def texts(c: dict) -> str:
    exc = (c.get("excerpts") or [""])[0]
    return (c.get("title", "") + "\n" + exc + "\n" + (c.get("cn") or ""))


def cmd_packets(per: int = 25):
    spec = load_spec()
    essays = [c for c in cards() if c["type"] != "case"]
    essays.sort(key=lambda c: c["id"])
    n = 0
    for i in range(0, len(essays), per):
        chunk = essays[i:i + per]
        n += 1
        L = [f"# 分类判读 · 第 {n} 包（{len(chunk)} 张）", ""]
        for c in chunk:
            L += [f"## {c['id']}", "",
                  f"**标题**：{c.get('title', '')}", "",
                  f"**原文摘录**：{(c.get('excerpts') or [''])[0]}", "",
                  f"**编辑转述**：{c.get('cn') or ''}", "",
                  f"**出处**：{c.get('ref') or ''}", ""]
        (WORK / f"batch-{n:02d}.md").write_text("\n".join(L), encoding="utf-8")
    print(f"共 {len(essays)} 张论述卡 → {n} 个判读包（每包 {per} 张）在 {WORK}")
    print(f"判读规格请用：{SPEC_FOR_JUDGE}")


def parse(path: Path) -> tuple[dict, list[str]]:
    got, bad = {}, []
    for ln, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line or not line.startswith("sk-"):
            continue
        m = LINE_RE.match(line)
        if not m:
            bad.append(f"{path.name}:{ln} 格式不符：{line[:70]}")
            continue
        cid, eid, claim, ev = m.groups()
        got[cid] = {"entry": eid.strip(), "claim": claim.strip(), "evidence": ev.strip(),
                    "from": path.name}
    return got, bad


def cmd_collect(write: bool = True):
    spec = load_spec()
    entry = {e["id"]: e for e in spec["entries"]}
    valid = {e["id"] for e in spec["entries"] if not e["tag"]}
    byid = {c["id"]: c for c in cards()}
    essays = [c for c in cards() if c["type"] != "case"]

    merged, bad = {}, []
    files = sorted(WORK.glob("out-*.txt")) + sorted(WORK.glob("batch-*.out.txt"))
    for f in files:
        g, b = parse(f)
        bad += b
        for k, v in g.items():
            if k in merged and merged[k]["entry"] != v["entry"]:
                bad.append(f"{k} 两次判读不一致：{merged[k]['entry']} vs {v['entry']}")
            merged[k] = v

    print(f"收卷：{len(merged)}/{len(essays)} 张　来源 {len(files)} 个文件")
    if len(merged) < len(essays):
        miss = [c["id"] for c in essays if c["id"] not in merged]
        print(f"⚠ 缺 {len(miss)} 张：{miss[:12]}{' …' if len(miss) > 12 else ''}")

    # 硬校验 1：条目编号合法
    illegal = [k for k, v in merged.items() if v["entry"] not in valid | {"SPLIT", "NONE"}]
    # 硬校验 2：**原文依据必须真的在卡里**（抓编造）
    fake = []
    for k, v in merged.items():
        if v["entry"] == "NONE":
            continue
        ev = re.sub(r"[「」“”\"'\s]", "", v["evidence"])
        src = re.sub(r"[「」“”\"'\s]", "", texts(byid[k]))
        key = ev[:14] if len(ev) >= 14 else ev
        if key and key not in src:
            fake.append((k, v["evidence"][:40]))
    # 硬校验 3：证据太短（没有说服力）
    short = [k for k, v in merged.items()
             if v["entry"] not in ("NONE",) and len(v["evidence"]) < 8]

    print(f"\n条目编号非法：{len(illegal)} {illegal[:8]}")
    print(f"原文依据对不上原文（疑似编造）：{len(fake)}")
    for k, e in fake[:10]:
        print(f"    {k}　「{e}」")
    print(f"原文依据过短（<8 字）：{len(short)} {short[:8]}")
    print(f"格式错误行：{len(bad)}")
    for b in bad[:8]:
        print(f"    {b}")

    kinds = {}
    for v in merged.values():
        kinds[v["entry"]] = kinds.get(v["entry"], 0) + 1
    print("\n分布：" + " · ".join(
        f"{k} {v}" for k, v in sorted(kinds.items(), key=lambda x: -x[1])))
    print(f"其中 SPLIT {kinds.get('SPLIT', 0)} · NONE {kinds.get('NONE', 0)}")

    if write and len(merged) == len(essays) and not illegal and not fake:
        out = {c["id"]: {"primary": merged[c["id"]]["entry"],
                         "claim": merged[c["id"]]["claim"],
                         "evidence": merged[c["id"]]["evidence"],
                         "title": c.get("title", ""),
                         "old_topics": c.get("topics", []),
                         "type": c["type"]}
               for c in essays if c["id"] in merged}
        for c in cards():
            if c["type"] == "case":
                out[c["id"]] = {"primary": None, "type": "case",
                                "title": c.get("title", ""),
                                "old_topics": c.get("topics", [])}
        RESULT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"\n已写入 {RESULT}（{len(out)} 张）")
    elif write:
        print("\n⚠ 有校验未通过，**未写文件**。先修干净再写。")


def cmd_merge(argv: list[str]):
    n = 0
    for i, a in enumerate(argv):
        src = Path(a)
        (WORK / f"out-{src.stem}.txt").write_text(src.read_text(encoding="utf-8"),
                                                  encoding="utf-8")
        n += 1
    print(f"并入 {n} 个判读输出")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    if cmd == "packets":
        per = 25
        if "--per" in sys.argv:
            per = int(sys.argv[sys.argv.index("--per") + 1])
        cmd_packets(per)
    elif cmd == "collect":
        cmd_collect(write=True)
    elif cmd == "merge":
        cmd_merge(sys.argv[2:])
    else:
        cmd_collect(write=False)

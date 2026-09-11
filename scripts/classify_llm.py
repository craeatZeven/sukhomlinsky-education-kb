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

LINE_RE = re.compile(
    r"^(sk-\d{4})\s*\|\s*(\S+)\s*\|\s*(?:参见：\s*(.*?)\s*\|\s*)?中心主张：(.*?)\s*\|\s*原文依据：(.*?)\s*$")

VALID_EXTRA = {"SPLIT", "NONE"}
SEP = re.compile(r"[,，、]")


def _split_see(cell: str) -> list[str]:
    if cell is None:
        return []
    return [x.strip() for x in SEP.split(cell)
            if x.strip() and x.strip() not in ("—", "-", "无", "None")]


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
        cid, eid, see, claim, ev = m.groups()
        got[cid] = {"entry": eid.strip(), "see": _split_see(see),
                    "claim": claim.strip(), "evidence": ev.strip(), "from": path.name}
    return got, bad


def norm_txt(s: str) -> str:
    return re.sub(r"[\s「」“”\"'，。、；：…—·（）()【】\[\]!？?!,.;:-]", "", s)


def evidence_match(evidence: str, text: str, n: int = 4, need: float = 0.7) -> tuple[bool, float]:
    """判读给的「原文依据」是否真的出自这张卡。

    **不能用精确子串匹配**：语料是 OCR 来的，错字不少
    （实测有「自已」应为「自己」、「就足是」应为「就是要」、「对白已」应为「对自己」）。
    精确匹配会把真引文判成编造。这里改用 n-gram 覆盖率：
    把依据切成 4 字窗口，看有多大比例能在卡片文字里找到；≥70% 即算通过。
    """
    e, t = norm_txt(evidence), norm_txt(text)
    if len(e) < n:
        return (e in t if e else False), (1.0 if e and e in t else 0.0)
    grams = [e[i:i + n] for i in range(len(e) - n + 1)]
    hit = sum(1 for g in grams if g in t)
    r = hit / len(grams)
    return r >= need, r


def cmd_collect(write: bool = True):
    spec = load_spec()
    entry = {e["id"]: e for e in spec["entries"]}
    valid = {e["id"] for e in spec["entries"] if not e["tag"]}
    byid = {c["id"]: c for c in cards()}
    essays = [c for c in cards() if c["type"] != "case"]

    merged, bad, conflicts = {}, [], []
    # v2/ 放「主归属 + 参见」那一轮的输出，最后处理，覆盖只有主归属的 v1
    files = (sorted(WORK.glob("out-*.txt")) + sorted(WORK.glob("*.out.txt"))
             + sorted(WORK.glob("v2/*.out.txt")))
    for f in files:
        g, b = parse(f)
        bad += b
        for k, v in g.items():
            if k in merged and merged[k]["entry"] != v["entry"]:
                conflicts.append((k, merged[k]["entry"], v["entry"],
                                  merged[k].get("from", ""), v["from"]))
            merged[k] = v

    print(f"收卷：{len(merged)}/{len(essays)} 张　来源 {len(files)} 个文件")
    if len(merged) < len(essays):
        miss = [c["id"] for c in essays if c["id"] not in merged]
        print(f"⚠ 缺 {len(miss)} 张：{miss[:12]}{' …' if len(miss) > 12 else ''}")

    illegal = [k for k, v in merged.items() if v["entry"] not in valid | {"SPLIT", "NONE"}]
    fake, ratios = [], []
    for k, v in merged.items():
        if v["entry"] == "NONE":
            continue
        ok, r = evidence_match(v["evidence"], texts(byid[k]))
        ratios.append(r)
        if not ok:
            fake.append((k, round(r, 2), v["evidence"][:40]))
    short = [k for k, v in merged.items()
             if v["entry"] not in ("NONE",) and len(v["evidence"]) < 8]

    print(f"\n条目编号非法：{len(illegal)} {illegal[:8]}")
    ok_n = len(ratios) - len(fake)
    print(f"原文依据能对上原文：{ok_n}/{len(ratios)}"
          f"（{ok_n / len(ratios) * 100:.1f}%）" if ratios else "原文依据：无")
    for k, r, e in fake[:10]:
        print(f"    对不上（覆盖率 {r}）{k}：「{e}」")
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
        write_review(out, entry, conflicts)
    elif write:
        print("\n⚠ 有校验未通过，**未写文件**。先修干净再写。")


def write_review(out: dict, entry: dict, conflicts: list | None = None):
    """出人工复核清单：SPLIT（待拆分）/ NONE（无主张）/ 两次判读不一致 / 与人工裁定表冲突。"""
    spec = load_spec()
    byid = {c["id"]: c for c in cards()}
    split = [k for k, v in out.items() if v.get("primary") == "SPLIT"]
    none_ = [k for k, v in out.items() if v.get("primary") == "NONE"]
    over = spec.get("override", {})
    conflict = [(k, over[k]["primary"], out[k].get("primary"))
                for k in out if k in over and out[k].get("primary") not in (None, over[k]["primary"])]
    L = ["# LLM 逐卡判读 · 人工复核清单", "",
         "> 由 `python scripts/classify_llm.py collect` 生成。判读记录见 `classification.json`。", "",
         f"## 一、待拆分 SPLIT（{len(split)} 张）", "",
         "原文有两个真正并列、无可见主次的主张——按元规则不强行破平局，需人工决定拆卡或选一个。", ""]
    for k in sorted(split):
        c = byid.get(k, {})
        L += [f"- **{k}　{c.get('title', '')}**",
              f"  - 主张：{out[k].get('claim', '')}",
              f"  - 依据：{out[k].get('evidence', '')}"]
    L += ["", f"## 二、无主张 NONE（{len(none_)} 张）", "",
          "原文摘录本身不构成判断或要求（纯写景 / 纯叙述 / 残句）。这些卡可能要补原文摘录，"
          "或本来就该留在故事域。", ""]
    for k in sorted(none_):
        c = byid.get(k, {})
        L += [f"- **{k}　{c.get('title', '')}**　依据：{out[k].get('evidence', '')}"]
    conflicts = conflicts or []
    if conflicts:
        L += ["", f"## 三、同一张卡两次判读不一致（{len(conflicts)} 张）", "",
              "这些卡被独立判读了两次（催办时重复投递），两次给出不同条目。"
              "**没有静默取其中一个**——两条都记下来，由人决定。"
              "这类卡正是「边界本来就模糊」的证据。", "",
              "| 卡片 | 标题 | 判读 A | 判读 B |", "|---|---|---|---|"]
        for k, a, b, fa, fb in sorted(conflicts):
            L.append(f"| {k} | {byid.get(k, {}).get('title', '')[:30]} | {a} | {b} |")
    L += ["", f"## 四、与人工裁定表冲突（{len(conflict)} 张）", "",
          "`taxonomy.md` §六 登记的人工裁定优先于算法。这里是判读与裁定不一致的卡——"
          "要么裁定过时了，要么判读错了，都要人看一眼。", "",
          "| 卡片 | 标题 | 人工裁定 | 本次判读 |", "|---|---|---|---|"]
    for k, manual, got in sorted(conflict):
        L.append(f"| {k} | {byid.get(k, {}).get('title', '')[:30]} | {manual} | {got} |")
    dst = ROOT / "docs" / "classification-llm-review.md"
    dst.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"已写入 {dst}（SPLIT {len(split)} · NONE {len(none_)} · 冲突 {len(conflict)}）")


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

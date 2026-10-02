# -*- coding: utf-8 -*-
"""规格段落卡检查点（A 模式）——把 docs/content-growth-loop.md §十二 的流程固化下来。

用法：D:\python\python.exe scripts/checkpoint_specs.py [--land]
  不带 --land：只审计（dry-run + 字数），报告哪些可落、哪些要作废。
  带 --land：审计通过的批次按 §十二 五步落地（重分配 id -> 查重 -> apply -> rebuild -> validate
            -> commit -> push -> 线上验收 -> 归档）。

设计原则：**审计失败即阻断**（绝不出现"审计崩了但照落"）。
"""
import io, json, os, re, subprocess, sys, time, urllib.request

W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = r"D:\python\python.exe"
GIT = r"D:\Dev\Git\cmd\git.exe"
S = os.path.join(W, "local_working_copy", "subagent-specs")
LOC = os.path.join(W, "local_working_copy", "fulltext", "card-locators.jsonl")
TOOL = os.path.join(W, "scripts", "new_cards_from_spec.py")
LAND = "--land" in sys.argv


def sh(args, cwd=W):
    r = subprocess.run(args, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def max_id():
    mx = 0
    for n in os.listdir(os.path.join(W, "cards")):
        m = re.match(r"^sk-(\d+)(?:-.*)?\.md$", n)
        if m:
            mx = max(mx, int(m.group(1)))
    return mx


def carded():
    out = set()
    for ln in io.open(LOC, encoding="utf-8"):
        if ln.strip():
            d = json.loads(ln)
            if d.get("section"):
                out.add((str(d.get("book")), str(d.get("section"))))
    return out


def move_to(sub, *paths):
    d = os.path.join(S, sub)
    os.makedirs(d, exist_ok=True)
    for p in paths:
        if os.path.exists(p):
            os.replace(p, os.path.join(d, os.path.basename(p)))


def main():
    pend = sorted([f for f in os.listdir(S) if f.endswith(".json") and f.startswith("batch")])
    print("待处理规格：%d 个" % len(pend))
    if not pend:
        print("无新规格 -> 本轮不落卡")
        return 0
    CARDED = carded()
    ready, void, dup = [], [], 0
    for fn in pend:
        p = os.path.join(S, fn)
        code, out = sh([PY, TOOL, os.path.relpath(p, W)])
        lens = [int(x) for x in re.findall(r"｜(\d+) 字｜", out)]
        bad = [n for n in lens if n < 90 or n > 250]
        items = []
        try:
            data = json.load(io.open(p, encoding="utf-8"))
            if isinstance(data, list): items = data
        except Exception:
            pass
        key = (str(items[0].get("book")), str(items[0].get("section"))) if items else ("", "")
        print("  %-58s exit=%d 条=%d 越界=%d" % (fn[:58], code, len(lens), len(bad)))
        if code != 0 or bad or not lens:
            note = os.path.join(S, "_void", fn + ".VOID.md")
            os.makedirs(os.path.join(S, "_void"), exist_ok=True)
            io.open(note, "w", encoding="utf-8", newline="\n").write(
                "# 作废（检查点自动判定）\n\ndry-run exit=%d｜字数越界 %s\n\n%s\n" % (code, bad, out.strip()[-800:]))
            void.append(fn)
            continue
        if key in CARDED:
            print("     -> 该章已产卡（%s / %s），整批不落" % (key[0][:14], key[1][:24]))
            dup += 1
            continue
        ready.append((fn, p, items))
    if not LAND:
        print("\n审计结论：可落 %d｜作废 %d｜章节重复 %d（未加 --land，不改仓库）" % (len(ready), len(void), dup))
        return 0
    if not ready:
        print("\n无可落批次。")
        return 0
    # --- 落地：先统一重分配 id（避免跨批撞车，见 §十一）---
    nxt = max_id() + 1
    first_ids = []
    for fn, p, items in ready:
        for it in items:
            it["id"] = "sk-%d" % nxt
            nxt += 1
        io.open(p, "w", encoding="utf-8", newline="\n").write(json.dumps(items, ensure_ascii=False, indent=1))
        first_ids.append((fn, len(items)))
    print("\n重分配 id 后开始落卡，共 %d 张" % sum(n for _, n in first_ids))
    for fn, p, items in ready:
        code, out = sh([PY, TOOL, os.path.relpath(p, W), "--apply"])
        print("  apply %s -> exit=%d" % (fn[:40], code))
        if code != 0:
            print("  **apply 失败，中止**：" + out[-300:])
            return 1
    code, out = sh([PY, os.path.join(W, "scripts", "rebuild_index.py")])
    print("  rebuild: " + out.strip().splitlines()[-1][:80] if out.strip() else "  rebuild: ?")
    code, out = sh([PY, os.path.join(W, "scripts", "validate_all.py")])
    tail = [l for l in out.strip().splitlines() if l.strip()][-2:]
    print("  validate_all: " + " / ".join(t.strip()[:40] for t in tail))
    if "ALL OK" not in out:
        print("  **validate_all 未通过，中止（未提交）**")
        return 1
    msg = "落卡 %d 张（规格段检查点自动落）：审计通过" % sum(n for _, n in first_ids)
    sh([GIT, "add", "cards/", "classification.json", "INDEX.md", "web/", "docs/"])
    code, out = sh([GIT, "-c", "i18n.commitEncoding=utf-8", "commit", "-q", "-m", msg])
    code, out = sh([GIT, "log", "--oneline", "-1"])
    print("  提交：" + out.strip()[:90])
    code, out = sh([GIT, "push"])
    print("  push exit=%d" % code)
    for fn, p, items in ready:
        move_to("_landed", p, p.replace(".json", ".NOTE.md"))
    print("  已归档 _landed/")
    # 线上验收
    time.sleep(110)
    try:
        base = "https://craeatzeven.github.io/sukhomlinsky-education-kb/web/data/"
        ids = json.loads(urllib.request.urlopen(base + "ids.json", timeout=30).read().decode("utf-8"))
        print("  线上 ids：%d" % len(ids))
    except Exception as e:
        print("  线上取不到：" + str(e)[:80])
    return 0


if __name__ == "__main__":
    sys.exit(main())
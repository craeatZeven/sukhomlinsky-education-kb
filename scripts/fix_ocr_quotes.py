# -*- coding: utf-8 -*-
"""把这 101 张卡的引文与语料原文对齐，用 OCR 原字校正讹字。默认 dry-run，--apply 才写。"""
import io, os, re, sys, json, difflib, sqlite3
W = r"D:\Work\sukhomlinsky-education-kb"
CD = os.path.join(W, "cards")
RP = os.path.join(W, "local_working_copy", "review-packs")
APPLY = "--apply" in sys.argv
Q = (0x300C, 0x300D, 0x201C, 0x201D, 0x2018, 0x2019, 0x22, 0x27)
def norm_map(s):
    out, imap = [], []
    for i, ch in enumerate(s):
        if ch.isspace() or ord(ch) in Q: continue
        if ch in "\u2014\u2013": ch = "-"
        out.append(ch); imap.append(i)
    return "".join(out), imap
CONN = sqlite3.connect(os.path.join(W, "local_working_copy", "fulltext", "corpus.db"))
CONN.row_factory = sqlite3.Row
bybook = {}
for r in CONN.execute("SELECT book, text FROM units"):
    bybook.setdefault(r["book"], []).append(r["text"])
# slug -> unit 表里的真实 book 名（借 locator 的 book 字段）
BOOKMAP = {}
for _l in io.open(os.path.join(W, "local_working_copy", "fulltext", "card-locators.jsonl"), encoding="utf-8"):
    if not _l.strip(): continue
    try: _r = json.loads(_l)
    except Exception: continue
    _b = str(_r.get("book") or "")
    if _b: BOOKMAP[str(_r.get("card"))] = _b
must = [l.split(chr(9))[0] for l in io.open(os.path.join(RP, "must-fix.tsv"), encoding="utf-8") if l.strip() and not l.startswith("card_id")]
ok, skip, changes = [], [], []
for cid in must:
    fs = [f for f in os.listdir(CD) if f.startswith(cid + "-")]
    if not fs: continue
    p = os.path.join(CD, fs[0])
    t = io.open(p, encoding="utf-8", errors="replace").read()
    m = re.search(r"^source:\s*(\S+)", t, re.M)
    src = m.group(1) if m else ""
    # 2026-10-20 修正：卡上的 source 是 slug，unit 表里 book 是全名 -> 用 locator 映射
    src = BOOKMAP.get(cid, src)
    raw = [x for x in t.splitlines() if x.startswith("> ")]
    if not raw: continue
    quote = "".join(x[2:].strip() for x in raw)
    qn, _ = norm_map(quote)
    best = None
    for u in bybook.get(src, []):
        un, imap = norm_map(u)
        if not un: continue
        sm = difflib.SequenceMatcher(None, qn, un, autojunk=False)
        blocks = sm.get_matching_blocks()
        cover = sum(b.size for b in blocks) / max(1, len(qn))
        if cover < 0.55: continue
        a = blocks[0].b; b = blocks[-2].b + blocks[-2].size if len(blocks) > 1 else a
        if a >= b: continue
        span = u[imap[a]:imap[b - 1] + 1]
        if best is None or cover > best[0]: best = (cover, span)
    if not best or not (60 <= len(best[1]) <= 320):
        skip.append((cid, "对齐失败或长度不合适", best[0] if best else 0)); continue
    newq = best[1].strip()
    nd = sum(1 for x, y in zip(quote, newq) if x != y) + abs(len(quote) - len(newq))
    ok.append((cid, p, quote, newq, round(best[0] * 100)))
    if newq != quote: changes.append((cid, nd))
print("对齐成功 %d 张｜需改写 %d 张｜跳过 %d 张" % (len(ok), len(changes), len(skip)))
if changes:
    tot = sum(c[1] for c in changes)
    print("累计改动字符数约 %d（平均每张 %.1f）" % (tot, tot / len(changes)))
print()
print("=== 示例（前 3 张）")
for cid, p, old, new, cov in ok[:3]:
    print("%s｜覆盖 %d%%｜%d 字 -> %d 字" % (cid, cov, len(old), len(new)))
    print("   原：%s" % old[:60])
    print("   新：%s" % new[:60])
if skip:
    print()
    print("=== 跳过（需人判）")
    for s in skip[:8]: print("  %s｜%s（覆盖 %.0f%%）" % (s[0], s[1], s[2] * 100))
if APPLY:
    n = 0
    for cid, p, old, new, cov in ok:
        if old == new: continue
        t = io.open(p, encoding="utf-8").read()
        lines = t.splitlines(); out = []; done = False
        for ln in lines:
            if ln.startswith("> "):
                if not done: out.append("> " + new); done = True
                continue
            out.append(ln)
        io.open(p, "w", encoding="utf-8", newline=chr(10)).write(chr(10).join(out) + chr(10))
        n += 1
    print()
    print("已写入 %d 张卡" % n)
else:
    print()
    print("（dry-run）加 --apply 才写盘")
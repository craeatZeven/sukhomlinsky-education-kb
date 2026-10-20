# -*- coding: utf-8 -*-
"""引文机器预筛：把每张 pending 卡的引文拿回原文里回找，分四档。
EXACT=原文逐字可寻（低风险）；NEAR=疑似 OCR 差异（>=80% 的 10 字窗命中）；
PARTIAL=部分命中（40~80%，可能引文被编辑过或定位错）；MISS=基本找不到（必改）。"""
import io, os, re, json, sqlite3, collections
W = r"D:\Work\sukhomlinsky-education-kb"
CD = os.path.join(W, "cards")
CONN = sqlite3.connect(os.path.join(W, "local_working_copy", "fulltext", "corpus.db"))
CONN.row_factory = sqlite3.Row
QUOTES = (0x300C, 0x300D, 0x201C, 0x201D, 0x2018, 0x2019, 0x22, 0x27, 0x300A, 0x300B)
def norm(s):
    s = s or ""
    s = s.replace(chr(0x2014), chr(45)).replace(chr(0x2013), chr(45))
    for cp in QUOTES:
        s = s.replace(chr(cp), "")
    return re.sub(r"\s+", "", s)
loc = {}
for l in io.open(os.path.join(W, "local_working_copy", "fulltext", "card-locators.jsonl"), encoding="utf-8"):
    if not l.strip(): continue
    try: r = json.loads(l)
    except Exception: continue
    loc[str(r.get("card"))] = str(r.get("unit") or "")
units = {}
for r in CONN.execute("SELECT unit_id, text FROM units"):
    units[r["unit_id"]] = r["text"]
rows = []
tally = collections.Counter()
for fn in sorted(os.listdir(CD)):
    if not (fn.startswith("sk-") and fn.endswith(".md")): continue
    t = io.open(os.path.join(CD, fn), encoding="utf-8", errors="replace").read()
    if "pending" not in t: continue
    m0 = re.match(r"(sk-\d+)", fn)
    if not m0: continue
    cid = m0.group(1)
    # 2026-10-20 修：卡片里的 `> 说明：` / `> 校勘：` 是编者按，不是引文正文。
    # 不剔除它们会把覆盖率算低（实测 265/518 张受影响，剔后 0.700 -> 0.972）。
    _ql = []
    for _l in t.splitlines():
        if not _l.startswith(">"): continue
        _s = _l.lstrip("> ").strip()
        if _s.startswith("说明") or _s.startswith("校勘") or _s.startswith("注"): continue
        _ql.append(_s)
    q = "".join(_ql)
    uid = loc.get(cid, "")
    ut = units.get(uid)
    if not ut or not q:
        rows.append((cid, "NO_UNIT_OR_QUOTE", 0, len(q), uid)); tally["NO_UNIT_OR_QUOTE"] += 1; continue
    qn, un = norm(q), norm(ut)
    if qn and qn in un:
        rows.append((cid, "EXACT", 1.0, len(q), uid)); tally["EXACT"] += 1; continue
    wid = 10
    tot = max(1, len(qn) - wid + 1)
    hit = sum(1 for i in range(tot) if qn[i:i + wid] in un)
    cover = hit / tot
    verdict = "NEAR" if cover >= 0.8 else ("PARTIAL" if cover >= 0.4 else "MISS")
    rows.append((cid, verdict, round(cover, 3), len(q), uid)); tally[verdict] += 1
od = os.path.join(W, "local_working_copy", "review-packs")
os.makedirs(od, exist_ok=True)
with io.open(os.path.join(od, "prescreen.tsv"), "w", encoding="utf-8", newline=chr(10)) as fh:
    fh.write("card_id\tverdict\tcover\tquote_len\tunit" + chr(10))
    for r in rows: fh.write("%s\t%s\t%s\t%d\t%s" % r + chr(10))
print("预筛卡片：%d 张 -> local_working_copy/review-packs/prescreen.tsv" % len(rows))
for k, v in tally.most_common(): print("  %-16s %4d" % (k, v))
miss = [r[0] for r in rows if r[1] in ("MISS", "PARTIAL", "NO_UNIT_OR_QUOTE")]
print("优先人看（MISS/PARTIAL/无定位）：%d 张" % len(miss))
print("  前 12 个：%s" % ", ".join(miss[:12]))
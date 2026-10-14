# -*- coding: utf-8 -*-
"""英译本平行层：跨语言锚点对齐（年份/四位数字/拉丁专名）。
为什么不用引注编号：实测 on-education / each-one-must-shine / To Children 前 60 unit 带引注特征 0/60。
锚点 = 语言无关的数字与专名（中译里人名是汉字，配不上，所以只靠数字 + 两侧共现的拉丁串）。"""
import sqlite3, os, re, collections, json
W = r"D:\Work\sukhomlinsky-education-kb"
conn = sqlite3.connect(os.path.join(W, "local_working_copy", "fulltext", "corpus.db"))
conn.row_factory = sqlite3.Row
def anchors(t):
    a = set(re.findall(r"\b(1[5-9]\d{2}|20\d{2})\b", t or ""))
    a |= set(w.lower() for w in re.findall(r"\b[A-Z][a-z]{4,}\b", t or ""))
    for s in ("Sukhomlinsky", "Pavlysh", "Makarenko", "Korczak", "Ukraine", "Kiev", "Moscow", "Soviet"): a.discard(s.lower())
    return a
EN, ZH = "To Children I Give My Heart", "ba-xin-xian-gei-hai-zi-zh"
en = [(r["unit_id"], anchors(r["text"])) for r in conn.execute("SELECT unit_id, text FROM units WHERE book=?", (EN,))]
zh = [(r["unit_id"], anchors(r["text"])) for r in conn.execute("SELECT unit_id, text FROM units WHERE book=?", (ZH,))]
print("英译本 %s：%d unit（有锚点 %d）" % (EN, len(en), sum(1 for _, a in en if a)))
print("中文源 %s：%d unit（有锚点 %d）" % (ZH, len(zh), sum(1 for _, a in zh if a)))
df = collections.Counter()
for _, a in en:
    for x in a: df[x] += 1
rare = [x for x, c in df.items() if c <= 3 and len(x) == 4 and x.isdigit()]
print("英译本里的【稀有年份】（<=3 次）：%s" % ", ".join(sorted(rare)[:12]))
pairs = []
for uid, a in en:
    rr = [x for x in a if x in rare]
    if not rr: continue
    for zid, za in zh:
        if set(rr) & za: pairs.append((uid, zid, sorted(set(rr) & za)))
print("按稀有年份得到的候选平行对：%d" % len(pairs))
for p in pairs[:8]: print("   %s  <->  %s   共现 %s" % (p[0], p[1], p[2]))
od = os.path.join(W, "local_working_copy", "parallel-en")
os.makedirs(od, exist_ok=True)
with open(os.path.join(od, "anchor-pairs.json"), "w", encoding="utf-8") as fh:
    json.dump([{"en": a, "zh": b, "anchors": c} for a, b, c in pairs], fh, ensure_ascii=False, indent=1)
print("候选对已写：local_working_copy/parallel-en/anchor-pairs.json")
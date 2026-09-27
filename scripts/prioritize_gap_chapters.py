# -*- coding: utf-8 -*-
"""缺口章优先级：用可测代理剔除「不值得成卡」的章。

判据（都可机检，不靠印象）：
  1) 非正文：章名含 注释/前言/序/目录/附录/编后/译后/版权/书名/目 次
  2) 他人评述：章开头 3 个 unit 内出现「著」类署名行（例：「阿·泽韦林著」）
  3) 论断密度低：含 我认为/应该/必须/不能/正是/意味着/首先/教育者 等词的 unit 占比 < 15%
     —— 这类章几乎全是课程描述、设备清单、叙事，成卡价值低
其余按「未被引用的 unit 数 × 论断密度」排序。
"""
import sqlite3, io, json, os, re, collections
ROOT = r"D:\Git\sukhomlinsky-education-kb"
c = sqlite3.connect(os.path.join(ROOT, "local_working_copy", "fulltext", "corpus.db")); c.row_factory = sqlite3.Row
loc = [json.loads(x) for x in io.open(os.path.join(ROOT, "local_working_copy", "fulltext", "card-locators.jsonl"), encoding="utf-8") if x.strip()]
ALIAS = {"xuan-ji-zh-vol1":"选集（五卷本）第1卷","xuan-ji-zh-vol2":"选集(五卷本)第2卷","xuan-ji-zh-vol3":"选集（五卷本）第3卷",
         "xuan-ji-zh-vol4":"选集(五卷本)第4卷","xuan-ji-zh-vol5":"选集（五卷本）第5卷","zuo-ren-de-gu-shi-zh":"做人的故事",
         "gei-jiao-shi-de-jian-yi-zh":"给教师的建议","ba-xin-xian-gei-hai-zi-zh":"ba-xin-xian-gei-hai-zi-zh"}
cited = collections.defaultdict(set)
for r in loc:
    if r.get("unit"): cited[str(r.get("book"))].add(r["unit"])
NONCONTENT = re.compile(r"注释|前 ?言|目录|目 ?次|附录|编后|译后|版权|书名|扉页|序 ?言|出版说明")
CLAIM = re.compile(r"我认为|我坚信|我深信|应该|必须|不能|正是|意味着|首先|教育者|教师应")
AUTHORSIGN = re.compile(r"著$|著[，,。]|（著）|编著")
rows = []
for slug, book in ALIAS.items():
    hit = cited.get(slug, set())
    us = list(c.execute("SELECT unit_id, section, text FROM units WHERE book=? ORDER BY unit_id", (book,)))
    by = collections.defaultdict(list)
    for u in us:
        by[u["section"] or "（无节名）"].append(u)
    for sec, lst in by.items():
        if len(lst) < 30: continue
        h = sum(1 for u in lst if u["unit_id"] in hit)
        if h > max(1, len(lst)//20): continue
        reason = None
        if NONCONTENT.search(sec): reason = "非正文"
        else:
            head = [re.sub(r"\s+","",u["text"] or "") for u in lst[:3]]
            if any(len(x) < 24 and AUTHORSIGN.search(x) for x in head): reason = "他人评述（署名行）"
        tot = len(lst)
        dens = sum(1 for u in lst if CLAIM.search(re.sub(r"\s+","",u["text"] or ""))) / float(tot)
        if not reason and dens < 0.15: reason = "论断密度低（%.0f%%）" % (dens*100)
        rows.append((tot - h, dens, book, sec, tot, h, reason))
good = [r for r in rows if not r[6]]
bad = [r for r in rows if r[6]]
good.sort(key=lambda r: -r[0]*r[1])
print("可补章（值得成卡）：%d｜不值得：%d｜合计 %d" % (len(good), len(bad), len(rows)))
print()
print("=== 优先级 Top 24（缺口 × 论断密度）")
for gap, dens, book, sec, tot, h, _ in good[:24]:
    print("   缺口 %4d｜密度 %3.0f%%｜%-20s 《%s》" % (gap, dens*100, book[:20], sec[:34]))
print()
print("=== 剔除示例（前 12）")
for gap, dens, book, sec, tot, h, why in bad[:12]:
    print("   缺口 %4d｜%-28s｜%s" % (gap, sec[:28], why))

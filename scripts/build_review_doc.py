# -*- coding: utf-8 -*-
"""把 must-fix.tsv 展开成人可核的对照文档（Markdown + TSV）。"""
import io, os, re, json, collections
W = r"D:\Work\sukhomlinsky-education-kb"
CD = os.path.join(W, "cards")
RP = os.path.join(W, "local_working_copy", "review-packs")
must = []
for l in io.open(os.path.join(RP, "must-fix.tsv"), encoding="utf-8"):
    p = l.rstrip().split(chr(9))
    if p and p[0] != "card_id": must.append(p[0])
print("must-fix 卡数：%d" % len(must))
cards = {}
for fn in os.listdir(CD):
    if not (fn.startswith("sk-") and fn.endswith(".md")): continue
    m = re.match(r"(sk-\d+)", fn)
    if not m: continue
    cid = m.group(1)
    if cid not in must: continue
    t = io.open(os.path.join(CD, fn), encoding="utf-8", errors="replace").read()
    def fm(k):
        mm = re.search(r"^" + k + r":\s*(.+)$", t, re.M)
        return mm.group(1).strip() if mm else ""
    ti = re.search(r"^#\s+(.+)$", t, re.M)
    q = "".join(x.lstrip("> ").strip() for x in t.splitlines() if x.startswith(">"))
    cards[cid] = {"title": ti.group(1).strip() if ti else "", "book": fm("source"), "ref": fm("ref"), "quote": q, "file": fn}
by_src = collections.defaultdict(list)
for cid in must:
    c = cards.get(cid)
    if c: by_src[c["book"]].append((cid, c))
md = []
md.append("# 引文人核清单 —— 机器在全书范围内都找不到引文的卡片（%d 张）" % len(cards))
md.append("")
md.append("> **为什么它们进了必看集**：机器把卡上的引文拿回**该卡所属书的全书文本**里逐字查找（10 字窗），命中率 < 40%；")
md.append("> 并且把同一段探针拿到**全库所有书**里再找一次，仍然找不到 → 可能是 ①错书 ②该段 OCR 严重讹变 ③引文被转述改写过 ④引文系误录。")
md.append("")
md.append("## 怎么核（每条只需 30 秒）")
md.append("")
md.append("在每条下面的三个方框里勾一个：")
md.append("- `□ 原书有` → 请在括号里写明**正确的卷/章/页**，我据此改定位")
md.append("- `□ 查无此句` → 该卡**删掉**（引文不可核 = 不可引用）")
md.append("- `□ 是转引` → 这句其实是别人（如马克思/马卡连柯）说的，请在括号写**真正出处**，我改归属")
md.append("")
md.append("---")
md.append("")
for src in sorted(by_src, key=lambda k: -len(by_src[k])):
    md.append("## 书：%s（%d 张）" % (src, len(by_src[src])))
    md.append("")
    for cid, c in sorted(by_src[src]):
        md.append("### %s ｜ %s" % (cid, c["title"]))
        md.append("")
        md.append("- 原书定位（卡上写的）：%s" % c["ref"])
        md.append("- 引文（%d 字）：" % len(c["quote"]))
        md.append("")
        md.append("  > " + c["quote"])
        md.append("")
        md.append("- 判定：□ 原书有（页：______）　□ 查无此句（删卡）　□ 是转引（真出处：______）")
        md.append("")
out_md = os.path.join(RP, "must-fix-review.md")
io.open(out_md, "w", encoding="utf-8", newline=chr(10)).write(chr(10).join(md) + chr(10))
print("已生成：local_working_copy/review-packs/must-fix-review.md（%d 张，按书分组）" % len(cards))
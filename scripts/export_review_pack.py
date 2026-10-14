# -*- coding: utf-8 -*-
"""引文人核包：把 reviewed_by 仍为 pending 的卡导出成人可逐条核对的两份文件（清单 + 明细）。"""
import io, os, re
W = r"D:\Work\sukhomlinsky-education-kb"
cd = os.path.join(W, "cards")
LIMIT = 120
items = []
for fn in sorted(os.listdir(cd), reverse=True):
    if not (fn.startswith("sk-") and fn.endswith(".md")): continue
    t = io.open(os.path.join(cd, fn), encoding="utf-8", errors="replace").read()
    if "paper check pending" not in t: continue
    cid = fn[:-3]
    def fm(key):
        m = re.search(r"^%s:\s*(.+)$" % key, t, re.M)
        return m.group(1).strip() if m else ""
    title = ""
    m = re.search(r"^#\s+(.+)$", t, re.M)
    if m: title = m.group(1).strip()
    quotes = [l.lstrip("> ").strip() for l in t.splitlines() if l.startswith(">") and l.strip("> ").strip()]
    quotes = [q for q in quotes if len(q) > 20]
    items.append({"id": cid, "title": title, "book": fm("book"), "section": fm("section"),
                  "page": fm("page"), "marker": fm("marker"), "relay": fm("relay"), "quote": (quotes[0] if quotes else "")})
total = len(items)
sel = items[:LIMIT]
od = os.path.join(W, "local_working_copy", "review-packs")
os.makedirs(od, exist_ok=True)
tsv = os.path.join(od, "review-pack-latest.tsv")
with io.open(tsv, "w", encoding="utf-8", newline=chr(10)) as fh:
    fh.write("card_id\tbook\tsection\tpage\tmarker\ttitle\tquote\t核对结论(填 pas/fix/删)\t备注" + chr(10))
    for it in sel:
        fh.write("\t".join([it["id"], it["book"], it["section"], it["page"], it["marker"], it["title"], it["quote"].replace("\t", " "), "", ""]) + chr(10))
md = os.path.join(od, "review-pack-latest.md")
with io.open(md, "w", encoding="utf-8", newline=chr(10)) as fh:
    fh.write("# 引文人核包（最近 %d 张，共 %d 张待核）" % (len(sel), total) + chr(10) + chr(10))
    fh.write("核对方法：对着原书该页看引文是否逐字一致。**结论填在 TSV 最后一列**：`pas` 一字不差 / `fix` 有小讹（写清）/ `删` 不该收。" + chr(10) + chr(10))
    cur = None
    for it in sel:
        if it["book"] != cur:
            cur = it["book"]; fh.write(chr(10) + "## " + (cur or "(无书名)") + chr(10) + chr(10))
        fh.write("- **%s** %s｜%s p%s｜锚点 `%s`" % (it["id"], it["title"], it["section"], it["page"], it["marker"]) + chr(10))
        fh.write("  > " + it["quote"][:200] + chr(10))
print("待核总数：%d｜本次导出：%d" % (total, len(sel)))
print("清单：local_working_copy/review-packs/review-pack-latest.tsv")
print("明细：local_working_copy/review-packs/review-pack-latest.md")
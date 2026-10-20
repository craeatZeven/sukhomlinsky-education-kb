# -*- coding: utf-8 -*-
"""从 sources/*.md 重新生成 web/cite.html 里的 BIB 对象字面量（单一数据源）。

cite.html 里 var BIB = { ... }; 是生成物，不要手改；改书目请改 sources/<slug>.md 再跑本脚本。
"""
import io, os, re, json, subprocess, sys

W = r"D:\Work\sukhomlinsky-education-kb"
SRC = os.path.join(W, "sources")
CITE = os.path.join(W, "web", "cite.html")

def fval(d, k):
    return (d.get(k) or "").strip()

bib = {}
for fn in sorted(os.listdir(SRC)):
    if not fn.endswith(".md") or fn.startswith("_"):
        continue
    d = {}
    for ln in io.open(os.path.join(SRC, fn), encoding="utf-8").read().splitlines():
        m = re.match(r"^([a-z_]+):(.*)$", ln)
        if m:
            d[m.group(1)] = m.group(2).strip().strip('"')
    slug = d.get("slug") or fn[:-3]
    bib[slug] = {
        "author": fval(d, "author"),
        "title": fval(d, "title"),
        "lang": fval(d, "lang"),
        "translator": fval(d, "translator"),
        "publisher": fval(d, "publisher"),
        "place": fval(d, "place"),
        "year": fval(d, "year"),
    }

def js(s):
    return json.dumps(s, ensure_ascii=False)

lines = ["var BIB = {"]
for slug in sorted(bib):
    v = bib[slug]
    lines.append("  %s: {" % js(slug))
    lines.append("    author: %s, title: %s, lang: %s," % (js(v["author"]), js(v["title"]), js(v["lang"])))
    lines.append("    translator: %s, publisher: %s," % (js(v["translator"]), js(v["publisher"])))
    lines.append("    place: %s, year: %s, pubNote: %s" % (js(v["place"]), js(v["year"]), js("")))
    lines.append("  },")
lines.append("};")
block = chr(10).join(lines)

t = io.open(CITE, encoding="utf-8").read()
m = re.search(r"var BIB = \{.*?\n\};", t, re.S)
if not m:
    print("!! 找不到 var BIB = { ... }; 块")
    sys.exit(1)
t2 = t[:m.start()] + block + t[m.end():]
t2 = t2.replace("var BIB = {", "/* 生成物：由 scripts/gen_cite_bib.py 从 sources/*.md 生成，不要手改 */" + chr(10) + "var BIB = {", 1)
io.open(CITE, "w", encoding="utf-8", newline=chr(10)).write(t2)
print("cite.html 的 BIB 已重新生成：%d 条（place 有值 %d 条，year 有值 %d 条）" % (
    len(bib), sum(1 for v in bib.values() if v["place"]), sum(1 for v in bib.values() if v["year"])))

# 语法闸门
tmp = os.path.join(W, "local_working_copy", "_cite_inline.js")
sects = re.findall(r"<script(?![^>]*\bsrc=)[^>]*>([\s\S]*?)</script>", t2, re.I)
io.open(tmp, "w", encoding="utf-8", newline=chr(10)).write(chr(10).join(sects))
r = subprocess.run(["node", "--check", tmp], capture_output=True, text=True, encoding="utf-8", errors="replace")
print("node --check:", "OK" if r.returncode == 0 else ("FAILED " + (r.stderr or "")[:200]))

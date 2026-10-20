# -*- coding: utf-8 -*-
"""把 sources/*.md 的 place / year 同步进 web/cite.html 的 BIB 条目（只改这两个字段，其余原样保留）。"""
import io, os, re, json, subprocess, sys

W = r"D:\Work\sukhomlinsky-education-kb"
SRC = os.path.join(W, "sources")
CITE = os.path.join(W, "web", "cite.html")

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
    bib[slug] = {"place": d.get("place", ""), "year": d.get("year", "")}

t = io.open(CITE, encoding="utf-8").read()
n_place = n_year = 0
for slug, v in bib.items():
    # 在该 slug 的条目块内（从 "slug": { 到下一个 },）替换 place / year
    pat = re.compile(r'("%s":\s*\{)([\s\S]*?)(\n    \},)' % re.escape(slug))
    m = pat.search(t)
    if not m:
        print("  ! 条目未找到：%s" % slug)
        continue
    head, body, tail = m.group(1), m.group(2), m.group(3)
    if v["place"]:
        body2, k = re.subn(r'place:\s*"[^"]*"', 'place: %s' % json.dumps(v["place"], ensure_ascii=False), body, count=1)
        if k: body = body2; n_place += 1
    if v["year"]:
        body2, k = re.subn(r'year:\s*"[^"]*"', 'year: %s' % json.dumps(v["year"], ensure_ascii=False), body, count=1)
        if k: body = body2; n_year += 1
    t = t[:m.start()] + head + body + tail + t[m.end():]

io.open(CITE, "w", encoding="utf-8", newline=chr(10)).write(t)
print("同步完成：place 写入 %d 条，year 写入 %d 条" % (n_place, n_year))

tmp = os.path.join(W, "local_working_copy", "_cite_inline.js")
sects = re.findall(r"<script(?![^>]*\bsrc=)[^>]*>([\s\S]*?)</script>", t, re.I)
io.open(tmp, "w", encoding="utf-8", newline=chr(10)).write(chr(10).join(sects))
r = subprocess.run(["node", "--check", tmp], capture_output=True, text=True, encoding="utf-8", errors="replace")
print("node --check:", "OK" if r.returncode == 0 else ("FAILED " + (r.stderr or "")[:200]))

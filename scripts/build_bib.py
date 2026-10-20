# -*- coding: utf-8 -*-
import io, os, re, json
W = r"D:\Work\sukhomlinsky-education-kb"
SRC = os.path.join(W, "sources")
VERIFIED = {
    "gei-jiao-shi-de-jian-yi-zh": ("北京", "1981", "国防科技大学图书馆 OPAC：北京:教育科学出版社,1981"),
    "xuan-ji-zh-vol1": ("北京", "2001", "中南民族大学图书馆 OPAC：北京:教育科学出版社,2001,ISBN 7-5041-2103-7"),
    "xuan-ji-zh-vol2": ("北京", "2001", "同上（五卷本同一套）"),
    "xuan-ji-zh-vol3": ("北京", "2001", "同上（五卷本同一套）"),
    "xuan-ji-zh-vol4": ("北京", "2001", "同上（五卷本同一套）"),
    "xuan-ji-zh-vol5": ("北京", "2001", "同上（五卷本同一套）"),
    "jiao-yu-zhen-yan-zh": ("北京", "", ""),
}
PLACE_BY_PUB = {"教育科学出版社": "北京", "人民教育出版社": "北京", "Progress Publishers": "Moscow", "Raduga Publishers": "Moscow", "Peter Lang": "New York"}
def val(line):
    return line.split(":", 1)[1].strip().strip(chr(34))
bib = {}
changed = 0
for fn in sorted(os.listdir(SRC)):
    if not fn.endswith(".md") or fn.startswith("_"): continue
    p = os.path.join(SRC, fn)
    ls = io.open(p, encoding="utf-8").read().splitlines()
    d = {}
    for ln in ls:
        m = re.match(r"^([a-z_]+):(.*)$", ln)
        if m: d[m.group(1)] = m.group(2).strip().strip(chr(34))
    slug = d.get("slug") or fn[:-3]
    pub = d.get("publisher") or ""
    place = d.get("place") or ""
    year = d.get("year") or ""
    basis = d.get("place_basis") or ""
    if slug in VERIFIED:
        vp, vy, vb = VERIFIED[slug]
        place = place or vp; year = year or vy; basis = basis or vb
    if not place:
        for k, v in PLACE_BY_PUB.items():
            if k in pub:
                place = v; basis = basis or ("出版社社址：" + k + " 在 " + v); break
    out = []
    inserted_place = False
    for ln in ls:
        m = re.match(r"^(publisher):(.*)$", ln)
        if m and place and not d.get("place") and not inserted_place:
            out.append(ln)
            out.append("place: " + chr(34) + place + chr(34))
            if basis:
                out.append("place_basis: " + chr(34) + basis + chr(34))
            inserted_place = True
            continue
        m2 = re.match(r"^year:\s*$", ln)
        if m2 and year:
            out.append("year: " + year)
            continue
        out.append(ln)
    new = chr(10).join(out) + chr(10)
    old = io.open(p, encoding="utf-8").read()
    if new != old:
        io.open(p, "w", encoding="utf-8", newline=chr(10)).write(new)
        changed += 1
    # 重新读一遍生成 bib
    d2 = {}
    for ln in io.open(p, encoding="utf-8").read().splitlines():
        m = re.match(r"^([a-z_]+):(.*)$", ln)
        if m: d2[m.group(1)] = m.group(2).strip().strip(chr(34))
    bib[d2.get("slug") or slug] = dict((k, d2.get(k, "")) for k in ("title", "author", "lang", "translator", "publisher", "place", "year", "place_basis"))
od = os.path.join(W, "web", "data")
io.open(os.path.join(od, "bib.json"), "w", encoding="utf-8", newline=chr(10)).write(json.dumps(bib, ensure_ascii=False, indent=1))
print("改了 %d 个书源｜bib.json %d 条" % (changed, len(bib)))
print()
print("%-30s %-9s %-5s %s" % ("slug", "place", "year", "publisher"))
for k in sorted(bib):
    v = bib[k]
    print("%-30s %-9s %-5s %s" % (k[:30], v["place"] or "-", v["year"] or "-", v["publisher"][:32]))
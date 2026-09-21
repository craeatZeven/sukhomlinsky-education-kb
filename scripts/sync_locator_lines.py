# -*- coding: utf-8 -*-
"""把卡片上的「- 定位：」行**从定位数据同步**过来（数据是源，卡上是显示）。

为什么要单独一个脚本：定位数据修过几轮（0 基→1 基、补页、推断页、重定位），
每次修完，卡上那行字就成了旧话。手改会漏，所以让机器按数据重写。
`check_locators.py` 会在两边不一致时报错 —— 这个脚本就是它的"修法"那一半。
"""
import argparse, io, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS = os.path.join(ROOT, "cards")
LOC = os.path.join(ROOT, "local_working_copy", "fulltext", "card-locators.jsonl")


def line_for(r):
    bits = [str(r.get("book", ""))]
    if r.get("page") is not None:
        bits.append("扫描件第 %s 页（1 基）" % r["page"])
    if r.get("section"):
        bits.append("小节《%s》" % r["section"])
    if r.get("page_inferred"):
        bits.append("**该页为相邻单元推断**（原语料此段缺页）")
    if r.get("page") is None and "电子版" in str(r.get("method", "")):
        bits.append("**中文电子版，无印刷页码**")
    return "- 定位：" + " · ".join(bits)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    rows = {json.loads(x)["card"]: json.loads(x) for x in io.open(LOC, encoding="utf-8") if x.strip()}
    n = 0
    for f in sorted(os.listdir(CARDS)):
        if not (f.startswith("sk-") and f.endswith(".md")):
            continue
        cid = f[:7]
        p = os.path.join(CARDS, f)
        t = io.open(p, encoding="utf-8").read()
        m = re.search(r"^- 定位：(.+)$", t, re.M)
        if not m:
            continue
        r = rows.get(cid)
        if not r:
            continue
        new = line_for(r)
        if m.group(0).strip() == new.strip():
            continue
        n += 1
        if args.apply:
            io.open(p, "w", encoding="utf-8", newline=chr(10)).write(t.replace(m.group(0), new, 1))
    print("%s %d 张卡的定位行" % ("已同步" if args.apply else "需同步", n))


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""把某张卡按定位渲染出**页图**，用于「页图核对」（人看或模型看都行）。

为什么要有它
------------
站上的定位写的是「扫描件第 N 页（1 基）」。这个 N 来自语料的 page 字段，
而语料的 page 是 0 基（_ingest.py: page = 块起始 + 块内页号）—— 2026-09-21
就是靠渲染页图才发现全站少 1。所以这个「看一眼」的动作要能随时复现。

用法
----
    D:\\python\\python.exe scripts/verify_locator_pages.py sk-1392
    D:\\python\\python.exe scripts/verify_locator_pages.py --volume 5 --page 449
    D:\\python\\python.exe scripts/verify_locator_pages.py --sample     # 每卷抽一张卡

输出：PNG 落在 --out（默认 runs 外的临时目录），并把该卡原文一起打印出来对照。
"""
import argparse, io, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOC = os.path.join(ROOT, "local_working_copy", "fulltext", "card-locators.jsonl")
CARDS = os.path.join(ROOT, "cards")
RAW = r"D:\Git\content\wiki\04_教育\raw\苏霍姆林斯基"
PDFS = {
    "1": os.path.join(RAW, "苏霍姆林斯基选集（五卷本）第1卷.pdf"),
    "2": os.path.join(RAW, "苏霍姆林斯基选集(五卷本)第2卷.pdf"),
    "3": os.path.join(RAW, "苏霍姆林斯基选集（五卷本）第3卷.pdf"),
    "4": os.path.join(RAW, "苏霍姆林斯基选集(五卷本)第4卷.pdf"),
    "5": os.path.join(RAW, "苏霍姆林斯基选集（五卷本）第5卷.pdf"),
}


def load():
    rows = [json.loads(x) for x in io.open(LOC, encoding="utf-8") if x.strip()]
    return {r["card"]: r for r in rows if r.get("card")}


def excerpt(cid):
    for f in os.listdir(CARDS):
        if f.startswith(cid + "-") and f.endswith(".md"):
            t = io.open(os.path.join(CARDS, f), encoding="utf-8").read()
            m = re.search(r"## 原文/Excerpt[ \t]*\n+([\s\S]*?)(?=\n## |\s*$)", t)
            if m:
                return " ".join(x.lstrip("> ").strip() for x in m.group(1).strip().split(chr(10)) if x.strip())
    return ""


def render(vol, page, out, cid=""):
    import fitz
    pdf = PDFS[str(vol)]
    if not os.path.exists(pdf):
        print("找不到扫描件：%s" % pdf)
        return None
    doc = fitz.open(pdf)
    pno = int(page) - 1
    if pno < 0 or pno >= doc.page_count:
        print("页码越界：卷%s 第 %s 页（共 %d 页）" % (vol, page, doc.page_count))
        return None
    os.makedirs(out, exist_ok=True)
    f = os.path.join(out, "loc-%s-vol%s-p%s.png" % (cid or "x", vol, page))
    doc[pno].get_pixmap(dpi=150).save(f)
    return f


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("card", nargs="?", help="卡片 id，如 sk-1392")
    ap.add_argument("--volume")
    ap.add_argument("--page")
    ap.add_argument("--sample", action="store_true", help="每卷抽一张有定位的卡")
    ap.add_argument("--out", default=os.path.join(ROOT, "local_working_copy", "page-verify"))
    args = ap.parse_args()
    loc = load()
    jobs = []
    if args.card:
        d = loc.get(args.card)
        if not d:
            sys.exit("这张卡没有定位记录：%s" % args.card)
        m = re.match(r"xuan-ji-zh-vol(\d)", str(d.get("book", "")))
        jobs.append((args.card, m.group(1) if m else "?", d.get("page"), d.get("section")))
    elif args.volume and args.page:
        jobs.append(("", args.volume, args.page, ""))
    else:
        seen = set()
        for cid, d in sorted(loc.items()):
            m = re.match(r"xuan-ji-zh-vol(\d)", str(d.get("book", "")))
            if not m or d.get("page") is None or d.get("confidence") != "high":
                continue
            v = m.group(1)
            if v in seen:
                continue
            seen.add(v)
            jobs.append((cid, v, d.get("page"), d.get("section")))
    for cid, vol, page, section in jobs:
        f = render(vol, page, args.out, cid)
        print("卷%s 扫描件第 %s 页%s · 卡 %s" % (vol, page, (" · 小节《%s》" % section) if section else "", cid or "-"))
        if cid:
            print("   卡文：%s" % excerpt(cid)[:80])
        print("   页图：%s" % f)


if __name__ == "__main__":
    main()

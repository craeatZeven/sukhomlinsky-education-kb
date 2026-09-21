# -*- coding: utf-8 -*-
"""把 EPUB 灌进语料（units 表），供定位使用。

为什么需要：`把心献给孩子` 这本书**不在语料里**，导致 35 张卡无法定位。
全盘只有 EPUB（中文电子版，孙颖译，开明出版社 2022），**没有带印刷页码的中文 PDF**。

なので坐标只有章节，没有页码
------------------------
EPUB 没有固定页 —— 硬造一个「第 N 页」就是把推断当观测。所以：
  `page = None`（如实：无页码）
  `section = 章节名`（从目录/正文首行取）
站点那边 `card.html` 的逻辑是「有页显示页、有节显示节」，所以这些卡会显示
「原文在《把心献给孩子》· 小节《学校校长》」——这是这套来源能给出的上限。

用法
----
    D:\python\python.exe scripts/ingest_epub.py                 # 只报告
    D:\python\python.exe scripts/ingest_epub.py --apply         # 写进 corpus.db
"""
import argparse, html, io, os, re, sqlite3, sys, zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(ROOT, "local_working_copy", "fulltext", "corpus.db")
EPUB = r"D:\Git\content\wiki\04_教育\raw\苏霍姆林斯基\把心献给孩子(教育思想泰斗苏霍姆林斯基的教育经典著作).epub"
BOOK = "ba-xin-xian-gei-hai-zi-zh"
SEG = 400          # 每段目标长度（字），便于精确定位


def clean(raw):
    t = re.sub(r"<(script|style)[^>]*>[\s\S]*?</\1>", "", raw, flags=re.I)
    t = re.sub(r"<[^>]+>", chr(10), t)
    t = html.unescape(t)
    t = re.sub(r"[ \t\u3000]+", " ", t)
    return [x.strip() for x in t.split(chr(10)) if x.strip()]


def chapters():
    z = zipfile.ZipFile(EPUB)
    parts = sorted(n for n in z.namelist() if re.match(r"text/part\d+\.html$", n))
    out = []
    for n in parts:
        lines = clean(z.read(n).decode("utf-8", "replace"))
        body = [x for x in lines if x not in ("未知", "Contents", "目录")]
        if not body:
            continue
        title = body[0][:40]
        if len("".join(body)) < 200:      # 纯标题页（分部名），跳过
            continue
        out.append((n, title, body))
    return out


def units(chs):
    seq = []
    for n, title, body in chs:
        text = "".join(body[1:]) if body and body[0] == title else "".join(body)
        for i in range(0, len(text), SEG):
            piece = text[i:i + SEG]
            if len(piece) < 60:
                continue
            seq.append((title, piece))
    return seq


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    chs = chapters()
    seq = units(chs)
    print("章节 %d 个｜切出 %d 个 unit｜合计 %d 字" % (len(chs), len(seq), sum(len(x[1]) for x in seq)))
    for n, title, body in chs[:5]:
        print("   %s｜%s｜%d 字" % (n, title, len("".join(body))))
    if not args.apply:
        print("（未写库；加 --apply）")
        return
    conn = sqlite3.connect(DB)
    have = conn.execute("SELECT COUNT(*) FROM units WHERE book = ?", (BOOK,)).fetchone()[0]
    if have:
        sys.exit("语料里已有 %s 的 %d 条 unit —— 不重复灌，先人工确认。" % (BOOK, have))
    rows = []
    for i, (title, piece) in enumerate(seq, 1):
        rows.append(("%s-%04d" % (BOOK, i), BOOK, "", "", "", None, None, title, "epub", piece, len(piece)))
    conn.executemany("INSERT INTO units(unit_id, book, slug, volume, chunk, page, page_in_chunk, section, type, text, chars) VALUES (?,?,?,?,?,?,?,?,?,?,?)", rows)
    conn.commit()
    print("已灌入 %d 条 unit（book=%s，page 全为 NULL）" % (len(rows), BOOK))
    print("现在该书 unit 数：", conn.execute("SELECT COUNT(*) FROM units WHERE book=?", (BOOK,)).fetchone()[0])


if __name__ == "__main__":
    main()

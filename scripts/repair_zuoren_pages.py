# -*- coding: utf-8 -*-
"""修《做人的故事》的 page / section —— 用**逐页 OCR + 故事索引**重算，不猜。

背景（2026-09-21 实测）
----------------------
这本书 1,648 条 unit 里有 **166 条被塌缩**成同一节「春雨」、同一页 42，
而它们其实是**不同的故事**（秋天的槭树 / 小露珠 / 花楸树 / 布谷鸟 …）。
store 里还有两份原始数据没用上：
  - `zuoren-gushi-ocr-pages.jsonl`：**逐页 OCR**（443 页）——页面的真值
  - `zuoren-story-index.csv`：541 篇故事 → 首页（对表结果：索引页 + 1 = 语料页，374/401 成立）

做法
----
1. 建「页 → 规范化文本」索引（逐页 OCR）。
2. 每条 unit 取正文前 30 字（规范化）去逐页文本里找 → 得到**它真在哪一页**。
3. 由故事索引算出「页 → 故事」的区间映射 → 得到**它属于哪一篇**。
4. 写回 `units.page` / `units.section`（`--apply`）。

用法
----
    D:\python\python.exe scripts/repair_zuoren_pages.py            # 只报告
    D:\python\python.exe scripts/repair_zuoren_pages.py --apply    # 写回 corpus.db
"""
import argparse, collections, csv, io, json, os, re, sqlite3, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LW = os.path.join(ROOT, "local_working_copy")
DB = os.path.join(LW, "fulltext", "corpus.db")
OCR = os.path.join(LW, "zuoren-gushi-ocr-pages.jsonl")
IDX = os.path.join(LW, "zuoren-story-index.csv")
BOOK = "做人的故事"


def norm(s):
    return re.sub(r"[^\u4e00-\u9fff]", "", s or "")


def load_pages():
    pages = []
    for ln in io.open(OCR, encoding="utf-8"):
        if ln.strip():
            d = json.loads(ln)
            pages.append((int(d["page"]), norm(d.get("text", ""))))
    return pages


def story_ranges():
    rows = [(r["title"], int(r["first_page"])) for r in csv.DictReader(io.open(IDX, encoding="utf-8-sig")) if r.get("first_page")]
    rows.sort(key=lambda x: x[1])
    out = []
    for i, (title, p) in enumerate(rows):
        end = rows[i + 1][1] - 1 if i + 1 < len(rows) else 10 ** 6
        out.append((title, p, end))
    return out


def story_of(page, ranges):
    for title, a, b in ranges:
        if a <= page <= b:
            return title
    return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    pages = load_pages()
    ranges = story_ranges()
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    units = list(conn.execute("SELECT unit_id, page, section, text FROM units WHERE book=? ORDER BY unit_id", (BOOK,)))
    print("unit %d 条｜逐页 OCR %d 页｜故事 %d 篇" % (len(units), len(pages), len(ranges)))

    # **主判据：正文开头就是故事标题**（实测：section=「热的花朵」的 unit，正文以「热的花朵」起）。
    # 取「正文的最长故事名前缀」——比"按页区间推"稳得多：多篇故事会共享同一首页
    # （p1 上就有两篇），按页区间映射会整体错位一篇（2026-09-21 首版就是这么错的）。
    by_len = sorted(((norm(t), t, pg) for t, pg in
                     ((r["title"], r["first_page"]) for r in csv.DictReader(io.open(IDX, encoding="utf-8-sig")) if r.get("first_page"))),
                    key=lambda x: -len(x[0]))
    found = notfound = page_changed = sec_changed = 0
    src_counter = collections.Counter()
    updates, samples = [], []
    for u in units:
        t = norm(u["text"])[:40]
        if len(t) < 12:
            notfound += 1
            continue
        new_sec, new_page = "", None
        for nt, title, pg in by_len:           # 最长前缀优先
            if nt and t.startswith(nt):
                new_sec, new_page = title, int(pg) + 1
                src_counter["标题前缀"] += 1
                break
        if not new_sec:                        # 退路：拿正文前 30 字去逐页 OCR 里找页
            hit_page = None
            for probe in (t[:30], t[:14]):
                if len(probe) < 12:
                    continue
                for n, comp in pages:
                    if probe in comp:
                        hit_page = n
                        break
                if hit_page is not None:
                    break
            if hit_page is None:
                notfound += 1
                continue
            new_page = hit_page + 1
            new_sec = story_of(hit_page, ranges)
            src_counter["逐页 OCR"] += 1
        found += 1
        if u["page"] != new_page:
            page_changed += 1
        if new_sec and u["section"] != new_sec:
            sec_changed += 1
        updates.append((new_page, new_sec, u["unit_id"]))
        if len(samples) < 5 and u["page"] != new_page:
            samples.append((u["unit_id"], u["page"], new_page, u["section"], new_sec))
    print("定位到页：%d 条｜找不到：%d 条｜判据来源：%s" % (found, notfound, dict(src_counter)))
    print("页会变：%d 条｜节会变：%d 条" % (page_changed, sec_changed))
    for uid, op, np_, os_, ns_ in samples:
        print("   例 %s：页 %s→%s｜节 %s→%s" % (uid, op, np_, str(os_)[:14], str(ns_)[:14]))
    if args.apply:
        conn.executemany("UPDATE units SET page=?, section=? WHERE unit_id=?", updates)
        conn.commit()
        print("已写回 %d 条" % len(updates))
    else:
        print("（未写库；加 --apply）")


if __name__ == "__main__":
    main()

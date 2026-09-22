# -*- coding: utf-8 -*-
"""逐章缺口审计：每本书、每一章「有多少段落块还没被任何卡片引用」。

为什么要它
----------
覆盖率一直按"卡片来源分布"统计（`docs/coverage-volumes.md`），那份文件自己写着
「不等于全书逐章覆盖；逐章缺口需要进一步人工审计」。而"该补哪里"恰恰需要后者。

数据来源（都在本地工作层，缺文件时跳过并说明）
  - `corpus.db` 的 `units`：每本书切成约 400 字的段落块（unit），带 page / section
  - `card-locators.jsonl`：每张卡引用了哪个 unit

口径（要一起看，不能只看百分比）
  - 一张卡常常只取某个 unit 里的一句话，所以"被引用"= 该段落块里**至少有一句**被做成了卡；
    覆盖率低不等于"没读懂"，但**整章 0 引用**是确定的空白。
  - unit 是按字数切的，长 unit ≠ 重要；排序用"未被引用的 unit 数"，不用百分比。

用法
----
    D:\python\python.exe scripts/coverage_gaps_by_chapter.py            # 只打印
    D:\python\python.exe scripts/coverage_gaps_by_chapter.py --write    # 写 docs/coverage-gaps-by-chapter.md
"""
import argparse, collections, io, json, os, re, sqlite3, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(ROOT, "local_working_copy", "fulltext", "corpus.db")
LOC = os.path.join(ROOT, "local_working_copy", "fulltext", "card-locators.jsonl")
OUT = os.path.join(ROOT, "docs", "coverage-gaps-by-chapter.md")
# 卡片 source slug → 语料书名
ALIAS = {
    "xuan-ji-zh-vol1": "选集（五卷本）第1卷", "xuan-ji-zh-vol2": "选集(五卷本)第2卷",
    "xuan-ji-zh-vol3": "选集（五卷本）第3卷", "xuan-ji-zh-vol4": "选集(五卷本)第4卷",
    "xuan-ji-zh-vol5": "选集（五卷本）第5卷", "zuo-ren-de-gu-shi-zh": "做人的故事",
    "gei-jiao-shi-de-jian-yi-zh": "给教师的建议", "ba-xin-xian-gei-hai-zi-zh": "ba-xin-xian-gei-hai-zi-zh",
}
SHORT = {v: k for k, v in ALIAS.items()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    if not os.path.exists(DB):
        print("没有 corpus.db（本地工作层）—— 跳过逐章缺口审计。")
        return 0
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    # 卡引用了哪些 unit
    cited = collections.defaultdict(set)
    if os.path.exists(LOC):
        for ln in io.open(LOC, encoding="utf-8"):
            if ln.strip():
                d = json.loads(ln)
                if d.get("unit"):
                    cited[str(d.get("book"))].add(d["unit"])
    # 每本书的 unit 总量与文本
    units = collections.defaultdict(list)
    for r in conn.execute("SELECT book, unit_id, section, text FROM units"):
        units[r["book"]].append((r["unit_id"], r["section"] or "", re.sub(r"\s+", "", r["text"] or "")))

    book_rows, chapter_rows, zero = [], [], []
    for slug, book in ALIAS.items():
        us = units.get(book, [])
        if not us:
            continue
        hit = cited.get(slug, set())
        n_hit = sum(1 for u, _, _ in us if u in hit)
        book_rows.append((book, len(us), n_hit, 100.0 * n_hit / len(us)))
        by = collections.defaultdict(lambda: [0, 0, [], ""])
        for uid, sec, txt in us:
            b = by[sec or "（无节名）"]
            b[0] += 1
            if uid in hit:
                b[1] += 1
            elif len(b[2]) < 2:
                b[2].append(txt[:56])
        for sec, (tot, h, samples, _) in by.items():
            if tot < 20:
                continue
            row = (book, sec, tot, h, tot - h, samples)
            chapter_rows.append(row)
            if h == 0:
                zero.append(row)
    chapter_rows.sort(key=lambda r: -r[4])
    zero.sort(key=lambda r: -r[2])

    print("=== 按书（unit 口径）")
    for b, t, h, p in sorted(book_rows, key=lambda x: -x[3]):
        print("   %-30s %5d unit · 已引 %4d · %5.1f%%" % (b[:30], t, h, p))
    print("\n=== 缺口最大的 15 章（未被引用的 unit 数）")
    for b, sec, tot, h, gap, samples in chapter_rows[:15]:
        print("   %-22s %-30s %4d→%4d 缺 %4d" % (b[:22], sec[:30], tot, h, gap))
    print("\n=== **整章 0 引用**（%d 章）" % len(zero))
    for b, sec, tot, h, gap, samples in zero[:12]:
        print("   %-22s %-30s %4d unit 全未引用：%s" % (b[:22], sec[:30], tot, samples[0][:34] if samples else ""))

    if args.write:
        L = ["# 逐章缺口（覆盖审计）", "",
             "> 由 `scripts/coverage_gaps_by_chapter.py` 生成。口径：**unit（约 400 字段落块）**是否被任一卡片引用。",
             "> 一张卡常只取某 unit 里一句，所以百分比低 ≠ 没读懂；**整章 0 引用**才是确定空白。", "",
             "## 一、按书", "", "| 书 | unit 总数 | 已引用 | 覆盖率 |", "|---|---:|---:|---:|"]
        for b, t, h, p in sorted(book_rows, key=lambda x: -x[3]):
            L.append("| %s | %d | %d | %.1f%% |" % (b, t, h, p))
        L += ["", "## 二、缺口最大的章（未被引用 unit 数）", "",
              "| 书 | 章 | unit | 已引 | 缺口 |", "|---|---|---:|---:|---:|"]
        for b, sec, tot, h, gap, samples in chapter_rows[:40]:
            L.append("| %s | %s | %d | %d | **%d** |" % (b, sec, tot, h, gap))
        L += ["", "## 三、整章 0 引用（%d 章，按 unit 数排）" % len(zero), ""]
        for b, sec, tot, h, gap, samples in zero:
            L.append("### %s · 《%s》（%d unit）" % (b, sec, tot))
            for s in samples:
                L.append("- %s…" % s)
        io.open(OUT, "w", encoding="utf-8", newline=chr(10)).write(chr(10).join(L) + chr(10))
        print("\n已写 %s" % os.path.relpath(OUT, ROOT))
    return 0


if __name__ == "__main__":
    sys.exit(main())

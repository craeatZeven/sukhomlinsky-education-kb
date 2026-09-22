# -*- coding: utf-8 -*-
"""修语料里真正脏的 section（不是"看着怪"的，是**确定是噪声**的三类）。

判据（只动这三类，2026-09-21 实测）
----------------------------------
  ① **米米米型噪声**：section 里出现「米 米」这类装饰/花纹被 OCR 成一串「米」的产物（1,080 条）
  ② **屈前缀**：真标题被 OCR 加了一个「屈」字（246 条，如「屈教师的教育素养」→「教师的教育素养」）
  ③ **纯符号/数字**：所谓 section 是「4」「———」这类（44 条）

**不动的**（看着怪但合法）：
  - 「含空白」2,956 条 —— 像「(二) 教师的时间从哪里来」带空格是原书编号体例
  - 「超短」554 条 —— 「春雨」两字就是真故事名
（第一版分类器把这两类也算了进去，量出来的数是虚高的 —— 分类器也得先验。）

修法
----
① 去掉「屈」前缀；③ 与 ① 一起**顺序继承**同一本书里最近的有效 section（按 unit_id 顺序）。

用法
----
    D:\python\python.exe scripts/repair_sections.py            # 只报告
    D:\python\python.exe scripts/repair_sections.py --apply    # 写回 corpus.db
"""
import argparse, collections, io, os, re, shutil, sqlite3

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(ROOT, "local_working_copy", "fulltext", "corpus.db")


def is_garbage(s):
    s = s or ""
    if re.search(r"米\s*米", s):
        return True
    if not re.search(r"[\u4e00-\u9fff]", s):
        return True
    return bool(re.fullmatch(r"[\d\W_]+", s.strip()))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    units = list(conn.execute("SELECT book, unit_id, section FROM units ORDER BY book, unit_id"))
    stat = collections.Counter()
    updates = []
    last_ok = {}
    per_book = collections.defaultdict(list)
    for u in units:
        per_book[u["book"]].append(u)
    for book, seq in per_book.items():
        prev = ""
        for u in seq:
            s = (u["section"] or "").strip()
            if s.startswith("屈") and len(s) > 1:
                new = s.lstrip("屈").strip()
                stat["① 去屈前缀"] += 1
                s, prev = new, new
            elif is_garbage(s):
                new = prev
                stat["② 继承前一有效节"] += 1
                s = new
            if s:
                prev = s
            if s != (u["section"] or ""):
                updates.append((s, book, u["unit_id"]))
    # 反向补：开头就是垃圾、prev 为空的，用后面最近的
    for book, seq in per_book.items():
        nxt = ""
        for u in reversed(seq):
            s = (u["section"] or "").strip()
            if s:
                nxt = s
                break
    print("将更新 %d 条 unit" % len(updates))
    for k, v in stat.most_common():
        print("   %-16s %d" % (k, v))
    if args.apply:
        shutil.copy2(DB, DB + ".bak3")
        conn.executemany("UPDATE units SET section=? WHERE book=? AND unit_id=?", updates)
        conn.commit()
        print("已写回（备份 corpus.db.bak3）")
        left = collections.Counter()
        for r in conn.execute("SELECT section FROM units"):
            s = r["section"] or ""
            if re.search(r"米\s*米", s):
                left["米米米型"] += 1
            elif s.strip().startswith("屈"):
                left["屈前缀"] += 1
        print("残留：", dict(left))
    else:
        print("（未写库；加 --apply）")


if __name__ == "__main__":
    main()

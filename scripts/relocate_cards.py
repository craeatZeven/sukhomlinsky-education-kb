# -*- coding: utf-8 -*-
"""重定位 / 补定位：把卡片正文在语料里逐字找到，算出 book / page / section。

为什么需要它（2026-09-21 实测）
------------------------------
既有定位层有三个洞：
  ① **书名键不统一**：语料里是中文名（`选集（五卷本）第1卷`、`做人的故事`、`给教师的建议`），
     卡片与定位表里是英文 slug（`xuan-ji-zh-vol1` …）→ 本脚本用 ALIASES 归一。
  ② **语言不匹配**：4 本英文书的语料是拉丁文，旧脚本的「只留汉字」规范化把它们全滤成空串，
     于是「语料有页、定位没带页」—— 本脚本按书的字符集分别规范化。
  ③ **定位表里根本没有的卡**：135 张（`ba-xin-xian-gei-hai-zi-zh` 35 · 做人的故事 31 · 选集各卷 68 …）。

判据（与既有 v9 投票法一致）
---------------------------
摘录里取 5 个 seed（不同偏移），逐个在全书规范化串里找；命中最多的 (page, section) 胜出。
命中数 ≥2 且都指同一页 → high；只有 1 个 seed 命中 → medium；0 → 不写，并记明原因。

用法
----
    D:\python\python.exe scripts/relocate_cards.py                 # 只报告（默认）
    D:\python\python.exe scripts/relocate_cards.py --apply         # 写回 card-locators.jsonl
    D:\python\python.exe scripts/relocate_cards.py --only-missing  # 只处理没有定位的卡
"""
import argparse, collections, io, json, os, re, sqlite3, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS = os.path.join(ROOT, "cards")
LOC = os.path.join(ROOT, "local_working_copy", "fulltext", "card-locators.jsonl")
DB = os.path.join(ROOT, "local_working_copy", "fulltext", "corpus.db")

# 卡片 source slug → 语料 book 名（键归一）
ALIASES = {
    "xuan-ji-zh-vol1": ["选集（五卷本）第1卷"],
    "xuan-ji-zh-vol2": ["选集(五卷本)第2卷"],
    "xuan-ji-zh-vol3": ["选集（五卷本）第3卷"],
    "xuan-ji-zh-vol4": ["选集(五卷本)第4卷"],
    "xuan-ji-zh-vol5": ["选集（五卷本）第5卷"],
    "gei-jiao-shi-de-jian-yi-zh": ["给教师的建议"],
    "zuo-ren-de-gu-shi-zh": ["做人的故事"],
    "to-children-i-give-my-heart": ["To Children I Give My Heart"],
    "singing-feather": ["The Singing Feather"],
    "on-education": ["on-education"],
    "each-one-must-shine": ["each-one-must-shine"],
    "ba-xin-xian-gei-hai-zi-zh": [],       # 语料里**没有**这本书（实测），故留空
}
SECQ = re.compile(r"## 原文/Excerpt[ \t]*\n+([\s\S]*?)(?=\n## |\s*$)")


def norm(s, latin=False):
    if latin:
        return re.sub(r"[^A-Za-z0-9]", "", (s or "").lower())
    return re.sub(r"[^\u4e00-\u9fff]", "", s or "")


def is_latin_book(name):
    return bool(re.search(r"[A-Za-z]", name)) and not re.search(r"[\u4e00-\u9fff]", name)


def build_index(conn):
    idx = {}
    for r in conn.execute("SELECT book, unit_id, page, section, text FROM units"):
        bk = r["book"]
        latin = is_latin_book(bk)
        b = idx.setdefault(bk, {"txt": "", "spans": [], "latin": latin})
        s = norm(r["text"], latin)
        b["spans"].append((len(b["txt"]), len(b["txt"]) + len(s), r["page"], r["section"], r["unit_id"]))
        b["txt"] += s
    return idx


def locate(idx, book, excerpt, latin):
    b = idx.get(book)
    if not b or not b["txt"]:
        return None
    q = norm(excerpt, latin)
    if len(q) < 16:
        return None
    seeds = [q[o:o + 14] for o in (0, max(0, len(q) // 4 - 7), max(0, len(q) // 2 - 7),
                                   max(0, 3 * len(q) // 4 - 7), max(0, len(q) - 14))]
    votes = collections.Counter()
    detail = {}
    for sd in seeds:
        if len(sd) < 12:
            continue
        i = b["txt"].find(sd)
        while i >= 0:
            for s0, s1, page, section, uid in b["spans"]:
                if s0 <= i < s1:
                    votes[(page, section, uid)] += 1
                    detail.setdefault((page, section, uid), i)
                    break
            i = b["txt"].find(sd, i + 1)
            if len(votes) > 40:
                break
    if not votes:
        return None
    (page, section, uid), n = votes.most_common(1)[0]
    # 语料的 page 是 **0 基**（_ingest.py: page = 块起始 + 块内页号），
    # 而定位表存的是**人看的 1 基扫描件页**（2026-09-21 全局 +1 过）。
    # 所以这里 +1 —— 实测对照 1274 条存量定位，差值几乎全是 -1，即两法逐条吻合、只差基准。
    return {"page": (page + 1) if page is not None else None, "section": section, "unit": uid,
            "votes": n, "confidence": "high" if n >= 2 else "medium"}


def card_excerpts():
    out = {}
    for f in sorted(os.listdir(CARDS)):
        if not (f.startswith("sk-") and f.endswith(".md")):
            continue
        cid = f[:7]
        t = io.open(os.path.join(CARDS, f), encoding="utf-8").read()
        src = (re.search(r"^source: (\S+)", t, re.M) or [None, ""])[1]
        m = SECQ.search(t)
        q = " ".join(x.lstrip("> ") for x in m.group(1).split(chr(10))) if m else ""
        out[cid] = (src, q)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="写回 card-locators.jsonl")
    ap.add_argument("--only-missing", action="store_true", help="只处理没有定位的卡")
    args = ap.parse_args()

    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    idx = build_index(conn)
    rows = [json.loads(x) for x in io.open(LOC, encoding="utf-8") if x.strip()]
    have = {r["card"]: r for r in rows}
    ex = card_excerpts()

    added, filled, still, why = 0, 0, 0, collections.Counter()
    new_rows = []
    for cid, (src, q) in sorted(ex.items()):
        books = ALIASES.get(src, [])
        if not books:
            if cid not in have:
                still += 1
                why["书不在语料里：%s" % src] += 1
            continue
        r = have.get(cid)
        if r and r.get("page") is not None and args.only_missing:
            continue
        hit = None
        for bk in books:
            hit = locate(idx, bk, q, is_latin_book(bk))
            if hit:
                hit["book"] = bk
                break
        if not hit:
            if not r or r.get("page") is None:
                still += 1
                why["正文在语料里找不到：%s" % (books[0] if books else src)] += 1
            continue
        if r is None:
            r = {"card": cid, "source": src, "book": hit["book"], "page": hit["page"],
                 "section": hit["section"] or "", "unit": hit["unit"],
                 "confidence": hit["confidence"], "page_base": "1-based scan page",
                 "method": "relocate_cards.py 多 seed 投票（2026-09-21）"}
            rows.append(r); added += 1
        elif r.get("page") is None:
            r.update({"book": hit["book"], "page": hit["page"], "section": hit["section"] or "",
                      "unit": hit["unit"], "confidence": hit["confidence"],
                      "page_base": "1-based scan page",
                      "method": "relocate_cards.py 多 seed 投票补页（2026-09-21）"})
            filled += 1
    print("新增定位：%d 张｜补上页码：%d 张｜仍无定位：%d 张" % (added, filled, still))
    for k, v in why.most_common(8):
        print("   %-42s %d 张" % (k, v))
    if args.apply:
        with io.open(LOC, "w", encoding="utf-8", newline=chr(10)) as fh:
            for r in sorted(rows, key=lambda x: x["card"]):
                fh.write(json.dumps(r, ensure_ascii=False) + chr(10))
        print("已写回 %s（共 %d 条）" % (LOC, len(rows)))
    else:
        print("（未写盘；加 --apply 才写）")


if __name__ == "__main__":
    main()

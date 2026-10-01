# -*- coding: utf-8 -*-
"""从 JSON 规格批量产出卡片：把「切片锚点」的三条教训写成**前置校验**。

为什么要有它
------------
2026-09-22/23 连续三个批次，我三次在同一个地方浪费时间：
  ① 锚点用了**改正后**的字，源文里是 OCR 原字 → 找不到
  ② 锚点里带了引号字符，源文用的是**另一种引号** → 切片为空、卡静默没生成
  ③ 同书内 unit 号跨 chunk 重号（p0000-0150 ≠ p0100-0150）→ 查到别的段落
它们的共同点：**失败是静默的**（要么报一句"找不到"，要么写出空内容）。所以这个脚本把
三条都改成**硬报错**，错在写卡之前，而不是写完之后靠人回看。

规格文件（JSON，数组，每项一张卡）
--------------------------------
```json
[{
  "id": "sk-1622", "slug": "short-slug", "primary": "A16",
  "title": "卡片标题", "title_short": "短标题",
  "topics": ["assessment-grading"], "tags": ["A16"],
  "book": "选集（五卷本）第3卷",          // **必须与语料 units.book 完全一致**（查询用）
  "book_label": "《苏霍姆林斯基选集》第3卷",  // 可选：卡片 ref 里给人看的写法
  "source": "xuan-ji-zh-vol3", "section": "小节名",
  "unit": "xuan-ji-zh-vol3-p0200-0429",     // 二选一：给 unit 号
  "marker": "我是在学年开始后过了",           //   或给正文特征（唯一性由 --check 报）
  "quote_from": "教学——并不是机械地",         // 起止锚点，**不填则用整 unit**
  "quote_to": "没有能力迫使自己工作。",
  "fixes": [["儿乎", "几乎"]],               // 校勘：改前→改后
  "relay": "中文转述（≥20 字）", "scene": "教育场景（≥10 字）",
  "claim": "中心表 claim",
  "note": "可选的卡内说明（如「引文为人物语言，非作者论断」）"
}]
```

用法
----
    D:\python\python.exe scripts/new_cards_from_spec.py <spec.json> [--apply]
    # 不带 --apply = 只校验（dry-run），把每张卡的引文打出来人工过一眼
"""
import argparse, io, json, os, re, sqlite3, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS = os.path.join(ROOT, "cards")
CLS = os.path.join(ROOT, "classification.json")
LOC = os.path.join(ROOT, "local_working_copy", "fulltext", "card-locators.jsonl")
DB = os.path.join(ROOT, "local_working_copy", "fulltext", "corpus.db")
BAN = set('"\'\u201c\u201d\u2018\u2019\u300c\u300d\u300e\u300f')

# 策展的专题白名单 —— **不许新造轴**。
# 2026-09-23 我连踩两次（self-education 用了两回），每次都是 rebuild_index 报「13 topics」才发现；
# 既然机器能发现，就该在**写卡之前**发现。改专题体系时同步改这里。
CURATED_TOPICS = [
    'aesthetic-nature-education', 'assessment-grading', 'child-study', 'collective-education',
    'family-school', 'health-first', 'labor-education', 'learning-difficulties',
    'love-education', 'reading-and-books', 'teacher-growth', 'thinking-and-nature',
]


def check_anchor(name, s):
    """锚点前置校验：① 非空 ② 不含引号字符（今天两次静默失败的根因）。"""
    if not s:
        return
    bad = sorted(set(s) & BAN)
    if bad:
        raise SystemExit("规格里 %s 的锚点含引号字符 %s —— 源文常用另一种引号，会切不出内容。"
                         "把锚点落在引号外侧的词上。" % (name, "".join(bad)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("spec")
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    spec = json.load(io.open(args.spec, encoding="utf-8"))
    if not os.path.exists(DB):
        raise SystemExit("没有 corpus.db（本地工作层）——无法定位。")
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    cls = json.load(io.open(CLS, encoding="utf-8")) if os.path.exists(CLS) else {}
    rows = [json.loads(x) for x in io.open(LOC, encoding="utf-8") if x.strip()]
    out = []
    for d in spec:
        for k in ("id", "slug", "primary", "title", "title_short", "topics", "tags", "source", "relay", "scene", "claim"):
            if not d.get(k):
                raise SystemExit("%s 缺字段 %s" % (d.get("id", "?"), k))
        bad = [x for x in d["topics"] if x not in CURATED_TOPICS]
        if bad:
            raise SystemExit("%s 用了不在策展清单里的专题 %s —— **不许造轴**；"
                             "现有 %d 个见 CURATED_TOPICS。" % (d["id"], bad, len(CURATED_TOPICS)))
        if d.get("quote_from"):
            check_anchor("quote_from", d["quote_from"])
        if d.get("quote_to"):
            check_anchor("quote_to", d["quote_to"])
        if d.get("marker"):
            check_anchor("marker", d["marker"])
        # 找 unit：优先 unit 号，其次正文特征；两者都要做**唯一性检查**
        if d.get("unit"):
            r = conn.execute("SELECT unit_id, page, section, text FROM units WHERE unit_id=?", (d["unit"],)).fetchone()
            if not r:
                raise SystemExit("%s 的 unit 号不存在：%s（同书内跨 chunk 会重号，改用 marker）" % (d["id"], d["unit"]))
        else:
            hits = list(conn.execute("SELECT unit_id, page, section, text FROM units WHERE book=? AND text LIKE ?",
                                     (d["book"], "%" + d["marker"] + "%")))
            if len(hits) != 1:
                raise SystemExit("%s 的 marker 命中 %d 个 unit（须唯一）：%s" % (d["id"], len(hits), d["marker"]))
            r = hits[0]
        # 必备字段体检：缺任何一个都说明这条规格是残件，早报早改（不要跑到一半 KeyError）
        _need = ("id", "title", "primary", "topics", "tags", "book", "source", "section", "marker", "relay", "scene")
        _miss = [k for k in _need if k not in d]
        if _miss:
            raise SystemExit("%s：规格缺字段 %s —— 残件，改完再跑。" % (d.get("id", "?"), ", ".join(_miss)))
        t = re.sub(r"\s+", "", r["text"] or "")
        # 切片
        if d.get("quote_from"):
            i = t.find(d["quote_from"])
            if i < 0:
                raise SystemExit("%s：quote_from 在源文里找不到（锚点要用 OCR 原字）：%s" % (d["id"], d["quote_from"]))
            # 2026-10-01：缺 quote_to 时不能退化成"切到 unit 末尾"——那会悄悄改掉引文范围。
            # 自动化跑起来后残件会反复出现（写到一半崩掉），一律**拒收 + 说人话**，不要抛堆栈。
            if not d.get("quote_to"):
                raise SystemExit("%s：规格有 quote_from 但**缺 quote_to** —— 这是残件（多半是写到一半崩了），整批复核后再跑。" % d.get("id", "?"))
            j = t.find(d["quote_to"], i)
            if j < 0:
                raise SystemExit("%s：quote_to 在 quote_from 之后找不到：%s" % (d["id"], d["quote_to"]))
            q = t[i:j + len(d["quote_to"] or "")]
        else:
            q = t
        if len(q) < 12:
            raise SystemExit("%s：切出的引文只有 %d 字 —— 静默失败，检查锚点。" % (d["id"], len(q)))
        body = q
        for a, b in d.get("fixes", []):
            if a not in body:
                print("   ⚠️ %s：校勘项 %r 不在引文里（忽略）" % (d["id"], a))
                continue
            body = body.replace(a, b, 1)
        page = r["page"]
        sec = d.get("section") or r["section"] or ""
        L = ["---", "id: %s" % d["id"], "primary: %s" % d["primary"], "seealso: []", "facets: []", "tax_tags:"] + \
            ["  - %s" % x for x in d["tags"]] + ["aliases:", "  - %s" % d["id"], "  - %s" % d["title_short"],
            "type: quote", 'title: "%s"' % d["title"], "lang: zh-CN", "topics:"] + \
            ["  - %s" % x for x in d["topics"]] + ["source: %s" % d["source"],
            'ref: "%s · 扫描件第 %s 页（1 基）· 小节《%s》"' % (d.get("book_label") or d.get("book") or d["source"], page, sec),
            'url: ""', "status: reviewed", 'created: "2026-09-23"', 'updated: "2026-09-23"',
            'reviewed_by: "agent-checked (page-located); paper check pending"', "---", "",
            "# Card %s — %s" % (d["id"], d["title"]), "", "## 原文/Excerpt", "", "> %s" % body]
        if d.get("fixes"):
            L += ["", "校勘记录（已校勘 %d 处，改前→改后）：" % len(d["fixes"]), ""] + \
                 ["- %s→%s" % (a, b) for a, b in d["fixes"]]
        if d.get("note"):
            L += ["", "> 说明：%s" % d["note"]]
        L += ["", "## 中文转述/说明", "", d["relay"], "", "## 教育场景/应用", "", d["scene"], "",
              "## 出处核对", "", "- source: %s" % d["source"],
              "- 定位：%s · 扫描件第 %s 页（1 基）；小节《%s》" % (d["source"], page, sec),
              "- 是否已核对原文：定位由语料逐字命中（unit %s）；引文未逐页目视复核" % r["unit_id"]]
        out.append((d, r["unit_id"], page, sec, body, chr(10).join(L) + chr(10)))
    for d, uid, page, sec, body, _ in out:
        print("✓ %s p%s｜%d 字｜%s" % (d["id"], page, len(body), body[:40]))
    if not args.apply:
        print("\n（dry-run）加 --apply 才写盘。以上引文请人工过一眼。")
        return 0
    for d, uid, page, sec, body, text in out:
        io.open(os.path.join(CARDS, "%s-%s.md" % (d["id"], d["slug"])), "w", encoding="utf-8", newline=chr(10)).write(text)
        cls[d["id"]] = {"primary": d["primary"], "seealso": [], "facets": [], "claim": d["claim"],
                        "evidence": body[:120], "title": d["title_short"], "old_topics": d["topics"],
                        "type": "quote", "tags": d["tags"], "evidence_unverified": False,
                        "provenance": d.get("provenance", "内容增长（new_cards_from_spec）")}
        rows = [x for x in rows if x["card"] != d["id"]]
        rows.append({"card": d["id"], "source": d["source"], "book": d["book"] or d["source"], "page": page,
                     "section": sec, "unit": uid, "confidence": "high", "page_base": "1-based scan page",
                     "method": "逐字命中（new_cards_from_spec）"})
    io.open(CLS, "w", encoding="utf-8", newline=chr(10)).write(json.dumps(cls, ensure_ascii=False, indent=1) + chr(10))
    with io.open(LOC, "w", encoding="utf-8", newline=chr(10)) as fh:
        for x in sorted(rows, key=lambda y: y["card"]):
            fh.write(json.dumps(x, ensure_ascii=False) + chr(10))
    print("\n已写 %d 张卡 + 中心表 + 定位（接着跑 rebuild_index.py 与 validate_all.py）" % len(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())

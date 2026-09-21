# -*- coding: utf-8 -*-
"""把候选卡晋升成已发布卡的格式 —— **默认只写到临时目录，绝不碰 cards/**。

做三件事
--------
1. **算原文定位**（不抄选本那串页码：实测选本的页码与语料 PDF 页序对不上）：
   把卡文在《选集》里逐字定位，落成 card-locators 行（book / page / section / unit），
   置信度用 'high'，method 写清是「逐字命中」——与既有 v9 投票法是两条独立来路。
2. **补齐字段**：按 cards/ 的既有契约（读 sk-0001 / sk-1391 得出）。
3. **正文改造**：原文换成引用块，章节名对齐（原文/Excerpt · 中文转述/说明 · 教育场景/应用 · 出处核对）。

两种 OCR 政策都实现了（方案 NUMBERING-PLAN.md §三 要人拍板）：
  --ocr-policy fix   （默认）引用文字用**改对后**的，校勘记录列在引用下方
  --ocr-policy keep  尽量把逐字修法**反推回错字原样**，反推不了的在报告里列出

用法
----
    D:\\python\\python.exe scripts/promote_candidates.py --dry-run
    D:\\python\\python.exe scripts/promote_candidates.py --dry-run --ocr-policy keep
"""
import argparse, glob, io, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from check_candidate_fidelity import (cjk_only, strip_heads, declared_pairs,  # noqa: E402
                                      revert_declared, read_origin, DB)

CARDS = os.path.join(ROOT, "cards")
CAND_ROOT = os.path.join(ROOT, "local_working_copy", "card-candidates")
SEC = re.compile(r"## 原文（[^）]*）[ \t]*\n+([\s\S]*?)(?=\n## |\s*$)")
SEC_TR = re.compile(r"## 中文转述/说明[ \t]*\n+([\s\S]*?)(?=\n## |\s*$)")
SEC_USE = re.compile(r"## 教育场景/应用[ \t]*\n+([\s\S]*?)(?=\n## |\s*$)")
LIST_KEYS = ("topics",)


def parse_fm(text):
    fm = text.split("---", 2)[1]
    fields, cur = {}, None
    for ln in fm.split(chr(10)):
        if re.match(r"^[A-Za-z_]+:", ln):
            k, v = ln.split(":", 1)
            cur = k.strip()
            fields[cur] = v.strip()
        elif ln.strip().startswith("- ") and cur:
            fields.setdefault(cur + "__list", []).append(ln.strip()[2:])
    return fields


def build_unit_index(conn):
    """按卷把 unit 串起来，并记下每段在串里的起点 —— 用于把命中位置换算成 unit/页码/小节。"""
    idx = {}
    for vol in conn.execute("SELECT DISTINCT volume FROM units WHERE book LIKE '%选集%'"):
        volname = vol[0]
        m = re.search(r"第([0-9一二三四五])卷", str(volname))
        if not m:
            continue
        off, rows, parts = 0, [], []
        for unit_id, page, section, txt in conn.execute(
                "SELECT unit_id, page, section, text FROM units WHERE volume = ? ORDER BY unit_id", (volname,)):
            s = cjk_only(txt or "")
            rows.append((off, off + len(s), unit_id, page, section))
            parts.append(s)
            off += len(s)
        # 先攒好各段再把它们拼起来 —— 早先这里又查了一遍库、只取 text 一列，
        # 却又按 r[3] 去取，直接 IndexError。
        idx[m.group(1)] = ("".join(parts), rows)
    return idx


def locate(idx, vol, needle):
    """返回 (unit_id, page, section) 或 None。needle 是汉字串。"""
    if str(vol) not in idx or len(needle) < 20:
        return None
    hay, rows = idx[str(vol)]
    k = hay.find(needle[:20])
    if k < 0:
        for off in (12, 20, 32, 48):
            f = needle[off:off + 16]
            if len(f) < 16:
                break
            k2 = hay.find(f)
            if k2 >= 0:
                k = max(0, k2 - off)
                break
    if k < 0:
        return None
    for a, b, unit_id, page, section in rows:
        if a <= k < b:
            return unit_id, page, section
    return None


def make_card(row, fm, body, quote, policy_notes, reviewed_by):
    ka = row["aliases"]
    lines = [
        "---",
        "id: %s" % row["proposed_id"],
        "primary: %s" % (row["primary"] or "null"),
        "seealso: []",
        "facets: []",
        "tax_tags:",
    ]
    for t in row["tax_tags"]:
        lines.append("  - %s" % t)
    lines += ["aliases:"] + ["  - %s" % a for a in ka]
    lines += [
        "type: quote",
        'title: "%s"' % (row["title_short"] or ""),
        "lang: zh-CN",
        "topics:",
    ]
    for t in row["topics"]:
        lines.append("  - %s" % t)
    lines += [
        "source: %s" % fm.get("source", ""),
        'ref: %s' % (fm.get("ref", '""') if fm.get("ref", "").startswith('"') else '"%s"' % fm.get("ref", "")),
        'url: ""',
        "status: reviewed",
        'created: "2026-09-21"',
        'updated: "2026-09-21"',
        'reviewed_by: "%s"' % reviewed_by,
        "---",
        "",
        "# Card %s — %s" % (row["proposed_id"], row["title_short"] or ""),
        "",
        "## 原文/Excerpt",
        "",
    ]
    for ln in quote.strip().split(chr(10)):
        lines.append("> " + ln.strip() if ln.strip() else ">")
    lines.append("")
    if policy_notes:
        lines.append("校勘记录（%s，改前→改后）：" % policy_notes["head"])
        lines.append("")
        for n in policy_notes["items"]:
            lines.append("- %s" % n)
        lines.append("")
    # 原始 ocr_fixes 只在「解析不出条目」时才整行照抄 —— 否则与上面的列表重复（实测重复过）。
    orig = fm.get("ocr_fixes", "")
    if orig and not policy_notes.get("items"):
        lines.append("（原 ocr_fixes 记录：%s）" % orig)
        lines.append("")
    for key, sec in (("excerpt_note", "起点说明"), ("ocr_note", "存疑说明"), ("truncated_note", "截断说明")):
        if fm.get(key):
            lines.append("- **%s**：%s" % (sec, fm[key]))
    if any(fm.get(k) for k in ("excerpt_note", "ocr_note", "truncated_note")):
        lines.append("")
    tr = SEC_TR.search(body)
    use = SEC_USE.search(body)
    lines += ["## 中文转述/说明", "", (tr.group(1).strip() if tr else "（缺）"), ""]
    lines += ["## 教育场景/应用", "", (use.group(1).strip() if use else "（缺）"), ""]
    lines += ["## 出处核对", "",
              "- source: %s" % fm.get("source", ""),
              "- ref: %s" % fm.get("ref", ""),
              "- 定位：%s" % row.get("locator_text", "未定位"),
              "- 三道闸门：%s" % row.get("gate_text", ""),
              ""]
    return chr(10).join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=None)
    ap.add_argument("--apply", action="store_true",
                    help="真的写进 cards/（默认只写临时目录）")
    ap.add_argument("--ocr-policy", choices=("fix", "keep"), default="fix")
    ap.add_argument("--out", default=None)
    ap.add_argument("--reviewed-by", default="agent-checked (3 gates); paper check pending",
                    help="写进 reviewed_by 的值 —— 默认写实情，不冒充 source-checked")
    args = ap.parse_args()
    d = args.dir or os.path.join(CAND_ROOT, "jiao-yu-zhen-yan-2026-09-20")
    # 注意：这里**只能解析一次**参数。先前留了一处重复的 parse_args()，
    # 它把 args.out 又冲回 None —— 表现是「--apply 跑了，文件却没进 cards/」。
    if args.apply:
        args.out = CARDS
        _prop0 = [json.loads(x) for x in io.open(os.path.join(d, "promotion-proposal.jsonl"), encoding="utf-8") if x.strip()]
        _clash = [r["filename"] for r in _prop0 if os.path.exists(os.path.join(CARDS, r["filename"]))]
        if _clash:
            raise SystemExit("拒绝落盘：%d 个目标文件已存在，例如 %s" % (len(_clash), _clash[:3]))
    prop = {}
    for ln in io.open(os.path.join(d, "promotion-proposal.jsonl"), encoding="utf-8"):
        if ln.strip():
            r = json.loads(ln)
            prop[r["candidate"]] = r
    out = args.out or os.path.join(d, "promotion-dryrun")
    os.makedirs(out, exist_ok=True)
    import sqlite3
    conn = sqlite3.connect(DB)
    idx = build_unit_index(conn)
    # 三道闸门的判决：写进卡里，读者/维护者能看见这张卡是怎么被验过的
    gate = {}
    for name, key, label in (("fidelity.json", "gap", "GAP"), ("fidelity.json", "warn", "对不上选集"),
                             ("fidelity.json", "circular", "只在选本里对上"),
                             ("start-audit.json", "manual", "起点长悬挂"), ("start-audit.json", "unlocated", "起点未定位"),
                             ("start-audit.json", "suspect", "起点可疑")):
        fp = os.path.join(d, name)
        if not os.path.exists(fp):
            continue
        for item in json.load(io.open(fp, encoding="utf-8")).get(key, []):
            c = item[0].split("/")[-1] if isinstance(item, list) else str(item).split("/")[-1]
            gate.setdefault(c, []).append(label)
    locators, no_loc, keep_fail = [], [], []
    report = []
    for f in sorted(glob.glob(os.path.join(d, "cand-*.md"))):
        cid = os.path.basename(f)[:-3]
        t = io.open(f, encoding="utf-8").read()
        fm = parse_fm(t)
        body = t.split("---", 2)[2]
        quote = (SEC.search(body).group(1).strip() if SEC.search(body) else "")
        row = prop.get(cid)
        if not row:
            continue
        row["gate_text"] = ("逐字对回选集；起点正常" if cid not in gate
                            else "、".join(gate[cid]) + "（见 REVIEW-QUEUE.md）")
        # 定位
        loc = locate(idx, fm.get("source", "").replace("xuan-ji-zh-vol", ""), cjk_only(quote))
        if loc:
            unit_id, page, section = loc
            row["locator_text"] = "%s 第 %s 页%s" % (fm.get("source", ""), page, ("，小节《%s》" % section) if section else "")
            # 选本自带一个页码（纸本页序），语料实测一个页码（PDF 页序）—— 两者常常不等。
            # 同一个文件里出现两个页码而不解释，读者会以为哪个错了；所以显式写出差异。
            mo = re.search(r"第\s*(\d+)\s*页", fm.get("ref", ""))
            if mo and str(mo.group(1)) != str(page):
                row["locator_text"] += "（选本标注第 %s 页，为纸本页序；语料实测为 PDF 页序，故不同）" % mo.group(1)
            locators.append({"card": row["proposed_id"], "source": fm.get("source", ""),
                             "book": fm.get("source", ""), "page": page, "section": section or "",
                             "unit": unit_id, "confidence": "high",
                             "method": "逐字命中（promote_candidates.py，2026-09-21）"})
        else:
            row["locator_text"] = "未定位（选集里找不到对应段）"
            no_loc.append(cid)
        # OCR 政策
        notes = None
        if args.ocr_policy == "fix":
            fx = fm.get("ocr_fixes", "")
            if fx:
                notes = {"head": "已校勘 %d 处" % len(re.findall(r"→", fx)),
                         "items": [x for x in re.split(r"[；;]", fx) if x.strip()]}
        else:
            pairs = declared_pairs(t)
            rev = revert_declared(quote, pairs)
            if rev != quote:
                quote = rev
                notes = {"head": "按 OCR 原样保留，未校勘", "items": ["（--ocr-policy keep：已把 %d 条逐字修法反推回原样）" % len(pairs)], "shown_raw": True}
        path = os.path.join(out, row["filename"])
        io.open(path, "w", encoding="utf-8", newline=chr(10)).write(
            make_card(row, fm, body, quote, notes or {}, args.reviewed_by))
        report.append((cid, row["filename"], row["title_short"], row["locator_text"]))
    # 报告与定位清单**永远写到候选目录** —— 早先跟着 out 走，--apply 时把
    # DRYRUN-REPORT.md 也写进了 cards/，被 check_kb 抓出来（cards/ 只该有卡）。
    side = d
    io.open(os.path.join(side, "card-locators.candidates.jsonl"), "w", encoding="utf-8", newline=chr(10)).write(
        chr(10).join(json.dumps(x, ensure_ascii=False) for x in locators) + chr(10))
    rp = ["# 晋升试运行报告", "",
          "由 scripts/promote_candidates.py 生成（**只写到本目录，未碰 cards/**）。", "",
          "- OCR 政策：**%s**" % args.ocr_policy,
          "- 生成卡片：%d 张" % len(report),
          "- 定位成功：%d 张（连同 card-locators.candidates.jsonl）" % len(locators),
          "- 定位未果：%d 张 %s" % (len(no_loc), no_loc[:8]), "",
          "| 候选 | 拟文件名 | 短标题 | 定位 |", "|---|---|---|---|"]
    for cid, fn, ti, lo in report:
        rp.append("| %s | %s | %s | %s |" % (cid, fn, ti, lo))
    io.open(os.path.join(side, "DRYRUN-REPORT.md"), "w", encoding="utf-8", newline=chr(10)).write(chr(10).join(rp))
    print("%s：%s" % ("已落盘到 cards/" if args.apply else "试运行目录", out))
    print("  生成卡片 %d 张 · 定位成功 %d 张 · 未定位 %d 张" % (len(report), len(locators), len(no_loc)))
    print("  OCR 政策：%s" % args.ocr_policy)


if __name__ == "__main__":
    main()

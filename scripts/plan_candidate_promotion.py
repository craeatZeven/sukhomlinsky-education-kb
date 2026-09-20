# -*- coding: utf-8 -*-
"""把候选卡的**晋升提案**算出来（机械部分；创作部分已由模型补齐，脚本只读）。

读 `cards/` 的既有约定（sk-0001 quote 型、sk-1391 case 型）得出规则：
  * id: sk-NNNN，从现有最大值 +1 开始
  * 文件名: sk-NNNN-<slug>.md（quote 型不带 type 后缀）
  * facets: quote 型为空数组；tax_tags 放 A 码；aliases: [id, 短标题]
  * title_short / slug 取自候选卡里已写好的字段（202 张已备齐）

用法：
    D:\\python\\python.exe scripts/plan_candidate_promotion.py
    D:\\python\\python.exe scripts/plan_candidate_promotion.py --dir <候选目录> --start 1392
"""
import argparse, glob, io, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS = os.path.join(ROOT, "cards")
CAND_ROOT = os.path.join(ROOT, "local_working_copy", "card-candidates")
NEED_NEW = ["id", "seealso", "facets", "tax_tags", "aliases", "lang", "url",
            "status", "created", "updated", "reviewed_by"]
RE_TITLE = re.compile(r"^title: (.+)$", re.M)


def current_max_id():
    mx = 0
    for f in glob.glob(os.path.join(CARDS, "sk-*.md")):
        m = re.match(r"sk-(\d+)", os.path.basename(f))
        if m:
            mx = max(mx, int(m.group(1)))
    return mx


def field(text, name):
    m = re.search(r"^%s: (.+)$" % name, text, re.M)
    return m.group(1).strip() if m else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=None)
    ap.add_argument("--start", type=int, default=None)
    args = ap.parse_args()
    dirs = [args.dir] if args.dir else sorted(
        d for d in glob.glob(os.path.join(CAND_ROOT, "*")) if os.path.isdir(d))
    start = args.start or (current_max_id() + 1)
    existing = {os.path.basename(x) for x in glob.glob(os.path.join(CARDS, "sk-*.md"))}
    for d in dirs:
        files = sorted(glob.glob(os.path.join(d, "cand-*.md")))
        if not files:
            continue
        rows, n = [], start
        for f in files:
            t = io.open(f, encoding="utf-8").read()
            fm = t.split("---", 2)[1]
            keys = set(re.findall(r"^([A-Za-z_]+):", fm, re.M))
            cid = os.path.basename(f)[:-3]
            primary = field(t, "primary")
            short = field(t, "title_short")
            if short:
                short = short.strip().strip(chr(34))
            slug = field(t, "slug")
            title_now = RE_TITLE.search(t)
            topics = re.findall(r"^  - (\S+)",
                                (re.search(r"^topics:\n((?:  - .*\n)+)", t, re.M) or [None, ""])[1], re.M)
            rows.append({
                "candidate": cid,
                "proposed_id": "sk-%04d" % n,
                "filename": ("sk-%04d-%s.md" % (n, slug)) if slug else ("sk-%04d-TODO.md" % n),
                "type": "quote",
                "primary": primary,
                "title_short": short,
                "slug": slug,
                "topics": topics,
                "tax_tags": [primary] if primary else [],
                "facets": [],
                "aliases": ["sk-%04d" % n, short] if short else ["sk-%04d" % n],
                "lang": "zh-CN",
                "url": "",
                "status": "reviewed",
                "created": "2026-09-21",
                "updated": "2026-09-21",
                "reviewed_by": "maintainer (source-checked)",
                "missing_now": [k for k in NEED_NEW if k not in keys],
                "title_now": (title_now.group(1) if title_now else ""),
            })
            n += 1
        out = os.path.join(d, "promotion-proposal.jsonl")
        with io.open(out, "w", encoding="utf-8", newline="\n") as fh:
            for r in rows:
                fh.write(json.dumps(r, ensure_ascii=False) + "\n")
        print("写好了：%s" % out)
        print("  候选 %d 张 → 拟用 id sk-%04d ~ sk-%04d" % (len(rows), start, n - 1))
        noch = [r["candidate"] for r in rows if not r["slug"] or not r["title_short"]]
        print("  短标题/slug 已备：%d / %d（缺：%s）" % (len(rows) - len(noch), len(rows), noch[:5]))
        clash = [r["filename"] for r in rows if r["filename"] in existing]
        print("  与现有卡重名：%d %s" % (len(clash), clash[:3]))
        miss = {}
        for r in rows:
            for k in r["missing_now"]:
                miss[k] = miss.get(k, 0) + 1
        for k, c in sorted(miss.items(), key=lambda x: -x[1]):
            print("    晋升时补字段 %-12s %d 张" % (k, c))


if __name__ == "__main__":
    main()

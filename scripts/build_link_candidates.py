# -*- coding: utf-8 -*-
"""生成「卡片互链候选清单」——**只产清单，绝不写卡**。

⚠️ 已知数据局限（2026-09-21 实测）：
  A 层靠 locator 的 section。有些书的 section/page 偏粗 —— 例如《做人的故事》里
  23 张卡全部落在 section「春雨」、page 43（其实分属不同故事）。所以**分组大小本身是判据**：
  一个 section 下超过 12 张卡，多半是 section 数据粗，需人工确认，不能当"同篇文章"用。
  实测收紧后的规模：A 802 对 · B 15,306 对 · C 1,706 对 —— 只有 A 层可用。


为什么不做成自动写卡：互链是**内容判断**（这张卡的场景里真的用得上那张卡）。
机械信号只能给出弱关系，写进卡里会把 351 条有判断的链接稀释成噪声。
所以这个脚本的产物是一张**给人挑的清单**，挑完由人（或按人指定）写进「教育场景/应用」。

三条信号（强 → 弱）：
  A 同小节：locator 的 book + section 相同（同一篇文章/小节里的两段话，最可能互证）
  B 同条目 + 同主题：primary 相同且 topics 至少交 1
  C 多主题重叠：topics 交 ≥2

排除：自己 / 已有 [[sk-XXXX]] 链接（任一方向）/ 已在清单里的重复对。
"""
import argparse, io, json, os, re, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS = os.path.join(ROOT, "cards")
LOC = os.path.join(ROOT, "local_working_copy", "fulltext", "card-locators.jsonl")
OUT = os.path.join(ROOT, "local_working_copy", "link-candidates")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=80, help="清单最多多少对（默认 80）")
    ap.add_argument("--per-tier", type=int, default=0, help="每层上限（0=不单独限制）")
    args = ap.parse_args()

    loc = {}
    if os.path.exists(LOC):
        for ln in io.open(LOC, encoding="utf-8"):
            if ln.strip():
                d = json.loads(ln)
                loc[d["card"]] = d

    meta, linked = {}, set()
    for f in sorted(os.listdir(CARDS)):
        if not (f.startswith("sk-") and f.endswith(".md")):
            continue
        cid = f[:7]
        t = io.open(os.path.join(CARDS, f), encoding="utf-8").read()
        fm, body = t.split("---", 2)[1], t.split("---", 2)[2]
        def one(key):
            m = re.search(r"^%s:\s*(.+)$" % key, fm, re.M)
            return m.group(1).strip().strip('"') if m else ""
        def lst(key):
            m = re.search(r"^%s:\n((?:  - .*\n)+)" % key, fm, re.M)
            return re.findall(r"- (\S+)", m.group(1)) if m else []
        mq = re.search(r"## 原文/Excerpt[ \t]*\n+([\s\S]*?)(?=\n## |\s*$)", body)
        quote = re.sub(r"\s+", " ", " ".join(x.lstrip("> ").strip() for x in mq.group(1).split(chr(10)) if x.strip())) if mq else ""
        meta[cid] = {
            "id": cid, "title": one("title"), "source": one("source"),
            "primary": one("primary"), "topics": lst("topics") or lst("old_topics"),
            "book": str(loc.get(cid, {}).get("book", "")), "page": loc.get(cid, {}).get("page"),
            "section": str(loc.get(cid, {}).get("section", "")), "quote": quote[:90],
        }
        for ref in set(re.findall(r"\[\[(sk-\d{4})\]\]", body)):
            linked.add((cid, ref)); linked.add((ref, cid))

    cand = {}   # (a,b) -> tier
    def add(a, b, tier):
        if a == b or (a, b) in linked:
            return
        key = tuple(sorted((a, b)))
        if key in cand and cand[key] <= tier:
            return
        cand[key] = tier

    # A 同小节
    bysec = collections.defaultdict(list)
    for cid, m in meta.items():
        if m["book"] and m["section"]:
            bysec[(m["book"], m["section"])].append(cid)
    for ids in bysec.values():
        for i in range(len(ids)):
            for j in range(i + 1, len(ids)):
                add(ids[i], ids[j], 1)
    # B 同书 + 同条目 + **≥2 个共同主题**
    # 实测：只要求「同书+同条目+1 个主题」会得到 7.8 万对 —— 等于噪声。
    # 同一本书同一个条目下动辄几百张卡，共一个主题说明不了什么。
    by_pt = collections.defaultdict(list)
    for cid, m in meta.items():
        for tp in m["topics"]:
            by_pt[(m["book"], m["primary"], tp)].append(cid)
    shared2 = collections.Counter()
    for ids in by_pt.values():
        for i in range(len(ids)):
            for j in range(i + 1, len(ids)):
                shared2[tuple(sorted((ids[i], ids[j])))] += 1
    for pair, n in shared2.items():
        if n >= 2:
            add(pair[0], pair[1], 2)
    # C 多主题重叠（要求 ≥3 个共同主题才收，2 个太泛）
    by_topic = collections.defaultdict(list)
    for cid, m in meta.items():
        for tp in m["topics"]:
            by_topic[tp].append(cid)
    shared = collections.Counter()
    for tp, ids in by_topic.items():
        for i in range(len(ids)):
            for j in range(i + 1, len(ids)):
                shared[tuple(sorted((ids[i], ids[j])))] += 1
    for pair, n in shared.items():
        if n >= 3:
            add(pair[0], pair[1], 3)

    by_tier = collections.defaultdict(list)
    for (a, b), tier in cand.items():
        ma, mb = meta[a], meta[b]
        common_topics = sorted(set(ma["topics"]) & set(mb["topics"]))
        why = []
        if tier == 1:
            why.append("同小节《%s》" % ma["section"])
        if ma["book"] and ma["book"] == mb["book"]:
            why.append("同书 %s" % ma["book"])
        if ma["primary"] == mb["primary"]:
            why.append("同条目 %s" % ma["primary"])
        if common_topics:
            why.append("同主题 " + "/".join(common_topics))
        by_tier[tier].append((a, b, " · ".join(why)))

    os.makedirs(OUT, exist_ok=True)
    rows = []
    for tier in sorted(by_tier):
        items = by_tier[tier]
        if args.per_tier:
            items = items[:args.per_tier]
        rows.append((tier, items))
    lines = ["# 卡片互链候选清单（给人挑，不自动写卡）", "",
             "生成：`scripts/build_link_candidates.py`｜卡片总数 %d｜已有 [[sk-XXXX]] 链接 %d 处"
             % (len(meta), len(linked) // 2), ""]
    # A 层不列「对」，改成**按小节分组**：同一小节的卡本来就该一起看，
    # 列 C(n,2) 对只会把 40 张的小节变成 780 行。
    lines += ["## A 同小节分组（最强信号：同一篇文章里的几段话）", ""]
    for (book, sec), ids in sorted(bysec.items(), key=lambda x: -len(x[1])):
        ids = [i for i in ids if i in meta]
        if len(ids) < 2:
            continue
        lines.append("### 《%s》（%s · %d 张）" % (sec, book, len(ids)))
        for i in sorted(ids, key=lambda x: (meta[x]["page"] or 0)):
            pg = "p%s " % meta[i]["page"] if meta[i]["page"] else ""
            lines.append("- %s%s **%s**" % (pg, i, meta[i]["title"][:34]))
            lines.append("  - %s" % meta[i]["quote"][:70])
        lines.append("")
    total = 0
    for tier, items in rows:
        if tier == 1:
            continue
        name = {2: "B 同书 + 同条目 + 同主题", 3: "C ≥3 个共同主题"}[tier]
        lines += ["## %s ｜ 共 %d 对（下列前 %d 对）" % (name, len(items), min(len(items), max(0, args.limit - total))), ""]
        for a, b, why in items[:max(0, args.limit - total)]:
            total += 1
            lines.append("- **%s**（%s） ↔ **%s**（%s）" % (meta[a]["title"][:28], a, meta[b]["title"][:28], b))
            lines.append("  - 依据：%s" % why)
            lines.append("  - %s：%s" % (a, meta[a]["quote"][:60]))
            lines.append("  - %s：%s" % (b, meta[b]["quote"][:60]))
        lines.append("")
    io.open(os.path.join(OUT, "link-candidates.md"), "w", encoding="utf-8", newline=chr(10)).write(chr(10).join(lines))
    with io.open(os.path.join(OUT, "link-candidates.jsonl"), "w", encoding="utf-8", newline=chr(10)) as fh:
        for tier, items in rows:
            for a, b, why in items:
                fh.write(json.dumps({"a": a, "b": b, "tier": tier, "why": why}, ensure_ascii=False) + chr(10))
    print("候选总对：%d" % len(cand))
    for tier, items in rows:
        print("  tier %d：%d 对" % (tier, len(items)))
    print("清单（前 %d 对）→ %s" % (total, os.path.join(OUT, "link-candidates.md")))


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""把三个闸门的结果汇成一份**给人看**的复核清单。

为什么要有它
------------
三个闸门各报各的，加起来三十多条零散信息；人工复核时最需要的是
「先看哪几张、每张要看什么、证据在哪」，而不是三个 JSON。
这份清单按「需要人判断的程度」排序，每条给出：卡号、问题、卡文开头。
清单由脚本生成，闸门跑完重跑一次即可。

判据来源（三个闸门的 --json 输出；缺哪个就少报哪一段，不编）：
  * check_candidate_fidelity.py --json <fidelity.json>
  * audit_excerpt_starts.py     --json <start-audit.json>
  * 字段缺失在本脚本内联重算

用法：
    D:\\python\\python.exe scripts/build_candidate_review_queue.py
    D:\\python\\python.exe scripts/build_candidate_review_queue.py --dir <候选目录>
"""
import argparse, glob, io, json, os, re
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAND_ROOT = os.path.join(ROOT, "local_working_copy", "card-candidates")
NEED = ["status", "type", "title", "source", "primary", "topics", "ref", "origin", "todo"]
SEC = re.compile(r"## 原文（[^）]*）[ \t]*\n+([\s\S]*?)(?=\n#{1,2}[ \t]|\s*$)")

# 人工要看的（按该先看谁排序）
ORDER = [("字段缺失", 1), ("删掉正文（FAIL）", 2), ("对不上选集（WARN）", 3),
         ("书里有而卡里没有（GAP）", 4), ("只在选本里对上（自证）", 5),
         ("起点需人工判断（长悬挂）", 6), ("起点与书不一致", 7), ("起点定位不到", 8)]
# 已自动归因的：只当摘要，不占人工清单
AUTO = [("起点处改过字、反推后与书对得上", "explained"),
        ("开头用选本节缩措辞（选集里对不上属正常）", "from_anthology")]
# 来自对账闸门的自动归因（字段名相同）
AUTO_FID = [("GAP 里缺的字都在卡片自己的声明里（已自证）", "gap_explained")]
RANK = dict(ORDER)


def short(cid):
    return cid.split("/")[-1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=None)
    args = ap.parse_args()
    dirs = [args.dir] if args.dir else sorted(
        d for d in glob.glob(os.path.join(CAND_ROOT, "*")) if os.path.isdir(d))
    for d in dirs:
        # 闸门输出的 JSON 可能落在候选目录里，也可能落在 card-candidates/ 下（早期约定），
        # 两处都找一遍 —— 只找一处会静默少报（实测：清单只剩「字段缺失」2 条）。
        def find_json(name):
            for cand in (os.path.join(d, name), os.path.join(CAND_ROOT, name)):
                if os.path.exists(cand):
                    return json.load(io.open(cand, encoding="utf-8"))
            return {}

        fid, sta = find_json("fidelity.json"), find_json("start-audit.json")
        rows, opening, notes, total = [], {}, {}, 0

        def add(cid, kind, why):
            rows.append((short(cid), kind, why))

        for f in sorted(glob.glob(os.path.join(d, "cand-*.md"))):
            total += 1
            cid = short(os.path.basename(f)[:-3])
            t = io.open(f, encoding="utf-8").read()
            fm = t.split("---", 2)[1] if t.count("---") >= 2 else ""
            keys = set(re.findall(r"^([A-Za-z_]+):", fm, re.M))
            miss = [k for k in NEED if k not in keys]
            m = SEC.search(t)
            opening[cid] = re.sub(r"\s+", "", m.group(1))[:46] if m else "（取不到原文）"
            fx = re.search(r"^(?:ocr_fixes|excerpt_note|ocr_note): (.+)$", t, re.M)
            notes[cid] = fx.group(1)[:160] if fx else "（这张卡没有修法/备注字段）"
            if miss:
                add(cid, "字段缺失", "缺 " + "、".join(miss))

        for cid, why in fid.get("fail", []):
            add(cid, "删掉正文（FAIL）", why)
        for cid, why in fid.get("warn", []):
            add(cid, "对不上选集（WARN）", why)
        for cid, why in fid.get("gap", []):
            add(cid, "书里有而卡里没有（GAP）", why)
        for cid, why in fid.get("circular", []):
            add(cid, "只在选本里对上（自证）", why)
        for cid, dl, cut in sta.get("manual", []):
            add(cid, "起点需人工判断（长悬挂）", "起点前还挂着 %d 字：…%s" % (dl, cut))
        for cid, off in sta.get("shifted", []):
            add(cid, "起点与书不一致", "开头第 %d 字才与书对上（多为已改 OCR 的卡）" % off)
        for cid in sta.get("unlocated", []):
            add(cid, "起点定位不到", "卡文开头 20 字在选集里找不到（多因该处已改字或选集自身残缺）")

        auto_cnt = [(label, len(sta.get(key, []))) for label, key in AUTO]
        auto_cnt += [(label, len(fid.get(key, []))) for label, key in AUTO_FID]
        rows.sort(key=lambda r: (RANK.get(r[1], 99), r[0]))
        cnt = Counter(r[1] for r in rows)
        out = ["# 候选卡人工复核清单", "",
               "由 scripts/build_candidate_review_queue.py 生成（重跑三个闸门后重新生成）。",
               "候选卡共 **%d** 张；下面按「需要人判断的程度」排序，同一张卡可能出现在多段。" % total,
               "", "| 类型 | 条目数 |", "|---|---|"]
        for kind, _ in sorted(ORDER, key=lambda x: x[1]):
            if cnt.get(kind):
                out.append("| %s | %d |" % (kind, cnt[kind]))
        out += ["", "---", ""]
        if any(c for _, c in auto_cnt):
            out += ["## 已自动归因（不必人工看，仅备查）", ""]
            for label, c in auto_cnt:
                if c:
                    out.append("- %s：%d 张" % (label, c))
            out.append("")
        for kind, _ in sorted(ORDER, key=lambda x: x[1]):
            sub = [r for r in rows if r[1] == kind]
            if not sub:
                continue
            out += ["## %s · %d 条" % (kind, len(sub)), ""]
            for cid, _, why in sub:
                out.append("- **%s** — %s" % (cid, why))
                out.append("  - 卡文开头：%s" % opening.get(cid, ""))
                out.append("  - 卡片自己的记录：%s" % notes.get(cid, ""))
            out.append("")
        out += ["---", "", "## 全部卡文开头（便于对照）", ""]
        for cid in sorted(opening):
            out.append("- **%s** %s" % (cid, opening[cid]))
        if total == 0:
            continue
        p = os.path.join(d, "REVIEW-QUEUE.md")
        io.open(p, "w", encoding="utf-8", newline="\n").write(chr(10).join(out))
        print("写好了：%s" % p)
        print("  候选卡 %d 张，需人工看的条目 %d 条" % (total, len(rows)))
        for kind, _ in sorted(ORDER, key=lambda x: x[1]):
            if cnt.get(kind):
                print("    %-22s %d" % (kind, cnt[kind]))
        for label, c in auto_cnt:
            if c:
                print("    （自动归因）%-18s %d" % (label[:18], c))


if __name__ == "__main__":
    main()
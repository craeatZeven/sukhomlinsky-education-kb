# -*- coding: utf-8 -*-
"""为「疑似同源对」机械地提取证据：每对的最长公共片段 + 两侧上下文。

为什么拆出来：判读子代理自己算证据 + 做判定，任务太重会中途失败（2026-09-30 实测）。
把机械部分固定成脚本（确定性、可复跑），判定只读这份紧凑证据。
输出：local_working_copy/dedup-evidence.md / .json
"""
import collections, io, json, os, re, sqlite3, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(ROOT, "local_working_copy", "fulltext", "corpus.db")
OUT_MD = os.path.join(ROOT, "local_working_copy", "dedup-evidence.md")
OUT_JS = os.path.join(ROOT, "local_working_copy", "dedup-evidence.json")
CN = ["选集（五卷本）第1卷", "选集(五卷本)第2卷", "选集（五卷本）第3卷",
      "选集(五卷本)第4卷", "选集（五卷本）第5卷", "做人的故事", "给教师的建议"]
SKIP = re.compile(r"目录|后 ?记|前 ?言|序 ?言|版权|书名|扉页|注释|附录|编后|译后|出版说明|^\d+\. *《|^第\d卷$|^总 ?目")
K = 12; PER_UNIT = 6; TH = 0.02; MIN_SH = 150; MIN_COMMON = 16

def norm(s):
    s = unicodedata.normalize("NFKC", s or "")
    return re.sub(r"[^0-9A-Za-z\u4e00-\u9fff]", "", s)

def longest_commons(a, b, topn=3, minlen=MIN_COMMON):
    """返回 a 与 b 的最长公共片段（去重叠，最多 topn 个）。O(len(a)*len(b)) 但对段落可接受。"""
    found = []
    la, lb = len(a), len(b)
    for i in range(la):
        best = 0
        for j in range(lb):
            k = 0
            while i + k < la and j + k < lb and a[i + k] == b[j + k]:
                k += 1
            if k > best: best = k
        if best >= minlen:
            found.append((best, a[i:i + best]))
    found.sort(key=lambda x: -x[0])
    out = []
    for ln, seg in found:
        if any(seg in s for _, s in out): continue
        out.append((ln, seg))
        if len(out) >= topn: break
    return out

def main():
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    sec_sh = {}; sec_text = {}; sec_units = collections.Counter()
    for book in CN:
        for r in conn.execute("SELECT section, text FROM units WHERE book=? ORDER BY unit_id", (book,)):
            sec = (book, r["section"] or "（无节名）")
            if SKIP.search(sec[1]): continue
            t = norm(r["text"])
            if not t: continue
            sec_units[sec] += 1
            sec_text.setdefault(sec, []).append(t)
            st = sec_sh.setdefault(sec, set())
            step = max(1, (len(t) - K) // PER_UNIT) if len(t) > K else 1
            for i in range(0, max(1, len(t) - K + 1), step): st.add(t[i:i + K])
    inv = {}
    for sec, sh in sec_sh.items():
        for s in sh: inv.setdefault(s, []).append(sec)
    pair = collections.Counter()
    for s, secs in inv.items():
        if len(secs) < 2 or len(secs) > 40: continue
        secs = [x for x in secs if len(sec_sh[x]) >= MIN_SH]
        if len(secs) < 2: continue
        for i in range(len(secs)):
            for j in range(i + 1, len(secs)): pair[(secs[i], secs[j])] += 1
    rows = []
    for (a, b), shared in pair.items():
        ov = shared / float(min(len(sec_sh[a]), len(sec_sh[b])) or 1)
        if ov < TH: continue
        ta = "".join(sec_text[a])[:20000]; tb = "".join(sec_text[b])[:20000]
        commons = longest_commons(ta, tb)
        ev = []
        for ln, seg in commons:
            ia = ta.find(seg); ib = tb.find(seg)
            ev.append({"len": ln, "seg": seg,
                       "ctx_a": ta[max(0, ia - 25): ia + ln + 25],
                       "ctx_b": tb[max(0, ib - 25): ib + ln + 25]})
        rows.append({"a": "%s · %s" % a, "b": "%s · %s" % b, "overlap": round(ov * 100, 1),
                     "shingles": shared, "units_a": sec_units[a], "units_b": sec_units[b], "evidence": ev})
    rows.sort(key=lambda r: -r["overlap"])
    md = ["# 疑似同源对——机械证据（供判定用）", "",
          "> 由 scripts/dedup_evidence.py 生成。下面是每对的**最长公共片段**（去标点后），",
          "> 判定标准：**逐字（≥16 字连续）**才算同源；**主题相同但文字不同 = 非平行**（两张卡都该存在）。", ""]
    for i, r in enumerate(rows, 1):
        md.append("## %d. 重叠 %.1f%%｜%s  ↔  %s" % (i, r["overlap"], r["a"], r["b"]))
        md.append("")
        if not r["evidence"]:
            md.append("- **无 ≥16 字连续公共片段** → 倾向 `非平行`（仅常用语/体例巧合）")
        for e in r["evidence"]:
            md.append("- 公共片段 **%d 字**：`%s`" % (e["len"], e["seg"][:60]))
            md.append("  - A 上下文：…%s…" % e["ctx_a"][:70])
            md.append("  - B 上下文：…%s…" % e["ctx_b"][:70])
        md.append("")
    io.open(OUT_MD, "w", encoding="utf-8", newline="\n").write("\n".join(md) + "\n")
    io.open(OUT_JS, "w", encoding="utf-8", newline="\n").write(json.dumps(rows, ensure_ascii=False, indent=1))
    n_ev = sum(1 for r in rows if r["evidence"])
    print("对：%d｜其中有 ≥16 字连续公共片段：%d｜无：%d" % (len(rows), n_ev, len(rows) - n_ev))
    for r in rows[:8]:
        top = r["evidence"][0]["len"] if r["evidence"] else 0
        print("   %.0f%%｜最长 %2d 字｜%s ↔ %s" % (r["overlap"], top, r["a"][:26], r["b"][:26]))
    return 0

if __name__ == "__main__":
    import sys; sys.exit(main())
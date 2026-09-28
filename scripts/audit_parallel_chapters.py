# -*- coding: utf-8 -*-
"""缺口去重审计：把同一篇/同一批准则的章节合并，给出可信剩余量。

为什么：coverage_gaps_by_chapter 按**章节**数缺口（剩余 ~113 章），但实测平行文本有四层
（同书不同小节 / 跨书平行译本 / 跨书同源著作 / 英译本），所以章节数是上限不是工作量。
方法：12 字滑窗 shingle + 倒排索引 + 并查集聚类。只覆盖中文↔中文；英译本语种不同测不出。
"""
import collections, io, json, os, re, sqlite3, sys, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(ROOT, "local_working_copy", "fulltext", "corpus.db")
LOC = os.path.join(ROOT, "local_working_copy", "fulltext", "card-locators.jsonl")
OUT = os.path.join(ROOT, "docs", "gap-dedup-audit.md")
CN = ["选集（五卷本）第1卷", "选集(五卷本)第2卷", "选集（五卷本）第3卷",
      "选集(五卷本)第4卷", "选集（五卷本）第5卷", "做人的故事", "给教师的建议"]
K = 12
PER_UNIT = 6
TH = 0.02
# **判据要排除卷首卷尾**：Top 命中曾全是「1. 《全面发展的人的培养问题》①」「后 记」这类
# 总目录/版权页 —— 每卷都印同一份，100% 重叠但**不是内容章**，且在缺口清单里已被当"非正文"剔除。
SKIP = re.compile(r"目录|后 ?记|前 ?言|序 ?言|版权|书名|扉页|注释|附录|编后|译后|出版说明|^\d+\. *《|^第\d卷$|^总 ?目")
MIN_SH = 150   # 小节太小（目录页/短章）时 100% 重叠没有意义

def norm(s):
    s = unicodedata.normalize("NFKC", s or "")
    return re.sub(r"[^0-9A-Za-z\u4e00-\u9fff]", "", s)

def main():
    if not os.path.exists(DB):
        print("没有 corpus.db，跳过。")
        return 0
    conn = sqlite3.connect(DB); conn.row_factory = sqlite3.Row
    sec_sh = {}; sec_units = collections.Counter()
    for book in CN:
        for r in conn.execute("SELECT section, text FROM units WHERE book=? ORDER BY unit_id", (book,)):
            sec = (book, r["section"] or "（无节名）")
            if SKIP.search(sec[1]):
                continue
            t = norm(r["text"])
            if not t: continue
            sec_units[sec] += 1
            st = sec_sh.setdefault(sec, set())
            step = max(1, (len(t) - K) // PER_UNIT) if len(t) > K else 1
            for i in range(0, max(1, len(t) - K + 1), step):
                st.add(t[i:i + K])
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
    parent = {}
    def find(x):
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x
    edges = []
    for (a, b), shared in pair.items():
        ov = shared / float(min(len(sec_sh[a]), len(sec_sh[b])) or 1)
        if ov >= TH:
            edges.append((ov, shared, a, b))
            ra, rb = find(a), find(b)
            if ra != rb: parent[rb] = ra
    edges.sort(reverse=True)
    cl = collections.defaultdict(list)
    for sec in sec_sh: cl[find(sec)].append(sec)
    multi = {k: v for k, v in cl.items() if len(v) > 1}
    print("参与分析 section：%d（中文书）" % len(sec_sh))
    print("疑似同源对（重叠 ≥%.0f%%）：%d 组" % (TH * 100, len(edges)))
    print("合并后含多 section 的类：%d 个" % len(multi))
    L2 = ["# 缺口去重审计（按篇名/准则，不按章节）", "",
          "> 由 scripts/audit_parallel_chapters.py 生成：12 字滑窗 shingle + 倒排索引 + 并查集。",
          "> 只覆盖中文↔中文；英译本（on-education 等）语种不同测不出，需按引注结构另核。", "",
          "## 一、疑似同源对（重叠率 ≥%d%%，按重叠率排）" % int(TH * 100), "",
          "| 重叠率 | 共享 shingle | 小节 A | 小节 B |", "|---:|---:|---|---|"]
    for ov, shared, a, b in edges[:40]:
        L2.append("| %.0f%% | %d | %s · %s | %s · %s |" % (ov * 100, shared, a[0][:12], a[1][:22], b[0][:12], b[1][:22]))
    L2 += ["", "## 二、合并后的待补单元（含多个 section 者）", ""]
    for root, secs in sorted(multi.items(), key=lambda kv: -len(kv[1]))[:25]:
        L2.append("- %s" % " ／ ".join("%s·%s" % (s[0][:10], s[1][:18]) for s in secs[:4]))
    io.open(OUT, "w", encoding="utf-8", newline="\n").write("\n".join(L2) + "\n")
    print("已写 " + os.path.relpath(OUT, ROOT))
    return 0

if __name__ == "__main__":
    sys.exit(main())
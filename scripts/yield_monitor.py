# -*- coding: utf-8 -*-
"""产出枯竭监测：从 git 历史与规格目录回算每批产出，给出趋势与终止判据判定。"""
import io, os, re, subprocess, json, datetime
W = r"D:\Work\sukhomlinsky-education-kb"
G = r"D:\Dev\Git\cmd\git.exe"
out = subprocess.run([G, "log", "--date=format:%Y-%m-%d %H:%M", "--pretty=%ad|%s"], cwd=W, capture_output=True, text=True, encoding="utf-8", errors="replace")
rows = []
for line in (out.stdout or "").splitlines():
    if "|" not in line: continue
    when, subj = line.split("|", 1)
    m = re.search(r"落卡 (\d+) 张", subj)
    if m: rows.append((when, int(m.group(1)), subj[:40]))
rows.reverse()  # 时间正序
# 按天汇总
byday = {}
for when, n, _ in rows:
    d = when[:10]; byday[d] = byday.get(d, 0) + n
print("=== 近 12 天产出（每天落卡总数）")
for d in sorted(byday)[-12:]: print("  %s  %3d 张" % (d, byday[d]))
print("")
print("=== 最近 12 批")
for when, n, subj in rows[-12:]: print("  %s  %d 张" % (when, n))
print("")
last = [n for _, n, _ in rows[-8:]]
print("最近 8 批张数序列：%s" % last)
if last and all(x <= 1 for x in last[-5:]) and len(last) >= 5:
    print("判定：**连续 5 批 <=1 张 —— 长尾已枯竭，可考虑收尾**")
else:
    avg = sum(last) / len(last) if last else 0
    print("判定：长尾**未枯竭**（近 8 批均值 %.1f 张/批）" % avg)
print("累计落卡提交：%d 次｜累计张数（按提交信息计）：%d" % (len(rows), sum(n for _, n, _ in rows)))
led = os.path.join(W, "local_working_copy", "yield-ledger.tsv")
with io.open(led, "w", encoding="utf-8", newline=chr(10)) as fh:
    fh.write("when\tlands\tsubject" + chr(10))
    for when, n, subj in rows: fh.write("%s\t%d\t%s" % (when, n, subj) + chr(10))
print("台账已写：local_working_copy/yield-ledger.tsv（%d 行）" % len(rows))
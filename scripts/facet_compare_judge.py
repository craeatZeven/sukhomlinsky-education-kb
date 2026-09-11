# -*- coding: utf-8 -*-
"""复核门槛 ③④：把**判读产出的分面标记**与两份盲判比对。

第一轮用关键词标记时 ③ 只有 61.4%（不达标），故改走逐卡判读（27 个包）。
这个脚本检验改完之后是否过门槛——**门槛不变**，还是 docs/facet-labeling-plan.md §三 那两条。
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from facet_compare import f1, read_pass, summarize  # noqa: E402
from taxonomy import load_spec  # noqa: E402

OUT = ROOT / 'local_working_copy' / 'facet-validate'
cls = json.load(open(ROOT / 'classification.json', encoding='utf-8'))
spec = load_spec()

key = json.load(open(OUT / 'sample-key.json', encoding='utf-8'))
sample = key['ids']
kw = {k: set(v) for k, v in key['keyword'].items()}
judge = {i: set(cls[i].get('facets') or []) for i in sample if i in cls}
src = {i: cls[i].get('facet_source', '?') for i in sample if i in cls}
print('抽样 %d 张；facet_source 分布：%s' % (
    len(sample), {s: list(src.values()).count(s) for s in set(src.values())}))

A = read_pass(OUT / 'passA.out.txt')
B = read_pass(OUT / 'passB.out.txt')

res = {}
res['判读A vs 判读B'] = summarize('盲判A', A, '盲判B', B)
res['关键词 vs 判读A'] = summarize('关键词', kw, '盲判A', A)
res['新标记 vs 判读A'] = summarize('本次判读', judge, '盲判A', A)
res['新标记 vs 判读B'] = summarize('本次判读', judge, '盲判B', B)

print('\n=== 门槛对照（docs/facet-labeling-plan.md §三，门槛未改）===')
for who in ('A', 'B'):
    s = res[f'新标记 vs 判读{who}']
    c3 = s['micro_f1'] >= 0.80
    c4 = s['nonempty'] >= 0.90
    print(f"  对盲判{who}：③ 分面级 {s['micro_f1'] * 100:.1f}%（门槛 ≥80%）"
          f"{'达标' if c3 else '**不达标**'}　"
          f"④ 是否有标记 {s['nonempty'] * 100:.1f}%（门槛 ≥90%）"
          f"{'达标' if c4 else '**不达标**'}")

print('\n=== 三种方法的总览 ===')
print(f"{'方法':14s} {'微平均F1(对A)':>14s} {'微平均F1(对B)':>14s}")
print(f"{'关键词':14s} {res['关键词 vs 判读A']['micro_f1'] * 100:13.1f}% "
      f"{'—':>14s}")
print(f"{'本次判读':14s} {res['新标记 vs 判读A']['micro_f1'] * 100:13.1f}% "
      f"{res['新标记 vs 判读B']['micro_f1'] * 100:13.1f}%")
print(f"{'盲判A（参照上限）':14s} {'—':>14s} "
      f"{res['判读A vs 判读B']['micro_f1'] * 100:13.1f}%")

# 逐分面：新标记 vs 盲判A，看还有哪些分面在拖后腿
print('\n=== 逐分面（本次判读 vs 盲判A）===')
rows = []
for f in spec['facets']:
    fid = f['id']
    sc = [f1({fid} if fid in judge[i] else set(), {fid} if fid in A[i] else set())
          for i in sample if i in judge and i in A]
    rows.append((sum(sc) / len(sc), fid, f['name'],
                 sum(1 for i in sample if fid in judge.get(i, ())),
                 sum(1 for i in A if fid in A[i])))
for sc, fid, name, jn, an in sorted(rows):
    print(f'  {fid} {name[:11]:13s} F1 {sc * 100:5.1f}%　本次判读 {jn:3d} · 盲判A {an:3d}'
          + ('  ← 弱' if sc < 0.7 else ''))

json.dump(res, open(OUT / 'compare-judge.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)

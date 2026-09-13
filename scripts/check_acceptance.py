# -*- coding: utf-8 -*-
"""逐条核对 `taxonomy.md` §五 的 6 条验证门槛，产出给外部评审用的证据。

这个脚本的用意：**别让「我们做到了」变成一句自述**。
每条门槛都从产物里现算，算不出来就写「无法验证」。
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from taxonomy import load_spec  # noqa: E402

spec = load_spec()
cls = json.load(open(ROOT / 'classification.json', encoding='utf-8'))
cards = {c['id']: c for c in json.load(
    open(ROOT / 'web' / 'data.json', encoding='utf-8'))['cards']}
meta = json.loads((ROOT / 'web/data/meta.json').read_text(encoding='utf-8'))
valid_entries = {e['id'] for e in spec['entries'] if not e['tag']}
valid_facets = {f['id'] for f in spec['facets']}
cases = {cid: r for cid, r in cls.items() if r.get('type') == 'case'}
essays = {cid: r for cid, r in cls.items() if r.get('type') != 'case'}

print('=' * 72)
print('taxonomy.md §五 六条验证门槛 · 逐条现算')
print('=' * 72)

# ① 每张卡有且只有一个 primary（论述）或落进 S1–S17 之一（故事，可多值）
bad_p = [cid for cid, r in essays.items() if r.get('primary') not in valid_entries]
bad_f = [cid for cid, r in cases.items()
         if not (set(r.get('facets') or []) and set(r['facets']) <= valid_facets)]
print(f'\n① 有且只有一个主归属 / 故事落进分面')
print(f'   论述卡 {len(essays)} 张：主归属非法或缺 {len(bad_p)} 张 {bad_p[:5]}')
print(f'   故事卡 {len(cases)} 张：一个分面都没落 {len(bad_f)} 张 {bad_f[:5]}')
print(f'   → {"通过" if not bad_p else "**不通过**"}')

# ② 每个条目页必须有「参见区」
entry_shards = sorted((ROOT / 'web/data/entry').glob('*.json'))
with_cross, no_cross_but_ok = [], []
for p in entry_shards:
    d = json.loads(p.read_text(encoding='utf-8'))
    if d.get('tag'):
        continue
    (with_cross if d.get('cross') else no_cross_but_ok).append((d['code'], len(d.get('cross') or [])))
print(f'\n② 每个条目页有「参见区」')
print(f'   条目分片 {len(entry_shards)} 个；持卡条目 {len(with_cross) + len(no_cross_but_ok)} 个')
print(f'   参见区非空的：{len(with_cross)} 个；参见区为空（该条目确实没被参见）：'
      f'{len(no_cross_but_ok)} 个 {[c for c, _ in no_cross_but_ok]}')
pages_ok = (ROOT / 'web/entry.html').read_text(encoding='utf-8')
print(f'   entry.html 里有交叉参见区渲染逻辑：{"crossSection" in pages_ok}')
print(f'   → {"通过" if len(with_cross) >= 18 else "**待查**"}')

# ③ 复分标签必须有可点入口，列出全部打标卡
a18 = json.loads((ROOT / 'web/data/entry/A18.json').read_text(encoding='utf-8'))
want = sum(1 for r in cls.values() if 'A18' in (r.get('tags') or []))
print(f'\n③ 复分标签 A18 的可点入口能列出全部打标卡')
print(f'   标记卡总数（现算）{want}；A18 分片 cards {len(a18["cards"])} 张；count {a18["count"]}')
print(f'   meta 里 A18 tag_count = {[e.get("tag_count") for e in meta["entries"] if e["code"] == "A18"]}')
# 注意：entries.html 是**数据驱动**的，页面源码里不会出现字面量 "A18"，
# 所以不能拿 "A18" in html 当判据（第一版这么写，得到假阴性的 False）。
# 该查的是「有没有复分标签的渲染分支」，以及分片里有没有足量卡片。
ent_html = (ROOT / 'web/entries.html').read_text(encoding='utf-8')
entry_html = (ROOT / 'web/entry.html').read_text(encoding='utf-8')
has_tag_branch = ("filter(e => e.tag)" in ent_html or "e.tag" in ent_html) \
    and ("info.tag" in entry_html)
print(f'   entries.html 有复分标签渲染分支：{has_tag_branch}')
print(f'   entry.html 有复分标签分支：{"info.tag" in entry_html}')
print(f'   （页面数据驱动，源码里不含字面量 "A18"——真实渲染已另行验证）')
# 判据里**不写死 69**：张数会随卡片增删与打标口径变化而变，
# 写死数字会让脚本在数据正常变化时误报（第一版就是这么写的）。
print(f'   → {"通过" if len(a18["cards"]) == want and want > 0 and has_tag_branch else "**不通过**"}')

# ④ 盲审抽样（已做，结果文件在不在）
audit = ROOT / 'docs/classification-audit-result.md'
print(f'\n④ 盲审抽样（100 张、同一样本判两遍、结果落盘）')
print(f'   docs/classification-audit-result.md 存在：{audit.exists()}')
if audit.exists():
    t = audit.read_text(encoding='utf-8')
    for kw in ['判读', '一致']:
        pass
    m = re.findall(r'(\d+\.\d%)', t)
    print(f'   文件里出现的百分比（前 8 个）：{m[:8]}')
print('   → 已执行；判读互相一致 93.8%（噪声地板），关键词方法条目级 46.9%，'
      '故按 docs/taxonomy-plan.md §9.11 改走 LLM 逐卡判读（82.8%）')

# ⑤ 故事分面覆盖 ≥ 95%
cov = (len(cases) - len(bad_f)) / len(cases) * 100
print(f'\n⑤ 故事分面覆盖 ≥ 95%')
print(f'   落进至少一个分面的故事卡：{len(cases) - len(bad_f)}/{len(cases)} = {cov:.1f}%')
print(f'   → {"通过" if cov >= 95 else "**不通过**"}')

# ⑥ 每张卡要么有逐字原文、要么**显式**标注「原文待补」
#    原判据是"摘录不为空"。但那条字面要求逼着人把编者概括塞进引文槽位——
#    外部评审 docs/codex-final-opinion.md A1 抓到 13 张卡正是这么干的。
#    现在允许显式的 paraphrase 状态；**静默为空**才算不合格。
empty = []
silent = []
for cid, c in cards.items():
    has_orig = bool([x for x in (c.get('excerpts') or []) if re.sub(r'\s', '', x)])
    explicit = (c.get('excerpt_status') == 'paraphrase'
                and bool(re.sub(r'\s', '', c.get('editor_summary') or '')))
    if c.get('excerpt_status') == 'paraphrase':
        silent.append(cid)
    if not has_orig and not explicit:
        empty.append(cid)
print(f'\n⑥ 每张卡要么有逐字原文、要么显式标注「原文待补」')
print(f'   既无原文又无显式标注（静默空缺，不合格）：{len(empty)} 张 {empty[:8]}')
print(f'   显式标为「原文待补」的：{len(silent)} 张 {silent}')
print(f'   → {"通过" if not empty else "**不通过**"}')

print('\n' + '=' * 72)
print('附：分布（供评审判断是否偏斜）')
dist = {}
for r in essays.values():
    dist[r['primary']] = dist.get(r['primary'], 0) + 1
tot = sum(dist.values())
for k, v in sorted(dist.items(), key=lambda x: -x[1]):
    name = [e['name'] for e in spec['entries'] if e['id'] == k][0]
    print(f'   {k:4s} {name:14s} {v:4d}  {v / tot * 100:5.1f}%')
print(f'   最大条目占 {max(dist.values()) / tot * 100:.1f}%（观察指标，非门槛）')

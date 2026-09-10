# -*- coding: utf-8 -*-
"""分类迁移预演（dry-run）：不改任何卡片，只报告「新分类会怎么分」。

用法：
    python scripts/classify_cards.py            # 打印报告
    python scripts/classify_cards.py --write    # 写 docs/classification-preview.md

报告内容：
  1. 每个条目的主归属张数 + 范畴分布
  2. 每个条目的「参见区」（同时谈该主题的其他条目）
  3. 故事体的分面覆盖
  4. 验证门槛是否通过
  5. 每个旧主题的迁移去向
"""
from __future__ import annotations

import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))

from taxonomy import build_scorer, classify, load_spec  # noqa: E402

WEB_DATA = ROOT / 'web' / 'data.json'
SEARCH = ROOT / 'web' / 'data' / 'search' / 'all.json'


def load() -> tuple[list[dict], dict[str, str]]:
    import json
    cards = json.load(open(WEB_DATA, encoding='utf-8'))['cards']
    corpus = {e['id']: e for e in json.load(open(SEARCH, encoding='utf-8'))}
    hay = {}
    for c in cards:
        hay[c['id']] = ' '.join([c.get('title', ''), c.get('cn', ''),
                                 corpus.get(c['id'], {}).get('text', '')])
    return cards, hay


def main() -> int:
    spec = load_spec()
    cards, hay = load()
    score = build_scorer(cards, spec, hay)
    entry = {e['id']: e for e in spec['entries']}
    facet = {f['id']: f for f in spec['facets']}

    results = {c['id']: classify(c, spec, score, hay) for c in cards}
    essay = [c for c in cards if c['type'] != 'case']
    story = [c for c in cards if c['type'] == 'case']

    out = []
    def p(line: str = ''):
        out.append(line)
        print(line)

    p('# 分类迁移预演（dry-run，未改动任何卡片）\n')
    p(f'规格：{len(spec["layers"])} 范畴 · {len(spec["entries"])} 条目 · '
      f'{len(spec["facets"])} 故事分面 · {len(spec["mapping"])} 条旧→新映射\n')

    # 1) 条目分布
    p('## 一、条目主归属分布（论述体 %d 张）\n' % len(essay))
    dist = Counter(r['primary'] for r in results.values() if r['primary'])
    unassigned = [cid for cid, r in results.items() if not r['primary'] and r['facets'] == []]
    p('| 条目 | 范畴 | 主归属 | 占比 | 参见（同时谈该主题的其他条目数） |')
    p('|---|---|---|---|---|')
    see_counts = defaultdict(Counter)
    for cid, r in results.items():
        if r['primary']:
            for s in r['see_also']:
                see_counts[r['primary']][s] += 1
    for e in spec['entries']:
        n = dist.get(e['id'], 0)
        if not n:
            continue
        top_see = ' · '.join(f'{entry[s]["name"]} {k}' for s, k in see_counts[e['id']].most_common(3))
        p(f'| {e["id"]} {e["name"]} | {e["layer"]} | {n} | {n/len(essay)*100:.1f}% | {top_see or "—"} |')
    p()
    layer_dist = Counter(entry[r['primary']]['layer'] for r in results.values() if r['primary'])
    p('范畴分布：' + ' · '.join(f'{k} {v}（{v/len(essay)*100:.0f}%）' for k, v in layer_dist.most_common()) + '\n')

    # 2) 故事分面
    p('## 二、故事体分面（%d 篇）\n' % len(story))
    fcount = Counter(f for c in story for f in results[c['id']]['facets'])
    covered = sum(1 for c in story if results[c['id']]['facets'])
    p('| 分面 | 类型 | 篇数 |')
    p('|---|---|---|')
    for f in spec['facets']:
        p(f'| {f["id"]} {f["name"]} | {f["kind"]} | {fcount.get(f["id"], 0)} |')
    p(f'\n分面覆盖率：{covered}/{len(story)}（{covered/len(story)*100:.1f}%）\n')

    # 3) 门槛
    p('## 三、验证门槛\n')
    checks = []
    biggest = dist.most_common(1)[0] if dist else ('', 0)
    story_covered = sum(1 for c in story if results[c['id']]['facets'])
    essay_no_primary = [cid for cid, r in results.items()
                        if not r['primary'] and cid not in {c['id'] for c in story}]
    checks.append(('每张论述卡有主归属', not essay_no_primary, f'未归属 {len(essay_no_primary)} 张'))
    small = [(entry[k]['name'], v) for k, v in dist.items()
             if v < 4 and not entry[k].get('overview')]
    checks.append(('无条目低于 4 张（总纲页不持卡）', not small,
                   f'{small or "无"}（低于 15 张的应标注为小条目）'))
    checks.append(('最大条目 ≤20%', biggest[1] / len(essay) <= 0.20,
                   f'{entry[biggest[0]]["name"]} {biggest[1]} 张（{biggest[1]/len(essay)*100:.1f}%）'))
    checks.append(('故事分面覆盖 ≥95%', story_covered / len(story) >= 0.95,
                   f'{story_covered}/{len(story)}（{story_covered/len(story)*100:.1f}%），未覆盖 {len(story)-story_covered} 篇'))
    empty = [c['id'] for c in cards if not ((c.get('excerpts') or [''])[0]).strip()]
    checks.append(('无空摘录卡', not empty, f'空摘录 {len(empty)} 张：{empty[:5]}'))
    for name, ok, detail in checks:
        p(f'- [{"PASS" if ok else "FAIL"}] {name} —— {detail}')
    p()

    # 4) 旧主题迁移去向
    p('## 四、旧主题迁移去向（核对新体系是否接得住）\n')
    p('| 旧主题 | 张数 | 主要落点 |')
    p('|---|---|---|')
    for old, m in spec['mapping'].items():
        ids = [c['id'] for c in cards if old in c.get('topics', [])]
        if not ids:
            continue
        lac = Counter()
        for cid in ids:
            r = results[cid]
            if r['primary']:
                lac[entry[r['primary']]['name']] += 1
            elif r['facets']:
                lac['故事体'] += 1
            else:
                lac['未归属'] += 1
        top = ' · '.join(f'{k} {v}' for k, v in lac.most_common(3))
        p(f'| {old} | {len(ids)} | {top} |')
    p()

    report = ROOT / 'docs' / 'classification-preview.md'
    if '--write' in sys.argv:
        report.write_text('\n'.join(out) + '\n', encoding='utf-8')
        print(f'\n已写入 {report}')
    return 0


if __name__ == '__main__':
    sys.exit(main())

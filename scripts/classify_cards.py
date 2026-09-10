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
    p('## 二、故事体分面（%d 篇，三个字段可多值）\n' % len(story))
    fcount = Counter(f for c in story for f in results[c['id']]['facets'])
    covered = sum(1 for c in story if results[c['id']]['facets'])
    p('| 字段 | 分面 | 篇数 |')
    p('|---|---|---|')
    for f in spec['facets']:
        p(f'| {f["field"]} | {f["id"]} {f["name"]} | {fcount.get(f["id"], 0)} |')
    p(f'\n分面覆盖率：{covered}/{len(story)}（{covered/len(story)*100:.1f}%）')
    by_field = Counter()
    for c in story:
        for fld in {next(f["field"] for f in spec["facets"] if f["id"] == fid)
                    for fid in results[c['id']]['facets']}:
            by_field[fld] += 1
    p('字段覆盖：' + ' · '.join(f'{k} {v}（{v/len(story)*100:.0f}%）' for k, v in by_field.most_common()))
    multi = sum(1 for c in story if len({next(f["field"] for f in spec["facets"] if f["id"] == fid)
                                         for fid in results[c['id']]['facets']}) >= 2)
    p(f'至少落进两个字段：{multi}/{len(story)}（{multi/len(story)*100:.1f}%）\n')

    # 3) 门槛
    p('## 三、验证门槛\n')
    checks = []
    biggest = dist.most_common(1)[0] if dist else ('', 0)
    story_covered = sum(1 for c in story if results[c['id']]['facets'])
    essay_no_primary = [cid for cid, r in results.items()
                        if not r['primary'] and cid not in {c['id'] for c in story}]
    pending = [cid for cid, r in results.items() if r.get('source') == 'pending']
    stray = [cid for cid in essay_no_primary if cid not in pending]
    checks.append(('论述卡要么定案、要么登记待裁决', not stray,
                   f'无主归属 {len(essay_no_primary)} 张（其中已登记待裁决 {len(pending)} 张）'
                   + (f'；⚠ 未登记 {stray}' if stray else '')))
    if pending:
        p(f'  · 待裁决 {len(pending)} 张（旧标签可映射、但原文无任何关键词证据，按元规则不强行定案）：'
          + ' · '.join(pending))
    checks.append(('故事分面覆盖 ≥95%', story_covered / len(story) >= 0.95,
                   f'{story_covered}/{len(story)}（{story_covered/len(story)*100:.1f}%），未覆盖 {len(story)-story_covered} 篇'))
    empty = [c['id'] for c in cards if not ((c.get('excerpts') or [''])[0]).strip()]
    checks.append(('无空摘录卡', not empty, f'空摘录 {len(empty)} 张：{empty[:5]}'))
    for name, ok, detail in checks:
        p(f'- [{"PASS" if ok else "FAIL"}] {name} —— {detail}')

    # 观察指标（不作门槛）：分布是否异常
    p('\n观察指标（不作正确性门槛，只用于发现异常）：\n')
    p(f'- 最大条目：{entry[biggest[0]]["name"]} {biggest[1]} 张（{biggest[1]/len(essay)*100:.1f}%）')
    small = [(entry[k]['name'], v) for k, v in dist.items() if v < 15]
    tiny = [(entry[k]['name'], v) for k, v in dist.items() if v < 4]
    p(f'- 低于 15 张（页面标注「小条目」）：{" · ".join(f"{n} {v}" for n, v in sorted(small, key=lambda x: x[1])) or "无"}')
    p(f'- 低于 4 张（须人工确认是否条目本身有问题）：{" · ".join(f"{n} {v}" for n, v in tiny) or "无"}')
    zero = [e['id'] + ' ' + e['name'] for e in spec['entries'] if not e['tag'] and not dist.get(e['id'])]
    p(f'- 零主归属条目：{" · ".join(zero) or "无"}')
    p()

    # 3b) 复分标签
    tag_entries = [e for e in spec['entries'] if e['tag']]
    if tag_entries:
        p('## 三·补、复分标签（不参与主归属分区）\n')
        for e in tag_entries:
            hit = [cid for cid, r in results.items() if e['id'] in r['tags']]
            essay_hit = [cid for cid in hit if results[cid]['primary']]
            story_hit = [cid for cid in hit if results[cid]['facets']]
            p(f'- **{e["id"]} {e["name"]}**：{len(hit)} 张（论述 {len(essay_hit)} · 故事 {len(story_hit)}）；'
              f'这些卡的主归属仍由内容决定')
        p()

    # 3c) 人工裁定的自检：哪些裁定算法其实已经同意（同意 = 这条裁定暂时没用上）
    if spec.get('override'):
        no_op = dict(spec)
        no_op['override'] = {}
        agree, disagree = [], []
        for cid, ov in spec['override'].items():
            card = next(c for c in cards if c['id'] == cid)
            auto = classify(card, no_op, score, hay)['primary']
            (agree if auto == ov['primary'] else disagree).append((cid, auto, ov['primary']))
        p('## 三·补二、人工裁定自检\n')
        p(f'- 算法已能判对（裁定暂时没用上）：{len(agree)} 条'
          + ('（' + ' · '.join(c for c, _, _ in agree) + '）' if agree else ''))
        p(f'- 算法仍判错（裁定在起作用）：{len(disagree)} 条'
          + ('（' + ' · '.join(f'{c}：算法 {a} → 裁定 {m}' for c, a, m in disagree) + '）' if disagree else ''))
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

    # 5. 人工复核清单：列出**算法推翻了旧标签**的卡片（最可能判错的一批）
    review = []
    for c in cards:
        r = results[c['id']]
        if c['type'] == 'case' or r.get('source') not in ('override', 'none'):
            continue
        hits = sorted(((score(entry[e['id']]['keywords'], c['id']), e['id']) for e in spec['entries']),
                      key=lambda x: (-x[0], x[1]))
        alts = ' · '.join(f'{entry[eid]["name"]}（{s:.1f}）' for s, eid in hits[:3] if s > 0 and eid != r['primary'])
        review.append((c, r, alts or '（除建议条目外无其他关键词命中）'))
    review.sort(key=lambda x: x[0]['id'])
    confirmed = [c for c in cards if c['type'] != 'case' and results[c['id']].get('source') == 'prior']
    rl = ['# 分类人工复核清单', '',
          f'**算法推翻了旧标签**的卡片，共 {len(review)} 张。',
          '',
          '判断依据：新规则下旧标签只是加分先验（首选 +2.5 / 次选 +1.0）；',
          '下列卡片的文本证据足以压过先验，所以改判——改判可能是对的（旧标签本来就粗），',
          '也可能是关键词误伤。逐条看一遍是最省事的保险。',
          '',
          f'> 另有 **{len(confirmed)} 张**由旧标签先验定下（算法没有独立验证过它们），',
          '> 它们不进这张清单，改由 `docs/classification-audit.md` 的**盲审抽样**抽查。',
          '', '| 卡片 | 类型 | 旧标签 | 新主归属 | 判断依据 | 关键词命中的其他条目 |',
          '|---|---|---|---|---|---|']
    for c, r, alts in review:
        prim = f"{r['primary']} {entry[r['primary']]['name']}" if r['primary'] else '—'
        rl.append(f"| {c['id']} | {c['type']} | {', '.join(c.get('topics', []))} | {prim} | {r['reason']} | {alts} |")
    rl += ['', '## 逐条内容（判断用）', '']
    for c, r, alts in review:
        prim = f"{r['primary']} {entry[r['primary']]['name']}" if r['primary'] else '—'
        rl += [f"### {c['id']}　{c.get('title', '')}", '',
               f"- 旧标签：{', '.join(c.get('topics', []))}",
               f"- 建议：**{prim}**（{r['reason']}）",
               f"- 其他命中：{alts}",
               f"- 转述：{(c.get('cn') or '')[:160]}",
               f"- 出处：{(c.get('ref') or '')[:90]}", '']
    review_path = ROOT / 'docs' / 'classification-review.md'
    if '--write' in sys.argv:
        review_path.write_text('\n'.join(rl) + '\n', encoding='utf-8')
        print(f'已写入 {review_path}（{len(review)} 张待复核）')

    # 6) 盲审抽样：从**全部论述卡**分层抽 100 张，隐藏旧标签与算法答案
    #
    # 样本范围从「由旧标签直接认定的卡」扩到「全部论述卡」：只审前者只能回答
    # 「旧标签准不准」，审全部才能回答「这套分类准不准」——后者才是要报的数。
    import random
    rng = random.Random(20260910)
    essay_all = [c for c in cards if c['type'] != 'case']
    buckets: dict[str, list[dict]] = defaultdict(list)
    for c in essay_all:
        buckets[results[c['id']]['primary']].append(c)
    quota = {k: max(1, round(len(v) / len(essay_all) * 100)) for k, v in buckets.items()}
    sample: list[dict] = []
    for k, v in buckets.items():
        sample += rng.sample(v, min(quota[k], len(v)))
    sample = sample[:100]
    sample.sort(key=lambda c: c['id'])
    by_source = Counter(results[c['id']].get('source', '?') for c in sample)
    ap = ['# 分类盲审抽样（100 张）', '',
          f'样本来源：**全部 {len(essay_all)} 张论述卡**（不只是"由旧标签认定"的那一批）。',
          '分层方式：按算法给出的主归属等比例分配名额，随机种子 20260910。',
          '',
          '**审读方法**：先只看「原文摘录 / 编辑转述」，自己判断属于哪一条，写好「我的判断」；',
          '再展开「对答案」看算法结论与旧标签，把分歧写进「分歧说明」。',
          '旧标签本身就是要被检验的对象，所以它只出现在答案区。',
          '',
          f'样本数：{len(sample)} 张。按算法"怎么定下来的"分布：'
          + ' · '.join(f'{k} {v}' for k, v in by_source.most_common()),
          '', '盲审结果的汇总写在 `docs/classification-audit-result.md`。', '']
    for i, c in enumerate(sample, 1):
        r = results[c['id']]
        ap += [f'## {i}. {c["id"]}　{c.get("title", "")}', '',
               f'- 原文摘录：{(c.get("excerpts") or [""])[0]}',
               f'- 编辑转述：{c.get("cn") or ""}',
               f'- 出处：{c.get("ref") or ""}',
               '- 我的判断：______',
               '- 分歧说明：______', '',
               '<details><summary>对答案</summary>', '',
               f'算法：{r["primary"]} {entry[r["primary"]]["name"]}（{r["reason"]}，来源 {r.get("source")}）｜'
               f'旧标签：{", ".join(c.get("topics", []))}',
               '</details>', '']
    audit_path = ROOT / 'docs' / 'classification-audit.md'
    if '--write' in sys.argv:
        audit_path.write_text('\n'.join(ap) + '\n', encoding='utf-8')
        print(f'已写入 {audit_path}（{len(sample)} 张盲审样本）')
    return 0


if __name__ == '__main__':
    sys.exit(main())

# -*- coding: utf-8 -*-
"""路径验收：读者带着一个问题来，新分类能不能把他带到内容面前。

用法：
    python scripts/path_test.py            # 跑全部题目
    python scripts/path_test.py 劳动        # 只跑一道

设计原则：**本脚本必须调用 scripts/taxonomy.py**，不许自己再抄一份条目表。
（第一版验收脚本硬编码了一份条目，规格改了它不知道，于是同一天里出现了两套数字。）
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))

from taxonomy import build_scorer, classify, load_spec  # noqa: E402

# 读者的问题 → 探测词（读者会这么搜）+ 对照的旧标签（迁移前他是怎么找到的）
QUESTIONS = [
    {
        'q': '他对劳动教育的看法',
        'probe': ['劳动', '手工', '双手', '耕种', '收获', '创造'],
        'old': 'labor-education',
    },
    {
        'q': '后进生 / 学习困难的孩子怎么办',
        'probe': ['学习困难', '后进生', '差生', '落后', '不及格', '补课', '困难学生', '可教育性', '难教', '弱生'],
        'old': 'learning-difficulties',
    },
    {
        'q': '他怎么看待分数与评价',
        'probe': ['分数', '评价', '评分', '表扬', '批评', '检查知识'],
        'old': 'assessment-grading',
    },
    {
        'q': '他的美育与自然教育',
        'probe': ['美', '音乐', '绘画', '审美', '大自然', '思维课', '森林'],
        'old': 'aesthetic-nature-education',
    },
]


def load():
    cards = json.load(open(ROOT / 'web' / 'data.json', encoding='utf-8'))['cards']
    corpus = {e['id']: e for e in json.load(
        open(ROOT / 'web' / 'data' / 'search' / 'all.json', encoding='utf-8'))}
    hay = {c['id']: ' '.join([c.get('title', ''), c.get('cn', ''),
                              corpus.get(c['id'], {}).get('text', '')]) for c in cards}
    return cards, hay


def main() -> int:
    spec = load_spec()
    cards, hay = load()
    score = build_scorer(cards, spec, hay)
    entry = {e['id']: e for e in spec['entries']}
    facet = {f['id']: f for f in spec['facets']}
    res = {c['id']: classify(c, spec, score, hay) for c in cards}
    probe = sys.argv[1] if len(sys.argv) > 1 else None

    bad = 0
    for item in QUESTIONS:
        if probe and probe not in item['q']:
            continue
        ids = [c['id'] for c in cards if any(w in hay[c['id']] for w in item['probe'])]
        print(f'=== 问题：{item["q"]} ===')
        old = [c['id'] for c in cards if item['old'] in c.get('topics', [])]
        print(f'迁移前：点旧标签「{item["old"]}」→ {len(old)} 张')
        print(f'全库提到相关词的卡片：{len(ids)} 张\n')

        core = Counter(res[i]['primary'] for i in ids if res[i]['primary'])
        stories = [i for i in ids if res[i]['facets']]
        print('路径 ①：**主归属**落点（第一跳，读者的落脚页）')
        for eid, n in core.most_common():
            print(f'    {eid} {entry[eid]["name"]}　{n} 张')
        print(f'\n路径 ②：**参见区**（主归属在别处、但正文谈了这件事的卡片）')
        see = Counter(s for i in ids if res[i]['primary'] for s in res[i]['see_also'])
        for eid, n in see.most_common(6):
            print(f'    {eid} {entry[eid]["name"]}　{n} 张')
        print('\n路径 ③：**故事分面**（故事体不谈主张，谈处境）')
        fld = Counter(f for i in stories for f in res[i]['facets'])
        for fid, n in fld.most_common(6):
            print(f'    {facet[fid]["field"]}·{facet[fid]["name"]}　{n} 篇')

        tags = {e['id']: [i for i in ids if e['id'] in res[i]['tags']]
                for e in spec['entries'] if e['tag']}
        if any(tags.values()):
            print('\n路径 ④：**复分标签**（不参与分区，但必须是可点的入口）')
            for eid, hit in tags.items():
                if hit:
                    print(f'    {eid} {entry[eid]["name"]}　{len(hit)} 张')

        print(f'\n合计可达：{len(ids)} 张（迁移前 {len(old)} 张）')

        miss = [i for i in old if i not in set(ids)]
        if miss:
            print(f'⚠ 旧标签是它、但全文不含任何探测词的卡片：{len(miss)} 张')
            print('   （这些卡按内容归位，不再出现在这条路径上——旧标签在这一批上本来就是粗的）')
            for i in miss[:5]:
                c = next(c for c in cards if c['id'] == i)
                r = res[i]
                where = r['primary'] and f'{r["primary"]} {entry[r["primary"]]["name"]}' or '故事分面'
                print(f'     {i}  {c.get("title", "")[:34]}  → 现在归 {where}')
        print()


if __name__ == '__main__':
    sys.exit(main())

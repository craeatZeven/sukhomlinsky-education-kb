# -*- coding: utf-8 -*-
"""路径验收（生产版）：拿 `classification.json` 这份**实际上网的产物**来验收。

用法：
    python scripts/path_test_prod.py            # 跑全部题目
    python scripts/path_test_prod.py 劳动        # 只跑一道

为什么要有这个脚本，而不是改 `path_test.py`：
`path_test.py` 跑的是 `taxonomy.py` 里的**关键词** `classify()`——那是被淘汰的方法。
它当初的用意是"验收脚本不许自己抄一份条目表"，同一条纪律现在意味着：
**验收必须读生产的产物**，不能读一个跟生产无关的平行实现。
否则验收通过、上线的东西却是另一套。

读者带着问题来，四条路要都能走通：
    ① 条目页的主归属    ② 条目页的参见区    ③ 故事分面    ④ 复分标签
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))

from taxonomy import load_spec  # noqa: E402

QUESTIONS = [
    {'q': '他对劳动教育的看法',
     'probe': ['劳动', '手工', '双手', '耕种', '收获', '创造'],
     'old': 'labor-education',
     'main': ['A11'], 'near': ['A12'], 'facets': ['S12', 'S9']},
    {'q': '后进生 / 学习困难的孩子怎么办',
     'probe': ['学习困难', '后进生', '差生', '落后', '不及格', '补课', '困难学生',
               '可教育性', '难教', '弱生'],
     'old': 'learning-difficulties',
     'main': ['A18'], 'near': ['A15', 'A23', 'A7'], 'facets': ['S8']},
    {'q': '他怎么看待分数与评价',
     'probe': ['分数', '评价', '评分', '表扬', '批评', '检查知识'],
     'old': 'assessment-grading',
     'main': ['A16'], 'near': ['A20'], 'facets': ['S17']},
    {'q': '他的美育与自然教育',
     'probe': ['美', '音乐', '绘画', '审美', '大自然', '思维课', '森林'],
     'old': 'aesthetic-nature-education',
     'main': ['A14', 'A12'], 'near': ['A19'], 'facets': ['S11', 'S6']},
]


def main() -> int:
    spec = load_spec()
    cls = json.load(open(ROOT / 'classification.json', encoding='utf-8'))
    cards = json.load(open(ROOT / 'web' / 'data.json', encoding='utf-8'))['cards']
    corpus = {e['id']: e for e in json.load(
        open(ROOT / 'web' / 'data' / 'search' / 'all.json', encoding='utf-8'))}
    byid = {c['id']: c for c in cards}
    hay = {c['id']: ' '.join([c.get('title', ''), c.get('cn', ''),
                              corpus.get(c['id'], {}).get('text', '')]) for c in cards}
    entry = {e['id']: e for e in spec['entries']}
    facet = {f['id']: f for f in spec['facets']}
    probe = sys.argv[1] if len(sys.argv) > 1 else None

    for item in QUESTIONS:
        if probe and probe not in item['q']:
            continue
        # 「读者全库检索这组词」能捞到的候选集：这是内容量的上限
        ids = [c['id'] for c in cards if any(w in hay[c['id']] for w in item['probe'])]
        old = [c['id'] for c in cards if item['old'] in (c.get('topics') or [])]
        print(f'=== 问题：{item["q"]} ===')
        print(f'迁移前：点旧标签「{item["old"]}」→ {len(old)} 张')
        print(f'全库提到相关词的卡片（内容上限）：{len(ids)} 张\n')

        prim = Counter(cls[i]['primary'] for i in ids if cls[i].get('primary'))
        print('路径①：**主归属**落点（读者第一跳落脚在哪个条目页）')
        for eid, n in prim.most_common():
            print(f'    {eid} {entry[eid]["name"]}　{n} 张')

        see = Counter(s for i in ids for s in (cls[i].get('seealso') or []))
        print('\n路径②：**参见区**（主归属在别处、但正文也谈了这件事）')
        if see:
            for eid, n in see.most_common(6):
                print(f'    {eid} {entry[eid]["name"]}　{n} 张')
        else:
            print('    （无）')

        stories = [i for i in ids if cls[i].get('facets')]
        fld = Counter(f for i in stories for f in cls[i]['facets'])
        print('\n路径③：**故事分面**（故事体不谈主张，谈处境）')
        for fid, n in fld.most_common(6):
            print(f'    {facet[fid]["field"]}·{facet[fid]["name"]}　{n} 篇')

        print(f'\n合计可达：{len(ids)} 张（迁移前 {len(old)} 张）')

        # 关键区分：**分类路径的到达数** ≠ **全文检索的命中数**。
        # 上面那个 len(ids) 是"全库正文提到这组词"，那是内容上限，不是分类能带到的量。
        # 分类是**编过的**结构，本来就比全文检索窄——把两个数混着说会严重高估。
        main_ids = [i for i in ids if cls[i].get('primary') in item['main']]
        see_ids = [i for i in ids if set(cls[i].get('seealso') or []) & set(item['main'])]
        # A18 是复分标签：不进 primary / seealso，只按标记算
        tag_ids = [i for i in ids if set(cls[i].get('tags') or []) & set(item['main'])]
        facet_ids = [i for i in ids if set(cls[i].get('facets') or []) & set(item['facets'])]
        path_total = len(set(main_ids) | set(see_ids) | set(tag_ids) | set(facet_ids))
        print(f'\n--- 走分类路径实际能带到的（这才是"从条目页走进去"的量）---')
        print(f'    主归属{"、".join(item["main"])}：{len(main_ids)} 张')
        print(f'    参见区里挂着{"、".join(item["main"])}：{len(see_ids)} 张')
        if tag_ids:
            print(f'    复分标签：{len(tag_ids)} 张')
        print(f'    分面{"、".join(item["facets"])}：{len(facet_ids)} 篇')
        print(f'    → 分类路径合计：**{path_total} 张**')
        print(f'    （对照：全库正文提到相关词 {len(ids)} 张 = 全文检索的上限，'
              f'不等于分类带得到的量；旧标签给 {len(old)} 张）')
        print(f'    分类路径比全文检索窄 {len(ids) - path_total} 张——'
              f'这是应该的：分类是编过的结构，不是检索索引。')

        # 旧标签是它、但四条路都到不了的卡片
        fell = []
        for i in old:
            got = cls[i].get('primary')
            in_see = any(i in (cls[j].get('seealso') or []) for j in ids)
            if not got and not in_see and not cls[i].get('facets') and not cls[i].get('tags'):
                fell.append(i)
        print(f'\n旧标签命中、但四条路都到不了的卡片：{len(fell)} 张')
        for i in fell[:6]:
            print(f'     {i}  {byid[i].get("title", "")[:34]}'
                  f'  → 现在归 {cls[i].get("primary") or "故事体，无分面"}')

        # 最该看的一个数：**旧标签能到、这条问题路径反而到不了的卡**
        # 这是"变窄"的代价，必须量出来，不能因为不好看就不报
        path_set = set(main_ids) | set(see_ids) | set(tag_ids) | set(facet_ids)
        lost = [i for i in old if i not in path_set]
        print(f'\n**旧标签能到、这条路径到不了的：{len(lost)} 张**'
              f'（占旧标签的 {len(lost) / len(old) * 100:.0f}% 就是"变窄"的代价）')
        for i in lost[:8]:
            print(f'     {i}  {byid[i].get("title", "")[:30]}  → 现归 '
                  f'{cls[i].get("primary") or "故事体"}'
                  f'{"/分面 " + ",".join(cls[i]["facets"]) if cls[i].get("facets") else ""}')
        print()

    return 0


if __name__ == '__main__':
    sys.exit(main())

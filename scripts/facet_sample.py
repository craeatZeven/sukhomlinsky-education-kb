# -*- coding: utf-8 -*-
"""按 docs/facet-labeling-plan.md §三 的抽样规则，抽 60 张故事卡做独立判读复核。

抽样规则（跑数之前就写死在计划里）：固定随机种子 **20260911**，从全部故事卡里抽 60 张，
抽完不改。判读包**只给标题 / 原文摘录 / 编辑转述，不给关键词表**——
给了关键词表它只是在复述关键词，测不出关键词的偏差。
"""
from __future__ import annotations

import json
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from taxonomy import load_spec  # noqa: E402

SEED = 20260911
N = 60
OUT = ROOT / 'local_working_copy' / 'facet-validate'


def main() -> None:
    spec = load_spec()
    cls = json.load(open(ROOT / 'classification.json', encoding='utf-8'))
    cards = {c['id']: c for c in json.load(
        open(ROOT / 'web' / 'data.json', encoding='utf-8'))['cards']}

    cases = sorted(cid for cid, v in cls.items() if v.get('type') == 'case')
    rng = random.Random(SEED)
    sample = sorted(rng.sample(cases, N))

    OUT.mkdir(parents=True, exist_ok=True)

    # 给判读者的包：只有卡片内容，**不含关键词、不含已算出的分面**
    L = [f'# 故事分面判读 · 抽样 {N} 张（种子 {SEED}）', '',
         '请按下面给出的「三个字段、十七个分面」给每张卡打标记。', '',
         '## 分面表', '']
    for f in spec['facets']:
        L.append(f"- **{f['id']}　{f['name']}**（{f['field']}）")
    L += ['', '## 判读要求', '',
          '1. 三个字段**各自可多选**：角色（谁在场）、场景（在哪发生）、事件或情绪（发生了什么）。',
          '2. 一张卡可以落进多个分面，也可以落进多个字段。',
          '3. **只看卡片内容判断**，不要因为某个词出现就机械命中——'
          '要问"这张卡讲的事情里，这些东西真的在场吗"。',
          '4. 如果一个分面都不合适，就写 `NONE`（这本身是有用的信息，不要为了凑数硬选）。',
          '5. 输出每张一行，格式：`sk-XXXX | S3,S6 | 一句话理由`',
          '', '---', '']
    for cid in sample:
        c = cards[cid]
        exps = c.get('excerpts') or []
        L += [f'## {cid}', '',
              f"**标题**：{c.get('title', '')}", '',
              f'**原文摘录**：{" ".join(exps)}', '',
              f"**编辑转述**：{c.get('cn') or ''}", '',
              f"**出处**：{c.get('ref') or ''}", '']
    (OUT / 'sample.md').write_text('\n'.join(L), encoding='utf-8')

    # 关键词算出来的答案，判读时不能看，事后比对才用
    key = {cid: sorted(cls[cid].get('facets') or []) for cid in sample}
    (OUT / 'sample-key.json').write_text(
        json.dumps({'seed': SEED, 'ids': sample, 'keyword': key},
                   ensure_ascii=False, indent=1), encoding='utf-8')

    print(f'抽样 {len(sample)} 张（种子 {SEED}）→ {OUT / "sample.md"}')
    print(f'关键词答案（判读时不可看）→ {OUT / "sample-key.json"}')
    print('卡片：' + ' '.join(sample))


if __name__ == '__main__':
    main()

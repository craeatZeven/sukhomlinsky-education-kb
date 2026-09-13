# -*- coding: utf-8 -*-
"""给 116 张**教学案例**挂上「它属于哪些条目」，让它们回到主题路径上。

背景（外部评审 docs/codex-final-opinion.md A3·第三处）：
`type: case` 把两种东西混成了一类——
  · **儿童文学** 557 张（《做人的故事》541 等），谈的是处境，走分面就对了；
  · **教学案例 / 教育叙事** 116 张（五卷本、《给教师的建议》、On Education…），
    它们不是儿童文学，而是「这条主张在教学中怎样发生」的实例。
现在这 116 张不在任何条目页上，研究劳动教育的人在 A11 页看不到这些实例。

设计：**不推翻 case 的定义**（case 仍然不持「主归属」，它没有中心主张），
另给一个多值字段 `case_entries` ——「这张案例可以作哪几条的例证」。
条目页据此多一个「相关案例」区。

用法：
    python scripts/case_entries.py packets [--per 25]      # 出题
    python scripts/case_entries.py merge <输出文件> ...      # 收卷，写回 classification.json
    python scripts/case_entries.py check                    # 只统计，不改
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from taxonomy import load_spec  # noqa: E402

WORK = ROOT / 'local_working_copy' / 'llm-case-entries'
RESULT = ROOT / 'classification.json'

# 儿童文学：给孩子读的短故事，按出处区分，不靠猜
CHILD_LIT = {
    'zuo-ren-de-gu-shi-zh',
    'ba-xin-xian-gei-hai-zi-zh',
    'to-children-i-give-my-heart',
    'singing-feather',
}
LINE_RE = re.compile(r'^(sk-\d{4})\s*\|\s*([^|]*?)\s*\|\s*(.*?)\s*$')


def load():
    cards = {c['id']: c for c in json.load(
        open(ROOT / 'web' / 'data.json', encoding='utf-8'))['cards']}
    cls = json.load(open(RESULT, encoding='utf-8'))
    return cards, cls


def teaching_cases(cards, cls) -> list[str]:
    return sorted(cid for cid, rec in cls.items()
                  if rec.get('type') == 'case'
                  and cards.get(cid, {}).get('source') not in CHILD_LIT)


def cmd_packets(per: int = 25):
    spec = load_spec()
    cards, cls = load()
    ids = teaching_cases(cards, cls)
    WORK.mkdir(parents=True, exist_ok=True)
    n = 0
    for i in range(0, len(ids), per):
        chunk = ids[i:i + per]
        n += 1
        L = [f'# 教学案例挂条目 · 第 {n} 包（{len(chunk)} 张）', '']
        for cid in chunk:
            c = cards[cid]
            L += [f'## {cid}', '',
                  f"**标题**：{c.get('title', '')}", '',
                  f"**原文摘录**：{' '.join(c.get('excerpts') or [])}", '',
                  f"**编辑转述**：{c.get('cn') or ''}", '',
                  f"**出处**：{c.get('ref') or ''}", '']
        (WORK / f'batch-{n:02d}.md').write_text('\n'.join(L), encoding='utf-8')

    T = ['# 教学案例挂条目 · 任务说明', '',
         '下面是 **116 张教学案例 / 教育叙事**（不是儿童故事）。它们和论述卡不同：',
         '**没有自己的中心主张，讲的是「某件事在教学中怎样发生」**。', '',
         '请为每张案例挑 **1–3 个条目**，回答同一个问题：', '',
         '> **这张案例，可以作哪几条的例证？**', '',
         '注意：',
         '1. **不是**问"它讲了什么道理"，而是问"读哪一条的人会需要看这个例子"。',
         '2. 只给**确实相关**的；1 个也行，宁可少给不要凑数。',
         '3. 用下面的条目表，只写编号。', '',
         '## 条目表', '']
    for e in spec['entries']:
        mark = '（复分标签，可作标记用）' if e.get('tag') else ''
        T.append(f"- **{e['id']}　{e['name']}**{mark}：{e.get('include', '').strip()}")
    T += ['', '## 输出格式', '',
          '每张卡一行，三栏：', '',
          '```', 'sk-XXXX | A11, A18 | 一句话理由（不超过 30 字）', '```', '',
          '编号用逗号分隔、不加空格；**不要**写代码块围栏、不要表头。']
    (WORK / 'TASK.md').write_text('\n'.join(T), encoding='utf-8')
    print(f'{len(ids)} 张教学案例 → {n} 个包（每包 {per} 张）在 {WORK}')


def cmd_merge(files: list[str]):
    spec = load_spec()
    valid = {e['id'] for e in spec['entries']}
    got, bad = {}, []
    for a in files:
        p = Path(a)
        for ln, line in enumerate(p.read_text(encoding='utf-8').splitlines(), 1):
            line = line.strip()
            if not line.startswith('sk-'):
                continue
            m = LINE_RE.match(line)
            if not m:
                bad.append(f'{p.name}:{ln} 格式不符：{line[:60]}')
                continue
            cid, cell, why = m.groups()
            codes = [x.strip() for x in re.split(r'[,，、\s]+', cell) if x.strip()]
            codes = [c for c in codes if c not in ('NONE', '—', '-', '无')]
            unknown = [c for c in codes if c not in valid]
            if unknown:
                bad.append(f'{p.name}:{ln} {cid} 非法条目号 {unknown}')
                continue
            if not codes:
                bad.append(f'{p.name}:{ln} {cid} 一个条目都没给')
                continue
            got[cid] = {'entries': codes[:3], 'why': why}
    if bad:
        print(f'⚠ {len(bad)} 行不合规，**未写文件**：')
        for b in bad[:10]:
            print('   ' + b)
        return 1
    cls = json.loads(RESULT.read_text(encoding='utf-8'))
    cards = {c['id']: c for c in json.load(
        open(ROOT / 'web' / 'data.json', encoding='utf-8'))['cards']}
    n = 0
    for cid, v in got.items():
        if cid in cls and cls[cid].get('type') == 'case':
            cls[cid]['case_entries'] = v['entries']
            cls[cid]['case_entries_why'] = v['why']
            n += 1
    RESULT.write_text(json.dumps(cls, ensure_ascii=False, indent=1), encoding='utf-8')
    print(f'已给 {n} 张教学案例挂上条目 → {RESULT}\n')
    cmd_check()
    return 0


def cmd_check():
    cards, cls = load()
    ids = teaching_cases(cards, cls)
    done = [c for c in ids if cls[c].get('case_entries')]
    print(f'教学案例 {len(ids)} 张，已挂条目的 {len(done)} 张'
          f'（{len(done) / len(ids) * 100:.1f}%）')
    from collections import Counter
    c = Counter()
    for cid in done:
        for e in cls[cid]['case_entries']:
            c[e] += 1
    print('每个条目能多看到多少张案例：')
    for code, n in c.most_common():
        print(f'  {code} {n}')
    return 0


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'check'
    if cmd == 'packets':
        per = 25
        if '--per' in sys.argv:
            per = int(sys.argv[sys.argv.index('--per') + 1])
        cmd_packets(per)
    elif cmd == 'merge':
        sys.exit(cmd_merge(sys.argv[2:]))
    else:
        sys.exit(cmd_check())

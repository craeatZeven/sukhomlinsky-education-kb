# -*- coding: utf-8 -*-
"""Generate docs/coverage-volumes.md: card counts per five-volume work.

Reads cards with source xuan-ji-zh-vol1..vol5, parses the work title from the
ref (second 《...》 in the ref string), and writes a coverage report.

Usage:
    python scripts/coverage_volumes.py
"""
from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CARDS = ROOT / 'cards'
OUT = ROOT / 'docs' / 'coverage-volumes.md'
VOLUME_SOURCES = {f'xuan-ji-zh-vol{i}' for i in range(1, 6)}


def read(path: Path) -> str:
    return path.read_text(encoding='utf-8')


def frontmatter(text: str) -> dict:
    m = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    if not m:
        return {}
    fm: dict = {}
    current = None
    for line in m.group(1).splitlines():
        if re.match(r'^[A-Za-z_]+:', line):
            k, v = line.split(':', 1)
            current = k.strip()
            fm[current] = v.strip()
        elif line.startswith('  - ') and current is not None:
            fm.setdefault(current, '')
            fm[current] += (',' if fm[current] else '') + line.strip()[2:].strip()
    return fm


def clean(v: str) -> str:
    v = (v or '').strip()
    if len(v) >= 2 and v[0] == '"' and v[-1] == '"':
        return v[1:-1]
    return v


def work_from_ref(ref: str) -> str:
    found = re.findall(r'《([^》]+)》', ref)
    # first 《...》 is the five-volume set; second is normally the work inside it
    if len(found) >= 2:
        work = found[1]
    elif found:
        work = found[0]
    else:
        return '（未标注）'
    if '苏霍姆林斯基选集' in work:
        # e.g. 《苏霍姆林斯基选集（五卷本）第1卷·培养集体的方法》
        if '·' in work:
            return work.split('·', 1)[1].strip()
        # e.g. 《苏霍姆林斯基选集（五卷本）第2卷》，《怎样培养真正的人》...
        if len(found) >= 3:
            return found[2].strip()
        return '（未标注）'
    return work.strip()


def main() -> int:
    counts: dict[str, Counter] = {f'vol{i}': Counter() for i in range(1, 6)}
    unlabeled: dict[str, list[str]] = defaultdict(list)
    total = 0

    for p in sorted(CARDS.glob('*.md')):
        if p.name.startswith('_'):
            continue
        fm = frontmatter(read(p))
        src = clean(fm.get('source', ''))
        if src not in VOLUME_SOURCES:
            continue
        total += 1
        vol = src.replace('xuan-ji-zh-', '')
        ref = clean(fm.get('ref', ''))
        work = work_from_ref(ref)
        counts[vol][work] += 1
        if work == '（未标注）':
            unlabeled[vol].append(p.name)

    lines: list[str] = []
    lines.append('# 五卷本覆盖清单 Coverage by Work')
    lines.append('')
    lines.append('> 由 `scripts/coverage_volumes.py` 生成。按卡片 ref 中出现的作品名统计。')
    lines.append('> 说明：这里统计的是“已有卡片的来源分布”，不等于“全书逐章覆盖”；逐章缺口需要进一步人工审计。')
    lines.append('')
    lines.append(f'- 五卷本卡片总数：**{total}**')
    lines.append('')
    for i in range(1, 6):
        vol = f'vol{i}'
        lines.append(f'## 第 {i} 卷')
        lines.append('')
        lines.append('| 作品/章节 | 卡片数 |')
        lines.append('|---|---:|')
        for work, n in counts[vol].most_common():
            lines.append(f'| {work} | {n} |')
        lines.append('')
        if unlabeled[vol]:
            lines.append(f'> 未从 ref 解析出作品名的卡片：{len(unlabeled[vol])} 张')
            lines.append('')
    lines.append('## 后续审计建议')
    lines.append('')
    lines.append('- 以每卷目录为基准，逐章标记：已有卡 / 可补卡 / 暂无合法全文。')
    lines.append('- 优先补教育思想密度高、现有卡少的章节。')
    lines.append('- 英文/电子本同样需要按章节建立覆盖表。')

    OUT.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'wrote {OUT}')
    print(f'total_volume_cards={total}')
    for i in range(1, 6):
        print(f'vol{i}: {sum(counts[f"vol{i}"].values())} cards / {len(counts[f"vol{i}"])} works')
    return 0


if __name__ == '__main__':
    sys.exit(main())

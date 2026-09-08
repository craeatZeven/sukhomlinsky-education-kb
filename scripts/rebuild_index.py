# -*- coding: utf-8 -*-
"""Rebuild INDEX.md cards table and topic counts from cards/ frontmatter.

Preserves the source table and topic order/descriptions already in INDEX.md.
Run after adding/removing cards:
    python scripts/rebuild_index.py
"""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / 'INDEX.md'
CARDS = ROOT / 'cards'


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
            v = v.strip().strip('"')
            fm[current] = v
        elif line.startswith('  - ') and current is not None:
            item = line.strip()[2:].strip().strip('"')
            fm[current] = fm.get(current, '') + (',' if fm.get(current) else '') + item
    return fm


def main() -> int:
    text = INDEX.read_text(encoding='utf-8')

    # Read all cards
    cards = []
    for p in sorted(CARDS.glob('*.md')):
        if p.name.startswith('_'):
            continue
        fm = frontmatter(p.read_text(encoding='utf-8'))
        cid = fm.get('id', '')
        if not re.match(r'sk-\d{4}$', cid):
            continue
        topics = [x for x in (fm.get('topics') or '').split(',') if x]
        cards.append({
            'id': cid,
            'file': p.name,
            'type': fm.get('type', ''),
            'topics': topics,
            'source': fm.get('source', ''),
            'title': fm.get('title', ''),
        })

    # Count topics
    counts = {}
    for c in cards:
        for t in c['topics']:
            counts[t] = counts.get(t, 0) + 1

    # Replace topic counts in existing topic table rows
    lines = text.splitlines()
    new_lines = []
    for line in lines:
        m = re.match(r'^(\| \[)([a-z-]+)(\]\()(topics/[a-z-]+\.md\) \| [^|]+ \| )(\d+)( \|)$', line)
        if m:
            slug = m.group(2)
            cnt = counts.get(slug, 0)
            line = f"{m.group(1)}{slug}{m.group(3)}{m.group(4)}{cnt}{m.group(6)}"
        new_lines.append(line)
    text = '\n'.join(new_lines)

    # Build cards table
    header = '## 卡片 Cards\n\n| ID | 类型 | 主题 | 来源 | 一句话标题 |\n|---|---|---|---|---|\n'
    rows = []
    for c in sorted(cards, key=lambda x: x['id']):
        topic_str = ' / '.join(c['topics'])
        rows.append(f"| [{c['id']}](cards/{c['file']}) | {c['type']} | {topic_str} | {c['source']} | {c['title']} |")
    table = header + '\n'.join(rows) + '\n'

    # Replace from cards header onward
    pos = text.find('## 卡片 Cards')
    if pos == -1:
        raise RuntimeError('INDEX.md missing cards section')
    text = text[:pos] + table

    INDEX.write_text(text, encoding='utf-8')
    print(f'OK: {len(cards)} cards, {len(counts)} topics')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

# -*- coding: utf-8 -*-
"""Validate the Markdown knowledge base structure.

Usage:
    python scripts/check_kb.py

Checks sources/topics/cards frontmatter, references, INDEX consistency.
No third-party dependencies.
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / 'sources'
TOPICS = ROOT / 'topics'
CARDS = ROOT / 'cards'
INDEX = ROOT / 'INDEX.md'


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
            v = v.strip()
            if len(v) >= 2 and v[0] == '"' and v[-1] == '"':
                v = v[1:-1]
            fm[current] = v
        elif line.startswith('  - ') and current is not None:
            item = line.strip()[2:].strip()
            if item[:1] == '"' and item[-1:] == '"':
                item = item[1:-1]
            fm[current] = fm.get(current, '') + (',' if fm.get(current) else '') + item
    return fm


def main() -> int:
    errors = []

    source_slugs = set()
    for p in sorted(SOURCES.glob('*.md')):
        if p.name.startswith('_'):
            continue
        fm = frontmatter(read(p))
        if not fm.get('slug'):
            errors.append(f'{p}: missing slug')
            continue
        source_slugs.add(fm['slug'])
        for field in ['slug', 'title', 'author', 'rights_status', 'status']:
            if not fm.get(field):
                errors.append(f'{p}: missing {field}')

    card_ids = set()
    for p in sorted(CARDS.glob('*.md')):
        if p.name.startswith('_'):
            continue
        fm = frontmatter(read(p))
        cid = fm.get('id', '')
        if not re.match(r'sk-\d{4}$', cid):
            errors.append(f'{p}: bad/missing id {cid!r}')
            continue
        card_ids.add(cid)
        for field in ['id', 'type', 'title', 'lang', 'topics', 'source', 'ref', 'status']:
            if not fm.get(field):
                errors.append(f'{p}: missing {field}')
        if fm.get('type') not in ['quote', 'case', 'principle', 'method', 'practice']:
            errors.append(f'{p}: bad type {fm.get("type")}')
        if fm.get('source') not in source_slugs:
            errors.append(f'{p}: unknown source {fm.get("source")}')
        if not p.name.startswith(cid):
            errors.append(f'{p}: filename should start with {cid}')

    topic_slugs = set()
    for p in sorted(TOPICS.glob('*.md')):
        if p.name.startswith('_'):
            continue
        text = read(p)
        fm = frontmatter(text)
        slug = fm.get('slug', '')
        if not slug:
            errors.append(f'{p}: missing slug')
            continue
        topic_slugs.add(slug)
        for field in ['slug', 'title', 'summary', 'card_ids', 'source_ids', 'status']:
            if not fm.get(field):
                errors.append(f'{p}: missing {field}')
        for cid in re.findall(r'sk-\d{4}', fm.get('card_ids', '')):
            if cid not in card_ids:
                errors.append(f'{p}: card_ids references missing {cid}')
        for cid in re.findall(r'sk-\d{4}', text):
            if cid not in card_ids:
                errors.append(f'{p}: body references missing {cid}')

    idx = read(INDEX)
    for cid in card_ids:
        if cid not in idx:
            errors.append(f'INDEX missing card {cid}')
    for slug in source_slugs:
        if slug not in idx:
            errors.append(f'INDEX missing source {slug}')
    for slug in topic_slugs:
        if slug not in idx:
            errors.append(f'INDEX missing topic {slug}')

    required = ['README.md', 'SKILL.md', 'INDEX.md', 'LICENSE', 'NOTICE.md',
                'CONTRIBUTING.md', 'AGENTS.md']
    for name in required:
        if not (ROOT / name).exists():
            errors.append(f'missing required file {name}')

    if errors:
        print('ERRORS:')
        for e in errors:
            print(' -', e)
        return 1
    print(f'OK: {len(source_slugs)} sources, {len(card_ids)} cards, {len(topic_slugs)} topics')
    return 0


if __name__ == '__main__':
    sys.exit(main())

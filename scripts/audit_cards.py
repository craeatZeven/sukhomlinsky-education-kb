# -*- coding: utf-8 -*-
"""Quality audit for all knowledge-base cards.

Read-only. Distinguishes hard errors (structural problems) from soft warnings
(quality improvements). Page-number checks are enforced only for the ZuoRen
Chinese OCR source, where every story has a printed page.

Usage:
    python scripts/audit_cards.py
"""
from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CARDS = ROOT / 'cards'
SOURCES = ROOT / 'sources'
TOPICS = ROOT / 'topics'

ALLOWED_TYPES = {'quote', 'case', 'principle', 'method', 'practice'}
REQUIRED_FM = ['id', 'type', 'title', 'lang', 'topics', 'source', 'ref', 'status']
REQUIRED_SECTIONS = ['原文/Excerpt', '中文转述/说明', '教育场景/应用', '出处核对']
PAGE_STRICT_SOURCES = {'zuo-ren-de-gu-shi-zh'}
MIN_EXCERPT = {'quote': 8, 'case': 20, 'principle': 20, 'method': 20, 'practice': 20}


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


def clean_quotes(v: str) -> str:
    v = v.strip()
    if len(v) >= 2 and v[0] == '"' and v[-1] == '"':
        return v[1:-1]
    return v


def main() -> int:
    source_slugs = set()
    for p in sorted(SOURCES.glob('*.md')):
        fm = frontmatter(read(p))
        if fm.get('slug'):
            source_slugs.add(clean_quotes(fm['slug']))

    topic_slugs = set()
    for p in sorted(TOPICS.glob('*.md')):
        if p.name.startswith('_'):
            continue
        fm = frontmatter(read(p))
        if fm.get('slug'):
            topic_slugs.add(clean_quotes(fm['slug']))

    errors: list[tuple[str, str]] = []
    warnings: list[tuple[str, str]] = []
    titles_by_source: dict[tuple[str, str], list[str]] = defaultdict(list)
    refs_by_source: dict[tuple[str, str], list[str]] = defaultdict(list)
    type_counts: Counter = Counter()
    source_counts: Counter = Counter()
    topic_counts: Counter = Counter()
    page_ref_by_source: dict[str, list[bool]] = defaultdict(list)

    card_files = sorted(CARDS.glob('*.md'))
    processed = 0
    for p in card_files:
        if p.name.startswith('_'):
            continue
        processed += 1
        text = read(p)
        fm = frontmatter(text)
        cid = clean_quotes(fm.get('id', ''))
        label = f'{p.name} [{cid or "?"}]'

        for field in REQUIRED_FM:
            if not fm.get(field):
                errors.append((label, f'missing frontmatter field: {field}'))

        if not re.match(r'sk-\d{4}$', cid):
            errors.append((label, f'bad id: {cid!r}'))
        elif not p.name.startswith(cid):
            errors.append((label, f'filename should start with {cid}'))

        ctype = clean_quotes(fm.get('type', ''))
        type_counts[ctype] += 1
        if ctype not in ALLOWED_TYPES:
            errors.append((label, f'bad type: {ctype!r}'))

        src = clean_quotes(fm.get('source', ''))
        source_counts[src] += 1
        if src and src not in source_slugs:
            errors.append((label, f'unknown source: {src!r}'))

        topics = [x for x in clean_quotes(fm.get('topics', '')).split(',') if x]
        for t in topics:
            topic_counts[t] += 1
            if t not in topic_slugs:
                errors.append((label, f'unknown topic: {t!r}'))
        if not (1 <= len(topics) <= 3):
            errors.append((label, f'topic count {len(topics)} not in 1..3'))

        title = clean_quotes(fm.get('title', ''))
        if title:
            titles_by_source[(src, re.sub(r'\s+', '', title))].append(p.name)

        ref = clean_quotes(fm.get('ref', ''))
        has_page = bool(ref and re.search(r'p\s*\d+', ref))
        page_ref_by_source[src].append(has_page)
        if ref:
            found = re.findall(r'《([^》]+)》', ref)
            if found:
                refs_by_source[(src, found[-1])].append(p.name)
        else:
            errors.append((label, 'empty ref'))
        if src in PAGE_STRICT_SOURCES and not has_page:
            warnings.append((label, 'ZuoRen card ref has no printed page (pNNN)'))

        for section in REQUIRED_SECTIONS:
            if f'## {section}' not in text:
                errors.append((label, f'missing section: {section}'))

        m = re.search(r'## 原文/Excerpt\n(.*?)(?=\n## )', text, re.S)
        if m:
            excerpt = re.sub(r'^>\s?', '', m.group(1), flags=re.M).strip()
            excerpt = re.sub(r'\s+', '', excerpt)
            floor = MIN_EXCERPT.get(ctype, 20)
            if len(excerpt) < floor:
                warnings.append((label, f'{ctype} excerpt short ({len(excerpt)} chars, floor {floor})'))
            elif len(excerpt) > 3000:
                warnings.append((label, f'excerpt very long ({len(excerpt)} chars)'))

    for (src, title), files in titles_by_source.items():
        if len(files) > 1:
            warnings.append((f'DUP TITLE in {src}: {title}', ', '.join(files)))
    for (src, ref), files in refs_by_source.items():
        if len(files) > 1 and src == 'zuo-ren-de-gu-shi-zh':
            warnings.append((f'DUP ZUOREN REF: {ref}', ', '.join(files)))

    print(f'CARDS: {processed}')
    print(f'SOURCES: {len(source_slugs)}  TOPICS: {len(topic_slugs)}')
    print('TYPES:', dict(type_counts))
    print('SOURCES:', source_counts.most_common())
    print('TOPICS:', topic_counts.most_common())
    print('\nPAGE REF COVERAGE BY SOURCE:')
    for src in sorted(page_ref_by_source):
        vals = page_ref_by_source[src]
        print(f'  {src}: {sum(vals)}/{len(vals)}')
    print(f'\nHARD ERRORS: {len(errors)}')
    for label, msg in errors[:100]:
        print(f'  - {label}: {msg}')
    print(f'\nWARNINGS: {len(warnings)}')
    for label, msg in warnings[:150]:
        print(f'  - {label}: {msg}')
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())

# -*- coding: utf-8 -*-
"""Generate docs/coverage-dashboard.md from the current knowledge base.

Read-only with respect to cards. Writes only the dashboard file.

Usage:
    python scripts/coverage_report.py
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CARDS = ROOT / 'cards'
SOURCES = ROOT / 'sources'
TOPICS = ROOT / 'topics'
OUT = ROOT / 'docs' / 'coverage-dashboard.md'

ZUOREN = 'zuo-ren-de-gu-shi-zh'


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


def norm(s: str) -> str:
    return re.sub(r'[\s，。！？“”、：:；;·\-—－（）()]+', '', s)


def main() -> int:
    source_title = {}
    for p in sorted(SOURCES.glob('*.md')):
        fm = frontmatter(read(p))
        slug = clean(fm.get('slug', ''))
        if slug:
            source_title[slug] = clean(fm.get('title', slug))

    topic_title = {}
    for p in sorted(TOPICS.glob('*.md')):
        if p.name.startswith('_'):
            continue
        fm = frontmatter(read(p))
        slug = clean(fm.get('slug', ''))
        if slug:
            topic_title[slug] = clean(fm.get('title', slug))

    source_cards = Counter()
    source_with_page = Counter()
    type_cards = Counter()
    topic_cards = Counter()
    zuoren_ref_titles = set()
    zuoren_cards = 0
    total = 0

    for p in sorted(CARDS.glob('*.md')):
        if p.name.startswith('_'):
            continue
        text = read(p)
        fm = frontmatter(text)
        total += 1
        src = clean(fm.get('source', ''))
        source_cards[src] += 1
        ref = clean(fm.get('ref', ''))
        if re.search(r'p\s*\d+', ref):
            source_with_page[src] += 1
        type_cards[clean(fm.get('type', ''))] += 1
        for t in [x for x in clean(fm.get('topics', '')).split(',') if x]:
            topic_cards[t] += 1
        if src == ZUOREN:
            zuoren_cards += 1
            found = re.findall(r'《([^》]+)》', ref)
            if found:
                zuoren_ref_titles.add(norm(found[-1]))

    lines: list[str] = []
    lines.append('# 覆盖仪表盘 Coverage Dashboard')
    lines.append('')
    lines.append('> 由 `scripts/coverage_report.py` 自动生成；只读卡片后写本文件。')
    lines.append('> 用途：一眼看清每个来源的卡片量、页码覆盖和当前缺口。')
    lines.append('')
    lines.append('## 总览')
    lines.append('')
    lines.append(f'- 卡片总数：**{total}**')
    lines.append(f'- 来源数：**{len(source_cards)}**')
    lines.append(f'- 主题数：**{len(topic_cards)}**')
    lines.append(f'- 《做人的故事》：**{zuoren_cards} 张卡 / {len(zuoren_ref_titles)} 个目录标题**')
    lines.append('')
    lines.append('## 来源覆盖')
    lines.append('')
    lines.append('| 来源 | 卡片数 | 含印刷页码 ref |')
    lines.append('|---|---:|---:|')
    for src, n in source_cards.most_common():
        title = source_title.get(src, src)
        lines.append(f'| {title}（`{src}`） | {n} | {source_with_page[src]}/{n} |')
    lines.append('')
    lines.append('## 卡片类型')
    lines.append('')
    lines.append('| 类型 | 数量 |')
    lines.append('|---|---:|')
    for typ, n in type_cards.most_common():
        lines.append(f'| `{typ}` | {n} |')
    lines.append('')
    lines.append('## 主题分布')
    lines.append('')
    lines.append('| 主题 | 卡片数 |')
    lines.append('|---|---:|')
    for t, n in topic_cards.most_common():
        lines.append(f'| {topic_title.get(t, t)}（`{t}`） | {n} |')
    lines.append('')
    lines.append('## 当前已知缺口')
    lines.append('')
    lines.append('- 《做人的故事》540 个目录标题已全部建卡；页码已与 OCR 正文页逐条核对（含 OCR 异体字/错字映射）。')
    lines.append('- 《苏霍姆林斯基讲美德故事》44 篇已全量盘点：31 篇确认同源、11 篇高度可能、2 篇仅主题相关；详见 `docs/story-coverage-meide-gushi.md`。')
    lines.append('- 113 条官方故事书目已盘点，并完成“条目 ↔ 卡片”全量核验：96/113 高置信可挂现有卡（10 A + 86 H；17 条 E_none）；详见 `docs/coverage-official-tales-mapping.md` 及三份 verification 报告。')
    lines.append('- 五卷本已按作品统计（`docs/coverage-volumes.md`），并完成章节级覆盖审计（`docs/coverage-volumes-chapters.md`）：310 个审计单位中 13 个 covered、154 个 partial、143 个 gap。')
    lines.append('- 562 篇期刊文章：仅第五卷 68 篇已覆盖；其余受合法获取渠道限制，暂缓。')
    lines.append('- 英文/电子本（On Education、To Children I Give My Heart、Each One Must Shine、Singing Feather、把心献给孩子）：暂用本地文件/行号定位，未统一到印刷页码。')
    lines.append('')
    lines.append('## 维护命令')
    lines.append('')
    lines.append('```bash')
    lines.append('python scripts/validate_all.py')
    lines.append('python scripts/check_kb.py')
    lines.append('python scripts/audit_cards.py')
    lines.append('python scripts/coverage_report.py')
    lines.append('python scripts/coverage_volumes.py')
    lines.append('python scripts/build_site.py')
    lines.append('```')

    OUT.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'wrote {OUT}')

    web_json = ROOT / 'web' / 'coverage.json'
    payload = {
        'total_cards': total,
        'source_count': len(source_cards),
        'topic_count': len(topic_cards),
        'zuoren_cards': zuoren_cards,
        'zuoren_titles': len(zuoren_ref_titles),
        'sources': [
            {
                'slug': src,
                'title': source_title.get(src, src),
                'cards': n,
                'page_refs': source_with_page[src],
            }
            for src, n in source_cards.most_common()
        ],
        'types': [{'type': typ, 'cards': n} for typ, n in type_cards.most_common()],
        'topics': [
            {'slug': t, 'title': topic_title.get(t, t), 'cards': n}
            for t, n in topic_cards.most_common()
        ],
    }
    web_json.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'wrote {web_json}')
    print(f'cards={total} sources={len(source_cards)} topics={len(topic_cards)} zuoren={zuoren_cards}')
    return 0


if __name__ == '__main__':
    sys.exit(main())

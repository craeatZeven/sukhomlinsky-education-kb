# -*- coding: utf-8 -*-
"""Build web/data.json (agent-friendly snapshot) from the Markdown knowledge base.

Usage:
    python scripts/build_site.py

Reads sources/, topics/, cards/ and writes:
    web/data.json     全库快照（供 agent / 外部程序取用，浏览器不加载）
    web/sitemap.xml   站点地图

浏览器端数据由 scripts/build_shards.py 生成到 web/data/（分片、按需加载）。
No third-party dependencies.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES_DIR = ROOT / 'sources'
TOPICS_DIR = ROOT / 'topics'
CARDS_DIR = ROOT / 'cards'


def read_text(path: Path) -> str:
    return path.read_text(encoding='utf-8')


def strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == '"' and value[-1] == '"':
        return value[1:-1]
    if len(value) >= 2 and value[0] == "'" and value[-1] == "'":
        return value[1:-1]
    return value


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
            v = strip_quotes(v)
            fm[current] = v
        elif line.startswith('  - ') and current is not None:
            item = strip_quotes(line.strip()[2:])
            if fm.get(current):
                fm[current] = fm[current] + ',' + item
            else:
                fm[current] = item
    return fm


def section(text: str, title: str) -> str:
    """Return content under a '## Title' section until next '## '."""
    m = re.search(rf'^## {re.escape(title)}\s*$', text, re.M)
    if not m:
        return ''
    start = m.end()
    nxt = re.search(r'^## ', text[start:], re.M)
    if nxt:
        return text[start:start + nxt.start()]
    return text[start:]


def bullets(content: str) -> list[str]:
    out = []
    for line in content.splitlines():
        line = line.strip()
        m = re.match(r'^(?:[-*]|\d+\.)\s+(.*)$', line)
        if m:
            item = m.group(1).strip()
            if item:
                out.append(item)
    return out


def first_para(content: str) -> str:
    for line in content.splitlines():
        line = line.strip()
        if line and not line.startswith('#') and not line.startswith('|'):
            return line
    return ''


def parse_sources() -> list[dict]:
    sources = []
    for p in sorted(SOURCES_DIR.glob('*.md')):
        if p.name.startswith('_'):
            continue
        text = read_text(p)
        fm = frontmatter(text)
        if not fm.get('slug'):
            continue
        meta_parts = []
        if fm.get('publisher'):
            meta_parts.append(str(fm['publisher']))
        if fm.get('year'):
            meta_parts.append(str(fm['year']))
        sources.append({
            'slug': fm['slug'],
            'title': fm.get('title', p.stem),
            'lang': (fm.get('lang') or '').upper() or '?',
            'meta': ' · '.join(meta_parts),          # 只放出版信息，状态属于维护字段不进前台
            'status': fm.get('status', ''),
            'url': fm.get('url') or f"../sources/{fm['slug']}.md",
        })
    return sources


def parse_topics() -> list[dict]:
    topics = []
    for p in sorted(TOPICS_DIR.glob('*.md')):
        if p.name.startswith('_'):
            continue
        text = read_text(p)
        fm = frontmatter(text)
        if not fm.get('slug'):
            continue
        core = bullets(section(text, '核心判断'))
        methods = bullets(section(text, '可操作方法'))
        cross = first_para(section(text, '跨书综合'))
        aliases_raw = (fm.get('aliases') or '').strip()
        aliases = ' · '.join(x.strip() for x in aliases_raw.split(',') if x.strip()) if aliases_raw else ''
        topics.append({
            'slug': fm['slug'],
            'title': fm.get('title', p.stem),
            'aliases': aliases,
            'summary': fm.get('summary', ''),
            'core': core,
            'methods': methods,
            'cross': cross,
        })
    return topics


def parse_cards() -> list[dict]:
    cards = []
    for p in sorted(CARDS_DIR.glob('*.md')):
        if p.name.startswith('_'):
            continue
        text = read_text(p)
        fm = frontmatter(text)
        if not fm.get('id'):
            continue
        excerpt_section = section(text, '原文/Excerpt')
        excerpts: list[str] = []
        current: list[str] = []
        for line in excerpt_section.splitlines():
            if not line.startswith('>'):
                continue
            content = line.lstrip('>').strip()
            if content == '':
                if current:
                    excerpts.append(' '.join(current))
                    current = []
            else:
                current.append(content)
        if current:
            excerpts.append(' '.join(current))
        excerpt = ' '.join(excerpts)
        cn_section = section(text, '中文转述/说明')
        cn = first_para(cn_section)
        topics_raw = (fm.get('topics') or '').strip()
        topics = [x.strip() for x in topics_raw.split(',') if x.strip()]
        tags: list[str] = []
        if '[OCR待校]' in text or '[extraction待校]' in text:
            tags.append('OCR待校')
        if any(k in text for k in ('待纸本核', '纸本复核', '待纸本', '待原书')):
            tags.append('待纸本核')
        if len(topics) > 1:
            tags.append('跨主题')
        cards.append({
            'id': fm['id'],
            'type': fm.get('type', ''),
            'title': fm.get('title', ''),
            'source': fm.get('source', ''),
            'topics': topics,
            'excerpt': excerpt,
            'excerpts': excerpts,
            'cn': cn,
            'ref': fm.get('ref', ''),
            'tags': tags,
            # 溯源字段（详情页「关于本卡」用）
            'created': fm.get('created', ''),
            'updated': fm.get('updated', ''),
            'reviewed_by': fm.get('reviewed_by', ''),
        })
    return cards


def main() -> None:
    data = {
        'sources': parse_sources(),
        'topics': parse_topics(),
        'cards': parse_cards(),
    }
    # Agent-friendly plain JSON snapshot (browser pages use web/data/ shards instead).
    json_path = ROOT / 'web' / 'data.json'
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')

    # Sitemap for humans and crawlers/agents.
    base = 'https://craeatzeven.github.io/sukhomlinsky-education-kb/web/'
    urls = [
        base + 'index.html',
        base + 'explore.html',
        base + 'problem.html',
        base + 'clusters.html',
        base + 'cases.html',
        base + 'sources.html',
    ]
    urls += [base + 'topic.html?slug=' + t['slug'] for t in data['topics']]
    urls += [base + 'card.html?id=' + c['id'] + '#' + c['id'] for c in data['cards']]
    xml = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        xml.append(f'  <url><loc>{u}</loc></url>')
    xml.append('</urlset>')
    (ROOT / 'web' / 'sitemap.xml').write_text('\n'.join(xml), encoding='utf-8')

    print(f'wrote {json_path} ({len(data["sources"])} sources, '
          f'{len(data["topics"])} topics, {len(data["cards"])} cards)')
    print(f'wrote web/sitemap.xml ({len(urls)} URLs)')
    print('note: browser data shards come from scripts/build_shards.py → web/data/')


if __name__ == '__main__':
    main()

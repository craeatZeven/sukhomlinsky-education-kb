# -*- coding: utf-8 -*-
"""Build web/data.json (agent-friendly snapshot) from the Markdown knowledge base.

Usage:
    python scripts/build_site.py

Reads sources/, topics/, cards/ and writes:
    web/data.json     全库快照（供 agent / 外部程序取用，浏览器不加载）
    web/sitemap.xml   站点地图

快照同时带上分类字段（taxonomy.md 的条目/角度/分面 + classification.json 的逐卡判读），
agent 拿到一份 data.json 就能自己把卡片归到条目上，不必再读 Markdown。

浏览器端数据由 scripts/build_shards.py 生成到 web/data/（分片、按需加载）。
No third-party dependencies.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES_DIR = ROOT / 'sources'
TOPICS_DIR = ROOT / 'topics'
CARDS_DIR = ROOT / 'cards'
CLASSIFICATION = ROOT / 'classification.json'
sys.path.insert(0, str(ROOT / 'scripts'))

import taxonomy as T  # noqa: E402  (taxonomy.md 解析器)


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
        # 兼容写法：部分卡片的「原文/Excerpt」是普通段落而非 `>` 引用块。
        # 早期只收 `>` 行，导致这些卡的原文在网页与检索语料里完全不可见（18 张）。
        if not excerpts:
            for line in excerpt_section.splitlines():
                line = line.strip()
                if not line or line.startswith(('#', '|', '-', '*', '>')):
                    continue
                excerpts.append(line)
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


def clean_rule(text: str) -> str:
    """taxonomy.md「收录」单元格 → 可读正文（去 Markdown 记号，不增删实词）。"""
    text = (text or '').replace('<br>', ' ')
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = text.replace('`', '')
    return re.sub(r'\s{2,}', ' ', text).strip()


def load_taxonomy() -> dict | None:
    """合并 classification.json 与 taxonomy.md；缺分类数据时返回 None（快照照样能出）。"""
    if not CLASSIFICATION.exists():
        return None
    cls = json.loads(CLASSIFICATION.read_text(encoding='utf-8'))
    spec = T.load_spec()
    name_of = {e['id']: e['name'] for e in spec['entries']}
    layer_of = {e['id']: e['layer'] for e in spec['entries']}
    primary_count = {e['id']: 0 for e in spec['entries']}
    cross_count = {e['id']: 0 for e in spec['entries']}
    for rec in cls.values():
        p = rec.get('primary')
        if p in primary_count:
            primary_count[p] += 1
        for code in (rec.get('seealso') or []):
            if code in cross_count:
                cross_count[code] += 1
    return {'cls': cls, 'spec': spec, 'name_of': name_of, 'layer_of': layer_of,
            'primary_count': primary_count, 'cross_count': cross_count}


def _facet_counts(cls: dict, spec: dict) -> list[dict]:
    """17 个分面的真实计数（来自 classification.json 的 facets 字段）。"""
    counts = {f['id']: 0 for f in spec['facets']}
    for rec in cls.values():
        for fid in rec.get('facets') or []:
            if fid in counts:
                counts[fid] += 1
    return [{'code': f['id'], 'name': f['name'], 'field': f['field'],
             'count': counts[f['id']]} for f in spec['facets']]


def classification_fields(cid: str, tax: dict | None) -> dict:
    if not tax:
        return {}
    rec = tax['cls'].get(cid) or {}
    p = rec.get('primary') if rec.get('primary') in tax['name_of'] else None
    see = [c for c in (rec.get('seealso') or []) if c in tax['name_of']]
    return {
        'primary': p,
        'seealso': see,
        'primary_name': tax['name_of'].get(p, '') if p else '',
        'seealso_names': [tax['name_of'][c] for c in see],
    }


def taxonomy_block(tax: dict | None) -> dict:
    if not tax:
        return {'available': False}
    spec = tax['spec']
    entries = []
    for e in spec['entries']:
        entries.append({
            'code': e['id'],
            'name': e['name'],
            'layer': e['layer'],
            'rule': clean_rule(e['include']),
            'count': tax['primary_count'][e['id']],
            'cross': tax['cross_count'][e['id']],
            'tag': bool(e['tag']),
        })
    layers = []
    n = 0
    for layer in spec['layers']:
        codes = [e['id'] for e in spec['entries'] if e['layer'] == layer['name'] and not e['tag']]
        if not codes:                      # 「关照」层 = 复分标签，不是观察角度
            continue
        n += 1
        layers.append({'index': n, 'name': layer['name'],
                       'question': clean_rule(layer['question']),
                       'count': sum(tax['primary_count'][c] for c in codes),
                       'entries': codes})
    return {
        'available': True,
        'spec': 'taxonomy.md',
        'source': CLASSIFICATION.name,
        'entries': entries,
        'layers': layers,
        # 分面标记来自 classification.json 的 facets 字段（逐卡判读，已过复核门槛；
        # 见 docs/facet-labeling-plan.md §5.2）。计数照实算，不写死。
        'facets': _facet_counts(tax['cls'], spec),
        'facets_ready': all(rec.get('facet_source') == 'judge'
                            for rec in tax['cls'].values() if rec.get('type') == 'case'),
    }


def main() -> None:
    tax = load_taxonomy()
    cards = parse_cards()
    for card in cards:
        card.update(classification_fields(card['id'], tax))
    data = {
        'sources': parse_sources(),
        'topics': parse_topics(),
        'taxonomy': taxonomy_block(tax),
        'cards': cards,
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
        base + 'entries.html',
        base + 'facets.html',
    ]
    urls += [base + 'topic.html?slug=' + t['slug'] for t in data['topics']]
    if data['taxonomy'].get('available'):
        urls += [base + 'entry.html?code=' + e['code'] for e in data['taxonomy']['entries']]
    urls += [base + 'card.html?id=' + c['id'] + '#' + c['id'] for c in data['cards']]
    xml = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        xml.append(f'  <url><loc>{u}</loc></url>')
    xml.append('</urlset>')
    (ROOT / 'web' / 'sitemap.xml').write_text('\n'.join(xml), encoding='utf-8')

    tax_note = (f'{len(data["taxonomy"]["entries"])} entries, '
                f'{len(data["taxonomy"]["layers"])} angles, '
                f'{len(data["taxonomy"]["facets"])} facets (facets_ready='
                f'{data["taxonomy"]["facets_ready"]})'
                if data['taxonomy'].get('available') else 'classification.json 缺失，快照未带分类字段')
    print(f'wrote {json_path} ({len(data["sources"])} sources, '
          f'{len(data["topics"])} topics, {len(data["cards"])} cards; taxonomy: {tax_note})')
    print(f'wrote web/sitemap.xml ({len(urls)} URLs)')
    print('note: browser data shards come from scripts/build_shards.py → web/data/')


if __name__ == '__main__':
    main()

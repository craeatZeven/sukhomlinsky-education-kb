# -*- coding: utf-8 -*-
"""Build sharded web data for on-demand loading (档位 A).

Usage:
    python scripts/build_shards.py

Reads sources/, topics/, cards/ (same parsers as build_site.py) and writes:

    web/data/meta.json            书源 + 主题 + 计数（约 30 KB）
    web/data/index.json           全库卡片索引：元数据 + 摘要（正文不在此文件）
    web/data/index/<source>.json  按来源切分的索引（stories / 来源页按需加载）
    web/data/cards/<id>.json      单卡全文（详情页按需加载）
    web/data/search/all.json      全文检索语料（检索页 / 本地回退按需加载）
    web/data/search/<source>.json 按来源切分的检索语料

设计原则：首屏只加载 meta + 需要的索引切片；正文（excerpts）永远按需取。
"""
from __future__ import annotations

import gzip
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))

import build_site  # noqa: E402  (reuse frontmatter/section parsers)

WEB = ROOT / 'web'
DATA = WEB / 'data'
PREVIEW_LEN = 80
CN_LEN = 60


def clip(text: str, limit: int) -> str:
    text = (text or '').strip()
    if len(text) <= limit:
        return text
    return text[:limit].rstrip() + '…'


def dump(path: Path, obj) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    body = json.dumps(obj, ensure_ascii=False, separators=(',', ':'))
    path.write_text(body, encoding='utf-8')
    return len(body.encode('utf-8'))


def gz_len(path: Path) -> int:
    raw = path.read_bytes()
    return len(gzip.compress(raw, 9))


def card_index_entry(card: dict) -> dict:
    excerpts = card.get('excerpts') or ([card['excerpt']] if card.get('excerpt') else [])
    ref = card.get('ref', '')
    page = None
    m = re.search(r'p\s*(\d+)', ref or '')
    if m:
        page = int(m.group(1))
    entry = {
        'id': card['id'],
        'type': card.get('type', ''),
        'title': card.get('title', ''),
        'source': card.get('source', ''),
        'topics': card.get('topics', []),
        'tags': card.get('tags', []),
        'ref': ref,
        'cn': clip(card.get('cn', ''), CN_LEN),
        'preview': clip(excerpts[0] if excerpts else '', PREVIEW_LEN),
        'trunc': bool(excerpts) and len(excerpts[0]) > PREVIEW_LEN,
        'n': len(excerpts),
    }
    if page is not None:
        entry['page'] = page
    return entry


def card_full_entry(card: dict, prev_id=None, next_id=None, related=None) -> dict:
    """单卡全文 + 详情页上下文（上/下一张、相关卡片），详情页因此不必再拉整库索引。"""
    return {
        'id': card['id'],
        'type': card.get('type', ''),
        'title': card.get('title', ''),
        'source': card.get('source', ''),
        'topics': card.get('topics', []),
        'tags': card.get('tags', []),
        'ref': card.get('ref', ''),
        'cn': card.get('cn', ''),
        'excerpt': card.get('excerpt', ''),
        'excerpts': card.get('excerpts', []),
        # 「关于本卡」溯源块用
        'created': card.get('created', ''),
        'updated': card.get('updated', ''),
        'prev': prev_id,
        'next': next_id,
        'related': related or [],
    }


def build_related(cards: list[dict], limit: int = 6) -> dict[str, list[dict]]:
    """按共现主题数计算每张卡的相关卡片（同客户端原逻辑，改为构建期一次算好）。"""
    topic_index: dict[str, list[dict]] = {}
    for card in cards:
        for slug in card.get('topics', []):
            topic_index.setdefault(slug, []).append(card)
    by_id = {c['id']: c for c in cards}
    out: dict[str, list[dict]] = {}
    for card in cards:
        mine = set(card.get('topics', []))
        shared: dict[str, int] = {}
        for slug in mine:
            for other in topic_index.get(slug, []):
                if other['id'] == card['id']:
                    continue
                shared[other['id']] = shared.get(other['id'], 0) + 1
        picked = sorted(shared.items(), key=lambda kv: (-kv[1], kv[0]))[:limit]
        out[card['id']] = [
            {'id': cid, 'title': by_id[cid].get('title', ''), 'type': by_id[cid].get('type', ''),
             'topics': by_id[cid].get('topics', [])}
            for cid, _ in picked
        ]
    return out


def search_entry(card: dict) -> dict:
    excerpts = card.get('excerpts') or ([card['excerpt']] if card.get('excerpt') else [])
    return {
        'id': card['id'],
        'title': card.get('title', ''),
        'cn': card.get('cn', ''),
        'text': ' '.join(excerpts),
    }


def main() -> None:
    sources = build_site.parse_sources()
    topics = build_site.parse_topics()
    cards = build_site.parse_cards()

    DATA.mkdir(parents=True, exist_ok=True)
    report: list[tuple[str, int, int]] = []

    # 1) meta：书源 + 主题 + 计数
    generated = max(
        (p.stat().st_mtime for p in list((ROOT / 'cards').glob('*.md'))), default=0
    )
    source_counts: dict[str, int] = {}
    topic_counts: dict[str, int] = {}
    for card in cards:
        source_counts[card.get('source', '')] = source_counts.get(card.get('source', ''), 0) + 1
        for slug in card.get('topics', []):
            topic_counts[slug] = topic_counts.get(slug, 0) + 1
    for src in sources:
        src['cards'] = source_counts.get(src['slug'], 0)
    for topic in topics:
        topic['cards'] = topic_counts.get(topic['slug'], 0)
    meta = {
        'generated': int(generated),
        'counts': {
            'cards': len(cards),
            'sources': len(sources),
            'topics': len(topics),
        },
        'sources': sources,
        'topics': topics,
    }
    report.append(('data/meta.json', dump(DATA / 'meta.json', meta), gz_len(DATA / 'meta.json')))

    # 2) 全库索引（无正文）
    index_cards = [card_index_entry(c) for c in cards]
    report.append(('data/index.json',
                   dump(DATA / 'index.json', {'count': len(index_cards), 'cards': index_cards}),
                   gz_len(DATA / 'index.json')))

    # 3) 按来源切分的索引
    by_source: dict[str, list[dict]] = {}
    for entry, card in zip(index_cards, cards):
        by_source.setdefault(card['source'], []).append(entry)
    for slug, items in by_source.items():
        path = DATA / 'index' / f'{slug}.json'
        report.append((f'data/index/{slug}.json', dump(path, {'count': len(items), 'cards': items}),
                       gz_len(path)))

    # 3b) 按主题切分的索引
    by_topic: dict[str, list[dict]] = {}
    for entry, card in zip(index_cards, cards):
        for slug in card.get('topics', []):
            by_topic.setdefault(slug, []).append(entry)
    for slug, items in by_topic.items():
        path = DATA / 'topic' / f'{slug}.json'
        report.append((f'data/topic/{slug}.json', dump(path, {'count': len(items), 'cards': items}),
                       gz_len(path)))

    # 3c) id 清单（随机卡片）+ 最新卡片
    ids = [c['id'] for c in cards]
    report.append(('data/ids.json', dump(DATA / 'ids.json', ids), gz_len(DATA / 'ids.json')))
    latest = sorted(index_cards, key=lambda e: e['id'], reverse=True)[:60]
    report.append(('data/latest.json', dump(DATA / 'latest.json', {'count': len(latest), 'cards': latest}),
                   gz_len(DATA / 'latest.json')))

    # 4) 单卡全文 + 详情页上下文（上/下一张、相关卡片）
    cards_dir = DATA / 'cards'
    for old in cards_dir.glob('*.json'):
        old.unlink()
    related_map = build_related(cards)
    card_bytes = 0
    card_gz = 0
    for i, card in enumerate(cards):
        prev_id = cards[i - 1]['id'] if i > 0 else None
        next_id = cards[i + 1]['id'] if i < len(cards) - 1 else None
        path = cards_dir / f"{card['id']}.json"
        card_bytes += dump(path, card_full_entry(card, prev_id, next_id, related_map.get(card['id'])))
        card_gz += gz_len(path)
    report.append((f'data/cards/<id>.json x{len(cards)}', card_bytes, card_gz))

    # 5) 检索语料（全库 + 按来源）
    search_dir = DATA / 'search'
    all_search = [search_entry(c) for c in cards]
    path = search_dir / 'all.json'
    report.append(('data/search/all.json', dump(path, all_search), gz_len(path)))
    by_source_search: dict[str, list[dict]] = {}
    for card in cards:
        by_source_search.setdefault(card['source'], []).append(search_entry(card))
    for slug, items in by_source_search.items():
        path = search_dir / f'{slug}.json'
        report.append((f'data/search/{slug}.json', dump(path, items), gz_len(path)))

    print(f'shards: {len(cards)} cards, {len(sources)} sources, {len(topics)} topics')
    print(f'{"file":44s} {"raw":>10s} {"gzip":>10s}')
    for name, raw, gz in report:
        print(f'{name:44s} {raw:>10,d} {gz:>10,d}')


if __name__ == '__main__':
    main()

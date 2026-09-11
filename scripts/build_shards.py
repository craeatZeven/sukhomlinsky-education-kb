# -*- coding: utf-8 -*-
"""Build sharded web data for on-demand loading (档位 A).

Usage:
    python scripts/build_shards.py

Reads sources/, topics/, cards/ (same parsers as build_site.py) + the classification
produced by scripts/classify_llm.py (repository root classification.json) and writes:

    web/data/meta.json            书源 + 主题 + 分类条目/角度/分面 + 计数
    web/data/index.json           全库卡片索引：元数据 + 摘要（正文不在此文件）
    web/data/index/<source>.json  按来源切分的索引（stories / 来源页按需加载）
    web/data/topic/<slug>.json    按旧主题切分的索引（旧页面仍在使用）
    web/data/entry/<CODE>.json    条目分片：主归属卡 + 交叉参见卡（A1–A23）
    web/data/layer/<n>.json       观察角度分片：该角度下全部条目的主归属卡（1–5）
    web/data/facet/<CODE>.json    故事分面分片（S1–S17；分面标记未算出，暂为空）
    web/data/cards/<id>.json      单卡全文（详情页按需加载）
    web/data/search/all.json      全文检索语料（检索页 / 本地回退按需加载）
    web/data/search/<source>.json 按来源切分的检索语料

设计原则：首屏只加载 meta + 需要的索引切片；正文（excerpts）永远按需取。

分类字段一律来自 classification.json（逐卡判读的产物）与 taxonomy.md（唯一规格），
本脚本不重新判定任何一张卡，也不为缺失的数据编造占位数字。
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
import taxonomy as T  # noqa: E402  (taxonomy.md 解析器)

WEB = ROOT / 'web'
DATA = WEB / 'data'
PREVIEW_LEN = 80
CN_LEN = 60
CLASSIFICATION = ROOT / 'classification.json'


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


# ---------------------------------------------------------------- 分类数据

def clean_rule(text: str) -> str:
    """taxonomy.md 表格里的「收录」单元格 → 可直接显示的正文。

    只做去 Markdown 记号：`**强调**` 去掉星号、`<br>` 换成空格、压缩连续空白。
    不增删任何实词——页面上要显示的就是规格原文。
    """
    text = (text or '').replace('<br>', ' ')
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = text.replace('`', '')
    return re.sub(r'\s{2,}', ' ', text).strip()


def load_classification() -> dict:
    if not CLASSIFICATION.exists():
        raise SystemExit(f'缺少分类数据 {CLASSIFICATION}（先跑 scripts/classify_llm.py）')
    return json.loads(CLASSIFICATION.read_text(encoding='utf-8'))


class Taxonomy:
    """把 classification.json + taxonomy.md 合成前端要用的形状。

    只做计数与索引，不做任何判定：每张卡的主归属/参见都原样取自 classification.json。
    """

    def __init__(self, cls: dict, spec: dict):
        self.cls = cls
        self.spec = spec
        self.entries = spec['entries']
        self.name_of = {e['id']: e['name'] for e in self.entries}
        self.layer_of = {e['id']: e['layer'] for e in self.entries}
        self.tag_of = {e['id']: bool(e['tag']) for e in self.entries}
        # 复分标签条目（当前只有 A18）不参与主归属分区，从「五个观察角度」里剔除
        self.primary_entries = [e for e in self.entries if not e['tag']]
        self.tag_entries = [e for e in self.entries if e['tag']]

        self.primary: dict[str, str | None] = {}
        self.seealso: dict[str, list[str]] = {}
        self.primary_count: dict[str, int] = {e['id']: 0 for e in self.entries}
        self.cross_count: dict[str, int] = {e['id']: 0 for e in self.entries}
        # 复分标签（A18）：不持主归属，只给相关卡片打标记，所以单独计数
        self.tag_count: dict[str, int] = {e['id']: 0 for e in self.entries}
        self.tag_of_card: dict[str, list[str]] = {}
        self.cross_layer = 0
        self.seealso_links = 0
        for cid, rec in cls.items():
            p = rec.get('primary')
            sa = [c for c in (rec.get('seealso') or []) if c in self.name_of]
            self.primary[cid] = p if p in self.name_of else None
            self.seealso[cid] = sa
            tg = [t for t in (rec.get('tags') or []) if t in self.tag_of]
            self.tag_of_card[cid] = tg
            for code in tg:
                self.tag_count[code] += 1
            if self.primary[cid]:
                self.primary_count[self.primary[cid]] += 1
            for code in sa:
                self.cross_count[code] += 1
                self.seealso_links += 1
                if self.primary[cid] and self.layer_of.get(self.primary[cid]) != self.layer_of.get(code):
                    self.cross_layer += 1

    # ---- 单卡字段

    def names(self, codes) -> list[str]:
        return [self.name_of.get(c, c) for c in codes]

    def card_fields(self, cid: str) -> dict:
        p = self.primary.get(cid)
        sa = self.seealso.get(cid, [])
        tg = self.tag_of_card.get(cid, [])
        return {
            'primary': p,
            'seealso': sa,
            'primary_name': self.name_of.get(p, '') if p else '',
            'seealso_names': self.names(sa),
            'tags': tg,
            'tag_names': self.names(tg),
        }

    # ---- 汇总块

    def entry_meta(self) -> list[dict]:
        """23 项条目：收录口径 + 主归属卡数 + 被参见次数 +（复分标签）标记卡数。"""
        rows = []
        for e in self.entries:
            code = e['id']
            rows.append({
                'code': code,
                'name': e['name'],
                'layer': e['layer'],
                'rule': clean_rule(e['include']),
                'count': self.primary_count.get(code, 0),
                'cross': self.cross_count.get(code, 0),
                'tag': bool(e['tag']),
                # 复分标签用 tag_count（标记卡数），不是 count（主归属卡数，恒为 0）
                'tag_count': self.tag_count.get(code, 0),
            })
        return rows

    def layer_meta(self) -> list[tuple[int, dict, list[str]]]:
        """五个观察角度（按 taxonomy.md §一 顺序，复分标签层不在此列）。"""
        out = []
        n = 0
        for layer in self.spec['layers']:
            codes = [e['id'] for e in self.primary_entries if e['layer'] == layer['name']]
            if not codes:                      # 「关照」层只有复分标签条目 → 不是观察角度
                continue
            n += 1
            out.append((n, layer, codes))
        return out

    def facet_meta(self) -> list[dict]:
        """17 个故事分面的计数（来自 classification.json 的 facets 字段）。

        分面标记原本用关键词算，独立复核只有 61.4%（门槛 80%），原因见
        `docs/facet-labeling-plan.md` §5.2：「事件或情绪」一栏问的是「这件事有没有发生」，
        词面判断做不了。改走逐卡判读（27 个包）后对两份盲判分别 83.0% / 83.1%，过门槛。
        """
        counts: dict[str, int] = {f['id']: 0 for f in self.spec['facets']}
        for rec in self.cls.values():
            for fid in rec.get('facets') or []:
                if fid in counts:
                    counts[fid] += 1
        return [{'code': f['id'], 'name': f['name'], 'field': f['field'],
                 'count': counts[f['id']]}
                for f in self.spec['facets']]

    def facet_ready(self) -> bool:
        """分面标记是否全部来自判读（而非当初没过门槛的关键词）。

        只要还有一张故事卡的 facets 是关键词来的，就不算就绪——
        免得页面上混着两种来源的标记而看不出来。
        """
        return all(rec.get('facet_source') == 'judge'
                   for rec in self.cls.values() if rec.get('type') == 'case')


def card_index_entry(card: dict, tax: Taxonomy | None = None) -> dict:
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
    if tax is not None:
        entry.update(tax.card_fields(card['id']))
    if page is not None:
        entry['page'] = page
    return entry


def card_full_entry(card: dict, prev_id=None, next_id=None, related=None,
                    tax: Taxonomy | None = None) -> dict:
    """单卡全文 + 详情页上下文（上/下一张、相关卡片），详情页因此不必再拉整库索引。"""
    entry = {
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
    if tax is not None:
        entry.update(tax.card_fields(card['id']))
    return entry


def build_related(cards: list[dict], tax: Taxonomy | None = None,
                  limit: int = 6) -> dict[str, list[dict]]:
    """每张卡的相关卡片。

    优先按新分类算：**同 primary 的卡 + 与本卡（或本卡 seealso）有重叠的卡**；
    不足 limit 张时，才用旧 topics 共现补齐（旧标签只作兜底，不再当主判据）。
    """
    by_id = {c['id']: c for c in cards}

    def item(cid: str) -> dict:
        other = by_id[cid]
        out = {'id': cid, 'title': other.get('title', ''), 'type': other.get('type', ''),
               'topics': other.get('topics', [])}
        if tax is not None:
            p = tax.primary.get(cid)
            out['primary'] = p
            out['primary_name'] = tax.name_of.get(p, '') if p else ''
        return out

    # 兜底：旧 topics 共现
    topic_index: dict[str, list[str]] = {}
    for card in cards:
        for slug in card.get('topics', []):
            topic_index.setdefault(slug, []).append(card['id'])

    def fallback(card: dict, taken: set[str]) -> list[str]:
        shared: dict[str, int] = {}
        for slug in set(card.get('topics', [])):
            for cid in topic_index.get(slug, []):
                if cid != card['id'] and cid not in taken:
                    shared[cid] = shared.get(cid, 0) + 1
        return [cid for cid, _ in sorted(shared.items(), key=lambda kv: (-kv[1], kv[0]))]

    out: dict[str, list[dict]] = {}
    for card in cards:
        cid = card['id']
        if tax is None:
            out[cid] = [item(c) for c in fallback(card, set())[:limit]]
            continue
        mine_primary = tax.primary.get(cid)
        mine_see = set(tax.seealso.get(cid, []))
        scored: dict[str, int] = {}
        for other in cards:
            oid = other['id']
            if oid == cid:
                continue
            other_primary = tax.primary.get(oid)
            other_see = set(tax.seealso.get(oid, []))
            score = 0
            if mine_primary and other_primary == mine_primary:
                score += 2                      # 同一个主归属
            if other_primary and other_primary in mine_see:
                score += 2                      # 本卡把它列为参见
            if mine_primary and mine_primary in other_see:
                score += 2                      # 它把本卡的主归属列为参见
            score += len(mine_see & other_see)  # 参见集合重叠
            if score:
                scored[oid] = score
        picked = [oid for oid, _ in sorted(scored.items(), key=lambda kv: (-kv[1], kv[0]))[:limit]]
        if len(picked) < limit:
            picked += fallback(card, set(picked))[:limit - len(picked)]
        out[cid] = [item(oid) for oid in picked]
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
    tax = Taxonomy(load_classification(), T.load_spec())

    DATA.mkdir(parents=True, exist_ok=True)
    report: list[tuple[str, int, int]] = []

    # 1) meta：书源 + 主题 + 分类（条目 / 角度 / 分面）+ 计数
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

    entry_meta = tax.entry_meta()
    layer_blocks = tax.layer_meta()
    facet_meta = tax.facet_meta()
    layer_meta = []
    for n, layer, codes in layer_blocks:
        layer_meta.append({
            'index': n,
            'name': layer['name'],
            'question': clean_rule(layer['question']),
            'count': sum(tax.primary_count.get(c, 0) for c in codes),
            'entries': codes,
        })

    def entry_brief(code: str) -> dict:
        return next(r for r in entry_meta if r['code'] == code)

    assigned = sum(1 for cid in tax.primary if tax.primary[cid])
    story = len(cards) - assigned
    meta = {
        'generated': int(generated),
        'counts': {
            'cards': len(cards),
            'sources': len(sources),
            'topics': len(topics),
        },
        'sources': sources,
        'topics': topics,
        # 分类：条目（A1–A23）/ 观察角度（5）/ 故事分面（S1–S17）
        'entries': entry_meta,
        'layers': layer_meta,
        'facets': facet_meta,
        # 分面标记走逐卡判读，已通过独立复核门槛（对两份盲判各 83.0% / 83.1%，门槛 80%），
        # 见 docs/facet-labeling-plan.md §5.2。若哪天混进非判读来源，facet_ready() 会自动变 false。
        'facets_ready': tax.facet_ready(),
        'classification': {
            'source': CLASSIFICATION.name,
            'total': len(cards),
            'assigned': assigned,                              # 有主归属的论述卡
            'story': story,                                    # primary 为 null 的故事卡
            'seealso': tax.seealso_links,                      # 参见条目总条数
            'seealso_cards': sum(1 for cid in tax.seealso if tax.seealso[cid]),
            'cross_layer': tax.cross_layer,                    # 其中跨观察角度的
        },
    }
    report.append(('data/meta.json', dump(DATA / 'meta.json', meta), gz_len(DATA / 'meta.json')))

    # 2) 全库索引（无正文）
    index_cards = [card_index_entry(c, tax) for c in cards]
    index_by_id = {e['id']: e for e in index_cards}
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

    # 3c) 按条目切分：主归属卡 + 交叉参见卡（全站最重要的入口）
    entry_dir = DATA / 'entry'
    for old in entry_dir.glob('*.json'):
        old.unlink()
    entry_bytes = entry_gz = 0
    for row in entry_meta:
        code = row['code']
        if row['tag']:
            # 复分标签（A18）：不持主归属，所以 cards 就是「带这个标记的卡」。
            # 这正是 taxonomy.md 要求的「复分标签入口是硬要求」——读者问
            # 「后进生怎么办」时，进的就是这里。
            cards_here = [index_by_id[c['id']] for c in cards
                          if code in tax.tag_of_card.get(c['id'], [])]
        else:
            cards_here = [index_by_id[c['id']] for c in cards
                          if tax.primary.get(c['id']) == code]
        cross_here = []
        for c in cards:
            if code in tax.seealso.get(c['id'], []):
                item = dict(index_by_id[c['id']])
                item['cross_from'] = tax.primary.get(c['id'])     # 那张卡自己的主归属
                item['cross_from_name'] = (tax.name_of.get(item['cross_from'], '')
                                           if item['cross_from'] else '')
                cross_here.append(item)
        payload = {
            'code': code,
            'name': row['name'],
            'layer': row['layer'],
            'rule': row['rule'],
            'tag': row['tag'],
            'count': len(cards_here),
            'cards': cards_here,
            'cross': cross_here,
        }
        path = entry_dir / f'{code}.json'
        entry_bytes += dump(path, payload)
        entry_gz += gz_len(path)
    report.append((f'data/entry/<CODE>.json x{len(entry_meta)}', entry_bytes, entry_gz))

    # 3d) 按观察角度切分：该角度下全部条目的全部主归属卡
    layer_dir = DATA / 'layer'
    for old in layer_dir.glob('*.json'):
        old.unlink()
    layer_bytes = layer_gz = 0
    for n, layer, codes in layer_blocks:
        here = [index_by_id[c['id']] for c in cards if tax.primary.get(c['id']) in set(codes)]
        payload = {
            'index': n,
            'name': layer['name'],
            'question': clean_rule(layer['question']),
            'count': len(here),
            'entries': [entry_brief(c) for c in codes],
            'cards': here,
        }
        path = layer_dir / f'{n}.json'
        layer_bytes += dump(path, payload)
        layer_gz += gz_len(path)
    report.append((f'data/layer/<n>.json x{len(layer_blocks)}', layer_bytes, layer_gz))

    # 3e) 故事分面分片：该分面下的故事卡（标记来自逐卡判读，已过复核门槛）
    facet_dir = DATA / 'facet'
    for old in facet_dir.glob('*.json'):
        old.unlink()
    facet_bytes = facet_gz = 0
    ready = tax.facet_ready()
    for f in tax.spec['facets']:
        here = [index_by_id[c['id']] for c in cards
                if f['id'] in (tax.cls.get(c['id'], {}).get('facets') or [])]
        payload = {'code': f['id'], 'name': f['name'], 'field': f['field'],
                   'count': len(here), 'cards': here, 'ready': ready}
        path = facet_dir / f"{f['id']}.json"
        facet_bytes += dump(path, payload)
        facet_gz += gz_len(path)
    report.append((f'data/facet/<CODE>.json x{len(tax.spec["facets"])}', facet_bytes, facet_gz))

    # 3f) id 清单（随机卡片）+ 最新卡片
    ids = [c['id'] for c in cards]
    report.append(('data/ids.json', dump(DATA / 'ids.json', ids), gz_len(DATA / 'ids.json')))
    latest = sorted(index_cards, key=lambda e: e['id'], reverse=True)[:60]
    report.append(('data/latest.json', dump(DATA / 'latest.json', {'count': len(latest), 'cards': latest}),
                   gz_len(DATA / 'latest.json')))

    # 4) 单卡全文 + 详情页上下文（上/下一张、相关卡片）
    cards_dir = DATA / 'cards'
    for old in cards_dir.glob('*.json'):
        old.unlink()
    related_map = build_related(cards, tax)
    card_bytes = 0
    card_gz = 0
    for i, card in enumerate(cards):
        prev_id = cards[i - 1]['id'] if i > 0 else None
        next_id = cards[i + 1]['id'] if i < len(cards) - 1 else None
        path = cards_dir / f"{card['id']}.json"
        card_bytes += dump(path, card_full_entry(card, prev_id, next_id,
                                                 related_map.get(card['id']), tax))
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
    print(f'classification: {assigned} 论述卡有主归属 / {story} 故事卡走分面；'
          f'参见 {tax.seealso_links} 条（{meta["classification"]["seealso_cards"]} 张卡），'
          f'跨角度 {tax.cross_layer} 条')
    print(f'taxonomy: {len(entry_meta)} 条目 · {len(layer_meta)} 观察角度 · '
          f'{len(facet_meta)} 故事分面（facets_ready={meta["facets_ready"]}）')
    print(f'{"file":44s} {"raw":>10s} {"gzip":>10s}')
    for name, raw, gz in report:
        print(f'{name:44s} {raw:>10,d} {gz:>10,d}')


if __name__ == '__main__':
    main()

# -*- coding: utf-8 -*-
"""分类规格的解析器与分配器（只依赖标准库）。

规格在仓库根目录 taxonomy.md；本模块把它解析成结构化数据，并提供：
  - load_spec()            读 taxonomy.md → (范畴, 条目, 故事分面, 旧→新映射)
  - build_scorer(...)      按 IDF 打分（关键词越少见分越高）
  - classify(card, ...)    给一张卡算出 primary / 复分标记 / 故事分面 / 参见依据

主归属规则（见 docs/taxonomy-plan.md §五）：
  1. 候选集 = 该卡所有旧标签映射到的条目（首选 + 次选）之并集；
  2. 候选内部用**强证据关键词**得分选主归属；
  3. 候选全部无强证据命中时，任何条目只要有强证据命中就由它接管（新条目由此拿到卡片）；
  4. 全无证据才回落人工首选。

「弱证据关键词」只进参见区，不能单独构成一条主归属——防止「美德 / 美好 / 儿童 / 号召」
这类泛词把卡片吸走。「复分标签」条目（关照层）不参与主归属分区，只给相关卡片加标记。
"""
from __future__ import annotations

import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC = ROOT / 'taxonomy.md'

SEC_LAYERS = '一、五个范畴（教育学的层级，不是借来的字）'
SEC_ENTRIES = '二、十九条目'
SEC_FACETS = '三、故事域的十四个分面'
SEC_MAPPING = '四、旧主题 → 新条目映射（迁移用）'
SEC_OVERRIDE = '六、人工裁定（覆盖算法）'


def _rows(path: Path, section_title: str, expect_cols: int) -> list[list[str]]:
    """取出某个 ## 小节里的全部 Markdown 表格行（跳过分隔行）。"""
    text = path.read_text(encoding='utf-8')
    m = re.search(rf'^##\s*{re.escape(section_title)}\s*$', text, re.M)
    if not m:
        raise KeyError(f'taxonomy.md 缺少小节：{section_title}')
    body = text[m.end():]
    nxt = re.search(r'^##\s', body, re.M)
    if nxt:
        body = body[:nxt.start()]
    rows = []
    for line in body.splitlines():
        line = line.strip()
        if not line.startswith('|'):
            continue
        cells = [c.strip() for c in line.strip('|').split('|')]
        if len(cells) != expect_cols:
            continue
        if set(''.join(cells)) <= set('-: '):        # 分隔行
            continue
        rows.append(cells)
    return rows[1:]                                   # 去掉表头


def _kw(cell: str) -> list[str]:
    return [k.strip() for k in cell.split(',') if k.strip() and k.strip() != '—']


def load_spec(path: Path | None = None) -> dict:
    path = path or SPEC
    layers = [{'name': r[0], 'question': r[1], 'count': int(r[2])}
              for r in _rows(path, SEC_LAYERS, 3)]
    entries = []
    for r in _rows(path, SEC_ENTRIES, 7):
        entries.append({
            'id': r[0], 'name': r[1], 'layer': r[2],
            'keywords': _kw(r[3]),        # 强证据：可单独定主归属
            'weak': _kw(r[4]),            # 弱证据：只进参见区
            'include': r[5], 'exclude': r[6],
            # 复分标签（关照层）：不参与主归属分区，只给相关卡片加标记
            'tag': '复分' in r[5],
        })
    facets = [{'id': r[0], 'name': r[1], 'kind': r[2], 'keywords': _kw(r[3])}
              for r in _rows(path, SEC_FACETS, 4)]
    mapping = {}
    for r in _rows(path, SEC_MAPPING, 4):
        old = r[0].split()[0]                        # "love-education 爱的教育" → slug
        mapping[old] = {
            'primary': r[1].split()[0],
            'secondary': [x.split()[0] for x in r[2].split(',') if x.strip()],
            'note': r[3],
        }
    override = {}
    for r in _rows(path, SEC_OVERRIDE, 3):
        override[r[0]] = {'primary': r[1].split()[0], 'why': r[2]}
    return {'layers': layers, 'entries': entries, 'facets': facets,
            'mapping': mapping, 'override': override}


def build_scorer(cards: list[dict], spec: dict, haystack: dict[str, str]):
    """准备 IDF 打分函数（关键词命中越少见，分越高）。"""
    n = len(cards) or 1
    df: dict[str, int] = {}
    for e in spec['entries']:
        for k in e['keywords'] + e['weak']:
            df[k] = sum(1 for t in haystack.values() if k in t)
    for f in spec['facets']:
        for k in f['keywords']:
            df[k] = sum(1 for t in haystack.values() if k in t)

    def idf(k: str) -> float:
        return math.log((n + 1) / (df.get(k, 0) + 1)) + 1.0

    def score(keywords: list[str], cid: str) -> float:
        text = haystack.get(cid, '')
        return sum(idf(k) for k in keywords if k in text)

    return score


def classify(card: dict, spec: dict, score, haystack: dict[str, str]) -> dict:
    """返回 {'primary', 'facets', 'see_also', 'tags', 'reason'}"""
    cid = card['id']
    entry_of = {e['id']: e for e in spec['entries']}
    assignable = {e['id'] for e in spec['entries'] if not e['tag']}   # 复分标签不持卡

    # 复分标记：所有卡片（含故事）都算
    tags = [e['id'] for e in spec['entries'] if e['tag']
            and score(e['keywords'] + e['weak'], cid) > 0]

    if card.get('type') == 'case':                    # 故事体 → 分面
        facets = [f['id'] for f in spec['facets'] if score(f['keywords'], cid) > 0]
        return {'primary': None, 'facets': facets, 'see_also': [], 'tags': tags,
                'reason': '故事体走分面'}

    mapped: set[str] = set()
    first_choices: list[str] = []
    for t in card.get('topics', []):
        m = spec['mapping'].get(t)
        if not m:
            continue
        if m['primary'] in assignable:
            mapped.add(m['primary'])
            first_choices.append(m['primary'])
        mapped.update(s for s in m['secondary'] if s in assignable)

    # 强证据命中（弱证据不参与主归属）
    strong_hits = {e['id'] for e in spec['entries']
                   if e['id'] in assignable and score(e['keywords'], cid) > 0}

    # 人工裁定优先于算法（见 taxonomy.md §六）
    forced = spec.get('override', {}).get(cid)
    if forced:
        see = [e['id'] for e in spec['entries']
               if e['id'] != forced['primary'] and not e['tag']
               and score(e['keywords'] + e['weak'], cid) > 0]
        return {'primary': forced['primary'], 'facets': [], 'see_also': see, 'tags': tags,
                'reason': f'人工裁定（{forced["why"]}）'}

    candidates = mapped | strong_hits
    if not candidates:
        return {'primary': None, 'facets': [], 'see_also': [], 'tags': tags,
                'reason': '无旧标签映射且无关键词命中'}

    def best_of(pool: set[str]):
        ranked = sorted(((score(entry_of[e]['keywords'], cid), e) for e in pool),
                        key=lambda x: (-x[0], x[1]))
        return ranked[0] if ranked and ranked[0][0] > 0 else None

    # 三级：① 人工范围内有证据 → 范围内取最强；② 任何条目有证据 → 取最强（新条目由此获得卡片）；
    #       ③ 全无证据 → 回落人工首选
    pick = best_of(mapped & strong_hits)
    if pick:
        best, reason = pick[1], f'人工范围内命中（{pick[0]:.2f}，范围 {len(mapped)} 个）'
    else:
        pick = best_of(strong_hits)
        if pick:
            best, reason = pick[1], f'范围内无证据，按关键词归入新条目（{pick[0]:.2f}）'
        else:
            best, reason = (first_choices[0] if first_choices else sorted(candidates)[0]), '全无关键词证据，回落人工首选'

    # 参见区：强 + 弱证据都算（弱证据只能用在这里）
    see = [e['id'] for e in spec['entries']
           if e['id'] != best and e['id'] in assignable
           and score(e['keywords'] + e['weak'], cid) > 0]
    return {'primary': best, 'facets': [], 'see_also': see, 'tags': tags, 'reason': reason}


if __name__ == '__main__':
    spec = load_spec()
    print(f"范畴 {len(spec['layers'])} · 条目 {len(spec['entries'])} · "
          f"故事分面 {len(spec['facets'])} · 旧→新映射 {len(spec['mapping'])}")

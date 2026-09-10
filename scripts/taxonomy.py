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

SEC_LAYERS = '一、五个观察角度'
SEC_ENTRIES = '二、二十条目'
SEC_FACETS = '三、故事域的三个字段、十七个分面'
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
    facets = [{'id': r[0], 'name': r[1], 'field': r[2], 'keywords': _kw(r[3])}
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
            'mapping': mapping, 'override': override,
            # 旧标签先验加成（首选 / 次选）：见 docs/taxonomy-plan.md §五
            'prior': (2.5, 1.0)}


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
    assignable = {e['id'] for e in spec['entries'] if not e['tag']}   # 复分标签不持卡

    # 复分标记：所有卡片（含故事）都算
    tags = [e['id'] for e in spec['entries'] if e['tag']
            and score(e['keywords'] + e['weak'], cid) > 0]

    if card.get('type') == 'case':                    # 故事体 → 分面
        facets = [f['id'] for f in spec['facets'] if score(f['keywords'], cid) > 0]
        return {'primary': None, 'facets': facets, 'see_also': [], 'tags': tags,
                'reason': '故事体走分面'}

    # 人工裁定优先于算法（见 taxonomy.md §六）
    forced = spec.get('override', {}).get(cid)
    if forced:
        see = [e['id'] for e in spec['entries']
               if e['id'] != forced['primary'] and not e['tag']
               and score(e['keywords'] + e['weak'], cid) > 0]
        return {'primary': forced['primary'], 'facets': [], 'see_also': see, 'tags': tags,
                'reason': f'人工裁定（{forced["why"]}）'}

    # 旧标签 = **加分先验**，不是候选围栏：优先项加成大、次选项加成小、没被旧标签提到的条目 0 分。
    # 这样「文本证据明显更强」的条目能翻盘（新条目由此获得卡片），而旧标签在证据接近时仍然说了算。
    p_first, p_second = spec.get('prior', (2.5, 1.0))
    prior: dict[str, float] = {}
    for t in card.get('topics', []):
        m = spec['mapping'].get(t)
        if not m:
            continue
        if m['primary'] in assignable:
            prior[m['primary']] = max(prior.get(m['primary'], 0.0), p_first)
        for s in m['secondary']:
            if s in assignable:
                prior[s] = max(prior.get(s, 0.0), p_second)

    kw = {e['id']: score(e['keywords'], cid) for e in spec['entries'] if e['id'] in assignable}
    total = {e: kw[e] + prior.get(e, 0.0) for e in kw}
    candidates = {e for e in kw if kw[e] > 0 or prior.get(e, 0.0) > 0}
    if not candidates:
        return {'primary': None, 'facets': [], 'see_also': [], 'tags': tags,
                'reason': '无旧标签映射且无关键词命中'}

    best = sorted(candidates, key=lambda e: (-total[e], e))[0]
    if kw[best] <= 0:
        reason = '全无关键词证据，按旧标签先验定夺'
    elif best in prior:
        reason = (f'旧标签先验 + 文本证据（关键词 {kw[best]:.2f} + 先验 {prior[best]:.1f}'
                  f' = {total[best]:.2f}）')
        runner = sorted((e for e in candidates if e != best), key=lambda e: (-total[e], e))
        if runner and total[runner[0]] > total[best] - 1e-9:
            reason += '（并列）'
    else:
        runner = sorted((e for e in candidates if e != best), key=lambda e: (-total[e], e))
        beat = f'，压过旧标签项 {total[runner[0]]:.2f}' if runner else ''
        reason = f'文本证据推翻旧标签（关键词 {kw[best]:.2f}{beat}）'

    # 参见区：强 + 弱证据都算（弱证据只能用在这里）
    see = [e['id'] for e in spec['entries']
           if e['id'] != best and e['id'] in assignable
           and score(e['keywords'] + e['weak'], cid) > 0]
    return {'primary': best, 'facets': [], 'see_also': see, 'tags': tags, 'reason': reason}


if __name__ == '__main__':
    spec = load_spec()
    print(f"范畴 {len(spec['layers'])} · 条目 {len(spec['entries'])} · "
          f"故事分面 {len(spec['facets'])} · 旧→新映射 {len(spec['mapping'])}")

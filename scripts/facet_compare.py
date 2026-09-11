# -*- coding: utf-8 -*-
"""比对：关键词分面 vs 两份独立判读。

门槛（跑数之前定死在 docs/facet-labeling-plan.md §三）：
  ③ 分面级一致率 ≥ 80%
  ④ 「是否至少落进一个字段」一致率 ≥ 90%
判定用 F1（集合比较），并同时给出两份判读之间的一致率作为参照上限——
判读自己都对不齐的部分，不该算在关键词头上。
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
from taxonomy import load_spec  # noqa: E402

OUT = ROOT / 'local_working_copy' / 'facet-validate'


def read_pass(path: Path) -> dict[str, set[str]]:
    got = {}
    for line in path.read_text(encoding='utf-8').splitlines():
        line = line.strip()
        if not line.startswith('sk-'):
            continue
        m = re.match(r'^(sk-\d{4})\s*\|\s*([^|]*)\|', line)
        if not m:
            continue
        cid, cell = m.group(1), m.group(2).strip()
        if cell.upper() in ('NONE', '—', '-', ''):
            got[cid] = set()
        else:
            got[cid] = {x.strip() for x in re.split(r'[,，、\s]+', cell) if x.strip()}
    return got


def f1(a: set[str], b: set[str]) -> float:
    if not a and not b:
        return 1.0
    if not a or not b:
        return 0.0
    inter = len(a & b)
    if not inter:
        return 0.0
    p, r = inter / len(a), inter / len(b)
    return 2 * p * r / (p + r)


def summarize(name_a: str, a: dict[str, set[str]],
              name_b: str, b: dict[str, set[str]]) -> dict:
    ids = sorted(set(a) & set(b))
    f1s = [f1(a[i], b[i]) for i in ids]
    exact = sum(1 for i in ids if a[i] == b[i])
    nonempty = sum(1 for i in ids if (bool(a[i]) == bool(b[i])))
    micro_i = sum(len(a[i] & b[i]) for i in ids)
    micro_a = sum(len(a[i]) for i in ids)
    micro_b = sum(len(b[i]) for i in ids)
    micro_p = micro_i / micro_a if micro_a else 0
    micro_r = micro_i / micro_b if micro_b else 0
    micro_f1 = 2 * micro_p * micro_r / (micro_p + micro_r) if (micro_p + micro_r) else 0
    print(f'\n=== {name_a} vs {name_b}（{len(ids)} 张）===')
    print(f'  完全一致：{exact}/{len(ids)}（{exact / len(ids) * 100:.1f}%）')
    print(f'  平均 F1：{sum(f1s) / len(f1s) * 100:.1f}%')
    print(f'  微平均 F1：{micro_f1 * 100:.1f}%'
          f'（precision {micro_p * 100:.1f}% / recall {micro_r * 100:.1f}%）')
    print(f'  「是否有标记」一致：{nonempty}/{len(ids)}（{nonempty / len(ids) * 100:.1f}%）')
    return {'exact': exact / len(ids), 'f1': sum(f1s) / len(f1s),
            'micro_f1': micro_f1, 'nonempty': nonempty / len(ids), 'n': len(ids)}


def main() -> None:
    spec = load_spec()
    field_of = {f['id']: f['field'] for f in spec['facets']}
    key = json.load(open(OUT / 'sample-key.json', encoding='utf-8'))
    kw = {k: set(v) for k, v in key['keyword'].items()}

    files = {'A': OUT / 'passA.out.txt', 'B': OUT / 'passB.out.txt'}
    passed = {k: read_pass(p) for k, p in files.items() if p.exists()}
    print(f'读到：{", ".join(f"{k}({len(v)}张)" for k, v in passed.items())}')
    if len(passed) < 2:
        print('⚠ 两份判读还没齐，先只报有的。')

    res = {}
    if 'A' in passed and 'B' in passed:
        res['判读A vs 判读B'] = summarize('判读A', passed['A'], '判读B', passed['B'])
    for k, v in passed.items():
        res[f'关键词 vs 判读{k}'] = summarize('关键词', kw, f'判读{k}', v)

    # 门槛
    print('\n=== 门槛对照（docs/facet-labeling-plan.md §三）===')
    ok = True
    if 'A' in passed:
        s = res['关键词 vs 判读A']
        c3 = s['micro_f1'] >= 0.80
        c4 = s['nonempty'] >= 0.90
        print(f"  ③ 分面级一致率（微平均 F1）{s['micro_f1'] * 100:.1f}%　门槛 ≥80%　"
              f"{'达标' if c3 else '**不达标**'}")
        print(f"  ④ 「是否有标记」一致 {s['nonempty'] * 100:.1f}%　门槛 ≥90%　"
              f"{'达标' if c4 else '**不达标**'}")
        ok = c3 and c4
    print(f"\n  结论：{'门槛全部达标' if ok else '有门槛不达标 → 按 §四 记例外'}")

    # 哪个分面在拖后腿（关键词 vs 判读A）
    if 'A' in passed:
        print('\n=== 逐分面（关键词 vs 判读A）===')
        rows = []
        for f in spec['facets']:
            fid = f['id']
            k_n = sum(1 for i in kw if fid in kw[i])
            a_n = sum(1 for i in passed['A'] if fid in passed['A'][i])
            both = sum(1 for i in kw if i in passed['A'] and fid in kw[i] and fid in passed['A'][i])
            only_kw = sum(1 for i in kw if i in passed['A'] and fid in kw[i] and fid not in passed['A'][i])
            only_a = sum(1 for i in kw if i in passed['A'] and fid not in kw[i] and fid in passed['A'][i])
            f1s = []
            for i in kw:
                if i in passed['A']:
                    f1s.append(f1({fid} if fid in kw[i] else set(),
                                  {fid} if fid in passed['A'][i] else set()))
            rows.append((sum(f1s) / len(f1s), fid, f['name'], k_n, a_n, both, only_kw, only_a))
        for sc, fid, name, k_n, a_n, both, only_kw, only_a in sorted(rows):
            flag = '  ← 弱' if sc < 0.5 else ''
            print(f'  {fid} {name[:10]:12s} F1 {sc * 100:5.1f}%　关键词给 {k_n:3d} · 判读给 {a_n:3d}'
                  f' · 都对 {both:3d} · 只关键词 {only_kw:3d} · 只判读 {only_a:3d}{flag}')

    json.dump(res, open(OUT / 'compare.json', 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()

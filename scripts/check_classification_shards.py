# -*- coding: utf-8 -*-
"""数据层一致性体检：`web/data/` 的分片必须和 `classification.json` 对得上。

为什么需要这个脚本（都是真踩过的坑）：
  1. `collect` 一度把 673 张故事卡的**判读分面**重算成关键词分面，而关键词那一版
     的一致率只有 61.4%（没过门槛）——数据被悄悄换成了不该上线的那一套。
  2. `build_site.py` 里的 `facets_ready` 一度是硬编码 `False`、计数写死 0，
     于是 `data.json` 和 `meta.json` 说的不是同一件事。
  3. 卡片改过 type（论述 ↔ 故事）之后，旧分片会继续留在 `web/data/` 里，
     页面上看不出任何异常。

这三种错误**都不会让任何别的检查失败**，但都会让页面显示错的东西。
所以这里逐条对账：分类 JSON 是唯一真相，分片必须服从它。

用法：
    python scripts/check_classification_shards.py      # 只查，不写
退出码非 0 表示有不一致。
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))

from taxonomy import load_spec  # noqa: E402

DATA = ROOT / 'web' / 'data'
PROBLEMS: list[str] = []


def fail(msg: str) -> None:
    PROBLEMS.append(msg)


def main() -> int:
    spec = load_spec()
    cls = json.loads((ROOT / 'classification.json').read_text(encoding='utf-8'))
    meta = json.loads((DATA / 'meta.json').read_text(encoding='utf-8'))
    data = json.loads((ROOT / 'web' / 'data.json').read_text(encoding='utf-8'))
    index = json.loads((DATA / 'index.json').read_text(encoding='utf-8'))['cards']
    index_by_id = {c['id']: c for c in index}

    # --- 1) 每张卡的主归属/参见/分面/标签，分片里必须与分类 JSON 一致
    for cid, rec in cls.items():
        got = index_by_id.get(cid)
        if got is None:
            fail(f'index.json 缺少卡片 {cid}')
            continue
        if (rec.get('primary') or None) != (got.get('primary') or None):
            fail(f'{cid} 主归属不一致：分类 {rec.get("primary")} vs 分片 {got.get("primary")}')
        if sorted(rec.get('seealso') or []) != sorted(got.get('seealso') or []):
            fail(f'{cid} 参见不一致：{rec.get("seealso")} vs {got.get("seealso")}')
        if (got.get('tags') or []) != (rec.get('tags') or []):
            fail(f'{cid} 复分标签不一致：{rec.get("tags")} vs {got.get("tags")}')

    # --- 2) meta 的条目计数/被参见数/复分标记数，必须现算一致
    for e in meta['entries']:
        code = e['code']
        want_p = sum(1 for r in cls.values() if r.get('primary') == code)
        want_c = sum(1 for r in cls.values() if code in (r.get('seealso') or []))
        want_t = sum(1 for r in cls.values() if code in (r.get('tags') or []))
        if e['count'] != want_p:
            fail(f'meta {code} count={e["count"]} 与现算 {want_p} 不一致')
        if e['cross'] != want_c:
            fail(f'meta {code} cross={e["cross"]} 与现算 {want_c} 不一致')
        if e.get('tag') and e.get('tag_count') != want_t:
            fail(f'meta {code} tag_count={e.get("tag_count")} 与现算 {want_t} 不一致')
        if not e.get('tag') and e['count'] == 0:
            fail(f'meta {code} 既不是复分标签又没有卡片——条目可能是死的')

    # --- 3) 分面：计数与卡片清单，以及「来源」标记
    srcs = {r.get('facet_source') for r in cls.values() if r.get('type') == 'case'}
    ready = meta.get('facets_ready')
    if srcs == {'judge'} and not ready:
        fail('分面全部来自判读，但 facets_ready 是 false')
    if 'keyword' in srcs and ready:
        fail('还有分面来自关键词（未过门槛），但 facets_ready 是 true')
    if ready != data['taxonomy']['facets_ready']:
        fail(f'facets_ready 不一致：meta={ready} vs data.json={data["taxonomy"]["facets_ready"]}')
    for f in meta['facets']:
        want = sum(1 for r in cls.values() if f['code'] in (r.get('facets') or []))
        if f['count'] != want:
            fail(f'meta 分面 {f["code"]} count={f["count"]} 与现算 {want} 不一致')
        shard = DATA / 'facet' / f'{f["code"]}.json'
        if not shard.exists():
            fail(f'缺少分面分片 {f["code"]}.json')
            continue
        payload = json.loads(shard.read_text(encoding='utf-8'))
        if payload['count'] != want or len(payload['cards']) != want:
            fail(f'分面分片 {f["code"]} count={payload["count"]}/cards={len(payload["cards"])}'
                 f' 与现算 {want} 不一致')
        if payload.get('ready') != ready:
            fail(f'分面分片 {f["code"]} ready={payload.get("ready")} 与 meta {ready} 不一致')

    # --- 4) 条目分片：主归属卡 / 交叉参见卡 / 复分标记卡
    for e in meta['entries']:
        code = e['code']
        shard = DATA / 'entry' / f'{code}.json'
        if not shard.exists():
            fail(f'缺少条目分片 {code}.json')
            continue
        payload = json.loads(shard.read_text(encoding='utf-8'))
        if e.get('tag'):
            want = sum(1 for r in cls.values() if code in (r.get('tags') or []))
        else:
            want = sum(1 for r in cls.values() if r.get('primary') == code)
        if len(payload['cards']) != want:
            fail(f'条目分片 {code} cards={len(payload["cards"])} 与现算 {want} 不一致')
        want_cross = sum(1 for r in cls.values() if code in (r.get('seealso') or []))
        if len(payload['cross']) != want_cross:
            fail(f'条目分片 {code} cross={len(payload["cross"])} 与现算 {want_cross} 不一致')

    # --- 5) 卡片总数
    if meta['counts']['cards'] != len(cls):
        fail(f'meta 卡数 {meta["counts"]["cards"]} ≠ classification.json {len(cls)}')
    if len(data['cards']) != len(cls):
        fail(f'data.json 卡数 {len(data["cards"])} ≠ classification.json {len(cls)}')

    if PROBLEMS:
        print(f'分类分片一致性：**{len(PROBLEMS)} 处不一致**')
        for p in PROBLEMS[:25]:
            print('  ✗ ' + p)
        if len(PROBLEMS) > 25:
            print(f'  … 另有 {len(PROBLEMS) - 25} 处')
        return 1
    print(f'分类分片一致性：全部一致（{len(cls)} 张卡 · {len(meta["entries"])} 条目 · '
          f'{len(meta["facets"])} 分面 · facets_ready={meta["facets_ready"]}）')
    return 0


if __name__ == '__main__':
    sys.exit(main())

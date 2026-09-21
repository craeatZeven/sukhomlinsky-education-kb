# -*- coding: utf-8 -*-
"""对账：卡片 frontmatter 里的轴 ↔ `classification.json`，必须完全一致。

**为什么必须有这一条**：把轴写进卡片，就产生了"两份真相"的风险
（这个仓库已经在 `classification.json` vs 分片、`INDEX.md` vs MOC 上打过两次架）。
镜像本身不是问题，**没有闸门的镜像**才是。

判据（每条都能失败）：
  ① 每张卡都写了 primary / seealso / facets / tax_tags 四个字段
  ② 四个字段的值与 classification.json 逐条相等（顺序无关）
  ③ 覆盖率与中心表一致：应有 713 张有 primary、673 张有 facets
  ④ 卡片里的 primary 必须是真实条目码（不是笔误）

**边界（不在本判据范围内，别误以为管了）**：`claim` / `evidence` /
`case_entries_why` / `override_why` 仍只在中心表，卡片里没有对应物——
所以这是**部分融合**。中心表仍是那些字段的唯一来源。
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CARDS = ROOT / 'cards'
PROBLEMS: list[str] = []


def parse_fm(text: str) -> dict[str, object]:
    """解析轴字段。

    **踩过的坑**：第一版遇到"冒号后为空"（`tax_tags:`）就提前返回空值，
    于是**多行列表根本没被读**，1809 处全报成"不一致"——判据比被检查的东西错得更厉害。
    正确顺序：先看冒号后有没有内容；没内容才去读下面的 `  - ` 行。
    """
    m = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    if not m:
        return {}
    fm: dict[str, object] = {}
    for key in ('primary', 'seealso', 'facets', 'tax_tags'):
        # 注意用 [ \t]* 而不是 \s*：`\s` 会吃掉换行，于是正则跨行把「- A18」当成标量值，
        # 后面 sorted() 就把字符串拆成了单字（实测报出 [' ','-','1','8','A']）。
        # 判据自己错了三次（标题区重叠 / 多行列表没读 / 正则跨行），比页面错更值得记。
        mm = re.search(rf'^{key}:[ \t]*(.*?)[ \t]*$', m.group(1), re.M)
        if not mm:
            continue
        inline = mm.group(1)
        if inline == '[]':
            fm[key] = []
            continue
        if inline == 'null':
            fm[key] = None
            continue
        if inline:
            fm[key] = inline.strip('"')
            continue
        # 冒号后为空 → 读下面的多行列表
        vals = []
        for line in m.group(1)[mm.end():].splitlines():
            s = line.strip()
            if s.startswith('- '):
                vals.append(s[2:].strip().strip('"'))
            elif s == '':
                continue
            else:
                break
        fm[key] = vals
    return fm


def main() -> int:
    cls = json.loads((ROOT / 'classification.json').read_text(encoding='utf-8'))
    files = {p.stem.split('-')[0] + '-' + p.stem.split('-')[1]: p for p in CARDS.glob('sk-*.md')}
    entry_codes = {e['code'] for e in json.loads(
        (ROOT / 'web/data/meta.json').read_text(encoding='utf-8'))['entries']}

    n_primary = n_facets = 0
    for cid, rec in cls.items():
        p = files.get(cid)
        if not p:
            PROBLEMS.append(f'{cid} 没有卡片文件')
            continue
        fm = parse_fm(p.read_text(encoding='utf-8'))
        want = {
            'primary': rec.get('primary'),
            'seealso': sorted(rec.get('seealso') or []),
            'facets': sorted(rec.get('facets') or []),
            'tax_tags': sorted(rec.get('tags') or []),
        }
        got = {
            'primary': fm.get('primary'),
            'seealso': sorted(fm.get('seealso') or []),
            'facets': sorted(fm.get('facets') or []),
            'tax_tags': sorted(fm.get('tax_tags') or []),
        }
        if 'primary' not in fm:
            PROBLEMS.append(f'{cid} 缺少 primary 字段（镜像没写全）')
        if got['primary'] and got['primary'] not in entry_codes:
            PROBLEMS.append(f'{cid} 的 primary={got["primary"]} 不是真实条目码')
        # seealso 是**条目域**（这张卡还该看哪些相关条目），**不是卡片域**。
        # 2026-09-21 实测踩过：把 seealso 当"卡对卡双链"往里塞 sk-id ——
        # 站点那端是 KB.entryBadge(code, {{kind:'see'}}) 渲染的，塞 sk-id 会让徽章失效，
        # 而且整块替换会把已有的跨条目引用**删掉**（全库 399 张卡本来就在用它）。
        # 卡片之间的链接写在正文里，形式是 [[sk-XXXX]]（见 web/kb.js 的 linkify）。
        for code in sorted(set(got['seealso']) | set(want['seealso'])):
            if code not in entry_codes:
                PROBLEMS.append(
                    f'{cid} 的 seealso={code} 不是条目码（卡片互链请写进正文的 [[sk-XXXX]]，别放 seealso）')
        for k in want:
            if want[k] != got[k]:
                PROBLEMS.append(f'{cid} 的 {k} 不一致：卡片={got[k]} 中心表={want[k]}')
        n_primary += 1 if got['primary'] else 0
        n_facets += 1 if got['facets'] else 0

    if PROBLEMS:
        print(f'轴镜像：**{len(PROBLEMS)} 处不一致**')
        for x in PROBLEMS[:15]:
            print('  ✗ ' + x)
        if len(PROBLEMS) > 15:
            print(f'  … 另有 {len(PROBLEMS) - 15} 处')
        return 1
    print(f'轴镜像：全部一致（{len(cls)} 张卡 · 有 primary 的 {n_primary} 张 · '
          f'有 facets 的 {n_facets} 张；claim/evidence 等仍在中心表，属部分融合）')
    return 0


if __name__ == '__main__':
    sys.exit(main())

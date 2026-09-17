# -*- coding: utf-8 -*-
"""重排顶栏导航：**一条主轴 + 换一种切法**（用户 2026-09-17 选 B）。

## 为什么用程序改
20 个页面共用同一段顶栏，手改必然各不相同——这个项目在"同源样式被逐页写死"上
已经栽过三次（见 `docs/review-disposition.md`）。这里只写一处模板，逐页替换，
并对每个文件断言：**恰好替换到一次**、替换后**组数与目的地数符合预期**。

## 这次改了什么（15 个目的地 → 7 个）
旧导航是 15 个目的地平铺，其中**5 个页面都在回答"这个库怎么分类"**，读者不知道该看哪个：
分类总图 / 分类条目 / 故事分面 / 思想地图 / 教育专题。
新结构把**分类立成主轴**，其余都降为"换一种切法"（由枢纽页内部链接提供）：

    找材料  分类总图（主轴）· 全库检索 · 读本
    看来源  书源与作品 · 覆盖报告
    用起来  使用指南 · 最近更新

被移出导航的 8 个目的地（分类条目 / 故事分面 / 思想地图 / 筛选浏览 / 教育专题 /
真实问题 / 困境案例 / 故事索引）**必须仍能从枢纽页点到**——
这条由 `scripts/check_site_links.py` 守着（从首页 ≤3 跳可达），不靠人记。
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WEB = ROOT / 'web'

GROUPS = [
    ('find', '找材料', [
        ('taxonomy.html', '分类总图', '主轴：这个库怎么分类 · 换一种切法'),
        ('search.html', '全库检索', '按词找；先给成篇材料，再给卡片'),
        ('reads.html', '读本', '12 篇长文 + 分析 / 对比 / 问答'),
    ]),
    ('source', '看来源', [
        ('sources.html', '书源与作品', '13 个来源、OCR 状态与作品清单'),
        ('coverage.html', '覆盖报告', '卡片量、来源分布与覆盖缺口'),
    ]),
    ('use', '用起来', [
        ('guide.html', '使用指南', '5 分钟上手：三种用法、引用与导出'),
        ('latest.html', '最近更新', '按编号倒序看最新补入的卡片'),
    ]),
]

# 每页高亮：(组, href)。**分类轴的下级页面统一高亮"分类总图"**——
# 它们都是主轴上的"换一种切法"，读者仍处在"找材料"这件事里。
ACTIVE: dict[str, tuple[str | None, str | None]] = {
    'index.html': (None, None),
    'taxonomy.html': ('find', 'taxonomy.html'),
    'entries.html': ('find', 'taxonomy.html'),
    'entry.html': ('find', 'taxonomy.html'),
    'facets.html': ('find', 'taxonomy.html'),
    'facet.html': ('find', 'taxonomy.html'),
    'clusters.html': ('find', 'taxonomy.html'),
    'explore.html': ('find', 'taxonomy.html'),
    'search.html': ('find', 'search.html'),
    'problem.html': ('find', 'search.html'),
    'reads.html': ('find', 'reads.html'),
    'topics.html': ('find', 'reads.html'),
    'topic.html': ('find', 'reads.html'),
    'cases.html': ('find', 'reads.html'),
    'stories.html': ('find', 'reads.html'),
    'sources.html': ('source', 'sources.html'),
    'coverage.html': ('source', 'coverage.html'),
    'guide.html': ('use', 'guide.html'),
    'latest.html': ('use', 'latest.html'),
    'card.html': (None, None),
}

# 一页顶栏的形状。**必须与页面里真实存在的结构一致**：
# 实测真实结构是 `<nav class="topnav"><div class="inner"><div class="nav-groups">…`；
# 我第一版新工具按 `<header class="topnav">` 写，一跑就 SystemExit
# ——工具与产物脱节是"同源被逐页写死"的另一种表现，同样要防。
NAV_RE = re.compile(r'<nav class="topnav">.*?</nav>', re.S)


def esc(s: str) -> str:
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def build_nav(page: str) -> str:
    act_group, act_href = ACTIVE.get(page, (None, None))
    out = ['<nav class="topnav">', '  <div class="inner">',
           '    <a class="brand" href="index.html">苏霍姆林斯基教育知识库</a>',
           '    <div class="nav-groups">']
    for gid, glabel, items in GROUPS:
        gcls = 'nav-group active' if gid == act_group else 'nav-group'
        mid = f'navMenu-{gid}'
        out.append(f'      <div class="{gcls}" data-group="{gid}">')
        out.append(f'        <button class="nav-group-btn" type="button" '
                   f'aria-expanded="false" aria-controls="{mid}">{esc(glabel)}</button>')
        out.append(f'        <div class="nav-menu" id="{mid}">')
        for href, label, sub in items:
            cls = 'nav-link' + (' active' if act_href and href == act_href else '')
            extra = ' aria-current="page"' if act_href and href == act_href else ''
            out.append(f'          <a class="{cls}" href="{href}"{extra}>'
                       f'<span class="nav-menu-label">{esc(label)}</span>'
                       f'<span class="nav-menu-sub">{esc(sub)}</span></a>')
        out.append('        </div>')
        out.append('      </div>')
    out += ['    </div>', '  </div>', '</nav>']
    return '\n'.join(out)


def main() -> int:
    want_links = sum(len(items) for _g, _l, items in GROUPS)
    n_pages = 0
    for path in sorted(WEB.glob('*.html')):
        page = path.name
        if page not in ACTIVE:
            print(f'  !! {page} 不在 ACTIVE 表里，跳过（新页面要补进来）')
            continue
        text = path.read_text(encoding='utf-8')
        found = NAV_RE.findall(text)
        if len(found) != 1:
            raise SystemExit(f'{page}: 期望恰好 1 段顶栏，实际 {len(found)} 段')
        new = NAV_RE.sub(lambda _m: build_nav(page), text, count=1)
        n_links = len(re.findall(r'class="nav-link', new))
        n_groups = len(re.findall(r'class="nav-group[ "]', new))
        if n_groups != len(GROUPS) or n_links != want_links:
            raise SystemExit(f'{page}: 组数 {n_groups}（应 {len(GROUPS)}）· '
                             f'链接数 {n_links}（应 {want_links}）')
        if new != text:
            path.write_text(new, encoding='utf-8', newline='\n')
        n_pages += 1
        print(f'  {page:16s} {n_groups} 组 / {n_links} 项 · 高亮 {ACTIVE[page][1] or "无"}')
    print(f'\n{n_pages} 个页面已重排（{len(GROUPS)} 组 / {want_links} 个目的地）')
    return 0


if __name__ == '__main__':
    sys.exit(main())

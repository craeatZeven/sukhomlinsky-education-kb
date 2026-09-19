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

# 2026-09-20：用户贴了 B 站顶栏的图 ——「导航栏能不能做成 B 站这个这样，可以不止三个，展开一点也行」。
# 原来是**三个下拉组**（找材料 / 看来源 / 用起来），七个目的地要悬停才看得见。
# 现在改成**一排平铺的「图标 + 文字」**：七个入口全部露在外面，一次点到位。
#
# 为什么不是简单的「删掉下拉」：原来那三个组名（找材料 / 看来源 / 用起来）是**分类**，
# 分类对熟悉站点的人有用，对新读者是二次抽象。B 站那种做法把分类丢掉、直接给入口 ——
# 代价是丢了一层「这些页面是同一类事」的提示，收益是**零悬停成本**。用户要的就是后者。
ITEMS = [
    ('taxonomy.html', '分类总图', 'map',    '这个库怎么分类 · 换一种切法'),
    ('search.html',   '全库检索', 'search', '按词找；先给成篇材料，再给卡片'),
    ('reads.html',    '读本',     'book',   '12 篇长文 + 分析 / 对比 / 问答'),
    ('sources.html',  '书源',     'stack',  '13 个来源、OCR 状态与作品清单'),
    ('coverage.html', '覆盖',     'chart',  '卡片量、来源分布与覆盖缺口'),
    ('guide.html',    '指南',     'compass','5 分钟上手：三种用法、引用与导出'),
    ('latest.html',   '更新',     'clock',  '按编号倒序看最新补入的卡片'),
]

# 图标：内联 SVG，20px，描边走 currentColor（不引外部图标库，零依赖）。
# 每个都带 title 用不上 —— 可见文字就是标签，图标只是**扫读时的锚点**（B 站那排的意义也在这）。
ICONS = {
    'map':     '<path d="M3 6.5l6-2 6 2 6-2v13l-6 2-6-2-6 2z"/><path d="M9 4.5v13M15 6.5v13"/>',
    'search':  '<circle cx="11" cy="11" r="6.5"/><path d="M15.8 15.8L21 21"/>',
    'book':    '<path d="M12 6.5C10.6 5 8.6 4.2 6 4.2H4v13.6h2c2.6 0 4.6.8 6 2.3"/><path d="M12 6.5c1.4-1.5 3.4-2.3 6-2.3h2v13.6h-2c-2.6 0-4.6.8-6 2.3"/><path d="M12 6.5v13.6"/>',
    'stack':   '<path d="M4 5.5h4v15H4zM10 5.5h4v15h-4z"/><path d="M16.4 6.6l3.4 1-3.6 13.6-3.4-1z"/>',
    'chart':   '<path d="M4 20V11M10 20V5M16 20v-6"/><path d="M2 20h20"/>',
    'compass': '<circle cx="12" cy="12" r="8.6"/><path d="M15.4 8.6l-2.1 4.7-4.7 2.1 2.1-4.7z"/>',
    'clock':   '<circle cx="12" cy="12" r="8.6"/><path d="M12 7v5.3l3.6 2.1"/>',
}

# 每页高亮：(组, href)。**分类轴的下级页面统一高亮"分类总图"**——
# 它们都是主轴上的"换一种切法"，读者仍处在"找材料"这件事里。
# 每页高亮哪个入口。平铺之后不再需要组名，只留 href。
# **分类轴的下级页面统一高亮「分类总图」**——它们都是主轴上的「换一种切法」，
# 读者仍处在「找材料」这件事里。
ACTIVE: dict[str, str | None] = {
    'index.html': None,
    'taxonomy.html': 'taxonomy.html',
    'entries.html': 'taxonomy.html',
    'entry.html': 'taxonomy.html',
    'facets.html': 'taxonomy.html',
    'facet.html': 'taxonomy.html',
    'clusters.html': 'taxonomy.html',
    'explore.html': 'taxonomy.html',
    'search.html': 'search.html',
    'problem.html': 'search.html',
    'reads.html': 'reads.html',
    'topics.html': 'reads.html',
    'topic.html': 'reads.html',
    'cases.html': 'reads.html',
    'stories.html': 'reads.html',
    'sources.html': 'sources.html',
    'coverage.html': 'coverage.html',
    'guide.html': 'guide.html',
    'latest.html': 'latest.html',
    'sitemap.html': 'guide.html',
    'card.html': None,
}

# 一页顶栏的形状。**必须与页面里真实存在的结构一致**：
# 实测真实结构是 `<nav class="topnav"><div class="inner"><div class="nav-groups">…`；
# 我第一版新工具按 `<header class="topnav">` 写，一跑就 SystemExit
# ——工具与产物脱节是"同源被逐页写死"的另一种表现，同样要防。
NAV_RE = re.compile(r'<nav class="topnav">.*?</nav>', re.S)


def esc(s: str) -> str:
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def build_nav(page: str) -> str:
    act = ACTIVE.get(page)
    out = ['<nav class="topnav">', '  <div class="inner">',
           '    <a class="brand" href="index.html">苏霍姆林斯基教育知识库</a>',
           '    <div class="nav-groups">']
    for href, label, icon, sub in ITEMS:
        on = (href == act)
        cls = 'nav-item active' if on else 'nav-item'
        extra = ' aria-current="page"' if on else ''
        # title 保留一句话说明：平铺后文字更短（书源 / 覆盖 / 指南 / 更新），
        # 悬停能看到全称；屏幕阅读器读到的是 <span> 里的可见文字 + 这里的 title。
        out.append(f'      <a class="{cls}" href="{href}"{extra} title="{esc(sub)}">'
                   f'<span class="ni-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" '
                   f'stroke="currentColor" stroke-width="1.7" stroke-linecap="round" '
                   f'stroke-linejoin="round">{ICONS[icon]}</svg></span>'
                   f'<span class="ni-label">{esc(label)}</span></a>')
    out += ['    </div>', '  </div>', '</nav>']
    return '\n'.join(out)


def main() -> int:
    want_links = len(ITEMS)
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
        n_links = len(re.findall(r'class="nav-item', new))
        if n_links != want_links:
            raise SystemExit(f'{page}: 入口数 {n_links}（应 {want_links}）')
        # 平铺之后不该再有下拉：残留 .nav-group 说明模板没换干净
        if 'nav-group"' in new or 'nav-menu' in new:
            raise SystemExit(f'{page}: 仍残留下拉结构')
        if new != text:
            path.write_text(new, encoding='utf-8', newline='\n')
        n_pages += 1
        print(f'  {page:16s} {n_links} 个平铺入口 · 高亮 {ACTIVE[page] or "无"}')
    print(f'\n{n_pages} 个页面已重排（{want_links} 个平铺入口，无下拉）')
    return 0


if __name__ == '__main__':
    sys.exit(main())

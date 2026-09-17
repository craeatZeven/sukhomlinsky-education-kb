# -*- coding: utf-8 -*-
"""站点可达性判据：**从首页出发，每页都要能在 N 跳内点到**；链接不许指向不存在的文件。

## 为什么需要它
用户选了 B 方案（一条主轴 + "换一种切法"）——把导航从 15 个目的地减到 5 个，
**被移出导航的页面（分类条目 / 故事分面 / 思想地图 / 筛选浏览 / 覆盖报告 / 最近更新…）
就只剩"从枢纽页点进去"这一条路**。没有这张安全网，减导航等于制造孤岛：
页面还在、URL 还能开，但读者永远撞不进去（搜索引擎也未必收录）。
这正是这个项目一贯警惕的**静默问题**。

## 判据（每条都能失败）
  ① 站内链接（web/*.html 之间的相对链接）不许指向不存在的文件
  ② 除首页外每一页都要能在 **≤3 跳**内从 index.html 到达
  ③ 报告每页的最短跳数（枢纽页应当 ≤2，深层页 ≤3）
"""
from __future__ import annotations

import re
import sys
from collections import deque
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
WEB = ROOT / 'web'
NOTE = WEB / 'note'
MAX_HOPS = 3
PROBLEMS: list[str] = []

HREF = re.compile(r'href="([^"#?]+)(?:\?[^"#]*)?(?:#[^"]*)?"')


def pages() -> list[Path]:
    return sorted(WEB.glob('*.html')) + sorted(NOTE.glob('*.html'))


def static_hrefs(text: str) -> list[str]:
    """只取**静态** href。

    要跳过 JS 模板串里的 `href="${cardLink(prev)}"`——那是运行时才生成的，
    静态检查既解析不了、也不该报成死链（第一版报了 4427 处，绝大多数是它）。
    """
    out = []
    for m in HREF.finditer(text):
        h = m.group(1)
        if '${' in h or h.startswith(('http://', 'https://', 'mailto:', 'data:', '#')):
            continue
        out.append(h)
    return out


def resolve_dir(p: Path) -> Path:
    """一页里的相对链接该按哪个目录解析——**要认 `<base>`**。

    旁挂层页面（web/note/*.html）用 `<base href="../">` 把基准抬到 web/，
    所以它们的 `href="card.html"` 指的是 web/card.html。
    第一版按 `p.parent`（= web/note/）解析，于是把 50 个页面**本来正确的**链接
    全报成死链——判据不认 `<base>` 就等于不认浏览器怎么解析。
    """
    m = re.search(r'<base\s+href="([^"]+)"', p.read_text(encoding='utf-8'))
    if not m:
        return p.parent
    return (p.parent / m.group(1)).resolve()


def link_targets(p: Path, all_pages: set[str]) -> set[str]:
    """把一页里的站内链接解析成"目标页面名"（相对 web/ 的路径）。"""
    out: set[str] = set()
    base = resolve_dir(p)
    for h in static_hrefs(p.read_text(encoding='utf-8')):
        if h.startswith('../'):
            continue
        # 文件名里含中文/空格时是**百分号编码**（`note/%E5%AE%97%E6%97%A8.html` = `note/宗旨.html`），
        # 浏览器会自动解码，所以判据也要解码后再比——否则把正确的链接全报成死链。
        target = (base / unquote(h)).resolve()
        try:
            rel = target.relative_to(WEB.resolve()).as_posix()
        except ValueError:
            continue
        if rel in all_pages:
            out.add(rel)
    return out


def main() -> int:
    ps = pages()
    names = {p.relative_to(WEB).as_posix() for p in ps}

    # ① 死链
    for p in ps:
        base = resolve_dir(p)
        for h in static_hrefs(p.read_text(encoding='utf-8')):
            if h.startswith('../'):
                continue
            target = (base / unquote(h)).resolve()
            if not target.exists() and target.suffix in ('.html', ''):
                PROBLEMS.append(f'{p.relative_to(WEB)} → 链接指向不存在的文件：{h}')

    # ② 可达性（BFS）
    graph = {name: set() for name in names}
    for p in ps:
        rel = p.relative_to(WEB).as_posix()
        graph[rel] = link_targets(p, names)
    dist = {'index.html': 0}
    q = deque(['index.html'])
    while q:
        cur = q.popleft()
        for nxt in graph.get(cur, ()):
            if nxt not in dist:
                dist[nxt] = dist[cur] + 1
                q.append(nxt)
    unreachable = sorted(n for n in names if n not in dist)
    deep = sorted((d, n) for n, d in dist.items() if d > MAX_HOPS)

    if unreachable:
        PROBLEMS.append(f'{len(unreachable)} 个页面从首页点不到：{unreachable[:6]}')
    if deep:
        PROBLEMS.append(f'{len(deep)} 个页面超过 {MAX_HOPS} 跳：{deep[:6]}')

    if PROBLEMS:
        print(f'站点可达性：**{len(PROBLEMS)} 处问题**')
        for x in PROBLEMS[:12]:
            print('  ✗ ' + x)
        return 1

    buckets: dict[int, int] = {}
    for d in dist.values():
        buckets[d] = buckets.get(d, 0) + 1
    print(f'站点可达性：全部可达（{len(names)} 个页面 · 从首页 '
          + ' · '.join(f'{d} 跳 {n} 个' for d, n in sorted(buckets.items()))
          + f' · 站内死链 0）')
    return 0


if __name__ == '__main__':
    sys.exit(main())

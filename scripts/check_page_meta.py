# -*- coding: utf-8 -*-
"""页面元信息的离线检查：每页都要有能被分享出去的"那一行字"，且缩略图真的存在。

为什么要有这个：分享出去的样子，90% 由 `<head>` 里那十几个标签决定，
而它们**在浏览器里完全看不见**——没人会顺手发现"这页忘了写描述"。
本仓库已经有过一次同类教训：条目页整页隐形，而所有检查全 PASS，因为
元素都在 DOM 里。元信息更是如此：它连 DOM 都不进（爬虫读的是原始 HTML）。

判据（每条都能失败）：
  ① 每个页面（含仓库根的重定向页）都有 social 块：description / canonical /
     robots / og:title / og:description / og:url / og:image / twitter:card
  ② description 与 og:description **逐页不同**（同一句复制到 20 页 = 等于没有描述）
  ③ description 长度合理（20–200 字），不是占位符
  ④ og:url 是本站绝对地址，且与该页文件名对得上
  ⑤ og:image 指向的**文件真的在仓库里**，且是 1200×630 的 PNG 或 JPEG（读文件头，不解码图片）
  ⑥ 没有放不生效的 robots.txt —— 它只在源站根生效，放项目子目录会被爬虫忽略；
     若将来绑了自有域名（根 = 本站），这条要改成"必须有 robots.txt"
"""
from __future__ import annotations

import re
import struct
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
WEB = ROOT / 'web'
BASE = 'https://craeatzeven.github.io/sukhomlinsky-education-kb'
NEED_META = ['name="description"', 'rel="canonical"', 'name="robots"',
             'property="og:title"', 'property="og:description"', 'property="og:url"',
             'property="og:image"', 'property="og:image:width"', 'property="og:image:height"',
             'name="twitter:card"', 'name="twitter:title"', 'name="twitter:description"']

PROBLEMS: list[str] = []


def fail(msg: str) -> None:
    PROBLEMS.append(msg)


def attr(head: str, key: str) -> str | None:
    m = re.search(rf'<meta {re.escape(key)} content="([^"]*)"', head)
    return m.group(1) if m else None


def image_size(path: Path) -> tuple[int, int] | None:
    """读图片头部拿尺寸，不解码整张图。

    2026-09-19 扩到 JPEG：这一条原来只认 PNG，而站点在第十二版把 og.png（930 KB）
    换成了 og.jpg（90 KB）—— 于是 28 个页面全部被判失败，而**没有任何一道别的闸门看得见它**
    （页面照常渲染，浏览器里毫无痕迹）。判据要跟得上被它约束的东西，否则它会一直报假故障，
    最后被人关掉 —— 那比没有判据更糟。"""
    d = path.read_bytes()
    if d[:8] == b'\x89PNG\r\n\x1a\n':
        return struct.unpack('>II', d[16:24])
    if d[:2] == b'\xff\xd8':                       # JPEG：扫到 SOFn 段
        i = 2
        while i < len(d) - 9:
            if d[i] != 0xFF:
                i += 1
                continue
            m = d[i + 1]
            if m in (0xD8, 0x01) or 0xD0 <= m <= 0xD7:
                i += 2
                continue
            seg = struct.unpack('>H', d[i + 2:i + 4])[0]
            if 0xC0 <= m <= 0xCF and m not in (0xC4, 0xC8, 0xCC):
                h, w = struct.unpack('>HH', d[i + 5:i + 9])
                return (w, h)
            i += 2 + seg
        return None
    return None


def main() -> int:
    pages = sorted(WEB.glob('*.html'))
    # 旁挂层页面（web/note/*.html，由 build_notes.py 生成）也纳入——
    # 它们是**真正会被分享出去**的分析页，元信息错了没人会发现（浏览器里看不见）。
    note_pages = sorted((WEB / 'note').glob('*.html'))
    root_page = ROOT / 'index.html'
    descs: dict[str, str] = {}
    images: set[str] = set()

    for p in pages + note_pages + [root_page]:
        head = p.read_text(encoding='utf-8').split('</head>')[0]
        label = 'index.html(根)' if p == root_page else (
            f'note/{p.name}' if p.parent.name == 'note' else p.name)
        for need in NEED_META:
            if need not in head:
                fail(f'{label} 缺 {need}')
        d = attr(head, 'name="description"')
        if not d:
            fail(f'{label} description 为空')
        else:
            if not 20 <= len(d) <= 200:
                fail(f'{label} description 长度 {len(d)}（应 20–200）')
            if d in descs:
                # 例外：仓库根那页是 0 秒跳转到 web/index.html 的**重定向桩**，
                # 它和首页是同一份内容，描述相同是对的（canonical 指向真正的页面）。
                if p != root_page:
                    fail(f'{label} 的 description 与 {descs[d]} 完全相同——复制粘贴等于没有描述')
            descs[d] = label
        og = attr(head, 'property="og:description"')
        if og != d:
            fail(f'{label} og:description 与 description 不一致')
        u = attr(head, 'property="og:url"')
        if not u or not u.startswith(BASE):
            fail(f'{label} og:url 不是本站绝对地址：{u}')
        else:
            # 网页在 web/ 下，旁挂层页面在 web/note/ 下——别把两处的路径假设混用。
            # 另外**要按解码后比**：note 页文件名含中文/空格，生成器写成百分号编码
            # （`A1%20%E5%85%A8…`）是合法 URL，与原始文件名是同一个地址；
            # 第一版按字面比，47 个 note 页各报 2 处，全属误报。
            rel_web = f'web/note/{p.name}' if p.parent.name == 'note' else f'web/{p.name}'
            if p == root_page:
                if u != f'{BASE}/':
                    fail(f'{label} og:url 应为站点根 {BASE}/，实际 {u}')
            elif not unquote(u).endswith('/' + rel_web):
                fail(f'{label} og:url 与文件名对不上：{u}（应 …/{rel_web}）')
        cm = re.search(r'<link rel="canonical" href="([^"]*)"', head)
        if not cm:
            fail(f'{label} canonical 为空')
        else:
            if p == root_page:
                want = f'{BASE}/web/index.html'
            elif p.parent.name == 'note':
                want = f'{BASE}/web/note/{p.name}'
            else:
                want = f'{BASE}/web/{p.name}'
            if unquote(cm.group(1)) != want:
                fail(f'{label} canonical 应为 {want}，实际 {cm.group(1)}')
        img = attr(head, 'property="og:image"')
        if img:
            images.add(img)
            rel = img.replace(f'{BASE}/', '')
            f = ROOT / rel
            if not f.exists():
                fail(f'{label} og:image 指向的文件不存在：{rel}')
            else:
                size = image_size(f)
                if size != (1200, 630):
                    fail(f'{label} og:image 不是 1200×630 的 PNG/JPEG（实测 {size}）：{rel}')

    if len(images) != 1:
        fail(f'og:image 不该有多个版本（当前 {len(images)} 个）：{sorted(images)}')

    # ⑥ robots.txt：放在项目子目录不生效，所以**故意不放**；放了反而误导。
    fake = WEB / 'robots.txt'
    if fake.exists():
        fail('web/robots.txt 存在但不会生效（robots.txt 只在源站根生效），应删掉或改绑自有域名后再放')

    if PROBLEMS:
        print(f'页面元信息：**{len(PROBLEMS)} 处问题**')
        for x in PROBLEMS[:20]:
            print('  ✗ ' + x)
        if len(PROBLEMS) > 20:
            print(f'  … 另有 {len(PROBLEMS) - 20} 处')
        return 1
    print(f'页面元信息：全部一致（{len(pages) + len(note_pages) + 1} 个页面 = '
          f'{len(pages)} 站点页 + {len(note_pages)} 旁挂层页 + 1 个根重定向桩 · '
          f'{len(descs)} 句互不相同的描述 · 缩略图 {sorted(images)[0].split("/")[-1]} 1200×630）')
    return 0


if __name__ == '__main__':
    sys.exit(main())

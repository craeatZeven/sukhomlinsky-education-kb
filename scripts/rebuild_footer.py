# -*- coding: utf-8 -*-
"""统一页脚链接行（`.foot-links`）——共用块只允许一处定义，手改必然各不相同。

为什么需要：`sitemap.html`（网站地图）此前只能从 note 页的页脚 3 跳到达，
而它是"想一眼看全"的入口，**应当从每一页 1 跳可达**（也方便爬虫）。
放进页脚链接行是自然位置：那一行本来就是"站级的次要入口"。

与 `rebuild_nav.py` 同一套路：一处模板 → 逐页替换 → 断言**恰好替换到一次**。
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WEB = ROOT / 'web'

LINKS = [
    ('reads.html', '读本'),
    ('sitemap.html', '网站地图'),
    ('cases.html', '案例 Review'),
    ('coverage.html', '覆盖报告'),
    ('guide.html', '使用指南'),
    ('latest.html', '最近更新'),
]
LINE = ('    <p class="foot-links">'
        + ' · '.join(f'<a href="{h}">{t}</a>' for h, t in LINKS)
        + '</p>')

FOOT_RE = re.compile(r'[ \t]*<p class="foot-links">.*?</p>', re.S)


def main() -> int:
    n = 0
    for path in sorted(WEB.glob('*.html')):
        text = path.read_text(encoding='utf-8')
        found = FOOT_RE.findall(text)
        if len(found) != 1:
            print(f'  !! {path.name}: 期望恰好 1 段 .foot-links，实际 {len(found)} 段，跳过')
            continue
        new = FOOT_RE.sub(lambda _m: LINE, text, count=1)
        if new != text:
            path.write_text(new, encoding='utf-8', newline='\n')
            n += 1
    print(f'页脚链接行已统一：{n} 个文件改动（{len(LINKS)} 个链接：'
          + ' / '.join(t for _h, t in LINKS) + '）')
    return 0


if __name__ == '__main__':
    sys.exit(main())

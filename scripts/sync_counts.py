# -*- coding: utf-8 -*-
"""把网页文案里的**卡片数字**同步成真实值（根治「站点说 1386、数据是 1675」）。

为什么要有它
------------
2026-09-27 站点评审发现：`search.html` 说「在 1386 张卡片里检索」、`sitemap.html` 说
「还有 1386 张卡片详情页」、`taxonomy.html` 说「1386 张卡分两类」、`index.html` 的 meta
description 也是 1386 —— 而线上数据是 **1675**。这些数字是 202 张新卡晋升前手写在文案里的，
晋升时没人回头改。**凡手写的计数都会过期**，所以改成构建期同步。

判据（故意只管**文案里的卡片数**，不做通用文本替换）
  - `<N> 张卡片` / `<N> 张卡`（N 是 3 位以上数字）→ 用真实卡片数
  - 只动 `web/*.html`；JS 里的 fallback 默认值（`SDATA ? … : 1386`）单独处理成数字本身
运行
    D:\python\python.exe scripts/sync_counts.py [--check]
    --check：只报差异、不写（给闸门用）
"""
import argparse, io, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WEB = os.path.join(ROOT, 'web')
IDS = os.path.join(WEB, 'data', 'ids.json')
# 只管**文案**；kb.js 的注释、离线 shim 由各自的构建处理
TARGETS = ['index.html', 'search.html', 'sitemap.html', 'taxonomy.html', 'explore.html',
           'entries.html', 'latest.html', 'coverage.html', 'sources.html', 'topics.html',
           'stories.html', 'cases.html', 'guide.html', 'reads.html', 'problem.html']
PAT_CARDS = re.compile(r'\b(\d{3,})\s*张卡片')
PAT_CARDS2 = re.compile(r'\b(\d{3,})\s*张卡(?!片)')


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--check', action='store_true')
    args = ap.parse_args()
    if not os.path.exists(IDS):
        print('没有 web/data/ids.json —— 先跑构建。跳过。')
        return 0
    n = len(json.load(io.open(IDS, encoding='utf-8')))
    changed, diffs = 0, []
    for name in TARGETS:
        p = os.path.join(WEB, name)
        if not os.path.exists(p):
            continue
        t = io.open(p, encoding='utf-8').read()
        orig = t
        for pat, unit in ((PAT_CARDS, '张卡片'), (PAT_CARDS2, '张卡')):
            def rep(m):
                return ('%d %s' % (n, unit)) if m.group(1) != str(n) else m.group(0)
            t = pat.sub(rep, t)
        if t != orig:
            olds = sorted(set(re.findall(r'\b(\d{3,})\s*张卡(?:片)?', orig)))
            diffs.append('%s：%s → %d' % (name, '/'.join(olds), n))
            if not args.check:
                io.open(p, 'w', encoding='utf-8', newline='\n').write(t)
                changed += 1
    print('真实卡片数：%d' % n)
    if diffs:
        print(('待同步' if args.check else '已同步') + ' %d 个文件：' % len(diffs))
        for d in diffs:
            print('   ' + d)
        return 1 if args.check else 0
    print('文案计数已一致，无需改动。')
    return 0


if __name__ == '__main__':
    sys.exit(main())

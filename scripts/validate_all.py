# -*- coding: utf-8 -*-
"""Run the full local validation chain.

Usage:
    python scripts/validate_all.py

Runs check_kb.py, audit_cards.py, coverage_report.py and build_site.py in
order. Exits non-zero on the first failure.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# **先全部构建、再全部检查**——顺序错了会拿旧产物做判断。
# 实测踩过：`check_page_meta.py` 原本排在 `build_notes.py` 前面，于是它检查的是
# **上一次生成的** reads.html，报"og:description 与 description 不一致"——
# 而生成器里那两行早就改成一致了。**判据对着旧产物下结论**是最难看出来的一类假报。
SCRIPTS = [
    # ── 构建（生成 web/data、页面、导航）
    'coverage_report.py',
    'coverage_volumes.py',
    'build_site.py',
    'build_shards.py',
    'rebuild_nav.py',
    # 页脚链接行也统一（与导航同理：共用块只允许一处定义，手改必然各不相同）。
    # 网站地图在这里拿到"每页 1 跳可达"——导航减到 7 项之后它是"想一眼看全"的唯一入口。
    'rebuild_footer.py',
    'build_notes.py',
    # ── 检查
    'check_kb.py',
    'audit_cards.py',
    # 必须排在两个 build 之后：它拿 classification.json 对账 web/data/ 的分片。
    # 这是唯一能拦住「分片悄悄和分类脱节」的一步（`collect` 曾经把判读分面
    # 重算成没过门槛的关键词分面，别的检查全都没报错）。
    'check_classification_shards.py',
    # 纯数据层的内容契约（原文身份 / 显式待补 / 入门卡角色 / 案例挂靠）。
    # 对应的**渲染层**检查在 tools/web-audit/verify-hardened.mjs，那一份要 Chrome
    # 加静态服务，进不了这条离线链，所以这里至少把数据层那几条盯住。
    'check_content_contract.py',
    # 页面元信息（分享预览 / 检索摘要）。它们**在浏览器里完全看不见**，
    # 没人会顺手发现"这页忘了写描述"——必须有机器守着。
    # **要排在 build_notes 之后**（它生成的那批 note 页与 reads.html 也在检查范围内）。
    'check_page_meta.py',
    # vault 层（wiki/）：双链有没有落点 + 索引有没有同步。
    # 这一层是 AI 全权写的，最容易出的错是**静默**的：死链在 Obsidian 里只显示成红字，
    # 忘了更新 index.md 更是没人会发现。
    'check_wiki_links.py',
    # 站点可达性：从首页 ≤3 跳要到得了每一页；站内链接不许指向不存在的文件。
    # 用户选 B（导航 15 → 7 个目的地）时，被移出导航的页面只剩"从枢纽页点进去"这一条路——
    # **减导航等于制造孤岛**，除非有这张网守着。
    'check_site_links.py',
    # 轴镜像对账：卡片的 primary/seealso/facets/tax_tags ↔ classification.json。
    # 把轴写进卡片是"融合"，但融合的代价是**可能变成两份真相**——
    # 这个仓库已经在中心表 vs 分片、INDEX.md vs MOC 上打过两次架，所以镜像必须有闸门。
    'check_axes_mirror.py',
    # 定位层一致性：卡上那行「扫描件第 N 页」必须与定位数据对得上；[[sk-XXXX]] 必须有落点。
    # 2026-09-21 修定位层时踩到的两类**静默**错误：数据改了卡上的字没改；卡上凭空写页。
    # 定位数据在 gitignored 的工作层，缺文件时这步自动跳过（不让新克隆因缺本地数据失败）。
    'check_locators.py',
    # 引文回卡核对：分析页里每条 `「」` 引文必须能在被引卡片的**该节**里逐字找到。
    # 这条机制最早是一次性脚本，抓到过 2 处真错（把转述当原文引、静默纠正 OCR 错字）——
    # 一次性脚本躺在 gitignored 目录里，下次写分析就没有它了，所以搬进仓库常驻。
    'check_quote_fidelity.py',
]

# ── 渲染层（浏览器里才看得到的那一层）
# 与上面不同：它要起本地静态服务、开浏览器跑 axe，**慢**（数十秒到两分钟），
# 而且依赖 D:\Git\tools\web-standard 的工具链（缺了会自动跳过并说明）。
# 2026-09-22 加它的理由：这一层抓到的都是**肉眼与静帧都看不出来**的错——
# 首跑就抓到 entry.html 两个 nav 之一没有可访问名、以及 .start-role 对比度 3.29:1
# （12px 小字要求 ≥4.5:1）。**带参页面必须带真参数**跑，否则测的是错误态。
# 想省时间用 `--no-rendering` 跳过。
RENDERING = ['check_rendering.py']


def main() -> int:
    args = sys.argv[1:]
    names = list(SCRIPTS)
    if '--no-rendering' not in args:
        names += RENDERING
    else:
        print('（--no-rendering：跳过渲染层闸门）')
    for name in names:
        path = ROOT / 'scripts' / name
        print(f'\n=== {name} ===')
        result = subprocess.run([sys.executable, str(path)], cwd=str(ROOT))
        if result.returncode != 0:
            print(f'FAILED: {name}')
            return result.returncode
    print('\nALL OK')
    return 0


if __name__ == '__main__':
    sys.exit(main())

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
SCRIPTS = [
    'check_kb.py',
    'audit_cards.py',
    'coverage_report.py',
    'coverage_volumes.py',
    'build_site.py',
    'build_shards.py',
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
    'check_page_meta.py',
    # vault 层（wiki/）：双链有没有落点 + 索引有没有同步。
    # 这一层是 AI 全权写的，最容易出的错是**静默**的：死链在 Obsidian 里只显示成红字，
    # 忘了更新 index.md 更是没人会发现。
    'check_wiki_links.py',
    # 成篇材料（专题长文 / 概念页 / 入口页 / 归档问答）→ 网站页面 + 检索语料。
    # 这一步的存在理由：用户问「找劳动，它给我的只是一堆零散的卡片」——
    # 检索里只有卡片，于是库里已有的成篇材料一个字都露不出来。
    'build_notes.py',
]


def main() -> int:
    for name in SCRIPTS:
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

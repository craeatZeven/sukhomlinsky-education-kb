# -*- coding: utf-8 -*-
"""vault 层（wiki/）的离线检查：**双链有没有落点** + **索引有没有同步**。

为什么要有这个：wiki/ 是 AI 全权拥有的一层，最容易出的错不是"写错字"，
而是两种**静默**问题：
  ① 死链——`[[A11 劳动与创造]]` 写出来了，但那个文件不存在（或名字差一个字）。
     Obsidian 只会把它显示成红字，不报错；等你哪天翻到才发现关系断了。
  ② 索引不同步——新加了一页但忘了更新 `wiki/index.md`。
     `_schema.md` 第 4 节明写了"新增或修改后同步"，但没有机器守着就一定会漂。

判据（每条都能失败）：
  ① wiki/ 下每个 `[[X]]` 都要有落点：X.md 存在，**或**某张卡的 aliases 里有 X
  ② 每个 wiki 页面都要在 index.md 里被点名（queries/moc/concepts/comparisons 四类都要）
  ③ wiki/index.md 与 _schema.md 存在（层的地基）
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / 'wiki'
CARDS = ROOT / 'cards'
PROBLEMS: list[str] = []

LINK_RE = re.compile(r'\[\[([^\]|]+?)(?:\|[^\]]*)?\]\]')
FENCE_RE = re.compile(r'^```.*?^```', re.S | re.M)          # 围栏代码块
CODE_RE = re.compile(r'`[^`\n]*`')                          # 行内代码


def strip_code(text: str) -> str:
    """去掉代码块与行内代码后再找链接。

    **为什么必须这样**：`_schema.md` 要"举例子说明链接怎么写"，
    于是里面有 `[[sk-XXXX]]`、`[[<slug>]]` 这类**示例**。
    在 Obsidian 里，反引号里的内容**不是链接**；第一版判据没区分，
    于是把 9 个示例全报成死链 —— 判据比页面错得更多。
    """
    return CODE_RE.sub(' ', FENCE_RE.sub(' ', text))


def main() -> int:
    if not WIKI.exists():
        print('wiki/ 不存在，跳过')
        return 0
    for need in ('_schema.md', 'index.md'):
        if not (WIKI / need).exists():
            PROBLEMS.append(f'wiki/{need} 不存在（这是这一层的地基）')

    # 可解析目标：wiki 下的文件名（去扩展名）+ 卡片的 aliases + 卡片文件名
    wiki_names = {p.stem for p in WIKI.rglob('*.md')}
    # 还要认 **vault 里的其它笔记**（topics/ sources/ 根级 .md）——
    # 它们同样是 Obsidian 能解析的目标。早先只认 wiki/ 与卡片，于是把
    # `[[劳动教育]]`（指向 topics/labor-education.md）报成了死链，属**判据自己的**误报。
    # Obsidian 按「文件名 / aliases / 标题层级」解析，**不按 frontmatter 的 title**，
    # 所以 topics 的标题必须也写进 aliases（见 2026-09-16 那次修复）才解析得到。
    for other in list((ROOT / 'topics').glob('*.md')) + list((ROOT / 'sources').glob('*.md')) \
            + [q for q in ROOT.glob('*.md')]:
        wiki_names.add(other.stem)
        tt = other.read_text(encoding='utf-8')
        am = re.search(r'^aliases:\s*$\n((?:\s+-\s+.*\n)+)', tt, re.M)
        if am:
            for line in am.group(1).splitlines():
                v = line.strip().lstrip('-').strip().strip('"').strip("'")
                if v:
                    wiki_names.add(v)
    card_alias: set[str] = set()
    for p in CARDS.glob('sk-*.md'):
        t = p.read_text(encoding='utf-8')
        m = re.match(r'^---\n(.*?)\n---', t, re.S)
        if not m:
            continue
        al = re.search(r'^aliases:\s*$\n((?:\s+-\s+.*\n)+)', m.group(1), re.M)
        if al:
            for line in al.group(1).splitlines():
                v = line.strip().lstrip('-').strip().strip('"').strip("'")
                if v:
                    card_alias.add(v)
        card_alias.add(p.stem)

    known = wiki_names | card_alias
    total = 0
    dead: list[str] = []
    for p in sorted(WIKI.rglob('*.md')):
        for m in LINK_RE.finditer(strip_code(p.read_text(encoding='utf-8'))):
            total += 1
            target = m.group(1).strip()
            if target not in known:
                dead.append(f'{p.relative_to(ROOT).as_posix()} → [[{target}]]')

    # ② 索引同步：每个页面都要在 index.md 里出现
    idx = (WIKI / 'index.md').read_text(encoding='utf-8') if (WIKI / 'index.md').exists() else ''
    missing = [p.stem for p in sorted(WIKI.rglob('*.md'))
               if p.name not in ('index.md', '_schema.md', '_log.md') and p.stem not in idx]

    # 分类统计
    kinds = {}
    for p in WIKI.rglob('*.md'):
        if p.name in ('index.md', '_schema.md', '_log.md'):
            continue
        kinds[p.parent.name] = kinds.get(p.parent.name, 0) + 1

    if dead:
        PROBLEMS.append(f'{len(dead)} 个双链没有落点（Obsidian 里会显示成红字）：{dead[:6]}')
    if missing:
        PROBLEMS.append(f'{len(missing)} 个页面没写进 index.md：{missing[:6]}')

    if PROBLEMS:
        print(f'vault 层：**{len(PROBLEMS)} 处问题**')
        for x in PROBLEMS:
            print('  ✗ ' + x)
        return 1
    print(f'vault 层：全部一致（{total} 个双链全部有落点 · '
          f'{sum(kinds.values())} 个页面全部在 index.md 里 · '
          f'分布 {kinds}）')
    return 0


if __name__ == '__main__':
    sys.exit(main())

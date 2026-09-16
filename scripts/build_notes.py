# -*- coding: utf-8 -*-
"""把「成篇材料」做成一等公民：topic 长文 + wiki 旁挂层 → 网站页面 + 检索语料。

**为什么**（用户原话）：「我在这个数据库里面找劳动，它能给我的只是一堆零散的卡片」。
实测：检索语料里**只有卡片**，所以《劳动教育》专题长文（1859 字）、条目页 A11、
分面页 S12、归档问答 **一个都不会出现在搜索结果里** —— 库里明明有"一篇讲清楚"的东西。
（另有实测：搜「劳动」命中 514 张卡。）

产出三样：
  ① `web/note/<slug>.html` —— wiki 层每一页的网站版本（12 篇专题已有 `topic.html`，不重复生成）
  ② `web/data/docs.json`    —— 成篇材料的检索语料（含它引用了哪些卡，供卡片页反向指回）
  ③ 供 search.html / card.html 使用

设计取舍：
  · **构建期渲染**，不在前端做 Markdown（站点本来就没有 MD 渲染器；构建期出错能立刻发现）
  · 渲染器只支持 wiki 页面**实际用到**的构造：标题/段落/引用/列表/表格/加粗/行内码/链接/双链。
    未知构造降级为段落，并由判据兜底：**成品里不许残留 `[[` 或 `**`**（残留即渲染失败）。
  · `[[sk-XXXX]]` → 链到卡片页；`[[别的页]]` → 链到对应 note/topic 页；解析不到就**保留文字但不加链接**
    （宁可少一个链接，也不要造一个死链）。
"""
from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WEB = ROOT / 'web'
NOTE = WEB / 'note'
DATA = WEB / 'data'

SITE = 'https://craeatzeven.github.io/sukhomlinsky-education-kb'


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def strip_fm(t: str) -> tuple[dict, str]:
    if not t.startswith('---'):
        return {}, t
    m = re.match(r'^---\n(.*?)\n---\n?', t, re.S)
    if not m:
        return {}, t
    fm: dict = {}
    for line in m.group(1).splitlines():
        mm = re.match(r'^([a-z_]+):\s*(.*)$', line)
        if mm:
            fm[mm.group(1)] = mm.group(2).strip().strip('"')
    return fm, t[m.end():]


# ── 极简 Markdown 渲染（只覆盖这些页面用到的构造）
def inline(s: str, resolve) -> str:
    s = esc(s)
    s = re.sub(r'\[\[([^\]|]+?)(?:\|([^\]]+))?\]\]',
               lambda m: resolve(m.group(1).strip(), m.group(2) or m.group(1).strip()), s)
    s = re.sub(r'\[([^\]]+)\]\((https?:[^)]+)\)',
               lambda m: f'<a href="{m.group(2)}" target="_blank" rel="noopener">{m.group(1)}</a>', s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    return s


def strip_md(s: str) -> str:
    """把 Markdown 记号洗掉——用于 <meta description>。
    踩过的坑：描述原本直接取正文首行，于是 MOC 页那句 `> 所属角度：[[宗旨]] · 主归属 32 张`
    把 `[[ ]]` 原样带进了 meta 标签（44 个页面）。
    """
    s = re.sub(r'\[\[([^\]|]+?)\|([^\]]+)\]\]', r'\2', s)
    s = re.sub(r'\[\[([^\]]+)\]\]', r'\1', s)
    s = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', s)
    s = re.sub(r'[#>*`|]', ' ', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip()


def reflow(lines: list[str]) -> list[str]:
    """把段落内的**软换行**并成一行（标准 Markdown 语义）。

    为什么必须做：渲染器是逐行的，于是**跨行的加粗**（`**…\\n…**`）找不到配对，
    成品里会残留 `**`。实测概念页就被抓到 2 处。
    只合并"普通段落行"——标题/列表/引用/表格行不合并。
    """
    BLOCK = re.compile(r'^\s*(#{1,4}\s|[-*]\s|\d+\.\s|>|\|)')
    out: list[str] = []
    for ln in lines:
        s = ln.strip()
        if not s:
            out.append('')
            continue
        if out and out[-1].strip() and not BLOCK.match(s) and not BLOCK.match(out[-1]):
            out[-1] = out[-1].rstrip() + ' ' + s
        else:
            out.append(ln)
    return out


def render(md: str, resolve) -> str:
    out: list[str] = []
    lines = reflow(md.splitlines())
    i = 0
    while i < len(lines):
        ln = lines[i]
        s = ln.strip()
        if not s:
            i += 1
            continue
        if s.startswith('|') and i + 1 < len(lines) and re.match(r'^\|[\s:|-]+\|$', lines[i + 1].strip()):
            head = [c.strip() for c in s.strip('|').split('|')]
            rows = []
            i += 2
            while i < len(lines) and lines[i].strip().startswith('|'):
                rows.append([c.strip() for c in lines[i].strip().strip('|').split('|')])
                i += 1
            out.append('<table class="note-table"><thead><tr>' +
                       ''.join(f'<th>{inline(c, resolve)}</th>' for c in head) + '</tr></thead><tbody>' +
                       ''.join('<tr>' + ''.join(f'<td>{inline(c, resolve)}</td>' for c in r) + '</tr>' for r in rows) +
                       '</tbody></table>')
            continue
        if s.startswith('>'):
            buf = []
            while i < len(lines) and lines[i].strip().startswith('>'):
                buf.append(lines[i].strip().lstrip('>').strip())
                i += 1
            out.append('<blockquote>' + ''.join(f'<p>{inline(x, resolve)}</p>' for x in buf if x) + '</blockquote>')
            continue
        if re.match(r'^[-*]\s+', s):
            buf = []
            while i < len(lines) and re.match(r'^\s*[-*]\s+', lines[i]):
                buf.append(re.sub(r'^\s*[-*]\s+', '', lines[i]))
                i += 1
            out.append('<ul>' + ''.join(f'<li>{inline(x, resolve)}</li>' for x in buf) + '</ul>')
            continue
        h = re.match(r'^(#{1,4})\s+(.*)$', s)
        if h:
            lvl = len(h.group(1))
            out.append(f'<h{lvl + 1}>{inline(h.group(2), resolve)}</h{lvl + 1}>')
            i += 1
            continue
        out.append(f'<p>{inline(s, resolve)}</p>')
        i += 1
    return '\n'.join(out)


CHROME = '''<!doctype html>
<html lang="zh-CN"><head><meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title} · 苏霍姆林斯基教育知识库</title>
<meta name="description" content="{desc}" />
<meta name="robots" content="index,follow" />
<link rel="canonical" href="{site}/web/note/{slug}.html" />
<meta property="og:type" content="article" />
<meta property="og:title" content="{title} · 苏霍姆林斯基教育知识库" />
<meta property="og:description" content="{desc}" />
<meta property="og:url" content="{site}/web/note/{slug}.html" />
<meta property="og:image" content="{site}/web/og.png" />
<meta name="twitter:card" content="summary_large_image" />
<link rel="stylesheet" href="../style.css?v={ver}" />
</head><body class="reveal">
<header class="topnav"><div class="wrap topnav-in">
<a class="brand" href="index.html">苏霍姆林斯基教育知识库</a>
<nav class="nav-groups"><a class="nav-link" href="search.html">全库检索</a>
<a class="nav-link" href="taxonomy.html">分类总图</a>
<a class="nav-link" href="topics.html">专题长文</a></nav></div></header>
<main class="wrap layer-reading">
<article class="note-body">
<p class="meta">{kindlabel}</p>
{body}
</article>
<hr />
<p class="section-sub">这一页是<b>旁挂层</b>（编者的综合与分析），不是卡片原文。
回到 <a href="search.html">检索</a> · <a href="entries.html">分类条目</a> ·
<a href="topics.html">专题长文</a>；卡片一律以 <code>sk-XXXX</code> 链接可回查。</p>
</main>
<script src="kb.js?v={ver}"></script>
<script src="theme.js?v={ver}"></script>
</body></html>
'''

KIND_LABEL = {'concept': '概念页（分析）', 'moc': '入口页（索引）',
              'moc-entry': '条目入口页', 'moc-facet': '分面入口页',
              'moc-facet-exception': '入口页（例外登记）', 'moc-angle': '角度入口页',
              'query': '归档问答', 'topic': '专题长文'}


def main() -> int:
    ver = '20260916c'
    NOTE.mkdir(parents=True, exist_ok=True)
    card_ids = {p.stem.split('-')[0] + '-' + p.stem.split('-')[1] for p in (ROOT / 'cards').glob('sk-*.md')}

    # 先收集所有"成篇材料"，才能让 [[跨页链接]] 互相解析
    docs: list[dict] = []
    for group, pats in [('topic', [ROOT / 'topics' / '*.md']),
                        ('wiki', [ROOT / 'wiki' / 'moc' / '*.md',
                                  ROOT / 'wiki' / 'concepts' / '*.md',
                                  ROOT / 'wiki' / 'queries' / '*.md',
                                  ROOT / 'wiki' / 'comparisons' / '*.md'])]:
        for pat in pats:
            for p in sorted(pat.parent.glob(pat.name)):
                if p.name.startswith('_'):
                    continue
                fm, body = strip_fm(p.read_text(encoding='utf-8'))
                docs.append({'kind': group, 'type': fm.get('type', group), 'slug': p.stem,
                             'title': fm.get('title', p.stem), 'path': p, 'body': body})

    by_title: dict[str, dict] = {}
    for d in docs:
        by_title[d['title']] = d
        by_title.setdefault(d['slug'], d)

    def make_resolver(page: dict):
        def resolve(target: str, text: str) -> str:
            if re.fullmatch(r'sk-\d{4}', target):
                if target in card_ids:
                    return f'<a class="wikilink" href="card.html?id={target}">{esc(text)}</a>'
                return esc(text)
            tgt = by_title.get(target)
            if tgt:
                kind = tgt['kind']
                href = (f'topic.html?slug={tgt["slug"]}' if kind == 'topic'
                        else f'note/{quote(tgt["slug"])}.html')
                return f'<a href="{href}">{esc(text)}</a>'
            return esc(text)
        return resolve

    from urllib.parse import quote

    made = []
    for d in docs:
        if d['kind'] == 'topic':
            continue                      # topic.html 已经渲染，不重复生成
        body_html = render(d['body'], make_resolver(d))
        first = next((x for x in strip_md(d['body']).split('.') if len(x.strip()) > 12), '')
        desc = (first.strip() + '。')[:110] if first.strip() else d['title']
        out = CHROME.format(title=esc(d['title']), desc=esc(desc), site=SITE, ver=ver,
                            slug=quote(d['slug']), kindlabel=KIND_LABEL.get(d['type'], '旁挂层'),
                            body=body_html)
        (NOTE / f'{d["slug"]}.html').write_text(out, encoding='utf-8', newline='\n')
        made.append(d)

    # docs.json：检索语料 + 卡片反向索引
    corpus = []
    for d in docs:
        text = re.sub(r'\s+', ' ', re.sub(r'[#>*`|\[\]]', ' ', d['body']))
        refs = sorted(set(re.findall(r'sk-\d{4}', d['body'])))
        corpus.append({'kind': d['kind'], 'type': d['type'], 'slug': d['slug'],
                       'title': d['title'], 'text': text[:2000], 'refs': refs,
                       'link': (f'topic.html?slug={d["slug"]}' if d['kind'] == 'topic'
                                else f'note/{quote(d["slug"])}.html')})
    (DATA / 'docs.json').write_text(json.dumps(corpus, ensure_ascii=False, separators=(',', ':')),
                                    encoding='utf-8', newline='\n')

    print(f'note 页面 {len(made)} 个；docs.json {len(corpus)} 条成篇材料 '
          f'（专题 {sum(1 for c in corpus if c["kind"] == "topic")} · '
          f'旁挂层 {sum(1 for c in corpus if c["kind"] == "wiki")}）')
    print(f'  体积：{(DATA / "docs.json").stat().st_size / 1024:.0f} KB')
    return 0


if __name__ == '__main__':
    sys.exit(main())

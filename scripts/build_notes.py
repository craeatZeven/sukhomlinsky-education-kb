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
<!-- 旁挂层页面在 web/note/ 下，而站内链接一律按 **web/ 为根**来写
     （card.html / note/xxx.html / data/…）。用 <base> 统一基准，比给每个链接手加 ../ 可靠：
     实测第一版没加，50 个 note 页的**每一个**站内链接都指向 web/note/xxx 而 404——
     被 scripts/check_site_links.py 的可达性判据抓到（页面还在，但点不动）。 -->
<base href="../" />
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
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{title} · 苏霍姆林斯基教育知识库" />
<meta name="twitter:description" content="{desc}" />
<link rel="stylesheet" href="style.css?v={ver}" />
</head><body class="reveal">
{nav}
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

# 「读本」枢纽页：成篇材料的**唯一静态入口**。
# 它必须在导航里有一席，否则这些页面只能靠检索结果/卡片页的 JS 反查进入——
# 静态可达性判据（也是爬虫）看不见那种入口。{nav} 从 index.html 抓，保持单一来源。
HUB = '''<!doctype html>
<html lang="zh-CN"><head><meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>读本 · 苏霍姆林斯基教育知识库</title>
<meta name="description" content="已经写好的一篇篇文章：12 篇编者长文、跨卡片的分析页、两条主张的对比页与归档问答，每句判断后面都挂着卡号、可回查出处。" />
<meta name="robots" content="index,follow" />
<link rel="canonical" href="{site}/web/reads.html" />
<meta property="og:type" content="website" />
<meta property="og:title" content="读本 · 苏霍姆林斯基教育知识库" />
<meta property="og:description" content="已经写好的一篇篇文章：12 篇编者长文、跨卡片的分析页、两条主张的对比页与归档问答，每句判断后面都挂着卡号、可回查出处。" />
<meta property="og:url" content="{site}/web/reads.html" />
<meta property="og:image" content="{site}/web/og.png" />
<meta property="og:image:width" content="1200" />
<meta property="og:image:height" content="630" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="读本 · 苏霍姆林斯基教育知识库" />
<meta name="twitter:description" content="已经写好的一篇篇文章：12 篇编者长文、跨卡片的分析页、两条主张的对比页与归档问答，每句判断后面都挂着卡号、可回查出处。" />
<link rel="stylesheet" href="style.css?v={ver}" />
</head><body class="reveal">
{nav}
<main class="wrap layer-archive">
  <header class="page-head">
    <p class="meta">READ</p>
    <h1>读本</h1>
    <p class="hero-note">这个库不只是卡片。这里有 {n_topic} 篇编者长文、{n_analysis} 篇跨卡片的分析与对比、
    {n_query} 份归档问答——<b>每一句判断后面都挂着卡号</b>，点得开、可回查。</p>
    <p class="section-sub">换一种切法：想按<b>分类</b>找材料去 <a href="taxonomy.html">分类总图</a>；
    想按<b>词</b>找去 <a href="search.html">全库检索</a>（它会先给成篇材料，再给卡片）；
    想按<b>问题/困境/故事</b>读，见下面「换一种读法」。</p>
  </header>

  <section>
    <h2 class="section-title">编者长文（{n_topic} 篇）</h2>
    <p class="section-sub">一个教育专题一篇：核心判断 + 可操作方法 + 跨书综合。</p>
    <div class="read-list">
{topics}
    </div>
  </section>

  <section>
    <h2 class="section-title">分析与对比（{n_analysis} 篇）</h2>
    <p class="section-sub">跨卡片把散着的主张合成论断：指出张力、前提与边界。
    <b>编者推论</b>与<b>能反驳它的条件</b>都写在页内。</p>
    <div class="read-list">
{concepts}
{comparisons}
    </div>
  </section>

  <section>
    <h2 class="section-title">归档问答（{n_query} 份）</h2>
    <p class="section-sub">问过的好问题与查法，留在库里而不是消失在聊天里。</p>
    <div class="read-list">
{queries}
    </div>
  </section>

  <section>
    <h2 class="section-title">换一种读法</h2>
    <p class="section-sub">同样一批材料，按你手上的问题选入口。</p>
    <div class="read-list">
      <a class="read-row" href="problem.html"><span class="read-title">按问题读</span>
        <span class="read-snip">16 个常见问题（孩子说谎 / 坐不住 / 后进生…），附想法与案例…</span></a>
      <a class="read-row" href="cases.html"><span class="read-title">按困境读</span>
        <span class="read-snip">16 个教育困境反查知识库，给出可执行建议与对应原文…</span></a>
      <a class="read-row" href="stories.html"><span class="read-title">按故事读</span>
        <span class="read-snip">《做人的故事》541 篇，按原书页码顺序通读…</span></a>
    </div>
  </section>
</main>
<footer class="site-footer"><div class="wrap">
  <p class="section-sub">读本里的每一页都是<b>旁挂层</b>（编者的综合与分析），不是卡片原文。
  引用时请按页内标注区分「原文」与「编者推论」。</p>
</div></footer>
<script src="kb.js?v={ver}"></script>
<script src="theme.js?v={ver}"></script>
</body></html>
'''


def main() -> int:
    ver = '20260916c'
    NOTE.mkdir(parents=True, exist_ok=True)

    def read_nav() -> str:
        """从 `web/index.html` 抓现成的导航块——**单一来源**。

        导航由 `rebuild_nav.py` 统一写进每个页面；枢纽页是新生成的，
        与其在这里再写死一份（下次改导航必然漏掉它），不如从 index.html 读。
        抓不到就返回空（页面仍可用，只是没有顶栏）。
        """
        try:
            t = (WEB / 'index.html').read_text(encoding='utf-8')
            m = re.search(r'<nav class="topnav">.*?</nav>', t, re.S)
            return m.group(0) if m else ''
        except Exception:
            return ''
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

    # **决定哪些"成篇材料"要生成独立的网站页面**。
    # 只给"分析层"（概念页 / 对比页 / 归档问答）生成——它们是 vault 独有的内容。
    # moc（5 角度 + 23 条目 + 17 分面）**不生成**：网站已经有 entries.html / entry.html /
    # facets.html / facet.html 在做同一件事，生成 note 版就是**同一内容两套页面**
    # （第一版生成了 46 个，被 check_site_links 的"从首页点不到"顺带暴露出来）。
    # 但它们仍要进 docs.json（检索语料），只是链接指向**已有页面**。
    NO_PAGE_TYPES = {'moc', 'moc-entry', 'moc-facet', 'moc-angle', 'moc-facet-exception'}

    meta = json.loads((ROOT / 'web/data/meta.json').read_text(encoding='utf-8'))
    for e in meta['entries']:
        kind = 'tag' if e.get('tag') else 'entry'
        docs.append({'kind': 'entry', 'type': kind, 'slug': e['code'], 'title': f'{e["code"]} {e["name"]}',
                     'path': None, 'body': f'{e.get("rule", "")}',
                     'link': f'entry.html?code={e["code"]}'})
    for f in meta['facets']:
        docs.append({'kind': 'facet', 'type': 'facet', 'slug': f['code'],
                     'title': f'{f["code"]} {f["name"]}', 'path': None,
                     'body': f'{f.get("field", "")} · {f.get("count", 0)} 张故事',
                     'link': f'facet.html?code={f["code"]}'})

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
                # 条目/分面没有 note 页 → 指向**已有页面**（entry.html / facet.html）。
                # 其余（topic / concept / comparison / query）指向各自页面。
                if tgt.get('link'):
                    href = tgt['link']
                elif tgt['kind'] == 'topic':
                    href = f'topic.html?slug={tgt["slug"]}'
                else:
                    href = f'note/{quote(tgt["slug"])}.html'
                return f'<a href="{href}">{esc(text)}</a>'
            return esc(text)
        return resolve

    from urllib.parse import quote

    made = []
    for d in docs:
        if d['path'] is None:
            continue
        if d['kind'] == 'topic':
            continue                      # topic.html 已经渲染，不重复生成
        if d['type'] in NO_PAGE_TYPES:
            continue                      # 见上：moc 不生成独立页面
        body_html = render(d['body'], make_resolver(d))
        first = next((x for x in strip_md(d['body']).split('.') if len(x.strip()) > 12), '')
        desc = (first.strip() + '。')[:110] if first.strip() else d['title']
        out = CHROME.format(title=esc(d['title']), desc=esc(desc), site=SITE, ver=ver,
                            nav=read_nav(),
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
                       'link': d.get('link') or (
                           f'topic.html?slug={d["slug"]}' if d['kind'] == 'topic'
                           else f'note/{quote(d["slug"])}.html')})
    (DATA / 'docs.json').write_text(json.dumps(corpus, ensure_ascii=False, separators=(',', ':')),
                                    encoding='utf-8', newline='\n')

    # ── 「读本」枢纽页：成篇材料唯一的静态入口 ──────────────────────────
    # 为什么必须有它：check_site_links.py 报「50 个 note 页从首页点不到」——
    # note 页此前**只能靠检索结果或卡片页的 JS 反查**进入，**没有静态入口**
    # （搜索与反查都是运行时生成的链接，静态可达性判据看不见，爬虫也看不见）。
    def rows(items: list[dict]) -> str:
        out = []
        for d in items:
            href = d.get('link') or (f'topic.html?slug={d["slug"]}' if d['kind'] == 'topic'
                                     else f'note/{quote(d["slug"])}.html')
            first = next((x for x in strip_md(d['body']).split('.') if len(x.strip()) > 12), '')
            snip = re.sub(r'\s+', ' ', first).strip()[:78]
            out.append(f'<a class="read-row" href="{esc(href)}">'
                       f'<span class="read-title">{esc(d["title"])}</span>'
                       f'<span class="read-snip">{esc(snip)}…</span></a>')
        return '\n'.join(out) or '<p class="section-sub">（暂无）</p>'

    kinds = {
        'topic': [d for d in docs if d['kind'] == 'topic'],
        'concept': [d for d in docs if d['type'] == 'concept'],
        'comparison': [d for d in docs if d['type'] == 'comparison'],
        'query': [d for d in docs if d['type'] == 'query'],
    }
    hub = HUB.format(
        ver=ver, site=SITE, nav=read_nav(),
        n_topic=len(kinds['topic']), n_analysis=len(kinds['concept']) + len(kinds['comparison']),
        n_query=len(kinds['query']),
        topics=rows(kinds['topic']), concepts=rows(kinds['concept']),
        comparisons=rows(kinds['comparison']), queries=rows(kinds['query']))
    (WEB / 'reads.html').write_text(hub, encoding='utf-8', newline='\n')

    print(f'note 页面 {len(made)} 个 + 读本枢纽 reads.html；docs.json {len(corpus)} 条成篇材料 '
          f'（专题 {len(kinds["topic"])} · 分析 {len(kinds["concept"]) + len(kinds["comparison"])} · '
          f'问答 {len(kinds["query"])} · 条目 {sum(1 for c in corpus if c["kind"] == "entry")} · '
          f'分面 {sum(1 for c in corpus if c["kind"] == "facet")}）')
    print(f'  体积：{(DATA / "docs.json").stat().st_size / 1024:.0f} KB')
    return 0


if __name__ == '__main__':
    sys.exit(main())


# -*- coding: utf-8 -*-
"""把 cards/*.md 导出成 Cloudflare D1 可直接导入的 SQL。

用法：
    python scripts/build_d1_sql.py            # 生成 cloudflare/schema.sql + cloudflare/data.sql
    python scripts/build_d1_sql.py --fts      # 额外生成 cloudflare/schema_fts.sql（FTS5 trigram，可选）

产物：
    cloudflare/schema.sql        表 + 索引（必导）
    cloudflare/schema_fts.sql    FTS5 虚拟表 + 数据回填（可选；D1 若不支持 FTS5 就跳过这个文件）
    cloudflare/data.sql          INSERT 语句（必导）
    cloudflare/coverage.json     web/coverage.json 的副本（供 Worker 内嵌返回 /api/coverage）

无第三方依赖。
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

import build_site  # noqa: E402

CARDS_DIR = ROOT / 'cards'
OUT_DIR = ROOT / 'cloudflare'


def esc(v: str) -> str:
    return "'" + str(v or '').replace("'", "''") + "'"


def parse_cards() -> list[dict]:
    """复用 build_site 的解析逻辑，补上 created/updated。"""
    cards = []
    for p in sorted(CARDS_DIR.glob('*.md')):
        if p.name.startswith('_'):
            continue
        text = build_site.read_text(p)
        fm = build_site.frontmatter(text)
        if not fm.get('id'):
            continue
        excerpt_section = build_site.section(text, '原文/Excerpt')
        excerpts: list[str] = []
        current: list[str] = []
        for line in excerpt_section.splitlines():
            if not line.startswith('>'):
                continue
            content = line.lstrip('>').strip()
            if content == '':
                if current:
                    excerpts.append(' '.join(current))
                    current = []
            else:
                current.append(content)
        if current:
            excerpts.append(' '.join(current))
        excerpt = ' '.join(excerpts)
        cn = build_site.first_para(build_site.section(text, '中文转述/说明'))
        topics = [x.strip() for x in (fm.get('topics') or '').split(',') if x.strip()]
        tags: list[str] = []
        if '[OCR待校]' in text or '[extraction待校]' in text:
            tags.append('OCR待校')
        if any(k in text for k in ('待纸本核', '纸本复核', '待纸本', '待原书')):
            tags.append('待纸本核')
        if len(topics) > 1:
            tags.append('跨主题')
        cards.append({
            'id': fm['id'], 'type': fm.get('type', ''), 'title': fm.get('title', ''),
            'source': fm.get('source', ''), 'ref': fm.get('ref', ''),
            'excerpt': excerpt, 'excerpts': excerpts, 'cn': cn,
            'topics': topics, 'tags': tags,
            'created': fm.get('created', ''), 'updated': fm.get('updated', ''),
            'file': p.name,
        })
    return cards


SCHEMA = """-- 苏霍姆林斯基教育知识库 · Cloudflare D1 schema
-- 生成脚本：scripts/build_d1_sql.py
DROP TABLE IF EXISTS card_topics;
DROP TABLE IF EXISTS cards;
DROP TABLE IF EXISTS cards_fts;

CREATE TABLE cards (
  id TEXT PRIMARY KEY,
  type TEXT,
  title TEXT,
  source TEXT,
  ref TEXT,
  excerpt TEXT,
  excerpts_json TEXT,
  cn TEXT,
  topics_json TEXT,
  tags_json TEXT,
  created TEXT,
  updated TEXT,
  file TEXT
);
CREATE TABLE card_topics (
  card_id TEXT NOT NULL,
  topic TEXT NOT NULL
);
CREATE INDEX idx_cards_source ON cards(source);
CREATE INDEX idx_cards_type ON cards(type);
CREATE INDEX idx_card_topics_topic ON card_topics(topic);
CREATE INDEX idx_card_topics_card ON card_topics(card_id);
"""

SCHEMA_FTS = """-- 可选：FTS5 trigram 全文索引（D1 若不支持 FTS5，跳过本文件即可，Worker 会自动回退 LIKE）
CREATE VIRTUAL TABLE IF NOT EXISTS cards_fts USING fts5(
  id UNINDEXED, title, cn, excerpt, ref, topics,
  tokenize='trigram'
);
"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--fts', action='store_true', help='额外生成 schema_fts.sql')
    args = ap.parse_args()

    cards = parse_cards()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    (OUT_DIR / 'schema.sql').write_text(SCHEMA, encoding='utf-8')

    lines: list[str] = ['-- 数据导入：python scripts/build_d1_sql.py 生成；用 wrangler d1 execute --file 导入']
    fts_rows: list[str] = []
    CARD_COLS = ('id,type,title,source,ref,excerpt,excerpts_json,cn,topics_json,tags_json,created,updated,file')
    # D1 对单条 SQL 语句有上限（实测 60 KB 会报 SQLITE_TOOBIG），因此按字符数动态分批（目标 ≤ 25 KB/条）
    MAX_SQL = 25000
    card_batch: list[str] = []
    card_len = 0
    topic_batch: list[str] = []
    topic_len = 0
    fts_batch: list[str] = []
    fts_len = 0

    def flush_cards() -> None:
        nonlocal card_len
        if card_batch:
            lines.append(f'INSERT INTO cards ({CARD_COLS}) VALUES ' + ','.join(card_batch) + ';')
            card_batch.clear()
            card_len = 0

    def flush_topics() -> None:
        nonlocal topic_len
        if topic_batch:
            lines.append('INSERT INTO card_topics (card_id,topic) VALUES ' + ','.join(topic_batch) + ';')
            topic_batch.clear()
            topic_len = 0

    def flush_fts() -> None:
        nonlocal fts_len
        if fts_batch:
            fts_rows.append('INSERT INTO cards_fts (id,title,cn,excerpt,ref,topics) VALUES '
                            + ','.join(fts_batch) + ';')
            fts_batch.clear()
            fts_len = 0

    for c in cards:
        row = '(' + ','.join([
            esc(c['id']), esc(c['type']), esc(c['title']), esc(c['source']), esc(c['ref']),
            esc(c['excerpt']), esc(json.dumps(c['excerpts'], ensure_ascii=False)),
            esc(c['cn']), esc(json.dumps(c['topics'], ensure_ascii=False)),
            esc(json.dumps(c['tags'], ensure_ascii=False)), esc(c['created']), esc(c['updated']), esc(c['file']),
        ]) + ')'
        card_batch.append(row)
        card_len += len(row) + 1
        if card_len >= MAX_SQL:
            flush_cards()

        for t in c['topics']:
            trow = f'({esc(c["id"])},{esc(t)})'
            topic_batch.append(trow)
            topic_len += len(trow) + 1
        if topic_len >= MAX_SQL:
            flush_topics()

        frow = '(' + ','.join([esc(c['id']), esc(c['title']), esc(c['cn']), esc(c['excerpt']),
                               esc(c['ref']), esc(' '.join(c['topics']))]) + ')'
        fts_batch.append(frow)
        fts_len += len(frow) + 1
        if fts_len >= MAX_SQL:
            flush_fts()

    flush_cards()
    flush_topics()
    flush_fts()

    (OUT_DIR / 'data.sql').write_text('\n'.join(lines) + '\n', encoding='utf-8')

    if args.fts:
        (OUT_DIR / 'schema_fts.sql').write_text(SCHEMA_FTS + '\n'.join(fts_rows) + '\n', encoding='utf-8')

    cov = ROOT / 'web' / 'coverage.json'
    if cov.exists():
        (OUT_DIR / 'coverage.json').write_text(cov.read_text(encoding='utf-8'), encoding='utf-8')

    print(f'cards={len(cards)}  schema.sql / data.sql'
          + (' / schema_fts.sql' if args.fts else '')
          + f'  -> {OUT_DIR}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

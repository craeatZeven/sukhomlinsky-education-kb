# -*- coding: utf-8 -*-
"""Build a read-only SQLite database (with FTS5 full-text index) from cards/.

Usage:
    python scripts/build_db.py [--out api/kb.db] [--check]

Schema
------
cards(id TEXT PRIMARY KEY, type, title, source, ref, excerpt, excerpts_json,
      cn, topics_json, tags_json, created, updated, file)
card_topics(card_id, topic)          -- 便于按主题聚合
cards_fts                            -- FTS5 虚拟表（trigram 分词，中文可用），
                                        列：id/title/cn/excerpt/ref/topics

FTS5 的 trigram 分词器要求 SQLite >= 3.34（本机 3.39 已满足），
对中文按 3 字符滑窗切分，配合 `MATCH` 即可做子串检索。

无第三方依赖。
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

import build_site  # noqa: E402  (同目录脚本，复用卡片解析逻辑)

CARDS_DIR = ROOT / 'cards'
DEFAULT_OUT = ROOT / 'api' / 'kb.db'


def parse_frontmatter_extra(text: str) -> dict:
    """取 created / updated / status 等 build_site.frontmatter 已覆盖的字段即可。"""
    return build_site.frontmatter(text)


def build(out_path: Path) -> dict:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if out_path.exists():
        out_path.unlink()
    conn = sqlite3.connect(str(out_path))
    cur = conn.cursor()
    cur.executescript(
        """
        PRAGMA journal_mode = WAL;
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
        CREATE VIRTUAL TABLE cards_fts USING fts5(
            id UNINDEXED, title, cn, excerpt, ref, topics,
            tokenize='trigram'
        );
        """
    )

    n = 0
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

        cur.execute(
            'INSERT INTO cards VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)',
            (
                fm['id'], fm.get('type', ''), fm.get('title', ''), fm.get('source', ''),
                fm.get('ref', ''), excerpt, json.dumps(excerpts, ensure_ascii=False),
                cn, json.dumps(topics, ensure_ascii=False), json.dumps(tags, ensure_ascii=False),
                fm.get('created', ''), fm.get('updated', ''), p.name,
            ),
        )
        for t in topics:
            cur.execute('INSERT INTO card_topics VALUES (?,?)', (fm['id'], t))
        cur.execute(
            'INSERT INTO cards_fts (id, title, cn, excerpt, ref, topics) VALUES (?,?,?,?,?,?)',
            (fm['id'], fm.get('title', ''), cn, excerpt, fm.get('ref', ''), ' '.join(topics)),
        )
        n += 1

    conn.commit()
    # 简单统计
    stats = {
        'cards': n,
        'sources': cur.execute('SELECT COUNT(DISTINCT source) FROM cards').fetchone()[0],
        'topics': cur.execute('SELECT COUNT(DISTINCT topic) FROM card_topics').fetchone()[0],
        'fts_rows': cur.execute('SELECT COUNT(*) FROM cards_fts').fetchone()[0],
    }
    conn.close()
    return stats


def check(db_path: Path) -> int:
    conn = sqlite3.connect(str(db_path))
    cur = conn.cursor()
    problems = []
    cards = cur.execute('SELECT COUNT(*) FROM cards').fetchone()[0]
    fts = cur.execute('SELECT COUNT(*) FROM cards_fts').fetchone()[0]
    if cards != fts:
        problems.append(f'cards={cards} != fts={fts}')
    probe = cur.execute("SELECT COUNT(*) FROM cards_fts WHERE cards_fts MATCH '苏霍姆林斯基'").fetchone()[0]
    if probe == 0:
        problems.append("MATCH '苏霍姆林斯基' 返回 0 行")
    probe2 = cur.execute("SELECT COUNT(*) FROM cards_fts WHERE cards_fts MATCH '劳动'").fetchone()[0]
    print(f'cards={cards} fts={fts} match(苏霍姆林斯基)={probe} match(劳动)={probe2}')
    conn.close()
    if problems:
        print('CHECK FAILED:', problems)
        return 1
    print('CHECK OK')
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default=str(DEFAULT_OUT))
    ap.add_argument('--check', action='store_true')
    args = ap.parse_args()
    out = Path(args.out)
    if args.check:
        return check(out)
    stats = build(out)
    print('wrote', out, stats)
    return check(out)


if __name__ == '__main__':
    raise SystemExit(main())

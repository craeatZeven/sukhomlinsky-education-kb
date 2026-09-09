# -*- coding: utf-8 -*-
"""苏霍姆林斯基教育知识库 —— 只读 API 服务（FastAPI + SQLite FTS5）。

启动：
    python scripts/build_db.py                 # 先建库 api/kb.db
    uvicorn api.main:app --host 127.0.0.1 --port 8000
    浏览器打开 http://127.0.0.1:8000/          # 同一进程也托管 web/ 静态站

接口：
    GET /api/health
    GET /api/meta                                    # 计数 + 来源/主题/类型
    GET /api/search?q=&source=&topic=&type=&page=1&size=20
    GET /api/cards/{id}
    GET /api/cards?ids=sk-0001,sk-0002               # 批量
    GET /api/random
    GET /api/related/{id}?limit=8
    GET /api/sources   /api/sources/{slug}
    GET /api/topics    /api/topics/{slug}
    GET /api/coverage                                # 转发 web/coverage.json

检索说明：FTS5 使用 trigram 分词（中文按 3 字滑窗），因此 **查询词 ≥3 字** 走 FTS（bm25 排序），
**1–2 字**（如「劳动」「教育」）自动回退到 LIKE 子串扫描（1386 行，毫秒级）。
"""
from __future__ import annotations

import json
import os
import random
import sqlite3
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = Path(os.environ.get('KB_DB', ROOT / 'api' / 'kb.db'))
WEB_DIR = ROOT / 'web'

app = FastAPI(
    title='苏霍姆林斯基教育知识库 API',
    description='只读检索接口；数据源为仓库 cards/*.md，构建脚本 scripts/build_db.py。',
    version='0.1.0',
)

_origins = [o.strip() for o in os.environ.get('KB_CORS_ORIGINS', '*').split(',') if o.strip()]
app.add_middleware(
    CORSMiddleware,
    allow_origins=_origins or ['*'],
    allow_methods=['GET'],
    allow_headers=['*'],
)


def db() -> sqlite3.Connection:
    conn = sqlite3.connect(f'file:{DB_PATH}?mode=ro', uri=True)
    conn.row_factory = sqlite3.Row
    return conn


def row_to_card(row: sqlite3.Row, full: bool = True) -> dict[str, Any]:
    card = {
        'id': row['id'],
        'type': row['type'],
        'title': row['title'],
        'source': row['source'],
        'ref': row['ref'],
        'topics': json.loads(row['topics_json'] or '[]'),
        'tags': json.loads(row['tags_json'] or '[]'),
        'cn': row['cn'] or '',
    }
    if full:
        card['excerpt'] = row['excerpt'] or ''
        card['excerpts'] = json.loads(row['excerpts_json'] or '[]')
    return card


def facets(conn: sqlite3.Connection) -> dict[str, Any]:
    sources = [dict(r) for r in conn.execute(
        'SELECT source AS slug, COUNT(*) AS cards FROM cards GROUP BY source ORDER BY cards DESC')]
    types = [dict(r) for r in conn.execute(
        'SELECT type, COUNT(*) AS cards FROM cards GROUP BY type ORDER BY cards DESC')]
    topics = [dict(r) for r in conn.execute(
        'SELECT topic AS slug, COUNT(*) AS cards FROM card_topics GROUP BY topic ORDER BY cards DESC')]
    return {'sources': sources, 'types': types, 'topics': topics}


@app.get('/api/health')
def health() -> dict[str, Any]:
    if not DB_PATH.exists():
        raise HTTPException(503, f'数据库不存在：{DB_PATH}，请先运行 python scripts/build_db.py')
    conn = db()
    n = conn.execute('SELECT COUNT(*) FROM cards').fetchone()[0]
    conn.close()
    return {'status': 'ok', 'cards': n, 'db': str(DB_PATH)}


@app.get('/api/meta')
def meta() -> dict[str, Any]:
    conn = db()
    total = conn.execute('SELECT COUNT(*) FROM cards').fetchone()[0]
    data = {'total_cards': total, **facets(conn)}
    conn.close()
    return data


def _snippet(card: dict, terms: list[str], width: int = 60) -> str:
    """从 cn / excerpt 中截取包含查询词的片段。"""
    for field in ('cn', 'excerpt'):
        text = card.get(field) or ''
        for t in terms:
            i = text.find(t)
            if i >= 0:
                a = max(0, i - width // 2)
                b = min(len(text), i + len(t) + width // 2)
                return ('…' if a > 0 else '') + text[a:b] + ('…' if b < len(text) else '')
    return (card.get('cn') or card.get('excerpt') or '')[:width * 2]


def _like_search(conn: sqlite3.Connection, terms: list[str], where: str, params: list[Any],
                 page: int, size: int) -> tuple[list[dict], int]:
    sql_where = where
    p = list(params)
    for t in terms:
        sql_where += ' AND (title LIKE ? OR cn LIKE ? OR excerpt LIKE ? OR ref LIKE ?)'
        like = f'%{t}%'
        p += [like, like, like, like]
    total = conn.execute(f'SELECT COUNT(*) FROM cards {sql_where}', p).fetchone()[0]
    rows = conn.execute(
        f'SELECT * FROM cards {sql_where} ORDER BY id LIMIT ? OFFSET ?',
        p + [size, (page - 1) * size]).fetchall()
    return [row_to_card(r) for r in rows], total


def _fts_search(conn: sqlite3.Connection, terms: list[str], where: str, params: list[Any],
                page: int, size: int) -> tuple[list[dict], int]:
    match = ' AND '.join('"' + t.replace('"', '""') + '"' for t in terms)
    base = 'FROM cards_fts f JOIN cards c ON c.id = f.id WHERE cards_fts MATCH ?'
    sql_where = base + (where.replace('WHERE', 'AND') if where else '')
    p = [match] + list(params)
    total = conn.execute(f'SELECT COUNT(*) {sql_where}', p).fetchone()[0]
    rows = conn.execute(
        f'SELECT c.* {sql_where} ORDER BY bm25(cards_fts) LIMIT ? OFFSET ?',
        p + [size, (page - 1) * size]).fetchall()
    return [row_to_card(r) for r in rows], total


def run_search(conn: sqlite3.Connection, q: str, where: str, params: list[Any],
               page: int, size: int) -> tuple[list[dict], int, str]:
    """混合检索：≥3 字的词走 FTS5 trigram，1–2 字的词走 LIKE；多词为 AND 关系。"""
    terms = [t for t in q.split() if t]
    if not terms:
        return [], 0, 'empty'
    long_terms = [t for t in terms if len(t) >= 3]
    short_terms = [t for t in terms if len(t) < 3]

    def attach(items: list[dict]) -> list[dict]:
        for it in items:
            it['snippet'] = _snippet(it, terms)
        return items

    if long_terms and not short_terms:
        items, total = _fts_search(conn, long_terms, where, params, page, size)
        if total:
            return attach(items), total, 'fts-trigram'
        items, total = _like_search(conn, terms, where, params, page, size)
        return attach(items), total, 'like-fallback'
    if long_terms and short_terms:
        # 长词先用 FTS 缩小集合，再在结果内用 LIKE 过滤短词
        match = ' AND '.join('"' + t.replace('"', '""') + '"' for t in long_terms)
        base = 'FROM cards_fts f JOIN cards c ON c.id = f.id WHERE cards_fts MATCH ?'
        sql_where = base + (where.replace('WHERE', 'AND') if where else '')
        p = [match] + list(params)
        for t in short_terms:
            sql_where += ' AND (c.title LIKE ? OR c.cn LIKE ? OR c.excerpt LIKE ? OR c.ref LIKE ?)'
            like = f'%{t}%'
            p += [like, like, like, like]
        total = conn.execute(f'SELECT COUNT(*) {sql_where}', p).fetchone()[0]
        if total:
            rows = conn.execute(
                f'SELECT c.* {sql_where} ORDER BY bm25(cards_fts) LIMIT ? OFFSET ?',
                p + [size, (page - 1) * size]).fetchall()
            return attach([row_to_card(r) for r in rows]), total, 'fts+like'
        items, total = _like_search(conn, terms, where, params, page, size)
        return attach(items), total, 'like-fallback'
    items, total = _like_search(conn, short_terms, where, params, page, size)
    return attach(items), total, 'like-short-query'


@app.get('/api/search')
def search(
    q: str = Query('', description='关键词；≥3 字走 FTS5，1–2 字自动回退 LIKE'),
    source: str = '',
    topic: str = '',
    type: str = '',
    page: int = Query(1, ge=1),
    size: int = Query(20, ge=1, le=100),
) -> dict[str, Any]:
    conn = db()
    where = 'WHERE 1=1'
    params: list[Any] = []
    if source:
        where += ' AND source = ?'
        params.append(source)
    if type:
        where += ' AND type = ?'
        params.append(type)
    if topic:
        where += ' AND id IN (SELECT card_id FROM card_topics WHERE topic = ?)'
        params.append(topic)

    q = q.strip()
    if not q:
        total = conn.execute(f'SELECT COUNT(*) FROM cards {where}', params).fetchone()[0]
        rows = conn.execute(
            f'SELECT * FROM cards {where} ORDER BY id LIMIT ? OFFSET ?',
            params + [size, (page - 1) * size]).fetchall()
        items = [row_to_card(r) for r in rows]
        mode = 'filter'
    else:
        items, total, mode = run_search(conn, q, where, params, page, size)
    conn.close()
    return {
        'query': q, 'mode': mode, 'page': page, 'size': size,
        'total': total, 'pages': (total + size - 1) // size,
        'items': items,
    }


@app.get('/api/cards/{card_id}')
def get_card(card_id: str) -> dict[str, Any]:
    conn = db()
    row = conn.execute('SELECT * FROM cards WHERE id = ?', (card_id,)).fetchone()
    conn.close()
    if row is None:
        raise HTTPException(404, f'未找到卡片 {card_id}')
    return row_to_card(row)


@app.get('/api/cards')
def get_cards(ids: str = Query('', description='逗号分隔的卡片 id')) -> dict[str, Any]:
    wanted = [x.strip() for x in ids.split(',') if x.strip()]
    if not wanted:
        return {'items': []}
    conn = db()
    marks = ','.join('?' * len(wanted))
    rows = conn.execute(f'SELECT * FROM cards WHERE id IN ({marks})', wanted).fetchall()
    conn.close()
    by_id = {r['id']: row_to_card(r) for r in rows}
    return {'items': [by_id[i] for i in wanted if i in by_id]}


@app.get('/api/random')
def random_card() -> dict[str, Any]:
    conn = db()
    row = conn.execute('SELECT * FROM cards ORDER BY RANDOM() LIMIT 1').fetchone()
    conn.close()
    if row is None:
        raise HTTPException(404, '知识库为空')
    return row_to_card(row)


@app.get('/api/related/{card_id}')
def related(card_id: str, limit: int = Query(8, ge=1, le=50)) -> dict[str, Any]:
    conn = db()
    row = conn.execute('SELECT * FROM cards WHERE id = ?', (card_id,)).fetchone()
    if row is None:
        conn.close()
        raise HTTPException(404, f'未找到卡片 {card_id}')
    topics = json.loads(row['topics_json'] or '[]')
    out: list[dict] = []
    seen = {card_id}
    if topics:
        marks = ','.join('?' * len(topics))
        rows = conn.execute(
            f"""SELECT c.*, COUNT(*) AS overlap FROM cards c
                JOIN card_topics t ON t.card_id = c.id
                WHERE t.topic IN ({marks}) AND c.id != ?
                GROUP BY c.id ORDER BY overlap DESC, c.id LIMIT ?""",
            topics + [card_id, limit]).fetchall()
        for r in rows:
            if r['id'] not in seen:
                seen.add(r['id'])
                out.append(row_to_card(r))
    if len(out) < limit:
        rows = conn.execute(
            'SELECT * FROM cards WHERE source = ? AND id != ? ORDER BY id LIMIT ?',
            (row['source'], card_id, limit * 2)).fetchall()
        for r in rows:
            if r['id'] not in seen and len(out) < limit:
                seen.add(r['id'])
                out.append(row_to_card(r))
    conn.close()
    return {'id': card_id, 'topics': topics, 'items': out}


@app.get('/api/sources')
def list_sources() -> dict[str, Any]:
    conn = db()
    rows = conn.execute(
        'SELECT source AS slug, COUNT(*) AS cards FROM cards GROUP BY source ORDER BY cards DESC').fetchall()
    conn.close()
    return {'items': [dict(r) for r in rows]}


@app.get('/api/sources/{slug}')
def source_cards(slug: str, page: int = Query(1, ge=1), size: int = Query(50, ge=1, le=200)) -> dict[str, Any]:
    conn = db()
    total = conn.execute('SELECT COUNT(*) FROM cards WHERE source = ?', (slug,)).fetchone()[0]
    rows = conn.execute('SELECT * FROM cards WHERE source = ? ORDER BY id LIMIT ? OFFSET ?',
                        (slug, size, (page - 1) * size)).fetchall()
    conn.close()
    return {'slug': slug, 'total': total, 'page': page, 'size': size,
            'items': [row_to_card(r) for r in rows]}


@app.get('/api/topics')
def list_topics() -> dict[str, Any]:
    conn = db()
    rows = conn.execute(
        'SELECT topic AS slug, COUNT(*) AS cards FROM card_topics GROUP BY topic ORDER BY cards DESC').fetchall()
    conn.close()
    return {'items': [dict(r) for r in rows]}


@app.get('/api/topics/{slug}')
def topic_cards(slug: str, page: int = Query(1, ge=1), size: int = Query(50, ge=1, le=200)) -> dict[str, Any]:
    conn = db()
    total = conn.execute('SELECT COUNT(*) FROM card_topics WHERE topic = ?', (slug,)).fetchone()[0]
    rows = conn.execute(
        """SELECT c.* FROM cards c JOIN card_topics t ON t.card_id = c.id
           WHERE t.topic = ? ORDER BY c.id LIMIT ? OFFSET ?""",
        (slug, size, (page - 1) * size)).fetchall()
    conn.close()
    return {'slug': slug, 'total': total, 'page': page, 'size': size,
            'items': [row_to_card(r) for r in rows]}


@app.get('/api/coverage')
def coverage() -> JSONResponse:
    p = WEB_DIR / 'coverage.json'
    if not p.exists():
        raise HTTPException(404, 'web/coverage.json 不存在，请先运行 scripts/coverage_report.py')
    return JSONResponse(json.loads(p.read_text(encoding='utf-8')))


# 静态站（可选）：把 web/ 挂在根路径，一个进程同时提供前端与 API。
if WEB_DIR.exists():
    app.mount('/', StaticFiles(directory=str(WEB_DIR), html=True), name='web')

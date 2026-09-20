# -*- coding: utf-8 -*-
"""全文检索接口（C 方案）——只返回**命中片段**，不返回整段、不提供导出。

数据源：local_working_copy/fulltext/corpus.db（书全文的原子层，**不入 git**）。
这个库不存在时，本路由整体降级为 503，站点应回落到卡片检索。

## 为什么是这个形态（版权边界）
NOTICE.md：公开仓库只收短摘录，完整全文留在本地。所以这里：
  · 单条片段上限 SNIPPET_MAX 字（命中处左右各留一定上下文）；
  · 每次查询返回条数上限 LIMIT_MAX；
  · **没有**按书/按页导出全文的接口，也没有分页翻遍全书的路径
    （翻页上限 MAX_PAGE，且每页都只给片段）；
  · 想通读整本，只能去读纸本 —— 这是有意的。

## 接口
    GET /api/fulltext/health
    GET /api/fulltext/search?q=&limit=20&page=1&book=&min_len=
    GET /api/fulltext/context?unit=&q=      # 单条多用一点上下文（仍有限）
"""
from __future__ import annotations

import os
import re
import sqlite3
from pathlib import Path

from fastapi import APIRouter, HTTPException, Query

ROOT = Path(__file__).resolve().parent.parent
CORPUS_DB = Path(os.environ.get('KB_CORPUS_DB', ROOT / 'local_working_copy' / 'fulltext' / 'corpus.db'))

SNIPPET_MAX = 180      # 单条片段上限（字）
CONTEXT_MAX = 420      # context 接口的单条上限（字）
LIMIT_MAX = 50         # 每次查询最多返回多少条
MAX_PAGE = 5           # 最多翻到第几页（防止用翻页把全书捞完）

router = APIRouter(prefix='/api/fulltext', tags=['fulltext'])


def _db() -> sqlite3.Connection:
    if not CORPUS_DB.exists():
        raise HTTPException(503, '全文层不可用：corpus.db 不在本机（它不入 git）。')
    conn = sqlite3.connect(f'file:{CORPUS_DB}?mode=ro', uri=True)
    conn.row_factory = sqlite3.Row
    return conn


def _strip(t: str) -> str:
    return re.sub(r'\s+', '', t or '')


def _snippet(text: str, q: str, width: int) -> str:
    flat = _strip(text)
    if not q:
        return flat[:width]
    i = flat.find(q)
    if i < 0:
        return flat[:width]
    half = max(10, (width - len(q)) // 2)
    a = max(0, i - half)
    b = min(len(flat), i + len(q) + half)
    out = flat[a:b]
    if a > 0:
        out = '…' + out
    if b < len(flat):
        out = out + '…'
    return out


@router.get('/health')
def health() -> dict:
    if not CORPUS_DB.exists():
        return {'ok': False, 'reason': 'corpus.db 缺失', 'path': str(CORPUS_DB)}
    conn = _db()
    n, chars = conn.execute('SELECT COUNT(*), SUM(chars) FROM units').fetchone()
    books = [r[0] for r in conn.execute('SELECT DISTINCT slug FROM units ORDER BY slug')]
    conn.close()
    return {'ok': True, 'units': n, 'chars': chars, 'books': books,
            'snippet_max': SNIPPET_MAX, 'limit_max': LIMIT_MAX, 'max_page': MAX_PAGE}


@router.get('/search')
def search(q: str = Query(..., min_length=2, max_length=30),
           limit: int = Query(20, ge=1, le=LIMIT_MAX),
           page: int = Query(1, ge=1, le=MAX_PAGE),
           book: str | None = None,
           min_len: int = Query(0, ge=0, le=2000)) -> dict:
    conn = _db()
    offset = (page - 1) * limit
    sql = ['SELECT unit_id, slug, book, page AS p, section, text FROM units WHERE text LIKE ?']
    args: list = [f'%{q}%']
    if book:
        sql.append('AND slug = ?')
        args.append(book)
    if min_len:
        sql.append('AND chars >= ?')
        args.append(min_len)
    sql.append('ORDER BY slug, page LIMIT ? OFFSET ?')
    args += [limit, offset]
    rows = conn.execute(' '.join(sql), args).fetchall()
    n = conn.execute('SELECT COUNT(*) FROM units WHERE text LIKE ?', (f'%{q}%',)).fetchone()[0]
    conn.close()
    return {'q': q, 'total': n, 'page': page, 'limit': limit,
            'hits': [{'unit': r['unit_id'], 'book': r['book'], 'slug': r['slug'],
                      'page': r['p'], 'section': r['section'],
                      'snippet': _snippet(r['text'], q, SNIPPET_MAX)} for r in rows]}


@router.get('/context')
def context(unit: str = Query(..., min_length=4, max_length=80),
            q: str = Query('', max_length=30)) -> dict:
    conn = _db()
    r = conn.execute('SELECT unit_id, slug, book, page, section, text FROM units WHERE unit_id = ?',
                     (unit,)).fetchone()
    conn.close()
    if not r:
        raise HTTPException(404, f'没有这个单元：{unit}')
    return {'unit': r['unit_id'], 'book': r['book'], 'slug': r['slug'], 'page': r['page'],
            'section': r['section'], 'snippet': _snippet(r['text'], q, CONTEXT_MAX)}
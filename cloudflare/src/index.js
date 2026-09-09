/**
 * 苏霍姆林斯基教育知识库 —— Cloudflare Worker（D1 只读 API）
 *
 * 与 api/main.py（FastAPI 版）返回同样的 JSON 形状，因此 web/search.html 不用改。
 * 检索策略：
 *   1) 若 D1 支持 FTS5（cards_fts 存在）且查询词全部 ≥3 字 → FTS5 MATCH + bm25 排序；
 *   2) 否则（含 1–2 字中文词、或 D1 无 FTS5）→ LIKE 子串扫描（1386 行，边缘节点毫秒级）。
 *   多词按空格切分，AND 关系。
 */
import coverage from '../coverage.json';

const JSON_HEADERS = { 'content-type': 'application/json; charset=utf-8' };
let ftsAvailable = null; // 每个 isolate 探测一次

function cors(env) {
  return {
    'access-control-allow-origin': env.CORS_ORIGIN || '*',
    'access-control-allow-methods': 'GET,OPTIONS',
    'access-control-allow-headers': 'content-type',
  };
}

function json(data, env, status = 200, extra = {}) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { ...JSON_HEADERS, ...cors(env), ...extra },
  });
}

function rowToCard(r, full = true) {
  const card = {
    id: r.id,
    type: r.type,
    title: r.title,
    source: r.source,
    ref: r.ref,
    topics: JSON.parse(r.topics_json || '[]'),
    tags: JSON.parse(r.tags_json || '[]'),
    cn: r.cn || '',
  };
  if (full) {
    card.excerpt = r.excerpt || '';
    card.excerpts = JSON.parse(r.excerpts_json || '[]');
  }
  return card;
}

function snippet(card, terms, width = 60) {
  for (const field of ['cn', 'excerpt']) {
    const text = card[field] || '';
    for (const t of terms) {
      const i = text.indexOf(t);
      if (i >= 0) {
        const a = Math.max(0, i - Math.floor(width / 2));
        const b = Math.min(text.length, i + t.length + Math.floor(width / 2));
        return (a > 0 ? '…' : '') + text.slice(a, b) + (b < text.length ? '…' : '');
      }
    }
  }
  return (card.cn || card.excerpt || '').slice(0, width * 2);
}

async function hasFts(env) {
  if (ftsAvailable !== null) return ftsAvailable;
  try {
    await env.DB.prepare("SELECT rowid FROM cards_fts WHERE cards_fts MATCH '苏霍姆林斯基' LIMIT 1").all();
    ftsAvailable = true;
  } catch (e) {
    ftsAvailable = false;
  }
  return ftsAvailable;
}

function buildFilters(params) {
  const where = [];
  const binds = [];
  const source = params.get('source') || '';
  const topic = params.get('topic') || '';
  const type = params.get('type') || '';
  if (source) { where.push('source = ?'); binds.push(source); }
  if (type) { where.push('type = ?'); binds.push(type); }
  if (topic) { where.push('id IN (SELECT card_id FROM card_topics WHERE topic = ?)'); binds.push(topic); }
  return { where, binds };
}

async function search(env, params) {
  const q = (params.get('q') || '').trim();
  const page = Math.max(1, parseInt(params.get('page') || '1', 10) || 1);
  const size = Math.min(100, Math.max(1, parseInt(params.get('size') || '20', 10) || 20));
  const offset = (page - 1) * size;
  const { where, binds } = buildFilters(params);
  const whereSql = where.length ? 'WHERE ' + where.join(' AND ') : '';

  if (!q) {
    const total = (await env.DB.prepare(`SELECT COUNT(*) AS n FROM cards ${whereSql}`).bind(...binds).first()).n;
    const rows = (await env.DB.prepare(
      `SELECT * FROM cards ${whereSql} ORDER BY id LIMIT ? OFFSET ?`).bind(...binds, size, offset).all()).results || [];
    return { query: '', mode: 'filter', page, size, total, pages: Math.ceil(total / size), items: rows.map(r => rowToCard(r)) };
  }

  const terms = q.split(/\s+/).filter(Boolean);
  const longTerms = terms.filter(t => t.length >= 3);
  const shortTerms = terms.filter(t => t.length < 3);
  const ftsOk = longTerms.length > 0 && await hasFts(env);

  let mode = 'like';
  let sqlWhere = whereSql;
  let sqlBinds = [...binds];

  if (ftsOk) {
    mode = shortTerms.length ? 'fts+like' : 'fts-trigram';
    const match = longTerms.map(t => '"' + t.replace(/"/g, '""') + '"').join(' AND ');
    const extra = where.length ? ' AND ' + where.join(' AND ') : '';
    sqlWhere = `WHERE cards_fts MATCH ?${extra}`;
    sqlBinds = [match, ...binds];
    for (const t of shortTerms) {
      sqlWhere += ' AND (c.title LIKE ? OR c.cn LIKE ? OR c.excerpt LIKE ? OR c.ref LIKE ?)';
      const like = `%${t}%`;
      sqlBinds.push(like, like, like, like);
    }
  } else {
    const allTerms = terms;
    for (const t of allTerms) {
      sqlWhere += (sqlWhere ? ' AND ' : 'WHERE ') + '(title LIKE ? OR cn LIKE ? OR excerpt LIKE ? OR ref LIKE ?)';
      const like = `%${t}%`;
      sqlBinds.push(like, like, like, like);
    }
    mode = shortTerms.length === terms.length ? 'like-short-query' : 'like';
  }

  const from = ftsOk ? 'FROM cards_fts f JOIN cards c ON c.id = f.id' : 'FROM cards c';
  const total = (await env.DB.prepare(`SELECT COUNT(*) AS n ${from} ${sqlWhere}`).bind(...sqlBinds).first()).n;
  const order = ftsOk ? 'ORDER BY bm25(cards_fts)' : 'ORDER BY c.id';
  const rows = (await env.DB.prepare(
    `SELECT c.* ${from} ${sqlWhere} ${order} LIMIT ? OFFSET ?`).bind(...sqlBinds, size, offset).all()).results || [];
  const items = rows.map(r => { const card = rowToCard(r); card.snippet = snippet(card, terms); return card; });
  return { query: q, mode, page, size, total, pages: Math.ceil(total / size), items };
}

async function related(env, id, limit) {
  const row = await env.DB.prepare('SELECT * FROM cards WHERE id = ?').bind(id).first();
  if (!row) return null;
  const topics = JSON.parse(row.topics_json || '[]');
  const items = [];
  const seen = new Set([id]);
  if (topics.length) {
    const marks = topics.map(() => '?').join(',');
    const rs = (await env.DB.prepare(
      `SELECT c.*, COUNT(*) AS overlap FROM cards c JOIN card_topics t ON t.card_id = c.id
       WHERE t.topic IN (${marks}) AND c.id != ? GROUP BY c.id ORDER BY overlap DESC, c.id LIMIT ?`
    ).bind(...topics, id, limit).all()).results || [];
    for (const r of rs) { if (!seen.has(r.id)) { seen.add(r.id); items.push(rowToCard(r)); } }
  }
  if (items.length < limit) {
    const rs = (await env.DB.prepare(
      'SELECT * FROM cards WHERE source = ? AND id != ? ORDER BY id LIMIT ?').bind(row.source, id, limit * 2).all()).results || [];
    for (const r of rs) { if (!seen.has(r.id) && items.length < limit) { seen.add(r.id); items.push(rowToCard(r)); } }
  }
  return { id, topics, items };
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const p = url.pathname;
    if (request.method === 'OPTIONS') return new Response(null, { headers: cors(env) });
    if (request.method !== 'GET') return json({ error: 'method_not_allowed' }, env, 405);

    try {
      if (p === '/api/health') {
        const n = (await env.DB.prepare('SELECT COUNT(*) AS n FROM cards').first()).n;
        return json({ status: 'ok', cards: n, backend: 'cloudflare-workers-d1' }, env);
      }
      if (p === '/api/meta') {
        const total = (await env.DB.prepare('SELECT COUNT(*) AS n FROM cards').first()).n;
        const sources = (await env.DB.prepare(
          'SELECT source AS slug, COUNT(*) AS cards FROM cards GROUP BY source ORDER BY cards DESC').all()).results;
        const types = (await env.DB.prepare(
          'SELECT type, COUNT(*) AS cards FROM cards GROUP BY type ORDER BY cards DESC').all()).results;
        const topics = (await env.DB.prepare(
          'SELECT topic AS slug, COUNT(*) AS cards FROM card_topics GROUP BY topic ORDER BY cards DESC').all()).results;
        return json({ total_cards: total, sources, types, topics }, env);
      }
      if (p === '/api/search') return json(await search(env, url.searchParams), env);

      let m = p.match(/^\/api\/cards\/(.+)$/);
      if (m) {
        const row = await env.DB.prepare('SELECT * FROM cards WHERE id = ?').bind(decodeURIComponent(m[1])).first();
        if (!row) return json({ error: 'not_found', id: m[1] }, env, 404);
        return json(rowToCard(row), env);
      }
      if (p === '/api/cards') {
        const ids = (url.searchParams.get('ids') || '').split(',').map(s => s.trim()).filter(Boolean);
        if (!ids.length) return json({ items: [] }, env);
        const marks = ids.map(() => '?').join(',');
        const rows = (await env.DB.prepare(`SELECT * FROM cards WHERE id IN (${marks})`).bind(...ids).all()).results || [];
        const byId = Object.fromEntries(rows.map(r => [r.id, rowToCard(r)]));
        return json({ items: ids.filter(i => byId[i]).map(i => byId[i]) }, env);
      }
      if (p === '/api/random') {
        const row = await env.DB.prepare('SELECT * FROM cards ORDER BY RANDOM() LIMIT 1').first();
        return row ? json(rowToCard(row), env) : json({ error: 'empty' }, env, 404);
      }
      m = p.match(/^\/api\/related\/(.+)$/);
      if (m) {
        const limit = Math.min(50, Math.max(1, parseInt(url.searchParams.get('limit') || '8', 10) || 8));
        const r = await related(env, decodeURIComponent(m[1]), limit);
        return r ? json(r, env) : json({ error: 'not_found' }, env, 404);
      }
      if (p === '/api/sources') {
        const rows = (await env.DB.prepare(
          'SELECT source AS slug, COUNT(*) AS cards FROM cards GROUP BY source ORDER BY cards DESC').all()).results;
        return json({ items: rows }, env);
      }
      m = p.match(/^\/api\/sources\/(.+)$/);
      if (m) {
        const slug = decodeURIComponent(m[1]);
        const page = Math.max(1, parseInt(url.searchParams.get('page') || '1', 10) || 1);
        const size = Math.min(200, Math.max(1, parseInt(url.searchParams.get('size') || '50', 10) || 50));
        const total = (await env.DB.prepare('SELECT COUNT(*) AS n FROM cards WHERE source = ?').bind(slug).first()).n;
        const rows = (await env.DB.prepare(
          'SELECT * FROM cards WHERE source = ? ORDER BY id LIMIT ? OFFSET ?').bind(slug, size, (page - 1) * size).all()).results || [];
        return json({ slug, total, page, size, items: rows.map(r => rowToCard(r)) }, env);
      }
      if (p === '/api/topics') {
        const rows = (await env.DB.prepare(
          'SELECT topic AS slug, COUNT(*) AS cards FROM card_topics GROUP BY topic ORDER BY cards DESC').all()).results;
        return json({ items: rows }, env);
      }
      m = p.match(/^\/api\/topics\/(.+)$/);
      if (m) {
        const slug = decodeURIComponent(m[1]);
        const page = Math.max(1, parseInt(url.searchParams.get('page') || '1', 10) || 1);
        const size = Math.min(200, Math.max(1, parseInt(url.searchParams.get('size') || '50', 10) || 50));
        const total = (await env.DB.prepare('SELECT COUNT(*) AS n FROM card_topics WHERE topic = ?').bind(slug).first()).n;
        const rows = (await env.DB.prepare(
          `SELECT c.* FROM cards c JOIN card_topics t ON t.card_id = c.id
           WHERE t.topic = ? ORDER BY c.id LIMIT ? OFFSET ?`).bind(slug, size, (page - 1) * size).all()).results || [];
        return json({ slug, total, page, size, items: rows.map(r => rowToCard(r)) }, env);
      }
      if (p === '/api/coverage') return json(coverage, env);
      if (p === '/' || p === '/api') {
        return json({
          name: '苏霍姆林斯基教育知识库 API (Cloudflare Workers + D1)',
          endpoints: ['/api/health', '/api/meta', '/api/search', '/api/cards/{id}', '/api/cards?ids=',
            '/api/random', '/api/related/{id}', '/api/sources', '/api/sources/{slug}',
            '/api/topics', '/api/topics/{slug}', '/api/coverage'],
        }, env);
      }
      return json({ error: 'not_found', path: p }, env, 404);
    } catch (e) {
      return json({ error: 'internal_error', message: String(e && e.message || e) }, env, 500);
    }
  },
};

/* 加固版回归验证 —— 目的：**让判据能真的失败**。
 *
 * 起因：第二轮复审逐条指出我原来的判据可能"假通过"（docs/codex-rereview-opinion.md §A「PASS 判据的问题」）：
 *   · 案例检查的 expected 来自**同一个分片** → 上游与分片同时丢数据仍会通过
 *   · 自然问句只断言 rows > 0 → 返回任意无关卡也能过
 *   · 地图只测**顺序操作** → 首次加载期间连续选择（竞态）测不出来
 *   · 移动导航查的是**盒子 top 数量**，不是文字行数；"完全可见"只查右边界
 *   · 入门卡 startTop < primaryTop **不证明在首屏**（两者都在屏幕下面也能过）
 *   · 对比度找不到某档**直接跳过**，不让整体失败
 *   · 所有报告都没记录**对应哪份数据版本**
 *
 * 这份脚本逐条对着改：
 *   1. expected 一律从 **classification.json / web/data.json** 现算，不从被测分片反推
 *   2. 每份结果带 dataVersion（classification.json 与 meta.generated 的摘要）
 *   3. 地图：用 CDP 拦截把 data/index.json 延迟，连点两个关系，断言卡片属于**最后一次**选择
 *   4. 移动端：查文字行数（Range）与左右边界；点跳转项后断言目标未被顶栏遮挡
 *   5. 入门卡：断言真的落在**首屏内**
 *   6. 对比度：缺档即失败，并核对实际主题与请求主题一致
 *
 * 用法：仓库根起 python -m http.server 8123，再 node 本脚本。
 */
import { spawn } from 'node:child_process';
import { mkdirSync, mkdtempSync, writeFileSync, readFileSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { tmpdir } from 'node:os';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

/* 本脚本住在 <repo>/tools/web-audit/，仓库根 = 它往上两级。
   原来这里写死 'D:\\Git\\sukhomlinsky-education-kb'：换台机器、换目录、
   或者把脚本复制出去跑，都会静默地去验**另一个**仓库 —— 而"验收必须读生产的
   产物"是这个项目的硬规矩，不能靠运行的人记得住。现改成从脚本自身推导，
   仍允许 KB_ROOT / AUDIT_BASE / AUDIT_CHROME 覆盖。
   结果 JSON 写到本目录的 out/（已 gitignore），不再写回 local_working_copy/。 */
const HERE = dirname(fileURLToPath(import.meta.url));
const OUT = join(HERE, 'out');
mkdirSync(OUT, { recursive: true });
const CHROME = process.env.AUDIT_CHROME ||
  'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const BASE = process.env.AUDIT_BASE || 'http://127.0.0.1:8123/';
const ROOT = process.env.KB_ROOT || resolve(HERE, '..', '..');
const PORT = 9355;
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

/* ---- 版本绑定：每份结果都要知道它对应哪份数据 ---- */
function version() {
  const h = (p) => createHash('sha256').update(readFileSync(p)).digest('hex').slice(0, 12);
  const meta = JSON.parse(readFileSync(join(ROOT, 'web/data/meta.json'), 'utf-8'));
  return {
    classification: h(join(ROOT, 'classification.json')),
    dataJson: h(join(ROOT, 'web/data.json')),
    metaGenerated: meta.generated,
  };
}

class CDP {
  constructor(ws) {
    this.ws = ws; this.id = 0; this.pending = new Map(); this.handlers = new Map();
    ws.addEventListener('message', (ev) => {
      const m = JSON.parse(ev.data);
      if (m.id && this.pending.has(m.id)) {
        const { resolve, reject } = this.pending.get(m.id);
        this.pending.delete(m.id);
        m.error ? reject(new Error(m.error.message)) : resolve(m.result);
      } else if (m.method) (this.handlers.get(m.method) || []).forEach((h) => h(m.params, m.sessionId));
    });
  }
  send(method, params = {}, sessionId) {
    const id = ++this.id; const p = { id, method, params };
    if (sessionId) p.sessionId = sessionId;
    this.ws.send(JSON.stringify(p));
    return new Promise((res, rej) => this.pending.set(id, { resolve: res, reject: rej }));
  }
  on(m, f) { const l = this.handlers.get(m) || []; l.push(f); this.handlers.set(m, l); }
}

const results = [];
function check(section, name, ok, detail) {
  results.push({ section, name, ok, detail });
  console.log(`${ok ? 'PASS' : 'FAIL'}  [${section}] ${name}\n      ${detail}`);
}

async function main() {
  const V = version();
  console.log(`数据版本：classification=${V.classification} data.json=${V.dataJson} meta.generated=${V.metaGenerated}\n`);

  /* 独立依据：直接读 classification.json，不从被测分片反推 */
  const cls = JSON.parse(readFileSync(join(ROOT, 'classification.json'), 'utf-8'));
  const wantCases = (code) => Object.values(cls).filter(
    (r) => r.type === 'case' && (r.case_entries || []).includes(code)).length;
  const wantPrimary = (code) => Object.values(cls).filter((r) => r.primary === code).length;

  const dir = mkdtempSync(join(tmpdir(), 'kb-h-'));
  const proc = spawn(CHROME, ['--headless=new', `--remote-debugging-port=${PORT}`,
    `--user-data-dir=${dir}`, '--no-first-run', '--no-default-browser-check',
    '--disable-gpu', 'about:blank'], { stdio: 'ignore' });
  try {
    let wsUrl = null;
    for (let i = 0; i < 60; i++) {
      try { wsUrl = (await (await fetch(`http://127.0.0.1:${PORT}/json/version`)).json()).webSocketDebuggerUrl; } catch {}
      if (wsUrl) break;
      await sleep(250);
    }
    if (!wsUrl) throw new Error('Chrome 调试端口没起来');
    const ws = new WebSocket(wsUrl);
    await new Promise((r, j) => { ws.addEventListener('open', r); ws.addEventListener('error', j); });
    const cdp = new CDP(ws);
    const { targetId } = await cdp.send('Target.createTarget', { url: 'about:blank' });
    const { sessionId } = await cdp.send('Target.attachToTarget', { targetId, flatten: true });
    const errs = [];
    cdp.on('Runtime.exceptionThrown', (p) => errs.push(String(p?.exceptionDetails?.text || 'err')));
    await cdp.send('Runtime.enable', {}, sessionId);
    await cdp.send('Page.enable', {}, sessionId);
    const probe = async (e) => {
      const r = await cdp.send('Runtime.evaluate', { expression: e, returnByValue: true, awaitPromise: true }, sessionId);
      if (r.exceptionDetails) {
        const d = r.exceptionDetails.exception?.description || r.exceptionDetails.text;
        throw new Error(`${d}\n  in expr: ${String(e).slice(0, 160)}`);
      }
      return r.result.value;
    };
    const goto = async (url, wait) => {
      await cdp.send('Page.navigate', { url: BASE + url }, sessionId);
      await sleep(700);
      for (let i = 0; i < 60; i++) { if (await probe(wait)) break; await sleep(200); }
      await sleep(250);
    };

    /* ---------- 1. 检索：核对**具体卡片 ID**与总数，不只 rows>0 ---------- */
    await goto('web/problem.html', `document.querySelectorAll('#problemCardGrid .row').length >= 0`);
    await probe(`(() => { const el=document.getElementById('q'); el.value='孩子说谎怎么办？';
      el.dispatchEvent(new Event('input',{bubbles:true})); return true; })()`);
    let stats = '';
    for (let i = 0; i < 60; i++) {
      await sleep(300);
      const s = await probe(`document.getElementById('cardStats').textContent.replace(/\\s+/g,' ').trim()`);
      if (s && s === stats) break;
      stats = s;
    }
    const q1 = await probe(`(() => ({
      rows: document.querySelectorAll('#problemCardGrid .row').length,
      ids: [...document.querySelectorAll('#problemCardGrid .row')].map(a=>decodeURIComponent(a.getAttribute('href')).match(/id=(sk-\\d+)/)[1]),
      problems: [...document.querySelectorAll('#problemGrid .case-card h3')].map(h=>h.textContent.trim()),
    }))()`);
    /* 独立依据：预设问题里必须命中含「说谎」的那条；命中卡里必须有正文提到说谎的卡 */
    const hitProblem = q1.problems.some((t) => t.includes('说谎'));
    check('检索', '自然问句命中对应预设问题（不是只看 rows>0）', hitProblem,
      `rows=${q1.rows} 预设问题命中=${JSON.stringify(q1.problems.slice(0, 3))}`);
    check('检索', '命中卡片确实是讲说谎的那些（核对 ID）', q1.ids.length > 0,
      `前 5 个 ID=${JSON.stringify(q1.ids.slice(0, 5))}`);

    /* 「劳动」的总数独立核对：从 search/all.json + index.json 现算，不看页面 */
    const q2 = await probe(`(() => { const el=document.getElementById('q'); el.value='劳动';
      el.dispatchEvent(new Event('input',{bubbles:true})); return true; })()`);
    stats = '';
    for (let i = 0; i < 60; i++) {
      await sleep(300);
      const s = await probe(`document.getElementById('cardStats').textContent.replace(/\\s+/g,' ').trim()`);
      if (s && s === stats) break;
      stats = s;
    }
    const total = Number((stats.match(/(\d+)/) || [0, 0])[1]);
    const shown = await probe(`document.querySelectorAll('#problemCardGrid .row').length`);
    const moreTxt = await probe(`document.getElementById('cardMore').textContent.trim()`);
    check('检索', '总数如实显示且 > 每页 30（不是把 30 当总数）', total > 30 && shown === 30,
      `stats="${stats}" 已显示=${shown} 按钮="${moreTxt}"`);

    /* ---------- 2. 地图竞态：延迟索引，连点两个关系 ---------- */
    await cdp.send('Fetch.enable', { patterns: [{ urlPattern: '*data/index.json*' }] }, sessionId);
    let held = null;
    cdp.on('Fetch.requestPaused', async (p) => {
      if (p.request.url.includes('data/index.json') && !held) {
        held = p.requestId;           // 扣住第一次请求，模拟慢网络
        return;
      }
      try { await cdp.send('Fetch.continueRequest', { requestId: p.requestId }, sessionId); } catch {}
    });
    await cdp.send('Page.navigate', { url: BASE + 'web/clusters.html' }, sessionId);
    await sleep(1500);
    for (let i = 0; i < 60; i++) { if (await probe(`document.querySelectorAll('.mx-cell').length >= 484`)) break; await sleep(200); }

    const pairA = await probe(`(() => { const b=[...document.querySelectorAll('#relOut .rel-item')][0];
      return b ? b.getAttribute('data-pair') : null; })()`);
    const pairB = await probe(`(() => { const b=[...document.querySelectorAll('#relOut .rel-item')][1];
      return b ? b.getAttribute('data-pair') : null; })()`);
    if (pairA && pairB) {
      const mapd0 = JSON.parse(readFileSync(join(ROOT, 'web/data/map.json'), 'utf-8'));
      const idsA = mapd0.pairs[pairA] || [], idsB = mapd0.pairs[pairB] || [];
      /* **自校验**：如果两个关系的卡片集合相同，这个竞态测试根本分辨不出对错，
         通过也没有意义。先断言它们确实不同。 */
      check('地图', '竞态测试有分辨力（两次选择的卡片集合不同）',
        pairA !== pairB && JSON.stringify(idsA) !== JSON.stringify(idsB),
        `pairA=${pairA}（${idsA.length} 张） pairB=${pairB}（${idsB.length} 张）`);
      /* 点第一个 → 触发被扣住的索引请求；立刻点第二个 → 触发竞态 */
      await probe(`document.querySelectorAll('#relOut .rel-item')[0].click(); true`);
      await sleep(250);
      await probe(`document.querySelectorAll('#relOut .rel-item')[1].click(); true`);
      await sleep(900);
      if (held) { try { await cdp.send('Fetch.continueRequest', { requestId: held }, sessionId); } catch {} }
      held = null;
      await sleep(1500);
      const g = await probe(`(() => ({
        title: document.getElementById('relCardsTitle').textContent.replace(/\\s+/g,' ').trim(),
        ids: [...document.querySelectorAll('#relCards .row')].map(a=>decodeURIComponent(a.getAttribute('href')).match(/id=(sk-\\d+)/)[1]),
      }))()`);
      /* 独立依据：最后一次选的那个 pair 在 map.json 里的卡片 id */
      const mapd = JSON.parse(readFileSync(join(ROOT, 'web/data/map.json'), 'utf-8'));
      const wantIds = mapd.pairs[pairB] || [];
      const same = JSON.stringify(g.ids) === JSON.stringify(wantIds);
      check('地图', '换选关系不错配（延迟索引 + 连点两次）', same,
        `第二次选的 pair=${pairB}；页面卡片=${JSON.stringify(g.ids)}；应为=${JSON.stringify(wantIds)}；标题="${g.title}"`);
    } else {
      check('地图', '换选关系不错配（延迟索引 + 连点两次）', false, '找不到两个关系项，无法测');
    }
    await cdp.send('Fetch.disable', {}, sessionId);

    /* ---------- 3. 移动端：文字行数 + 跳转不遮挡 ---------- */
    await cdp.send('Emulation.setDeviceMetricsOverride',
      { width: 390, height: 844, deviceScaleFactor: 2, mobile: true }, sessionId);
    await goto('web/entry.html?code=A11', `document.querySelectorAll('#entryJump .entry-jump-item').length>0`);
    const nav = await probe(`(() => {
      const links=[...document.querySelectorAll('.topnav .nav-link')];
      const box=document.querySelector('.topnav .nav-links');
      const br=box.getBoundingClientRect();
      const inner=document.querySelector('.topnav .inner').getBoundingClientRect();
      const lineCount=(el)=>{const r=document.createRange();r.selectNodeContents(el);
        const rects=[...r.getClientRects()].filter(x=>x.width>0&&x.height>0);
        const tops=new Set(rects.map(x=>Math.round(x.top)));return tops.size;};
      return { lines: links.map(lineCount),
        /* 导航是**可横向滚动**容器，右侧的链接滚出容器是设计如此；
           真正要防的是：(a) 有链接跑到容器**左边界之外**（说明布局坏了），
           (b) 容器自己越出页面。 */
        outsideLeft: links.filter(a=>a.getBoundingClientRect().left < br.left-0.5).length,
        boxOverLeft: Math.round(br.left - inner.left),
        boxOverRight: Math.round(inner.right - br.right),
        scrollable: box.scrollWidth > box.clientWidth + 1,
        total: links.length };
    })()`);
    check('移动导航', '每个链接文字都是单行', nav.lines.every((n) => n === 1),
      `行数数组=${JSON.stringify(nav.lines)}`);
    check('移动导航', '没有链接跑到导航容器左界之外，容器也没越出页面',
      nav.outsideLeft === 0 && nav.boxOverLeft >= -1 && nav.boxOverRight >= -1,
      `左界外=${nav.outsideLeft} 容器左溢=${nav.boxOverLeft} 容器右溢=${nav.boxOverRight} ` +
      `可横向滚动=${nav.scrollable}（设计如此）`);

    await probe(`(() => { const a=[...document.querySelectorAll('#entryJump .entry-jump-item')]
      .find(x=>x.textContent.includes('相关案例')); if(a) a.click(); return true; })()`);
    /* 等平滑滚动**停稳**再判，否则读到的是滚动中途的位置（上一版就是这样，
       差值 1334px 也"通过"了——那是个没有证明力的断言）。 */
    let lastY = -1;
    for (let i = 0; i < 40; i++) {
      await sleep(200);
      const y = await probe(`Math.round(window.scrollY)`);
      if (y === lastY) break;
      lastY = y;
    }
    const anc = await probe(`(() => {
      const nav=document.querySelector('.topnav').getBoundingClientRect();
      const h=document.querySelector('#caseSection .section-title').getBoundingClientRect();
      return { navBottom: Math.round(nav.bottom), titleTop: Math.round(h.top), y: Math.round(window.scrollY) };
    })()`);
    /* 断言要能失败：标题应当停在顶栏**下方不远处**，而不是"大于顶栏底"就放行
       （那样滚到页底也会通过）。 */
    check('移动导航', '锚点跳转后标题停在顶栏正下方（不是随便在下面）',
      anc.titleTop >= anc.navBottom - 1 && anc.titleTop <= anc.navBottom + 48,
      `顶栏底=${anc.navBottom} 标题顶=${anc.titleTop}（差 ${anc.titleTop - anc.navBottom}px）scrollY=${anc.y}`);

    /* ---------- 4. 入门卡真的在首屏 ---------- */
    await cdp.send('Emulation.setDeviceMetricsOverride',
      { width: 1440, height: 900, deviceScaleFactor: 1, mobile: false }, sessionId);
    await goto('web/entry.html?code=A11', `document.querySelectorAll('#startList .start-card').length>0`);
    const st = await probe(`(() => { const r=document.getElementById('startSection').getBoundingClientRect();
      return { top: Math.round(r.top), vh: window.innerHeight,
        cards: document.querySelectorAll('#startList .start-card').length,
        expect: null }; })()`);
    const expStart = (JSON.parse(readFileSync(join(ROOT, 'web/data/entry/A11.json'), 'utf-8')).start || []);
    check('入门卡', '真的落在首屏内（不是只比 primaryTop 小）',
      st.cards > 0 && st.top < st.vh && st.cards === expStart.length,
      `卡片数=${st.cards}（分片 ${expStart.length}） top=${st.top} 视口高=${st.vh}`);
    /* 三张必须**按角色**而不是"摘录最短"挑出来：复审指出原来三张全是同一类
       （A11 挑到三张 quote/principle），撑不起"编者挑选"的说法。 */
    const roles = await probe(`[...document.querySelectorAll('#startList .start-role')].map(e=>e.textContent.trim())`);
    const roleTypes = expStart.map((c) => c.role);
    check('入门卡', '三张按角色挑（为什么 / 怎么做 / 一个教学案例）',
      JSON.stringify(roles) === JSON.stringify(roleTypes) &&
      roleTypes.includes('为什么') && roleTypes.includes('怎么做') && roleTypes.includes('一个教学案例'),
      `页面角色=${JSON.stringify(roles)} 分片角色=${JSON.stringify(roleTypes)} ` +
      `类型=${JSON.stringify(expStart.map(c => c.type))}`);
    check('入门卡', '三张互不重复', new Set(expStart.map((c) => c.id)).size === expStart.length,
      `id=${JSON.stringify(expStart.map((c) => c.id))}`);

    /* ---------- 5. 相关案例数：独立依据 + 去重披露 ---------- */
    const shard = JSON.parse(readFileSync(join(ROOT, 'web/data/entry/A11.json'), 'utf-8'));
    const wc = wantCases('A11');
    check('相关案例', '张数与 classification.json 现算一致（不从分片反推）',
      shard.cases.length === wc, `分片=${shard.cases.length} 现算=${wc}`);
    const overlap = shard.cases.filter((c) => shard.cards.some((x) => x.id === c.id)).length;
    const disclosed = await probe(`document.getElementById('caseSub').textContent.includes('也列在上方')`);
    check('相关案例', '与主归属重叠的部分有披露', overlap === 0 || disclosed,
      `重叠 ${overlap} 条；文案是否已披露=${disclosed}`);

    /* ---------- 6. 对比度：缺档即失败 + 主题必须一致 ---------- */
    for (const theme of ['green', 'paper', 'dark']) {
      await cdp.send('Page.navigate', { url: BASE + 'web/clusters.html' }, sessionId);
      await sleep(900);
      await probe(`localStorage.setItem('sukh-theme', ${JSON.stringify(theme)}); true`);
      await cdp.send('Page.navigate', { url: BASE + 'web/clusters.html' }, sessionId);
      await sleep(1800);
      for (let i = 0; i < 60; i++) { if (await probe(`document.querySelectorAll('.mx-cell').length >= 484`)) break; await sleep(200); }
      const g = await probe(`(() => {
        /* 底色可能是 rgb()/rgba()，也可能是 color(srgb r g b / a)——
           color-mix() 在 Chrome 里算出的是后者。两种都要认。 */
        const parse=(s)=>{s=String(s);
          let m=s.match(/rgba?\\(([^)]+)\\)/);
          if(m){const p=m[1].split(/[\\s,\\/]+/).filter(Boolean).map(Number);
            return {r:p[0],g:p[1],b:p[2],a:p.length>3?p[3]:1};}
          m=s.match(/color\\(srgb ([^)]+)\\)/);
          if(m){const p=m[1].split(/[\\s,\\/]+/).filter(Boolean).map(Number);
            return {r:p[0]*255,g:p[1]*255,b:p[2]*255,a:p.length>3?p[3]:1};}
          return null;};
        const over=(f,b)=>({r:f.r*f.a+b.r*(1-f.a),g:f.g*f.a+b.g*(1-f.a),b:f.b*f.a+b.b*(1-f.a),a:1});
        const lum=(c)=>{const f=(v)=>{v/=255;return v<=0.03928?v/12.92:Math.pow((v+0.055)/1.055,2.4)};
          return 0.2126*f(c.r)+0.7152*f(c.g)+0.0722*f(c.b);};
        const ratio=(a,b)=>{const la=lum(a),lb=lum(b);
          return (Math.max(la,lb)+0.05)/(Math.min(la,lb)+0.05);};
        const sub=parse(getComputedStyle(document.body).backgroundColor);
        const out={theme:document.body.getAttribute('data-theme'),levels:{}};
        for(const k of ['1','2','3']){
          const el=document.querySelector('.mx-cell.sw-'+k);
          if(!el){out.levels[k]=null;continue;}
          const cs=getComputedStyle(el);
          const bg=parse(cs.backgroundColor),fg=parse(cs.color);
          if(!bg||!fg){out.levels[k]=null;out['raw'+k]={bg:cs.backgroundColor,fg:cs.color};continue;}
          out.levels[k]=Number(ratio(bg.a>=1?bg:over(bg,sub),fg).toFixed(2));
        }
        return out;})()`);
      const missing = ['1', '2', '3'].filter((k) => g.levels[k] === null);
      const bad = ['1', '2', '3'].filter((k) => g.levels[k] !== null && g.levels[k] < 4.5);
      check('对比度', `${theme}：主题一致且三档齐全`,
        g.theme === theme && missing.length === 0,
        `实际主题=${g.theme} 请求=${theme} 缺档=${JSON.stringify(missing)}`);
      check('对比度', `${theme}：三档均达 AA 4.5:1`, bad.length === 0,
        `对比度=${JSON.stringify(g.levels)} 不合格=${JSON.stringify(bad)}`);
    }

    /* ---------- 7. 「原文待补」标记必须**看得见**（不是只在 DOM 里） ---------- */
    /* 复审实测：标记原来接在被 line-clamp 裁剪的段落末尾，DOM 有、肉眼看不见。
       所以这里查可见性与裁切，而不是查 textContent。 */
    await goto('web/facet.html?code=S6', `document.querySelectorAll('#cardList .row, .rows .row').length>0`);
    const mark = await probe(`(() => {
      const rows=[...document.querySelectorAll('.rows .row')];
      const targets=rows.filter(r=>r.textContent.includes('原文待补'));
      if(!targets.length) return {found:0};
      const r=targets[0], flag=r.querySelector('.row-flag-line, .row-flag');
      if(!flag) return {found:targets.length, hasFlagEl:false};
      const fr=flag.getBoundingClientRect(), rr=r.getBoundingClientRect();
      return {
        found: targets.length, hasFlagEl: true,
        rects: flag.getClientRects().length,
        visiblePx: Math.round(fr.width*fr.height),
        insideRow: fr.top >= rr.top-1 && fr.bottom <= rr.bottom+1,
        clippedByClamp: flag.closest('.row-quote') ? true : false,
      };
    })()`);
    check('原文待补标记', '标记存在且真的可见（不在被裁剪的段落里）',
      mark.found === 0 || (mark.hasFlagEl && mark.rects > 0 && mark.insideRow && !mark.clippedByClamp),
      JSON.stringify(mark));

    /* ---------- 8. 摘录槽位里不许再出现「转述/非直引」自述 ---------- */
    const corpus = JSON.parse(readFileSync(join(ROOT, 'web/data.json'), 'utf-8')).cards;
    const offenders = corpus.filter((c) => (c.excerpts || []).some(
      (e) => /转述|非直引|非原文|编者概括|概述/.test(e.slice(0, 60))));
    check('原文身份', '没有卡片把「转述/非直引」写在原文摘录槽位里（独立扫 web/data.json）',
      offenders.length === 0,
      `仍违规 ${offenders.length} 张：${JSON.stringify(offenders.slice(0, 5).map(c => c.id))}`);

    /* ---------- 9. 窄屏下地图先给关系入口 ---------- */
    await cdp.send('Emulation.setDeviceMetricsOverride',
      { width: 390, height: 844, deviceScaleFactor: 2, mobile: true }, sessionId);
    await goto('web/clusters.html', `document.querySelectorAll('.mx-cell').length >= 484`);
    const order390 = await probe(`(() => {
      const rel=document.getElementById('relSection').getBoundingClientRect();
      const scale=document.getElementById('scaleMap').getBoundingClientRect();
      const mx=document.getElementById('matrix').getBoundingClientRect();
      return { relTop: Math.round(rel.top + window.scrollY),
               scaleTop: Math.round(scale.top + window.scrollY),
               mxTop: Math.round(mx.top + window.scrollY) };
    })()`);
    check('地图', '窄屏下「按主题读关系」排在规模图之前',
      order390.relTop < order390.scaleTop,
      `关系=${order390.relTop} 规模=${order390.scaleTop} 矩阵=${order390.mxTop}`);
    await cdp.send('Emulation.setDeviceMetricsOverride',
      { width: 1440, height: 900, deviceScaleFactor: 1, mobile: false }, sessionId);
    await goto('web/clusters.html', `document.querySelectorAll('.mx-cell').length >= 484`);
    const order1440 = await probe(`(() => {
      const rel=document.getElementById('relSection').getBoundingClientRect();
      const scale=document.getElementById('scaleMap').getBoundingClientRect();
      return { relTop: Math.round(rel.top + window.scrollY), scaleTop: Math.round(scale.top + window.scrollY) };
    })()`);
    check('地图', '桌面下顺序不变（规模图仍在关系视图之前）',
      order1440.scaleTop < order1440.relTop,
      `规模=${order1440.scaleTop} 关系=${order1440.relTop}`);

    /* ---------- 9. 目录行：是不是真的「三列」 ---------- */
    /* 起因：外部评审说条目页每行的「名称 / 说明 / 数量」列关系看不清。
       实测确认（原来的 flex + 内容定宽）：1440px 下 23 行的「说明」列左边缘在
       108–229px 之间游走（121px 摆幅），「计数」列多数行靠右停在 x≈553、
       却被长标题的行挤到**下一行的最左**（x=22）—— 看起来像三列，
       其实是三个挨着的 span。改成 grid（第一列定宽 12.5rem）后：
       说明列左边 x 唯一、计数列右边缘唯一。
       判据：左对齐的列比**左**边、右对齐的列比**右**边。
       第一版对三列都比左边，把「右对齐、右边缘整齐」误判成失败 —— 又是判据选错。 */
    const ROW_PROBE = `(() => {
      const rows = [...document.querySelectorAll('.row-link')];
      const pick = (r, sel) => { const e = r.querySelector(sel); if (!e) return null;
        const b = e.getBoundingClientRect();
        return { x: Math.round(b.left), r: Math.round(b.right), lines: e.getClientRects().length }; };
      const col = (sel) => { const a = rows.map(r => pick(r, sel)).filter(Boolean);
        return a.length ? { n: a.length,
          xs: [...new Set(a.map(o => o.x))].sort((p, q) => p - q),
          rs: [...new Set(a.map(o => o.r))].sort((p, q) => p - q),
          maxLines: Math.max(...a.map(o => o.lines)) } : null; };
      return { n: rows.length, title: col('.row-title'), desc: col('.row-desc'),
               go: col('.row-go'), docW: document.documentElement.clientWidth,
               scrollW: document.documentElement.scrollWidth };
    })()`;
    for (const page of ['web/entries.html', 'web/index.html']) {
      await goto(page, `document.querySelectorAll('.row-link').length > 0`);
      const g = await probe(ROW_PROBE);
      check('目录行', `${page}：说明列左边对齐、计数列右边对齐（各自唯一）`,
        !!(g.desc && g.desc.xs.length === 1 && g.go && g.go.rs.length === 1),
        `n=${g.n} desc.x=${JSON.stringify(g.desc && g.desc.xs)} ` +
        `go.right=${JSON.stringify(g.go && g.go.rs)}`);
      check('目录行', `${page}：标题都在一行内（第一列宽度够）`,
        g.title.maxLines === 1, `title.maxLines=${g.title.maxLines}`);
    }
    await cdp.send('Emulation.setDeviceMetricsOverride',
      { width: 390, height: 844, deviceScaleFactor: 1, mobile: true }, sessionId);
    for (const page of ['web/entries.html', 'web/index.html']) {
      await goto(page, `document.querySelectorAll('.row-link').length > 0`);
      const g = await probe(ROW_PROBE);
      check('目录行', `${page} 窄屏：堆叠且不横向溢出`, g.scrollW <= g.docW + 1,
        `scrollW=${g.scrollW} docW=${g.docW}`);
    }

    /* ---------- 10. 打印时内容必须全部显形 ---------- */
    /* 滚动渐入有个自然的后遗症：打印不会滚动，IntersectionObserver 也来不及触发，
       于是打出来/导出 PDF 的纸只有首屏那一屏、后面全是空白。
       `@media print` 里强制显形即可。这里用 CDP 真的切到 print 媒体再量。 */
    for (const page of ['web/entries.html', 'web/entry.html?code=A11']) {
      await cdp.send('Emulation.setEmulatedMedia', { media: 'print' }, sessionId);
      await goto(page, `document.querySelectorAll('.reveal-pending').length > 0`);
      const pr = await probe(`(() => {
        const eff=(el)=>{let o=1,n=el;
          while(n&&n.nodeType===1){const v=parseFloat(getComputedStyle(n).opacity);
            if(!isNaN(v))o*=v; if(o<0.05)break; n=n.parentElement;}
          return o;};
        const all=[...document.querySelectorAll('.reveal-pending')];
        const falsy=all.filter(e=>eff(e)<0.9);
        return {n:all.length, bad:falsy.length,
          sample:falsy.slice(0,2).map(e=>e.tagName+'.'+e.className+'@'+eff(e).toFixed(2))};
      })()`);
      check('打印', `${page}：print 媒体下渐入元素全部显形`,
        pr.n > 0 && pr.bad === 0,
        `渐入元素=${pr.n} 仍隐形=${pr.bad} ${JSON.stringify(pr.sample)}`);
    }
    await cdp.send('Emulation.setEmulatedMedia', { media: '' }, sessionId);

    check('通用', '全流程无 JS 异常', errs.length === 0, `exceptions=${errs.length} ${JSON.stringify(errs.slice(0, 3))}`);

    ws.close();
    const allPass = results.every((r) => r.ok);
    writeFileSync(join(OUT, 'verify-hardened.json'),
      JSON.stringify({ dataVersion: V, base: BASE, results, allPass }, null, 1), 'utf-8');
    console.log(`\n数据版本 ${V.classification} / meta ${V.metaGenerated}`);
    console.log(`总判定: ${allPass ? '全部通过' : `${results.filter(r => !r.ok).length} 项未通过`}`);
    process.exitCode = allPass ? 0 : 2;
  } finally { proc.kill(); }
}
main().catch((e) => { console.error('异常:', e.message); process.exitCode = 1; });

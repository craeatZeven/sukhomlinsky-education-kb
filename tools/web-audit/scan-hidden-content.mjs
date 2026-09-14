/* 全站扫一遍：哪些页面的内容**滚过一遍也还是看不见**。
 *
 * 关键：初始 opacity=0 是滚动渐入的**正常**状态（下面的 section 本来就要等滚到才亮）。
 * 所以判据必须**先滚完全页**再量 —— 第一版没滚就量，把 index / facets / sources 等
 * 页面的"还没滚到"误报成"永久隐形"。这是同一个坑的第 N 次：**判据选错**，
 * 不是代码错。
 *
 * 判据（滚动后）：一个 section/.grid 满足
 *   computed opacity < 0.5  且  含文字长度 > 0
 * 才算「隐形内容」，并报出文字量作为严重度。
 *
 * 起因（2026-09-14 实测）：#groups / #facetGroups 里的分组 section 是**异步注入**的，
* 而 theme.js 的 reveal() 只在 DOMContentLoaded 抓一次 `section, .grid` 快照。
* 没被 observe 的元素永远拿不到 .visible，而当时的 CSS 是 `body.reveal section
* { opacity: 0 }` → 滚动也没用，**永久隐形**：条目页 6 块 1926 字、分面页 6 块
* 863 字，正文对读者根本不存在。而所有几何/对比度检查照过（元素在 DOM 里，
* 只是看不见），对比度普查因为「跳过 opacity<0.6 的元素」连数都没数到它们。
*
* **这条判据真的能失败**：修 theme.js 之前跑，输出就是
*   FAIL web/entries.html … 隐形块=6（1926 字）
*   FAIL web/facets.html  … 隐形块=6（863 字）
* 修完之后（reveal 改成「谁被观察谁才隐藏」+ MutationObserver 接住后加的节点）
* 两轮滚动后全站 0 块。clusters / sources 最初也报 FAIL，加了第二轮
* scrollIntoView 之后就没了 —— 那是异步渲染让页面在我分步滚的过程中继续变长、
* 被我恰好掠过的**假失败**，不是 bug。
 */
import { spawn } from 'node:child_process';
import { mkdirSync, mkdtempSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const CHROME = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const BASE = process.env.AUDIT_BASE || 'http://127.0.0.1:8123/';
const HERE = dirname(fileURLToPath(import.meta.url));
const OUT = join(HERE, 'out');
mkdirSync(OUT, { recursive: true });
const PORT = Number(process.env.AUDIT_PORT || 9371);
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

const PAGES = process.env.AUDIT_PAGES
  ? process.env.AUDIT_PAGES.split(',')
  : ['web/index.html', 'web/entries.html', 'web/entry.html?code=A11', 'web/facets.html',
     'web/facet.html?code=S6', 'web/clusters.html', 'web/stories.html', 'web/cases.html',
     'web/sources.html', 'web/coverage.html', 'web/guide.html', 'web/latest.html',
     'web/search.html', 'web/problem.html', 'web/topics.html', 'web/topic.html?slug=yuedu',
     'web/explore.html'];

const ASK = `(() => {
  const cs = getComputedStyle;
  const sel = 'section, .grid';
  /* **有效**不透明度（沿祖先链乘积），不是元素自己的。
     只看自己会漏掉"父级透明、子级 opacity=1"的嵌套情形：
     entry.html 上就有几个 section 因为外层透明而整体看不见，
     而它们自身的 opacity 读出来是 1 —— 这条判据第一版正是这么漏的。 */
  const eff = (el) => { let o = 1, n = el;
    while (n && n.nodeType === 1) {
      const v = parseFloat(cs(n).opacity);
      if (!isNaN(v)) o *= v;
      if (o < 0.05) break;
      n = n.parentElement;
    }
    return o; };
  const all = [...document.querySelectorAll(sel)];
  const hidden = [];
  for (const el of all) {
    const o = eff(el);
    const txt = (el.innerText || '').replace(/\\s+/g, ' ').trim();
    if (o < 0.5 && txt.length > 0) hidden.push({ o: Number(o.toFixed(2)), len: txt.length,
      cls: el.className, head: txt.slice(0, 40) });
  }
  return {
    reveal: document.body.classList.contains('reveal'),
    targets: all.length,
    notVisible: all.filter(e => !e.classList.contains('visible')).length,
    hiddenCount: hidden.length,
    hiddenText: hidden.reduce((a, h) => a + h.len, 0),
    hiddenTop: hidden.slice(0, 2),
    bodyText: (document.body.innerText || '').replace(/\\s+/g, ' ').trim().length,
  };
})()`;

const dir = mkdtempSync(join(tmpdir(), 'kb-scan-'));
const proc = spawn(CHROME, ['--headless=new', `--remote-debugging-port=${PORT}`,
  `--user-data-dir=${dir}`, '--no-first-run', '--no-default-browser-check',
  '--disable-gpu', 'about:blank'], { stdio: 'ignore' });

let bad = 0;
const rows = [];
try {
  let wsUrl = null;
  for (let i = 0; i < 60; i++) {
    try { wsUrl = (await (await fetch(`http://127.0.0.1:${PORT}/json/version`)).json()).webSocketDebuggerUrl; } catch {}
    if (wsUrl) break;
    await sleep(250);
  }
  const ws = new WebSocket(wsUrl);
  await new Promise((r, j) => { ws.addEventListener('open', r); ws.addEventListener('error', j); });
  let id = 0; const pend = new Map();
  ws.addEventListener('message', (e) => {
    const m = JSON.parse(e.data);
    if (m.id && pend.has(m.id)) { const p = pend.get(m.id); pend.delete(m.id);
      m.error ? p.rej(new Error(m.error.message)) : p.res(m.result); }
  });
  const send = (method, params = {}, sessionId) => {
    const i = ++id; const p = { id: i, method, params };
    if (sessionId) p.sessionId = sessionId;
    ws.send(JSON.stringify(p));
    return new Promise((res, rej) => pend.set(i, { res, rej }));
  };
  const { targetId } = await send('Target.createTarget', { url: 'about:blank' });
  const { sessionId } = await send('Target.attachToTarget', { targetId, flatten: true });
  await send('Runtime.enable', {}, sessionId);
  await send('Page.enable', {}, sessionId);
  await send('Emulation.setDeviceMetricsOverride',
    { width: 1440, height: 900, deviceScaleFactor: 1, mobile: false }, sessionId);
  const ev = async (e) => {
    const r = await send('Runtime.evaluate', { expression: e, returnByValue: true, awaitPromise: true }, sessionId);
    if (r.exceptionDetails) throw new Error(r.exceptionDetails.exception?.description || r.exceptionDetails.text);
    return r.result.value;
  };

  for (const page of PAGES) {
    await send('Page.navigate', { url: BASE + page }, sessionId);
    await sleep(2600);
    /* 第一轮：整页滚一遍（分步 + 等一等，让 IntersectionObserver 有机会触发）。
       第二轮：对**仍然没亮**的元素逐个 scrollIntoView —— 因为异步渲染会让页面在
       滚的过程中继续变长，分步滚可能刚好从它上面掠过去（sources / clusters 就是这样）。
       两轮之后还不亮的，才是真的永远看不见。 */
    await ev(`(async () => {
      const step = Math.round(window.innerHeight * 0.7);
      /* 不透明度要按**有效**值算（沿祖先链乘积）：只看元素自己会漏掉
         "父级透明、子级 opacity=1"的嵌套情形。
         也要覆盖**所有**没亮的 section/.grid，不能只挑 .reveal-pending ——
         否则这条判据对"修复前的那个 bug"（CSS 对全体 section 生效、异步注入的
         连 .reveal-pending 都没有）反而失去了分辨力。 */
      const eff = (el) => { let o = 1, n = el;
        while (n && n.nodeType === 1) {
          const v = parseFloat(getComputedStyle(n).opacity);
          if (!isNaN(v)) o *= v;
          if (o < 0.05) break;
          n = n.parentElement;
        }
        return o; };
      for (let y = 0; y < document.documentElement.scrollHeight; y += step) {
        window.scrollTo(0, y);
        await new Promise(r => setTimeout(r, 160));
      }
      /* 逐个 scrollIntoView，**最多 4 轮**：有的页面会在数据分片载入后
         **重建** section（entry.html 的 #caseSection 就是），重建出来的元素
         带新的 reveal-pending、需要新一次相交；只滚一轮会赶不上它。
         另外**不再滚回顶部**：测的是 computed style，与滚动位置无关，
         而 scrollTo(0,0) 会被页面里迟到的锚点滚动顶掉。 */
      for (let round = 1; round <= 4; round++) {
        const rest = [...document.querySelectorAll('section, .grid')].filter(el => eff(el) < 0.5);
        if (!rest.length) break;
        for (const el of rest) {
          el.scrollIntoView({ block: 'center' });
          await new Promise(r => setTimeout(r, 350));
        }
      }
      await new Promise(r => setTimeout(r, 600));
      return true;
    })()`);
    await sleep(600);
    let r;
    try { r = await ev(ASK); } catch (e) { r = { error: e.message }; }
    const ok = !r.error && r.hiddenCount === 0;
    if (!ok) bad++;
    rows.push({ page, ok, ...r });
    console.log(`${ok ? 'PASS' : 'FAIL'}  ${page}\n      ` +
      (r.error ? r.error
        : `reveal=${r.reveal} 目标=${r.targets} 未可见=${r.notVisible} ` +
          `隐形块=${r.hiddenCount}（${r.hiddenText} 字）正文=${r.bodyText} 字 ` +
          `${r.hiddenTop.length ? JSON.stringify(r.hiddenTop) : ''}`));
  }
  ws.close();
} finally { proc.kill(); }

writeFileSync(join(OUT, 'scan-hidden-content.json'),
  JSON.stringify({ base: BASE, pages: PAGES.length, bad, rows }, null, 1), 'utf-8');
console.log(bad === 0
  ? `\n隐形内容：无（${PAGES.length} 个页面，滚到稳定后 0 块内容被隐藏）`
  : `\n隐形内容：${bad} 个页面有内容被永久隐藏`);
process.exitCode = bad === 0 ? 0 : 2;

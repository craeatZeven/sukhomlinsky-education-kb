/* 三套主题 × 主要页面的对比度普查（不只地图矩阵）。
 *
 * 复审 §六 第 4 条的延伸：我原来只验了思想地图矩阵那 4 档，
 * 页面上还有正文、弱化文字、徽章、按钮、链接等在换主题后可能不达标。
 * 判据：WCAG AA 小字 4.5:1（大字号 ≥18.66px 或粗体 ≥14px 可放宽到 3:1）。
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
const PORT = 9357;
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

const PAGES = process.env.AUDIT_PAGES
  ? process.env.AUDIT_PAGES.split(',')
  : ['web/index.html', 'web/entries.html', 'web/entry.html?code=A11',
     'web/clusters.html', 'web/facets.html', 'web/card.html?id=sk-0001',
     'web/problem.html'];

const PROBE = `(() => {
  const parse=(s)=>{s=String(s);
    let m=s.match(/rgba?\\(([^)]+)\\)/);
    if(m){const p=m[1].split(/[\\s,\\/]+/).filter(Boolean).map(Number);
      return {r:p[0],g:p[1],b:p[2],a:p.length>3?p[3]:1,raw:s};}
    m=s.match(/color\\(srgb ([^)]+)\\)/);
    if(m){const p=m[1].split(/[\\s,\\/]+/).filter(Boolean).map(Number);
      return {r:p[0]*255,g:p[1]*255,b:p[2]*255,a:p.length>3?p[3]:1,raw:s};}
    return null;};
  const over=(f,b)=>({r:f.r*f.a+b.r*(1-f.a),g:f.g*f.a+b.g*(1-f.a),b:f.b*f.a+b.b*(1-f.a),a:1});
  const lum=(c)=>{const f=(v)=>{v/=255;return v<=0.03928?v/12.92:Math.pow((v+0.055)/1.055,2.4)};
    return 0.2126*f(c.r)+0.7152*f(c.g)+0.0722*f(c.b);};
  const ratio=(a,b)=>{const la=lum(a),lb=lum(b);
    return (Math.max(la,lb)+0.05)/(Math.min(la,lb)+0.05);};
  /* 衬底要从**元素自己**开始找（元素自身就可能是不透明背景）。
     第一版从 parentElement 开始，于是按钮的 accent 底色被跳过，
     把「白字在绿底上」算成「白字在纸色底上」，报出 1.05 的**假失败**——
     又一次「判据选错」。 */
  const ownSubstrate=(el)=>{const own=parse(getComputedStyle(el).backgroundColor);
    if(own&&own.a>=1)return own;
    let n=el.parentElement;
    while(n){const c=parse(getComputedStyle(n).backgroundColor);
      if(c&&c.a>=1)return c; n=n.parentElement;}
    return {r:255,g:255,b:255,a:1};};
  const big=(cs)=>{const fs=parseFloat(cs.fontSize);
    return fs>=18.66 || (fs>=14 && parseInt(cs.fontWeight,10)>=700);};
  /* **有效不透明度要沿祖先链乘积。** 只读元素自己的 opacity 是不够的：
     站点隐藏内容是给**父级 section** 加 opacity:0（滚动渐入），span 自己的
     opacity 仍然是 1。所以第一版那个「parseFloat(cs.opacity)<0.6」形同虚设 ——
     它照样会去量一个父级全透明、读者根本看不见的行，然后宣布"对比度达标"。
     这也是"条目页整页隐形却全项 PASS"能溜过去的原因之一。
     （注意：PROBE 本身是模板字符串，这段注释里不能出现反引号。） */
  const effOpacity=(el)=>{let o=1,n=el;const chain=[];
    while(n&&n.nodeType===1){const v=parseFloat(getComputedStyle(n).opacity);
      if(!isNaN(v))o*=v;
      if(o<0.05){chain.push(n.tagName.toLowerCase()+(n.id?'#'+n.id:'')+'@'+getComputedStyle(n).opacity);break;}
      n=n.parentElement;}
    return {o, chain};};
  const sel=['h1','h2','h3','p','.meta','.angle-note','.section-sub','.row-title','.row-desc',
             '.row-go','.badge','.chip','.ref','.cn','a','.nav-group-btn','.nav-menu-sub'];
  const out=[];
  let invisible=0;
  const invisibleSample=[];
  for(const s of sel){
    for(const el of [...document.querySelectorAll(s)].slice(0,6)){
      const cs=getComputedStyle(el);
      /* 自身可见性照查，但"看不见"现在按**有效**不透明度算 */
      const eo=effOpacity(el);
      if(cs.display==='none'||cs.visibility==='hidden'||eo.o<0.6){
        invisible++;
        if(invisibleSample.length<10) invisibleSample.push({sel:s,
          eff:Number(eo.o.toFixed(2)), display:cs.display, visibility:cs.visibility,
          /* 把"是谁在透明"记下来：没有这条，就只能看到"eff=0"而查不出原因。 */
          chain:eo.chain,
          text:(el.textContent||'').replace(/\\s+/g,' ').trim().slice(0,24)});
        continue;}
      const r=el.getBoundingClientRect();
      if(r.width<2||r.height<2) continue;
      const fg=parse(cs.color); if(!fg) continue;
      const sub=ownSubstrate(el);
      const comp=fg.a>=1?fg:over(fg,sub);
      const cr=Number(ratio(sub,comp).toFixed(2));
      const need=big(cs)?3:4.5;
      out.push({sel:s,tag:el.tagName.toLowerCase(),contrast:cr,need,
        fontSize:cs.fontSize,weight:cs.fontWeight,
        text:(el.textContent||'').replace(/\\s+/g,' ').trim().slice(0,24),
        pass: cr>=need || cr>=4.5});
    }
  }
  /* 把"因为看不见而没采样"的条数一并带出来：它是覆盖率的诚实度指标。
     滚动之后这个数应当接近 0；如果它很大，说明"全部达标"只覆盖了一部分页面。 */
  return {samples: out, invisible: invisible, invisibleSample: invisibleSample};})()`;

async function main() {
  const h = (p) => createHash('sha256').update(readFileSync(p)).digest('hex').slice(0, 12);
  const V = { classification: h(join(ROOT, 'classification.json')) };
  const dir = mkdtempSync(join(tmpdir(), 'kb-cc-'));
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
    const ws = new WebSocket(wsUrl);
    await new Promise((r, j) => { ws.addEventListener('open', r); ws.addEventListener('error', j); });
    const cdp = new (class {
      constructor(ws) {
        this.ws = ws; this.id = 0; this.pending = new Map(); this.handlers = new Map();
        ws.addEventListener('message', (ev) => {
          const m = JSON.parse(ev.data);
          if (m.id && this.pending.has(m.id)) {
            const { resolve, reject } = this.pending.get(m.id);
            this.pending.delete(m.id);
            m.error ? reject(new Error(m.error.message)) : resolve(m.result);
          } else if (m.method) (this.handlers.get(m.method) || []).forEach((fn) => fn(m.params, m.sessionId));
        });
      }
      send(method, params = {}, sessionId) {
        const id = ++this.id; const p = { id, method, params };
        if (sessionId) p.sessionId = sessionId;
        this.ws.send(JSON.stringify(p));
        return new Promise((res, rej) => this.pending.set(id, { resolve: res, reject: rej }));
      }
      on(m, f) { const l = this.handlers.get(m) || []; l.push(f); this.handlers.set(m, l); }
    })(ws);
    const { targetId } = await cdp.send('Target.createTarget', { url: 'about:blank' });
    const { sessionId } = await cdp.send('Target.attachToTarget', { targetId, flatten: true });
    await cdp.send('Runtime.enable', {}, sessionId);
    await cdp.send('Page.enable', {}, sessionId);
    const probe = async (e) => {
      const r = await cdp.send('Runtime.evaluate', { expression: e, returnByValue: true, awaitPromise: true }, sessionId);
      if (r.exceptionDetails) throw new Error((r.exceptionDetails.exception?.description || r.exceptionDetails.text));
      return r.result.value;
    };

    const all = [];
    let fails = 0;
    let invisibleTotal = 0;
    for (const theme of ['green', 'paper', 'dark']) {
      await cdp.send('Page.navigate', { url: BASE + 'web/index.html' }, sessionId);
      await sleep(800);
      await probe(`localStorage.setItem('sukh-theme', ${JSON.stringify(theme)}); true`);
      console.log(`\n=== 主题 ${theme} ===`);
      for (const p of PAGES) {
        await cdp.send('Page.navigate', { url: BASE + p }, sessionId);
        await sleep(1200);
        /* **先滚完全页再采样。** 站点的 section 是滚动渐入的（`body.reveal
           .reveal-pending { opacity: 0 }`），不滚就采样等于只量了首屏。
           滚两轮：①分步滚一遍，给懒加载的内容一个出现的机会；
           ②只要还有隐藏的 section/.grid，就逐个 scrollIntoView，最多 4 轮
           —— 因为 entry.html 的 #caseSection 会在案例分片载入后**被重建**，
           新一轮的 reveal-pending 需要新一次相交，一轮滚动可能刚好错过它
           （实测就是这个竞态让普查漏掉 7 个元素）。
           **不再滚回顶部再量**：测 computed style 与 rect 跟滚动位置无关，
           而 `scrollTo(0,0)` 会被页面里迟到的锚点滚动顶掉（实测停在 y≈680），
           反而把"没量到"伪装成"量过且达标"。 */
        const passInfo = await probe(`(async () => {
          const log = [];
          try {
            const step = Math.round(window.innerHeight * 0.7);
            const eff=(el)=>{let o=1,n=el;
              while(n&&n.nodeType===1){const v=parseFloat(getComputedStyle(n).opacity);
                if(!isNaN(v))o*=v; if(o<0.05)break; n=n.parentElement;}
              return o;};
            for (let y = 0; y < document.documentElement.scrollHeight; y += step) {
              window.scrollTo(0, y);
              await new Promise(r => setTimeout(r, 130));
            }
            for (let round = 1; round <= 4; round++) {
              const rest = [...document.querySelectorAll('section, .grid')]
                .filter(el => eff(el) < 0.5);
              log.push('r' + round + '=' + rest.length);
              if (!rest.length) break;
              for (const el of rest) { el.scrollIntoView({ block: 'center' });
                await new Promise(r => setTimeout(r, 250)); }
            }
            /* 等渐入过渡（.55s）走完，免得量到过渡中途更淡的颜色。 */
            await new Promise(r => setTimeout(r, 800));
            return { ok: true, log };
          } catch (e) { return { ok: false, log, err: String(e && e.message || e) }; }
        })()`);
        if (passInfo && !passInfo.ok) console.log('   [scroll pass 失败] ' + JSON.stringify(passInfo));
        const got = await probe(PROBE);
        const bad = got.samples.filter((x) => !x.pass);
        invisibleTotal += got.invisible;
        if (got.invisible) all.push({ theme, page: p, skippedInvisible: got.invisibleSample });
        for (const x of bad) {
          fails++;
          all.push({ theme, page: p, ...x });
          console.log(`  FAIL ${p} <${x.tag}> contrast=${x.contrast} need=${x.need} ` +
            `size=${x.fontSize}/${x.weight} "${x.text}"`);
        }
        console.log(`  ${bad.length ? '✗' : '✓'} ${p}：检查 ${got.samples.length} 处，` +
          `不达标 ${bad.length}，另有 ${got.invisible} 处因自身或祖先透明未采样`);
      }
    }
    writeFileSync(join(OUT, 'verify-contrast-census.json'),
      JSON.stringify({ dataVersion: V, fails, invisibleTotal, results: all }, null, 1), 'utf-8');
    console.log(`\n数据版本 ${V.classification}`);
    console.log(`总判定: ${fails === 0
      ? `三套主题 × 7 个页面，文本对比度全部达标（滚动后采样；因透明未采样 ${invisibleTotal} 处）`
      : `${fails} 处不达标（见 JSON）`}`);
    process.exitCode = fails === 0 ? 0 : 2;
  } finally { proc.kill(); }
}
main().catch((e) => { console.error('异常:', e.message); process.exitCode = 1; });

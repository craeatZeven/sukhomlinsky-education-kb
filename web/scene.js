/* 全站场景（2026-09-19 第六版）
   ------------------------------------------------------------
   为什么要有这个文件：风格原先只长在 body.page-home 上，另外 20 个页面还是旧的绿灰调，
   看起来像另一个站。现在藤蔓 + 花瓣铺满每一页（首页另有花束与花丛，HTML 里已有）。

   档案层 / 阅读层的底线不变：装饰只走页边与页脚之上，不压正文；reduced-motion 下全部让位。
   首页那套（花束视差、花丛分层）只有当页面里存在 .scene-hero / .scene-cluster 时才跑。 */
(function () {
  var doc = document;
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  var isHome = doc.body.classList.contains('page-home');

  var scene = doc.querySelector('.page-scene');
  if (!scene) {                                   /* 子页面：脚本自己把场景层搭出来 */
    scene = doc.createElement('div');
    scene.className = 'page-scene';
    scene.setAttribute('aria-hidden', 'true');
    scene.innerHTML = '<svg class="page-vine l" aria-hidden="true"></svg><svg class="page-vine r" aria-hidden="true"></svg>';
    doc.body.insertBefore(scene, doc.body.firstChild);
  }
  var layer = doc.getElementById('petalLayer');
  if (!layer) {
    layer = doc.createElement('div');
    layer.className = 'petal-layer';
    layer.id = 'petalLayer';
    layer.setAttribute('aria-hidden', 'true');
    doc.body.insertBefore(layer, scene.nextSibling);
  }

  var hero = doc.querySelector('.hero.cover');
  var art  = scene.querySelector('.scene-hero');
  var text = hero && hero.querySelector('.cv-text');

  /* ---------- 花瓣 ---------- */
  var SHAPES = [
    '<svg viewBox="0 0 24 34" xmlns="http://www.w3.org/2000/svg"><path d="M12 0C19 8 21 19 12 34 3 19 5 8 12 0Z" fill="#9C5A22" opacity=".85"/><path d="M12 5C13.4 13 13.8 22 12 29" stroke="#F0E3CA" stroke-width=".9" fill="none" opacity=".55"/></svg>',
    '<svg viewBox="0 0 30 22" xmlns="http://www.w3.org/2000/svg"><path d="M1 20C1 9 10 1 29 1 29 12 20 20 1 20Z" fill="#4C5A32" opacity=".8"/><path d="M3 18C10 13 18 7 27 3" stroke="#F0E3CA" stroke-width=".9" fill="none" opacity=".5"/></svg>',
    '<svg viewBox="0 0 28 28" xmlns="http://www.w3.org/2000/svg"><g fill="#B08428" opacity=".78"><ellipse cx="14" cy="6" rx="4" ry="6"/><ellipse cx="22" cy="14" rx="6" ry="4"/><ellipse cx="14" cy="22" rx="4" ry="6"/><ellipse cx="6" cy="14" rx="6" ry="4"/></g><circle cx="14" cy="14" r="3.4" fill="#9C5A22"/></svg>'
  ];
  var N = isHome ? 16 : 8;                        /* 内容页少一半：档案层要安静 */
  if (layer && !reduced.matches) {
    for (var i = 0; i < N; i++) {
      var el = doc.createElement('span');
      el.className = 'cv-petal';
      el.style.setProperty('--x', (Math.random() * 96 + 2).toFixed(2) + '%');
      el.style.setProperty('--dx', (Math.random() * 16 - 8).toFixed(1) + 'vw');
      el.style.setProperty('--s', (0.5 + Math.random() * 0.85).toFixed(2));
      el.style.setProperty('--d', (12 + Math.random() * 11).toFixed(1) + 's');
      el.style.setProperty('--delay', (-Math.random() * 20).toFixed(1) + 's');
      el.style.setProperty('--rot', Math.round(Math.random() * 760 - 380) + 'deg');
      el.innerHTML = SHAPES[i % SHAPES.length];
      layer.appendChild(el);
    }
  }

  /* ---------- 藤蔓：按整页高度程序生成 ---------- */
  var LEAF = 'M0,0 C9,-2 17,-11 15,-23 C2,-22 -6,-11 -4,1 Z';
  var RIB  = 'M0,0 C4,-6 8,-15 13,-20';
  var TEND = 'M2,-4 C14,-2 22,-10 20,-22 C19,-29 11,-30 8,-25 C6,-21 9,-18 13,-19 C16,-20 17,-23 16,-25';
  function buildVine(svg, W, H, phase) {
    if (!svg) return;
    svg.setAttribute('viewBox', '0 0 ' + W + ' ' + H);
    svg.setAttribute('width', W);
    svg.setAttribute('height', H);
    svg.style.height = H + 'px';
    var cx = W * 0.5, amp = W * 0.17, period = 720;
    var top = [], bot = [], y, c, k, t, w, out;
    for (y = 0; y <= H; y += 7) {
      c = cx + amp * Math.sin(2 * Math.PI * y / period + phase);
      t = (y % (period * 0.5)) / (period * 0.5);
      w = 1.7 + 3.3 * Math.sin(Math.PI * t);
      top.push((c - w).toFixed(1) + ',' + y);
      bot.push((c + w).toFixed(1) + ',' + y);
    }
    out = ['<path class="stem" d="M' + top.join('L') + 'L' + bot.reverse().join('L') + 'Z"/>'];
    k = 0;
    for (y = 150; y < H - 120; y += 210) {
      c = cx + amp * Math.sin(2 * Math.PI * y / period + phase);
      var slope = amp * (2 * Math.PI / period) * Math.cos(2 * Math.PI * y / period + phase);
      var ang = Math.atan(slope) * 180 / Math.PI;
      var dir = (k % 2 === 0) ? 1 : -1;
      var s = 0.85 + 0.4 * ((k % 3) / 2);
      out.push('<g transform="translate(' + c.toFixed(1) + ',' + y + ') rotate(' + (ang + dir * 36).toFixed(1) +
               ') scale(' + (dir * s).toFixed(2) + ',' + s.toFixed(2) + ')"><path class="leaf" d="' + LEAF +
               '"/><path class="rib" d="' + RIB + '"/></g>');
      if (k % 3 === 1) {
        out.push('<g transform="translate(' + c.toFixed(1) + ',' + (y + 96) + ') rotate(' +
                 (-ang - dir * 20).toFixed(1) + ') scale(' + (dir * 0.9).toFixed(2) + ',0.9)"><path class="stem" opacity=".8" d="' + TEND + '"/></g>');
      }
      if (k % 4 === 2) {
        out.push('<circle class="bud" cx="' + (c + dir * 13).toFixed(1) + '" cy="' + (y + 34) + '" r="4.8"/>');
      }
      k++;
    }
    svg.innerHTML = out.join('');
  }

  /* ---------- 视差：四层各走各的速率 ----------
     用户反馈："背景和文字的速度差还可以再强一些"。于是：
       正文 1.00 ｜ 花瓣层 1.00 + 滚动牵引 ｜ 花丛 0.22（外加缓慢放大）｜ 藤蔓 0.34
     藤蔓能拉到 0.34 是因为它是**程序生成的连续花纹**，往下拖多少都不会露空；
     花丛不行 —— 它被摆在玻璃面板底下，位移大了就从面板后面漂走，玻璃又没东西可透，
     所以它的"深度"主要靠**放大**而不是位移。 */
  var PAR = [
    [scene.querySelector('.page-vine.l'), 0.34],
    [scene.querySelector('.page-vine.r'), 0.34],
    [scene.querySelector('.scene-cluster.c1'), 0.22],
    [scene.querySelector('.scene-cluster.c2'), 0.22],
    [scene.querySelector('.scene-cluster.c3'), 0.22]
  ];
  var CLUSTERS = ['.scene-cluster.c1', '.scene-cluster.c2', '.scene-cluster.c3']
    .map(function (s) { return scene.querySelector(s); });
  var petals = layer;

  function layout() {
    var f = doc.querySelector('footer');
    var fh = (f && f.offsetHeight) || 0;
    var H = Math.max(doc.documentElement.scrollHeight - fh, 900);
    scene.style.height = (H + fh) + 'px';
    buildVine(scene.querySelector('.page-vine.l'), isHome ? 190 : 150, H, 0);
    buildVine(scene.querySelector('.page-vine.r'), isHome ? 190 : 150, H, Math.PI);
    if (art && hero) art.style.top = (hero.offsetTop + hero.offsetHeight / 2) + 'px';
  }

  var ticking = false;
  function frame() {
    ticking = false;
    if (reduced.matches) return;
    var s = window.scrollY;
    if (hero) {
      var p = Math.min(s, hero.offsetHeight) / (hero.offsetHeight || 1);
      if (text) {
        text.style.transform = 'translate3d(0,' + (-p * 92).toFixed(1) + 'px,0)';
        text.style.opacity = Math.max(0, 1 - p * 1.2).toFixed(3);
      }
      if (art) {
        art.style.transform = 'translate(-50%,-50%) translate3d(0,' + (p * 132).toFixed(1) +
                              'px,0) scale(' + (1 + p * 0.11).toFixed(3) + ')';
      }
    }
    for (var i = 0; i < PAR.length; i++) {
      if (PAR[i][0]) PAR[i][0].style.setProperty('--py', (s * PAR[i][1]).toFixed(1) + 'px');
    }
    for (var j = 0; j < CLUSTERS.length; j++) {
      if (CLUSTERS[j]) CLUSTERS[j].style.setProperty('--ps', (1 + s * 0.00008).toFixed(4));
    }
    /* 花瓣层随滚动被"带走"一点：空气也在动，飘落就不只是它自己的事 */
    if (petals) petals.style.transform = 'translate3d(0,' + (s * 0.07).toFixed(1) + 'px,0)';
  }

  var rt;
  window.addEventListener('resize', function () { clearTimeout(rt); rt = setTimeout(layout, 250); });
  /* 页高会变：搜索/浏览页的结果是异步灌进来的（实测 search.html 首屏藤蔓只到 900px，
     而整页 4544px）—— 正是"藤蔓短了"那个毛病。用 ResizeObserver 盯着 body 重算。
     场景层是 absolute，改它的高度不会反过来触发 observer，不会自激。 */
  if (window.ResizeObserver) {
    var lastH = 0;
    new ResizeObserver(function () {
      var h = doc.documentElement.scrollHeight;
      if (Math.abs(h - lastH) > 60) { lastH = h; clearTimeout(rt); rt = setTimeout(layout, 200); }
    }).observe(doc.body);
  }
  window.addEventListener('scroll', function () {
    if (!ticking) { ticking = true; requestAnimationFrame(frame); }
  }, { passive: true });
  if (doc.fonts && doc.fonts.ready) doc.fonts.ready.then(layout);
  layout();
  frame();
})();
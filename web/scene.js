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

  /* ---------- 子页面的花丛：数量跟页高走，不跟"三"走
     用户 2026-09-19：「美育和自然这些下面什么都没有了」。剂量实测（场景层开/关的
     平均像素差，只取左右边条）：
       首页   2.50 / 5.38 / 8.23 / 6.61                     —— 每屏都有
       专题页 1.39 / 5.00 / 1.38 / 1.37 / 4.82 / 3.88 / 1.35 / 2.08 / 3.45
              ↑ 峰在花丛处，谷 1.35 ≈ 只剩一条藤蔓
     两个根因，各修一处：
       ① **固定三丛 + 百分比布点**：同一个"三"，首页 3032px 里相隔 700px（不到一屏 = 密），
          专题页 7696px 里相隔 2300px（2.5 屏 = 空）。数量必须由页高决定。
       ② **位移式视差把花推走**：花丛原来跟藤蔓一样按 0.22 x scrollY 整体下移，
          滚到 5600 时花丛已经被推到 6900 —— 正好从你正在看的那一屏里消失。
          改成**相对视口中心的有界位移**：只有离视口中心 200px 内才让，越远越接近原位。 */
  var clusters = [];
  function makeCluster() {
    var cl = doc.createElement('div');
    cl.className = 'scene-cluster jc';
    var im = doc.createElement('img');
    im.src = 'motif.jpg'; im.width = 561; im.height = 720; im.alt = '';
    cl.appendChild(im);
    scene.appendChild(cl);
    clusters.push(cl);
    return cl;
  }

  var scene = doc.querySelector('.page-scene');
  if (!scene) {                                   /* 子页面：脚本自己把场景层搭出来 */
    scene = doc.createElement('div');
    scene.className = 'page-scene';
    scene.setAttribute('aria-hidden', 'true');
    scene.innerHTML = '<svg class="page-vine l" aria-hidden="true"></svg><svg class="page-vine r" aria-hidden="true"></svg>';
    /* 子页面也要有"可透之物"：玻璃后面没东西可透，玻璃就只是一块灰板
       （第四版实测：贴边时开关 backdrop-filter 只有 6.5% 的像素变）。
       这里给子页面也铺三丛花，位置由 CSS 定在正文面板附近。 */
    if (!isHome) {
      /* 先铺三丛占位，真正的数量在 layout() 里按页高算 */
      for (var ci = 1; ci <= 3; ci++) makeCluster();
    }
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
  /* 一朵五瓣小花，挂在藤上（藤蔓不能只有叶子和梗，会显得空） */
  function blossom(x, y, r, rot) {
    var p = ['<g class="blossom" transform="translate(' + x.toFixed(1) + ',' + y.toFixed(1) +
             ') rotate(' + rot.toFixed(1) + ')">'];
    for (var i = 0; i < 5; i++) {
      p.push('<ellipse cx="0" cy="' + (-r * 0.60).toFixed(1) + '" rx="' + (r * 0.33).toFixed(1) +
             '" ry="' + (r * 0.60).toFixed(1) + '" transform="rotate(' + (72 * i) + ')"/>');
    }
    p.push('<circle class="blossom-core" r="' + (r * 0.27).toFixed(1) + '"/></g>');
    return p.join('');
  }

  /* 藤蔓：按整页高度程序生成。
     2026-09-19 第二版 —— 用户：「藤蔓能不能做得更有质感一些」。原来只有一条等宽轮廓的带子，
     像铁丝。现在三层 + 两处细节：
       ① 淡墨：沿中心线画一条宽而虚的笔画（纸上的洇开）
       ② 主干：带呼吸宽度的轮廓带，两端用 linearGradient 淡入淡出（不再"突然开始/突然断掉"）
       ③ 叶：主叶 + 伴生小叶（一大一小才有层次），都带中脉
       ④ 花点：每四节挂一朵五瓣小花
     渐变用 currentColor，所以三套主题各自成立，不需要滤镜。 */
  function buildVine(svg, W, H, phase, uid) {
    if (!svg) return;
    svg.setAttribute('viewBox', '0 0 ' + W + ' ' + H);
    svg.setAttribute('width', W);
    svg.setAttribute('height', H);
    svg.style.height = H + 'px';
    var cx = W * 0.5, amp = W * 0.17, period = 720;
    var gid = 'vineGrad' + uid;
    var top = [], bot = [], mid = [], y, c, k, t, w;
    for (y = 0; y <= H; y += 7) {
      c = cx + amp * Math.sin(2 * Math.PI * y / period + phase);
      t = (y % (period * 0.5)) / (period * 0.5);
      w = 1.7 + 3.3 * Math.sin(Math.PI * t);
      top.push((c - w).toFixed(1) + ',' + y);
      bot.push((c + w).toFixed(1) + ',' + y);
      mid.push(c.toFixed(1) + ',' + y);
    }
    var ribbon = 'M' + top.join('L') + 'L' + bot.reverse().join('L') + 'Z';
    var centerline = 'M' + mid.join('L');
    var grad = '<defs><linearGradient id="' + gid + '" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="0" y2="' + H + '">' +
      '<stop offset="0" stop-color="currentColor" stop-opacity="0"/>' +
      '<stop offset="0.06" stop-color="currentColor" stop-opacity="1"/>' +
      '<stop offset="0.94" stop-color="currentColor" stop-opacity="1"/>' +
      '<stop offset="1" stop-color="currentColor" stop-opacity="0"/></linearGradient></defs>';
    var out = [grad,
      '<path class="stem-wash" d="' + centerline + '" fill="none" stroke="currentColor" stroke-width="' +
      (W * 0.085).toFixed(1) + '" stroke-linecap="round" stroke-opacity=".16"/>',
      '<path class="stem" style="fill:url(#' + gid + ')" d="' + ribbon + '"/>'];
    k = 0;
    for (y = 150; y < H - 120; y += 210) {
      c = cx + amp * Math.sin(2 * Math.PI * y / period + phase);
      var slope = amp * (2 * Math.PI / period) * Math.cos(2 * Math.PI * y / period + phase);
      var ang = Math.atan(slope) * 180 / Math.PI;
      var dir = (k % 2 === 0) ? 1 : -1;
      var s = 0.85 + 0.4 * ((k % 3) / 2);
      var fill = ' style="fill:url(#' + gid + ')"';
      out.push('<g transform="translate(' + c.toFixed(1) + ',' + y + ') rotate(' + (ang + dir * 36).toFixed(1) +
               ') scale(' + (dir * s).toFixed(2) + ',' + s.toFixed(2) + ')"><path class="leaf"' + fill +
               ' d="' + LEAF + '"/><path class="rib" d="' + RIB + '"/></g>');
      /* 伴生小叶：一大一小才有层次，单叶总像贴纸 */
      out.push('<g opacity=".8" transform="translate(' + c.toFixed(1) + ',' + (y + 30) + ') rotate(' +
               (ang + dir * 74).toFixed(1) + ') scale(' + (dir * s * 0.55).toFixed(2) + ',' + (s * 0.55).toFixed(2) +
               ')"><path class="leaf"' + fill + ' d="' + LEAF + '"/></g>');
      if (k % 3 === 1) {
        out.push('<g transform="translate(' + c.toFixed(1) + ',' + (y + 96) + ') rotate(' +
                 (-ang - dir * 20).toFixed(1) + ') scale(' + (dir * 0.9).toFixed(2) + ',0.9)"><path class="stem" d="' + TEND + '"/></g>');
      }
      if (k % 4 === 1) {
        out.push(blossom(c + dir * W * 0.30, y + 18, W * 0.062, dir * 18));
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
    [scene.querySelector('.page-vine.r'), 0.34]
  ];
  /* 首页的花丛仍是 HTML 里那三丛，用老办法（位移 + 放大）—— 实测每屏 2.5~8.2，不空。
     子页面的花丛由 layout() 按页高生成，视差走有界位移（见 frame）。 */
  var HOME_CLUSTERS = isHome ? ['.scene-cluster.c1', '.scene-cluster.c2', '.scene-cluster.c3']
    .map(function (s) { return scene.querySelector(s); }) : [];
  var petals = layer;

  /* 子页面：一丛花盖多少像素的页高。1150px 略大于一屏（900），保证每屏至少碰到一丛。 */
  var DENSITY = 1150, CLUSTER_H = 800;
  var placed = [];            /* 已定位的花丛：[元素, 版面中心(页坐标)] */

  function layoutClusters(H) {
    if (isHome) return;
    var n = Math.max(3, Math.min(12, Math.round(H / DENSITY)));
    while (clusters.length < n) makeCluster();
    placed = [];
    var seg = H / n;
    for (var i = 0; i < clusters.length; i++) {
      var el = clusters[i];
      if (i >= n) { el.style.display = 'none'; continue; }
      el.style.display = '';
      var onLeft = (i % 2 === 0);
      /* 段落中点再往上提半丛：花心压在正文面板附近，玻璃才有东西可透 */
      var top = i * seg + seg * 0.5 - CLUSTER_H * 0.5;
      el.style.top = Math.max(0, Math.round(top)) + 'px';
      el.style.left = onLeft ? '-15%' : 'auto';
      el.style.right = onLeft ? 'auto' : '-15%';
      el.style.setProperty('--xform', 'rotate(' + ((onLeft ? -7 : 6) + (i % 3) * 1.6).toFixed(1) +
                            'deg)' + (onLeft ? '' : ' scaleX(-1)'));
      placed.push([el, top + CLUSTER_H * 0.5]);
    }
  }

  function layout() {
    var f = doc.querySelector('footer');
    var fh = (f && f.offsetHeight) || 0;
    var H = Math.max(doc.documentElement.scrollHeight - fh, 900);
    scene.style.height = (H + fh) + 'px';
    buildVine(scene.querySelector('.page-vine.l'), isHome ? 190 : 150, H, 0, 1);
    buildVine(scene.querySelector('.page-vine.r'), isHome ? 190 : 150, H, Math.PI, 2);
    layoutClusters(H);
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
    /* 首页三丛：老办法（跟 scrollY 走 + 缓慢放大） */
    for (var j = 0; j < HOME_CLUSTERS.length; j++) {
      if (HOME_CLUSTERS[j]) HOME_CLUSTERS[j].style.setProperty('--ps', (1 + s * 0.00008).toFixed(4));
    }
    /* 子页面花丛：**相对视口中心的有界位移**。
       原来跟藤蔓一样按 0.22 x scrollY 整体下移，于是花从「正在看的那一屏」里被推走
       （实测：滚到 5600 时花丛已经在 6900，那一屏只剩藤蔓，剂量 1.35）。
       现在只在离视口中心 200px 内让位，越远越回到原位 —— 深度还在（近处约 0.78 倍速），
       但任何一屏的花都留在它该在的地方。放大也改成随距离，不再按 scrollY 一律涨到 1.6 倍。 */
    if (placed.length) {
      var vc = s + (window.innerHeight || 800) / 2, MAXD = 200, K = 0.22;
      for (var q = 0; q < placed.length; q++) {
        var d = (vc - placed[q][1]) * K;
        if (d > MAXD) d = MAXD; else if (d < -MAXD) d = -MAXD;
        placed[q][0].style.setProperty('--py', d.toFixed(1) + 'px');
        var near = (vc - placed[q][1]) / ((window.innerHeight || 800) * 1.5);
        if (near > 1) near = 1; else if (near < -1) near = -1;
        placed[q][0].style.setProperty('--ps', (1 + near * 0.05).toFixed(4));
      }
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
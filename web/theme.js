/* Shared theme switcher + scroll reveal */
(function () {
  var THEMES = [
    { id: "paper", label: "纸本", dot: "#9C5A22" },
    { id: "green", label: "森林", dot: "#2f6b4f" },
    { id: "dark", label: "夜读", dot: "#1c1917" }
  ];
  function currentTheme() {
    var saved = localStorage.getItem("sukh-theme");
    return saved && THEMES.some(function (t) { return t.id === saved; }) ? saved : "paper";
  }
  function applyTheme(id) {
    document.body.setAttribute("data-theme", id);
    localStorage.setItem("sukh-theme", id);
    var fab = document.getElementById("themeFab");
    if (fab) {
      var t = THEMES.find(function (x) { return x.id === id; });
      var label = fab.querySelector(".theme-label");
      if (label) label.textContent = "风格 · " + (t ? t.label : id);
      fab.querySelectorAll(".dot").forEach(function (dot, i) {
        dot.classList.toggle("active", THEMES[i].id === id);
      });
    }
  }
  function buildFab() {
    if (document.getElementById("themeFab")) return;
    var fab = document.createElement("button");
    fab.id = "themeFab";
    fab.setAttribute("aria-label", "切换风格");
    fab.innerHTML = THEMES.map(function (t) {
      return '<span class="dot" style="background:' + t.dot + '" title="' + t.label + '"></span>';
    }).join("") + '<span class="theme-label"></span>';
    fab.addEventListener("click", function () {
      var cur = currentTheme();
      var idx = THEMES.findIndex(function (t) { return t.id === cur; });
      var next = THEMES[(idx + 1) % THEMES.length].id;
      applyTheme(next);
    });
    /* 放进顶栏右侧（深 chrome 层）。
       **不放进 `.nav-groups`**：那个容器在窄屏是可横向滚动的（三组按钮在里面滚），
       把风格切换放进去会被一起滚走；而且它的宽度会把导航的可用空间挤到不够，
       导致标签折成两行（2026-09-13 实测 1280 下 10 个标签全部折行，那是平铺版；
       2026-09-14 改成三组下拉后同理，容器依旧不该放按钮）。 */
    var bar = document.querySelector(".topnav .inner");
    if (bar) {
      fab.className = "theme-nav";
      fab.title = "切换风格";
      bar.appendChild(fab);
    } else {
      fab.className = "theme-fab";
      document.body.appendChild(fab);
    }
    applyTheme(currentTheme());
  }
  function reveal() {
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    /* 不支持 IntersectionObserver 就**什么都不隐藏**（原来是把所有 target 标
       visible——那也对，但前提是先隐藏了；现在改成不隐藏，更省事也更快）。 */
    if (!("IntersectionObserver" in window)) return;
    document.body.classList.add("reveal");
    var SEL = "section, .grid";
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("visible"); io.unobserve(en.target); }
      });
    }, { threshold: 0.05, rootMargin: "0px 0px -30px 0px" });
    var watched = [];
    function watch(el) {
      if (watched.indexOf(el) >= 0) return;
      watched.push(el);
      /* 先挂牌再观察：只有挂了牌的元素才会被 CSS 隐藏。
         没挂上牌 = 内容可见，只是没有渐入。 */
      el.classList.add("reveal-pending");
      io.observe(el);
    }
    document.querySelectorAll(SEL).forEach(watch);
    /* 关键修复：条目页 / 分面页的分组 section 是**异步注入**的
       （DOMContentLoaded → await KB.ready() → innerHTML）。
       原来只在这里抓一次快照，注入的 section 永远进不了观察名单，
       于是永久停在 opacity:0 —— 整页 1926 字的正文对读者不存在，
       而所有几何/对比度检查都照过（元素在 DOM 里，只是看不见）。
       这里用 MutationObserver 把后加进来的 target 接上。 */
    if ("MutationObserver" in window) {
      new MutationObserver(function (muts) {
        muts.forEach(function (m) {
          Array.prototype.forEach.call(m.addedNodes, function (n) {
            if (!n || n.nodeType !== 1) return;
            if (n.matches && n.matches(SEL)) watch(n);
            if (n.querySelectorAll) Array.prototype.forEach.call(n.querySelectorAll(SEL), watch);
          });
        });
      }).observe(document.documentElement, { childList: true, subtree: true });
    }
    /* 兜底：**已经在视口里的元素立刻揭示**，不等 IntersectionObserver 回调。
       为什么需要：内容由 JS 异步注入时（首页的部分卡片、条目页的 section），
       IO 的首次回调可能在这一帧之前就已经"结算"过，于是个别块**永久停在
       opacity:0**——判据实测到过 1 块 155 字（"用起来"那张卡），重跑又变。
       reveal 只是装饰，**绝不能以内容不可见为代价**：宁可少一次渐入。
       同时监听一个短窗口内的滚动，覆盖"注入时还在视口外、随后被滚进来"的情形。 */
    function revealInView() {
      var vh = window.innerHeight || 800;
      watched.forEach(function (el) {
        if (el.classList.contains("visible")) return;
        var r = el.getBoundingClientRect();
        if (r.height === 0) return;
        if (r.top < vh && r.bottom > 0) el.classList.add("visible");
      });
    }
    [0, 120, 400, 1000, 2000].forEach(function (d) { setTimeout(revealInView, d); });
    window.addEventListener("scroll", revealInView, { passive: true });
  }
  function searchShortcut() {
    document.addEventListener("keydown", function (e) {
      if (e.key !== "/" || e.metaKey || e.ctrlKey || e.altKey) return;
      var tag = (document.activeElement && document.activeElement.tagName || "").toLowerCase();
      if (tag === "input" || tag === "textarea" || tag === "select") return;
      var box = document.getElementById("search") || document.getElementById("q");
      if (box) { e.preventDefault(); box.focus(); box.select && box.select(); }
    });
  }
  function readingProgress() {
    var bar = document.createElement("div");
    bar.className = "read-progress";
    var top = document.createElement("button");
    top.className = "back-top";
    top.type = "button";
    top.setAttribute("aria-label", "返回顶部");
    top.textContent = "↑";
    top.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
    document.body.appendChild(bar);
    document.body.appendChild(top);
    function update() {
      var max = document.documentElement.scrollHeight - window.innerHeight;
      var ratio = max > 0 ? (window.scrollY / max) : 0;
      bar.style.width = (Math.max(0, Math.min(1, ratio)) * 100) + "%";
      top.classList.toggle("show", window.scrollY > 400);
    }
    window.addEventListener("scroll", update, { passive: true });
    window.addEventListener("resize", update);
    update();
  }
  /* 顶栏三组下拉的开关（2026-09-14 导航重排）。
     桌面靠 CSS 的 :hover / :focus-within 也能开，这里主要给触屏与键盘用；
     两条路径都只是把菜单显示出来，不互相冲突。 */
  function navGroups() {
    var groups = Array.prototype.slice.call(
      document.querySelectorAll(".topnav .nav-group"));
    if (!groups.length) return;
    function closeAll(except) {
      groups.forEach(function (g) {
        if (g === except) return;
        g.classList.remove("open");
        var b = g.querySelector(".nav-group-btn");
        if (b) b.setAttribute("aria-expanded", "false");
      });
    }
    groups.forEach(function (g) {
      var btn = g.querySelector(".nav-group-btn");
      if (!btn) return;
      btn.addEventListener("click", function () {
        var open = !g.classList.contains("open");
        closeAll(g);
        g.classList.toggle("open", open);
        btn.setAttribute("aria-expanded", open ? "true" : "false");
      });
    });
    /* Esc 关、点空白关。点组按钮自己不关（它在 .nav-group 里面）。 */
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") closeAll(null);
    });
    document.addEventListener("click", function (e) {
      var t = e.target;
      if (t && t.closest && t.closest(".topnav .nav-group")) return;
      closeAll(null);
    });
  }
  document.addEventListener("DOMContentLoaded", function () {
    buildFab();
    reveal();
    navGroups();
    searchShortcut();
    readingProgress();
  });
})();

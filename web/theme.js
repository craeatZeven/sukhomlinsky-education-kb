/* Shared theme switcher + scroll reveal */
(function () {
  var THEMES = [
    { id: "paper", label: "纸本", dot: "#b4552d" },
    { id: "green", label: "森林", dot: "#2f6b4f" },
    { id: "dark", label: "夜读", dot: "#1c1917" }
  ];
  function currentTheme() {
    var saved = localStorage.getItem("sukh-theme");
    return saved && THEMES.some(function (t) { return t.id === saved; }) ? saved : "green";
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
    fab.className = "theme-fab";
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
    document.body.appendChild(fab);
    applyTheme(currentTheme());
  }
  function reveal() {
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    document.body.classList.add("reveal");
    var targets = document.querySelectorAll("section, .grid");
    if (!("IntersectionObserver" in window)) {
      targets.forEach(function (el) { el.classList.add("visible"); });
      return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("visible"); io.unobserve(en.target); }
      });
    }, { threshold: 0.05, rootMargin: "0px 0px -30px 0px" });
    targets.forEach(function (el) { io.observe(el); });
  }
  document.addEventListener("DOMContentLoaded", function () {
    buildFab();
    reveal();
  });
})();

/* kb.js — 苏霍姆林斯基教育知识库前端数据层（档位 A：按需分片加载）
 *
 * 设计要点：
 *   1) 首屏只取 meta.json（约 9 KB gzip），正文与全文检索语料一律按需加载；
 *   2) 所有数据文件走 data/ 目录，带 ?v=<meta.generated> 版本号，避免 Pages 缓存旧数据；
 *   3) 同一个请求只发一次（in-flight 去重 + 结果缓存）；
 *   4) 页面不再直接拼 innerHTML 里的原始文本——统一走 KB.esc()，避免
 *      ref 里的 `<!-- ... -->`、书名号引号等把 DOM 结构吃掉。
 *
 * 用法：
 *   KB.ready().then(meta => { ... })          // 书源 / 主题 / 计数
 *   KB.loadIndex().then(cards => { ... })     // 全库索引（含摘要，无正文）
 *   KB.loadIndexFor('zuo-ren-de-gu-shi-zh')   // 按来源的索引切片
 *   KB.loadCard('sk-0001')                    // 单卡全文
 *   KB.loadSearch('all' | '<source>')         // 全文检索语料（按需）
 */
(function () {
  "use strict";

  var DATA_BASE = "data/";
  var cache = new Map();
  var version = "";

  function getJSON(path) {
    var url = DATA_BASE + path + (version ? (path.indexOf("?") >= 0 ? "&" : "?") + version : "");
    if (cache.has(url)) return cache.get(url);
    var p = fetch(url, { cache: "default" }).then(function (r) {
      if (!r.ok) {
        var err = new Error("数据文件加载失败：" + path + "（HTTP " + r.status + "）");
        err.status = r.status;
        err.notFound = r.status === 404;
        throw err;
      }
      return r.json();
    }).catch(function (e) {
      cache.delete(url);   // 失败不缓存，允许重试
      throw e;
    });
    cache.set(url, p);
    return p;
  }

  var KB = {
    TYPE_LABELS: {
      quote: "quote 语录",
      case: "case 案例",
      principle: "principle 原则",
      method: "method 方法",
      practice: "practice 实践"
    },
    TAG_LABELS: {
      "OCR待校": "OCR 待校",
      "待纸本核": "待纸本核",
      "跨主题": "跨主题"
    },
    meta: null,
    version: "",

    /* ---------- 基础工具 ---------- */

    esc: function (value) {
      return String(value == null ? "" : value)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#39;");
    },

    /* ref 里夹着 OCR 标注的 HTML 注释（`<!-- ... -->`），直接注入会被浏览器吃掉。
       这里把它还原成可读文本。 */
    refText: function (ref) {
      return String(ref == null ? "" : ref)
        .replace(/<!--\s*/g, "")
        .replace(/\s*-->/g, "")
        .replace(/`/g, "")
        .replace(/\s{2,}/g, " ")
        .trim();
    },

    typeLabel: function (type) {
      return KB.TYPE_LABELS[type] || type || "";
    },

    sourceTitle: function (slug) {
      var list = (KB.meta && KB.meta.sources) || [];
      for (var i = 0; i < list.length; i++) if (list[i].slug === slug) return list[i].title;
      return slug;
    },

    topicTitle: function (slug) {
      var list = (KB.meta && KB.meta.topics) || [];
      for (var i = 0; i < list.length; i++) if (list[i].slug === slug) return list[i].title;
      return slug;
    },

    /* ---------- 加载器 ---------- */

    ready: function () {
      if (KB.meta) return Promise.resolve(KB.meta);
      return getJSON("meta.json").then(function (meta) {
        KB.meta = meta;
        KB.version = String(meta.generated || "");
        version = KB.version ? "v=" + KB.version : "";
        return meta;
      });
    },

    loadIndex: function () {
      return KB.ready().then(function () {
        return getJSON("index.json").then(function (data) { return data.cards || []; });
      });
    },

    loadIndexFor: function (slug) {
      return KB.ready().then(function () {
        return getJSON("index/" + encodeURIComponent(slug) + ".json")
          .then(function (data) { return data.cards || []; })
          .catch(function () { return []; });
      });
    },

    loadCard: function (id) {
      return KB.ready().then(function () {
        return getJSON("cards/" + encodeURIComponent(id) + ".json");
      });
    },

    loadSearch: function (scope) {
      return KB.ready().then(function () {
        return getJSON("search/" + encodeURIComponent(scope || "all") + ".json");
      });
    },

    loadIds: function () {
      return KB.ready().then(function () { return getJSON("ids.json"); });
    },

    loadLatest: function () {
      return KB.ready().then(function () {
        return getJSON("latest.json").then(function (data) { return data.cards || []; });
      });
    },

    loadTopicIndex: function (slug) {
      return KB.ready().then(function () {
        return getJSON("topic/" + encodeURIComponent(slug) + ".json")
          .then(function (data) { return data.cards || []; })
          .catch(function () { return []; });
      });
    },

    loadRandomCard: function () {
      return KB.loadIds().then(function (ids) {
        return KB.loadCard(ids[Math.floor(Math.random() * ids.length)]);
      });
    },

    /* ---------- 渲染辅助 ---------- */

    /* 索引条目 + 全文语料 → 可检索文本（小写） */
    searchText: function (card, corpusEntry) {
      var topics = (card.topics || []).map(KB.topicTitle).join(" ");
      var tags = [KB.typeLabel(card.type)].concat(card.tags || []).join(" ");
      return [
        card.id, card.title, card.cn, card.preview, KB.refText(card.ref),
        card.source, KB.sourceTitle(card.source), topics, tags,
        corpusEntry ? corpusEntry.text : ""
      ].join(" ").toLowerCase();
    },

    /* 列表卡片（索引数据即可渲染） */
    cardHTML: function (card, options) {
      options = options || {};
      var topicBadges = (card.topics || []).map(function (slug) {
        return '<a class="badge" style="margin-right:6px;text-decoration:none" href="explore.html?topic=' +
          encodeURIComponent(slug) + '">' + KB.esc(KB.topicTitle(slug)) + '</a>';
      }).join("");
      var extraTags = (card.tags || []).map(function (t) {
        return '<span class="meta" style="border:1px solid var(--line);border-radius:999px;padding:1px 8px;margin-left:6px">' +
          KB.esc(KB.TAG_LABELS[t] || t) + '</span>';
      }).join("");
      var excerptHtml = "";
      if (card.preview) {
        excerptHtml = '<p class="excerpt">“' + KB.esc(card.preview) + '”</p>';
      }
      if ((card.n || 0) > 1) {
        excerptHtml += '<p class="meta more-link" data-more="' + KB.esc(card.id) + '" ' +
          'style="cursor:pointer;color:var(--accent)">本卡另有 ' + (card.n - 1) + ' 段原文，展开 →</p>';
      } else if (card.trunc) {
        /* 摘要被截断时给出明确出口，避免用户以为是内容到此为止 */
        excerptHtml += '<p class="meta"><a href="card.html?id=' + encodeURIComponent(card.id) +
          '#' + KB.esc(card.id) + '" style="color:var(--accent)">读全文 →</a></p>';
      }
      return '\n  <article class="card" id="card-' + KB.esc(card.id) + '">\n' +
        '    <div class="card-top">\n' +
        '      <div>' + topicBadges + '</div>\n' +
        '      <span class="badge" style="background:transparent;border:1px solid var(--line);color:var(--soft)">' +
        KB.esc(KB.typeLabel(card.type)) + '</span>\n' +
        '    </div>\n' +
        '    <h3><a href="card.html?id=' + encodeURIComponent(card.id) + '#' + KB.esc(card.id) + '" style="color:inherit">' +
        KB.esc(card.title) + '</a></h3>\n' +
        excerptHtml + '\n' +
        (card.cn ? '    <p class="cn">' + KB.esc(card.cn) + '</p>\n' : '') +
        '    <div class="ref" style="margin-top:10px">' + KB.esc(card.id) + ' · ' +
        KB.esc(KB.sourceTitle(card.source)) + '<br>' + KB.esc(KB.refText(card.ref)) + '</div>\n' +
        (extraTags ? '    <div style="margin-top:8px">' + extraTags + '</div>\n' : '') +
        '  </article>';
    },

    /* 把「展开更多原文」绑到容器上（事件委托，只需绑一次） */
    bindMore: function (container) {
      if (!container || container.__kbMoreBound) return;
      container.__kbMoreBound = true;
      container.addEventListener("click", function (e) {
        var link = e.target.closest("[data-more]");
        if (!link) return;
        var id = link.getAttribute("data-more");
        var article = container.querySelector("#card-" + id);
        if (!article) return;
        link.textContent = "加载原文…";
        KB.loadCard(id).then(function (card) {
          var exps = card.excerpts || (card.excerpt ? [card.excerpt] : []);
          var html = exps.slice(1).map(function (q) {
            return '<p class="excerpt">“' + KB.esc(q) + '”</p>';
          }).join("");
          var box = document.createElement("div");
          box.className = "more-excerpts";
          box.innerHTML = html;
          article.insertBefore(box, link);
          link.remove();
        }).catch(function (err) {
          link.textContent = "加载失败，点此重试";
        });
      });
    }
  };

  window.KB = KB;
})();

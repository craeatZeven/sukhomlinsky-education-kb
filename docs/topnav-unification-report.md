# 顶栏统一 · 真实渲染验证报告

> **状态提示**：第 0–11 节是 **2026-09-13 第一轮（修复前）** 的记录，其中「第 6 节 1280 下 10 个标签全部折行」
> 是当时唯一的未通过项。该问题已由站点作者修复，**第 12 节是修复后的复验结论，以第 12 节为准**。
> 当前状态：**18/18 页 + 10/10 宽度档全部通过，折行与页面级横向滚动条均已消失。**

- 仓库：`D:\Git\sukhomlinsky-education-kb`
- 验证方式：CDP + headless Chrome（`--headless=new`），静态服务根 = 仓库根（`python -m http.server 8123`）
- 脚本：`local_working_copy/web-audit/verify-nav.mjs`（新写；未改动 `verify-fixes.mjs` / `verify-extra.mjs`）
- 结构化结果：`local_working_copy/web-audit/verify-nav.json`
- 运行日志：`local_working_copy/web-audit/verify-nav.log`
- 截图取证：`local_working_copy/web-audit/shots/nav-1280.png`、`nav-390.png`、`footer-1280.png`
- 页面清单：脚本用 `readdirSync('web')` 动态列出 **18** 个真实文件名，未写死
  （`card, cases, clusters, coverage, entries, entry, explore, facet, facets, guide, index, latest, problem, search, sources, stories, topic, topics`）
- 视口：桌面 **1280×900**、移动 **390×844**（`Emulation.setDeviceMetricsOverride`）
- 文中每个数字都是页面里读出来的值，没有"应该没问题"。

---

## 0. 结论一览

| 检查项 | 结果 |
|---|---|
| 顶栏 10 个链接（href + 文字 + 顺序） | **18/18 通过**（18 页只有 1 种写法） |
| 品牌文字 + href | **18/18 通过** |
| `active` / `aria-current` 映射 | **18/18 通过**（无多于 1 个 active） |
| 页脚 `footer .foot-links` 4 项 | **18/18 通过** |
| 页脚新 CSS 生效（marginBottom / underline） | **18/18 通过** |
| JS 错误（pageerror + console.error） | **18/18 通过**（pageerror=0，console.error=0） |
| 1280：`.nav-links` 不溢出、右边界不越界、`.inner` 高 60px | **18/18 通过** |
| 1280：**10 个标签各自单行** | **0/18 未通过** ← 唯一失败项，见第 6 节 |
| 390：页面不被撑破 + 顶栏单行 + `overflow-x:auto` | **18/18 通过** |

---

## 1. 顶栏 10 项：18/18 完全一致

每页按顺序读出 `.topnav .nav-links a`，18 页**全部**为下面这一串（`href | 文字`），顺序也对：

```
index.html      | 首页
entries.html    | 分类条目
facets.html     | 故事分面
explore.html    | 主题浏览
topics.html     | 教育专题
stories.html    | 541 篇故事
problem.html    | 问题检索
clusters.html   | 思想地图
sources.html    | 书源
search.html     | API 检索
```

- 每页 `a` 个数 = **10**（脚本按规格逐位比对 href 与文字，无一条 diff）
- 全库顶栏**不同写法只有 1 种**（`summary.distinctNavSets.length == 1`）——统一前那 5 种不一致已经消失
- **18/18 一致。**

> 补充事实（重要）：`.nav-links` 里实际有 **11** 个子元素，不是 10 个。
> `web/theme.js` 第 40–43 行会把风格切换按钮 `appendChild` 进 `.nav-links`：
> ```
> a + a + a + a + a + a + a + a + a + a + button#themeFab
> ```
> 18 页全部是这同一个结构。这不是本次改动引入的，但它占宽度，见第 6 节。

---

## 2. 品牌：18/18 通过

| 项 | 读到值 | 期望 | 结果 |
|---|---|---|---|
| `.topnav .brand` 文字 | `苏霍姆林斯基教育知识库` | 同 | 18/18 |
| `.topnav .brand` href | `index.html` | 同 | 18/18 |

实测样式：`font-size: 17px`，`white-space: nowrap`，宽度 **194.48px**。

---

## 3. `active` 映射逐页核对：18/18 通过

| 页面 | 期望 active | 实测 `.nav-link.active` href | active 个数 | 实测 `aria-current="page"` | 结果 |
|---|---|---|---|---|---|
| `card.html` | (无) | (无) | 0 | (无) | PASS |
| `cases.html` | (无) | (无) | 0 | (无) | PASS |
| `clusters.html` | `clusters.html` | `clusters.html` | 1 | `clusters.html` | PASS |
| `coverage.html` | (无) | (无) | 0 | (无) | PASS |
| `entries.html` | `entries.html` | `entries.html` | 1 | `entries.html` | PASS |
| `entry.html` | `entries.html`（详情页归父列表） | `entries.html` | 1 | `entries.html` | PASS |
| `explore.html` | `explore.html` | `explore.html` | 1 | `explore.html` | PASS |
| `facet.html` | `facets.html`（详情页归父列表） | `facets.html` | 1 | `facets.html` | PASS |
| `facets.html` | `facets.html` | `facets.html` | 1 | `facets.html` | PASS |
| `guide.html` | (无) | (无) | 0 | (无) | PASS |
| `index.html` | `index.html` | `index.html` | 1 | `index.html` | PASS |
| `latest.html` | (无) | (无) | 0 | (无) | PASS |
| `problem.html` | `problem.html` | `problem.html` | 1 | `problem.html` | PASS |
| `search.html` | `search.html` | `search.html` | 1 | `search.html` | PASS |
| `sources.html` | `sources.html` | `sources.html` | 1 | `sources.html` | PASS |
| `stories.html` | `stories.html` | `stories.html` | 1 | `stories.html` | PASS |
| `topic.html` | `topics.html`（详情页归父列表） | `topics.html` | 1 | `topics.html` | PASS |
| `topics.html` | `topics.html` | `topics.html` | 1 | `topics.html` | PASS |

- **没有任何一页出现多于 1 个 active。**
- `aria-current="page"` 与 `active` 同址，且每页恰好 0 或 1 个。
- 5 个"不在顶栏里"的页面（`card/cases/coverage/guide/latest`）实测 active = 0、`aria-current` = 0，符合要求。

---

## 4. 页脚 `footer .foot-links`：18/18 通过

每页都读到 4 个链接，顺序、文字、href 全对：

```
cases.html    | 案例 Review
coverage.html | 覆盖报告
guide.html    | 使用指南
latest.html   | 最近更新
```

结构（18 页一致）：`footer > div.wrap > p.foot-links` —— `p.foot-links` 在 `footer` 里不是"裸放的第一子元素"，
而是位于标准的 `.wrap` 容器内、且是 `footer` 的**第一行**，后面接着原有的 MIT / NOTICE / 数据源三行。
实测页脚文本顺序：`案例 Review · 覆盖报告 · 使用指南 · 最近更新 | 原创编排遵循 MIT License… | 数据源 INDEX.md · 自动生成 build_site.py`，
位置合理，没有出现"结构特殊导致位置怪"的页面。视觉见 `shots/footer-1280.png`。

---

## 5. JS 错误：pageerror 0、console.error 0（18/18 通过）

| 类别 | 合计 |
|---|---|
| `Runtime.exceptionThrown`（pageerror） | **0** |
| `Runtime.consoleAPICalled` type=error | **0** |
| `Log.entryAdded` level=error | 3 |
| `Network.loadingFailed` | 1 |

这 3 条 log error 全部**不属于 JS 错误**，逐条如下：

1. `GET /favicon.ico → 404`（只在 `card.html` 上被记到 1 次）
   - 仓库根与 `web/` 都**没有** favicon 文件，18 个页面也**都没写** `<link rel="icon">`；
   - 决定性验证：脚本另起一个**全新 Chrome（空 profile、无缓存）只打开 `index.html`**，同样出现这条 `/favicon.ico` 404
     （`summary.faviconProbe.favicon404 == true`）→ 这是浏览器对 origin 的默认请求，与加载哪一页无关，第一个加载的页面才会被记到。
   - **无害，缺 favicon 而已**，按要求不计入 `jsErrors` 失败。
2. `search.html` 的 2 条（同一次请求）：
   - `https://suk-kb-api.suk-kb.workers.dev/api/meta` 被 CORS 拦截（origin 是 `http://127.0.0.1:8123`）+ `net::ERR_FAILED`。
   - 这是**本地用 http.server 打开 API 检索页时访问线上 Worker 的跨域失败**，属于运行环境问题；页面没有抛 JS 异常（pageerror=0），其余检查全部通过。

> 更正一处：先前那句"`favicon.ico` 是唯一的 log error"只对 17 页成立；`search.html` 另有这 2 条 API 跨域 log error，一并如实列出。

---

## 6. 1280×900 排版测量（本节是最要紧的一节）

### 6.1 你给的两条硬判据：通过

18 页的**布局数字完全一致**（`innerContentWidth`、`boxWidth`、`boxScrollWidth/clientWidth`、`innerScrollWidth/clientWidth`、`rightBeyondContentPx`、`themeNavWidth` 等 14 个指标 distinct=1）：

| 指标 | 读到值 |
|---|---|
| `.inner` 内容区 | `left 64.5 → right 1200.5`，宽 **1136** |
| `.inner` 高度 | **60px**（CSS `height:60px`，18 页一致） |
| `.nav-links` 盒宽 | **923.52** |
| `.nav-links` 右边界 | **1200.5** |
| `.nav-links` `scrollWidth` / `clientWidth` | **924 / 924** → `scrollWidth <= clientWidth + 1` **成立** |
| `.nav-links` 右边界 vs `.inner` 右边界 | 1200.5 vs 1222.5 → **−22px（还余 22px）**，不越界 |
| `.nav-links` 右边界 vs `.inner` 内容右边界 | 1200.5 vs 1200.5 → 超出 **0px**（刚好贴住内容区右边） |
| `.inner` `scrollWidth` / `clientWidth` | 1180 / 1180 → `.inner` 自身无横向溢出 |
| 10 项 `offsetTop` | 只有 **1 个值**（`[-0.5]`）→ 10 个 flex 项在同一行，没有发生 flex 换行 |
| `gap` / `overflow-x` | `6px` / `visible` |
| `.nav-links` 内 `a` 个数 | **10** |

> 说明：`innerContentLeft/Right` 有两个取值（12 页为 `64.5→1200.5`，6 页为 `72→1208`），
> 差 7.5px 是**测量当刻页面有没有竖向滚动条**（body 宽 1265 vs 1280）造成的居中偏移；
> `.inner` 内容宽度恒为 1136，顶栏可用宽度因此**每页都是 923.52**，不影响本节任何结论。

### 6.2 但 1280 下 **10 个标签全部折成两行** —— 这是唯一未通过项

`scrollWidth <= clientWidth` 之所以成立，是因为 **flex 把标签压窄、文字自己折行**，从而"挤"进了容器，
并不是真的排得下。实测证据（18 页一致）：

| 证据 | 读到值 |
|---|---|
| 用 Range 数每个链接的**文字行盒个数** | `[2, 2, 2, 2, 2, 2, 2, 2, 2, 2]` → **10 个标签全是 2 行** |
| 每个链接的渲染高度 | **61px**（`= 2 × 24.5 行高 + 12 上下 padding`；单行应为 36.5px） |
| 顶栏实际高度 | **61px**（`.inner` 是 `height:60px`，即已竖向溢出 **1px**：`inner.scrollHeight 61 > clientHeight 60`） |
| 是否处于 flex 压缩态 | `shrinkMode = true`：子元素自然宽和 **906.36** 被压到当前 **853.52** |
| `.nav-links` 单行所需宽度（临时 `white-space:nowrap` 后读 `scrollWidth`） | **976px** |
| 同一时刻可给 `.nav-links` 的宽度 | **923.52px** |
| **差额** | **−52.48px（放不下）** |

视觉取证 `shots/nav-1280.png`（1280 顶栏，2× 缩放）实际渲染为：

```
首          分类条      故事分      主题浏      教育专      541 篇故     问题检      思想地      书         API 检       风格 · 森
页          目          面          览          题          事          索          图          源         索           林
```

即 `首页`、`分类条目`、`541 篇故事`、`API 检索`、甚至 theme.js 的 `风格 · 森林` 全部折行。

**机理**：`web/style.css` 只在 `@media (max-width:680px)` 里给 `.topnav .nav-link` 加了 `white-space: nowrap`
（第 90 行）；**桌面档没有 `nowrap`**，而 `.nav-links` 是 `display:flex` 且 `flex-wrap` 默认 `nowrap`，
于是宽度不够时 flex 把每个 `a` 压到 min-content，文字就在 `a` 内部折行——不产生滚动条，因此 `scrollWidth` 判据察觉不到。

### 6.3 差在哪：宽度账（可直接拿来决策）

| 组成 | 实测宽度 |
|---|---|
| 10 个链接**只有它们自己**（含 9 个 6px 间距） | **807.08px** |
| 加上 theme.js 注入的风格切换按钮 | flex 间距 6 + 按钮外框 **163.28**（按钮盒 153.28 + `margin-left:10px`） |
| **合计单行需要** | **976px** |
| 可用 | **923.52px** |
| **缺口** | **52.48px** |

逐项单行宽度（临时 nowrap 量到，非压缩值）：

| 标签 | 单行需要 | 当前被压成 |
|---|---|---|
| 首页 | 52.00 | 49.72 |
| 分类条目 | 80.00 | 75.45 |
| 故事分面 | 80.00 | 75.44 |
| 主题浏览 | 80.00 | 75.45 |
| 教育专题 | 80.00 | 75.44 |
| 541 篇故事 | 92.45 | 86.89 |
| 问题检索 | 80.00 | 75.44 |
| 思想地图 | 80.00 | 75.44 |
| 书源 | 52.00 | 49.72 |
| API 检索 | 76.63 | 72.34 |
| （风格切换按钮） | 153.28 | 142.19 |

**关键判断：你加的 10 个链接本身放得下（807.08 < 923.52，还余 116.44px）；
是 theme.js 塞进同一行的风格切换按钮（连间距共 169.28px）把整行顶爆了。**

### 6.4 诊断：改哪里能放下（只给数字，我没有动任何标签/链接/间距）

下表"省下"一列都是**由实测值推算**（实测 `gap=6px`、10 个间隙、链接数 10、按钮外框 163.28px），
不是直接量到的结果量；标注"未实测"的行是我没有实际改样式试过的，只作参考。

| 方案 | 省下（推算） | 结果 |
|---|---|---|
| `gap` 6px → 2px（10 个间隙 ×4px） | **40px**（实测 gap=6） | 仍差 **12.48px**，不够 |
| `gap` 6px → 0 | **60px** | **够了**，余 7.52px |
| `gap` 6px → 2px **且** 每链接左右 padding 各减 1px（12→11px，实测 padding 为 `12px / 12px`） | 40 + 20 = 60px | 够了 |
| 把风格切换按钮移出 `.nav-links`（回到 `.theme-fab` 胶囊，或挪到品牌一侧） | 169.28px | 10 个链接单独排，余 **116.44px**，最宽裕 |
| 品牌字号 17px → 15px | **未实测**（只作参考） | — |
| 放宽 `.inner` 的 `max-width` | — | 见下 |

**要让整行单行排开，`.inner` 的内容区至少要 1188.48px**（实测推算：品牌 194.48 + 间距 18 + 单行 need 976）；
当前是 **1136px**，差额 **52.48px**，与 6.2 节的缺口完全一致。
对应 `.inner` 的 border-box 要 ≥ **1232.48px**，即 `max-width` 需从 `1180px` 提到 **≥1232.5px**
（1280 视口带 15px 滚动条时 body 宽 1265px，1232.48 < 1265，**放得下**）——
但这会让顶栏比正文 `.wrap` 的 1180px 更宽，左右不再与正文对齐，属于设计取舍。

若把风格切换按钮移出顶栏，则只需 `.inner` 内容区 ≥ **1019.56px**（当前 1136px 已经够，余 116.44px）。

### 6.5 桌面宽度扫描（index.html，找真实临界点）

因为 `.inner` 的 `max-width:1180` 封顶，可用宽度在 viewport ≥1224 时恒为 923.52，
所以**折行不是某个宽度才出现，而是从 1440 一路到 681 全都在折**：

| viewport | `.inner` 内容宽 | `.nav-links` 盒宽 | 单行需要 | 越界 | 链接行数 | 折行 | 页面横滚 |
|---|---|---|---|---|---|---|---|
| 1440 | 1136 | 923.52 | 976 | 0 | 2 | **YES** | no |
| 1366 | 1136 | 923.52 | 976 | 0 | 2 | **YES** | no |
| **1280** | **1136** | **923.52** | **976** | **0** | **2** | **YES** | **no** |
| 1265 | 1136 | 923.52 | 976 | 0 | 2 | **YES** | no |
| 1240 | 1136 | 923.52 | 976 | 0 | 2 | **YES** | no |
| 1224 | 1136 | 923.52 | 976 | 0 | 2 | **YES** | no |
| 1200 | 1136 | 923.52 | 976 | 0 | 2 | **YES** | no |
| 1152 | 1093 | 880.52 | 976 | 0 | 2 | **YES** | no |
| 1100 | 1041 | 828.52 | 976 | 0 | 2 | **YES** | no |
| 1024 | 965 | 752.52 | 976 | 0 | 2 | **YES** | no |
| 900 | 841 | 628.52 | 976 | 0 | 4 | **YES** | no |
| 800 | 741 | 557.80 | 976 | +29.28 | 4 | **YES** | **YES** |
| 768 | 709 | 557.80 | 976 | +61.28 | 4 | **YES** | **YES** |
| 700 | 641 | 557.80 | 976 | +129.28 | 4 | **YES** | **YES** |
| 681 | 622 | 557.80 | 976 | +148.28 | 4 | **YES** | **YES** |
| 680 | 621 | 418.52 | 976 | 0 | **1** | no | no |

- **681–800px**：除折行外还出现**页面横向滚动条**（`.nav-links` 越界最多 148px）——这段是真正的"顶破页面"。
- **680px 及以下**：`@media (max-width:680px)` 的 `white-space:nowrap + overflow-x:auto` 生效，恢复单行、可横滑，正常。
- 结论：**坏掉的区间是 681px 及以上（无上界）**，1280 只是其中一个取样点。

---

## 7. 390×844 移动端：18/18 通过

按第 1 条要求的三项判据实测（18 页一致）：

| 判据 | 读到值 | 结果 |
|---|---|---|
| `document.documentElement.scrollWidth <= 391` | **390** | **PASS**（18/18） |
| 顶栏仍是一行（`offsetTop` 唯一） | `[10]`（唯一值） | **PASS**（18/18） |
| `.nav-links` 的 `overflow-x` | **`auto`** | **PASS**（18/18） |

其他实测值：`.nav-links` `scrollWidth 689` / `clientWidth 144`（内部横向滚动，**这正是 `style.css` 第 88 行的设计**：
`flex-wrap:nowrap; overflow-x:auto; scrollbar-width:none`），`.nav-links` 右边界 368 ≤ `.inner` 右边界 390，
移动端每链接高度 40px（`min-height:40px`）、**文字行数 `[1,1,1,1,1,1,1,1,1,1]`**（单行，不折行），主题按钮宽 65px。
视觉见 `shots/nav-390.png`（可见 `首页 分类条目 故事分面 …` 单行排列并在右缘处可滑动）。

> `.nav-links` 内部 `scrollWidth > clientWidth` 在窄屏是**设计如此**，已按此改判，不再计为失败。

---

## 8. 页脚新 CSS 是否真的命中：18/18 通过

`web/style.css` 里有两处 `footer` 规则（第 222 行"浅色页脚"、第 436 行"深 chrome 层"覆盖配色）。
实测 18 页计算值如下，两处规则**不冲突**，新加的次级入口规则正常生效：

| 读取项 | 读到值 | 来源/说明 |
|---|---|---|
| `footer .foot-links` 的 `marginBottom` | **`12px`** | 第 226 行 `margin: 0 0 12px`；第 436 行那条**没有**覆盖 margin，命中 |
| `footer .foot-links` 的 `marginTop` | `0px` | 同上 |
| `footer .foot-links a` 的 `textDecorationLine` | **`underline`** | 第 227 行 `text-decoration: underline` 命中（第 223 行 `footer a{text-decoration:none}` 被更高特异性覆盖） |
| `footer .foot-links a` 的 `color` | `rgb(238, 242, 236)` | `--chrome-ink`，来自第 440 行（后者确实覆盖了配色，且对比度更好） |
| `footer` 的 `color` | `rgb(167, 178, 170)` | `--chrome-soft`，第 436 行生效 |
| `footer` 的 `background` | `rgb(44, 53, 47)` | `--chrome`，第 436 行生效 |
| `footer` 的 `borderTop` | `0px none` | 第 437 行 `border-top:none` 覆盖了第 222 行的 `1px`（符合"深 chrome 层"的意图） |
| `footer` 的 `padding` / `marginTop` | `34px / 44px` / `70px` | 第 437 行生效 |

即：**配色由第 436/440 行（深 chrome 层）说了算，而 `.foot-links` 的间距与下划线由第 226/227 行说了算，二者互不干扰，都真实命中。**
`shots/footer-1280.png` 可见新入口行是页脚里最亮的一行（`--chrome-ink` + 下划线），层级正确。

---

## 9. 未通过项（如实列出）

**只有 1 项未通过：1280×900 下顶栏 10 个标签全部折成两行（18/18 页）。**

- 你给的两条字面判据（`.nav-links` 的 `scrollWidth <= clientWidth + 1`、右边界不超出 `.inner` 右边界）**都通过**；
- 但更强的"标签在自己那一行里"判据**不通过**——原因是 flex 压缩 + 文字自动折行把溢出"吸收"了，`scrollWidth` 看不出来；
- 实测缺口 **52.48px**（单行需要 976px vs 可用 923.52px），机理与宽度账见第 6 节；
- **我没有改动任何标签措辞、没有删链接、没有动 `gap`/`padding`** —— 按你的要求，这属于要你拍板的事。
  第 6.4 节给了几套方案的实测省量供你判断（`gap 6→2` 省 40px 仍差 12.48px；`gap→0` 或把风格切换按钮移出 `.nav-links` 才够）。

另外两项"非 JS 错误"的环境性提示（未计入失败，也未"修"，因为都不属于顶栏/页脚统一的范围）：
`/favicon.ico` 404（缺 favicon 文件，与页面无关）；`search.html` 访问线上 Worker API 的 CORS 失败。

---

## 10. 我改了什么 / 没改什么

**没有修改 `web/` 下任何文件**——`git status` 里 `web/*.html` + `web/style.css` 共 19 个文件的改动是你自己的顶栏统一工作
（`19 files changed, 125 insertions(+), 29 deletions(-)`），我一个字都没动，也没有 `git commit`。
`scripts/`、`classification.json`、`taxonomy.md` 全程未触碰。

**本次新增（均为验证产物）**：

| 文件 | 说明 |
|---|---|
| `local_working_copy/web-audit/verify-nav.mjs` | 新写的验证脚本（未改动 `verify-fixes.mjs` / `verify-extra.mjs`） |
| `local_working_copy/web-audit/verify-nav.json` | 结构化结果（含 18 页逐项 probe 原始值） |
| `local_working_copy/web-audit/verify-nav.log` | 本次完整运行日志 |
| `local_working_copy/web-audit/shots/nav-1280.png` | 1280 顶栏截图（折行取证） |
| `local_working_copy/web-audit/shots/nav-390.png` | 390 顶栏截图（单行 + 可横滑） |
| `local_working_copy/web-audit/shots/footer-1280.png` | 页脚次级入口截图 |
| `docs/topnav-unification-report.md` | 本报告 |

**没有发现需要当场修的小问题**：18 页顶栏/页脚结构逐页一致（1 种写法），没有"某页 footer 结构特殊"，
也没有"某页 active 漏标"（18 页 active 映射逐页核对全对）。因此没有产生对站点的修改。

---

## 11. 复现方式

```powershell
$env:PYTHONIOENCODING='utf-8'; $OutputEncoding=[Text.Encoding]::UTF8; [Console]::OutputEncoding=[Text.Encoding]::UTF8
cd D:\Git\sukhomlinsky-education-kb
# 静态服务根必须是仓库根（页面走 data/ 相对路径，且 ../docs 要可达）
D:\python\python.exe -m http.server 8123 --bind 127.0.0.1   # 后台起
node local_working_copy\web-audit\verify-nav.mjs            # 退出码 2 = 有未通过项
```

脚本行为：动态列出 `web/*.html` → 逐页起 target → 1280×900 读顶栏/品牌/active/页脚 + 量排版 →
切 390×844（mobile:true）再量 → 收 pageerror/console.error/Log/Network →
额外做「桌面宽度扫描（16 档）」「全新 Chrome 单独验证 favicon 404」「1280/390 顶栏与页脚截图」。
所有判定只依赖页面里读出的值。

---
---

# 12. 修复后复验（2026-09-13 第二轮）

站点作者针对第 6 节的折行 bug 改了三处（`web/style.css`、`web/theme.js`，**18 个 HTML 一个字没动**）：

1. `theme.js`：风格切换按钮从 `.nav-links` 移到 `.topnav .inner`（成为 `.nav-links` 的**兄弟**），并加 `title="切换风格"`。
2. `style.css`：`.theme-nav { flex: none }`；`.theme-nav .theme-label { display: none }` 从 ≤680px 提到**全局**。
3. `style.css`：`.topnav .nav-link { white-space: nowrap }` **全局**；
   `.topnav .nav-links` 加 `min-width: 0; overflow-x: auto; scrollbar-width: none`。

## 12.1 复验结论：全部通过

| 检查项 | 结果 |
|---|---|
| **★ 每个链接文字行数 = 1**（1280，Range 数行盒） | **18/18 通过**，行数 `[1,1,1,1,1,1,1,1,1,1]` |
| **★ 链接高度**（单行应 ≈36.5px） | 18/18 页全部 **36.5px**（修复前是 61px） |
| **★ `.inner` 无竖向溢出** | `scrollHeight 60 <= clientHeight 60`，竖向溢出 **0**；`.inner` 实际高 **60px** |
| **★ 顶栏整行仍是一行** | 10 个 `offsetTop` 只有 1 个值 `[11.75]` |
| **★ 10 档宽度扫描** | **10/10 通过**：无折行、无页面级横向滚动条（详见 12.3） |
| 顶栏 10 项 + 顺序 | 18/18（全库仍只有 1 种写法） |
| 品牌 | 18/18 |
| `active` / `aria-current` 映射 | 18/18（无多于 1 个 active） |
| 页脚 `foot-links` 4 项 + 样式 | 18/18 |
| `.theme-nav` 落位 | 18/18（是 `.inner` 直接子元素、与 `.nav-links` 平级、不在其内部） |
| JS 错误 | 18/18（pageerror=0、console.error=0） |

`.nav-links` 的子元素从 `a×10 + button#themeFab` 变成 **`a×10`**；
`.inner` 的子元素为 **`a.brand + div.nav-links + button#themeFab.theme-nav`**（18 页一致）。

## 12.2 1280 的宽度账：现在真的放得下

| 项 | 修复前 | 修复后 |
|---|---|---|
| `.nav-links` 单行需要 | 976px（含风格按钮） | **807.08px**（只剩 10 个链接） |
| 可给 `.nav-links` 的宽度 | 923.52px（含按钮） | **826.52px** |
| **余量** | **−52.48px（不够）** | **+19.44px（够）** |
| `.theme-nav` 盒宽 | 153.28px（含「风格 · 森林」那行字） | **69px**（只剩 3 个圆点） |
| `.theme-nav` 的 `flex` | — | `0 0 auto`（`flex:none` 生效，不被压缩） |
| `.theme-label` 的 `display` | 桌面为 `inline`（文字占宽） | **`none`**（全局隐藏） |
| 是否处于 flex 压缩态 | `inShrinkMode = true`（906.36 → 853.52） | **`false`**（当前和 = nowrap 和 = 753.08） |

逐项单行宽（10 个链接合计 **753.08px**，加 9 个 6px 间距 = **807.08px**）：
首页 52 · 分类条目 80 · 故事分面 80 · 主题浏览 80 · 教育专题 80 · 541 篇故事 92.45 ·
问题检索 80 · 思想地图 80 · 书源 52 · API 检索 76.63。

`.theme-nav` 的 69px = 12px 左 padding + 1px 左边框 + 3 个圆点 36px + 2 个 8px 间隙 16px + 4px 右 padding。
连同它 10px 的 `margin-left` 与 18px 的 flex 间距，风格切换区共占 97px；`807.08 + 97 = 904.08`，
而 `.inner` 内容区 1136 − 品牌 194.48 − 两个 18px 间距 = 923.52 → **余 19.44px**，与实测一致。

生效的 computed 值（1280，18 页一致）：`.nav-link` 的 `white-space: nowrap`、
`.nav-links` 的 `flex-wrap: nowrap`、`overflow-x: auto`、`min-width: 0px`。

## 12.3 10 档宽度扫描（index.html）

判据：**不折行（行数全为 1）+ 页面无横向滚动条 + `.inner` 无竖向溢出**；
`.nav-links` 内部横向滚动按你的要求**允许**，单独统计，不与"折行"混算。

| 视口 | 10 个链接行数 | 链接高 | `.inner` 高 / 竖向溢出 | `docScrollWidth / clientWidth` | 页面横滚 | `.nav-links` 内部滚动 | 余量 | 判定 |
|---|---|---|---|---|---|---|---|---|
| 1440 | `[1,1,1,1,1,1,1,1,1,1]` | 36.5 | 60 / 0 | 1425 / 1425 | no | 0 | +19.44 | **FITS** |
| **1280** | `[1,1,1,1,1,1,1,1,1,1]` | 36.5 | 60 / 0 | 1265 / 1265 | no | 0 | +19.44 | **FITS** |
| 1200 | `[1,1,1,1,1,1,1,1,1,1]` | 36.5 | 60 / 0 | 1185 / 1185 | no | 0 | +19.44 | **FITS** |
| 1100 | `[1,1,1,1,1,1,1,1,1,1]` | 36.5 | 60 / 0 | 1085 / 1085 | no | 75px | −75.56 | NAV-INTERNAL-SCROLL（可接受） |
| 1024 | `[1,1,1,1,1,1,1,1,1,1]` | 36.5 | 60 / 0 | 1009 / 1009 | no | 151px | −151.56 | NAV-INTERNAL-SCROLL（可接受） |
| 900 | `[1,1,1,1,1,1,1,1,1,1]` | 36.5 | 60 / 0 | 885 / 885 | no | 275px | −275.56 | NAV-INTERNAL-SCROLL（可接受） |
| 800 | `[1,1,1,1,1,1,1,1,1,1]` | 36.5 | 60 / 0 | 785 / 785 | no | 375px | −375.56 | NAV-INTERNAL-SCROLL（可接受） |
| 700 | `[1,1,1,1,1,1,1,1,1,1]` | 36.5 | 60 / 0 | 685 / 685 | no | 475px | −475.56 | NAV-INTERNAL-SCROLL（可接受） |
| 680 | `[1,1,1,1,1,1,1,1,1,1]` | 40 | 60 / 0 | 665 / 665 | no | 276px | −276.26 | NAV-INTERNAL-SCROLL（可接受） |
| 390 (M) | `[1,1,1,1,1,1,1,1,1,1]` | 40 | 60 / 0 | 390 / 390 | no | 551px | −551.26 | NAV-INTERNAL-SCROLL（可接受） |

- **出现折行的档位：无。**（修复前 681–1440 每一档都在折行）
- **出现页面级横向滚动条的档位：无。**（修复前 681/700/768/800 四档会撑破页面，最糟越界 148px）
- 需要 `.nav-links` 内部滚动的档位（**可接受**）：1100 / 1024 / 900 / 800 / 700 / 680 / 390
- 未通过的档位：**无（10/10 通过）**

**上一轮发现的「681–800px 出现页面级横向滚动条」坏区间已消失。**
现在窄桌面档的表现是：标签**保持单行**、溢出被收进 `.nav-links` 内部横向滚动（`overflow-x: auto`，滚动条隐藏），
页面本身不产生横向滚动条。截图 `shots/nav-760-fixed.png`（760px）可以看到标签仍是单行、
右侧主题圆点仍在，导航区在内部滚动。

**两种状态的区分**（本轮严格分开统计，不混算）：

| 状态 | 含义 | 本轮出现 | 判定 |
|---|---|---|---|
| 折行（WRAPPED） | 标签文字在 `.nav-link` 内部换成两行（高 61px） | **无** | 坏 |
| 页面横滚（PAGE-SCROLL） | `documentElement.scrollWidth > clientWidth`，整个页面出现横向滚动条 | **无** | 坏 |
| 容器内滚动（NAV-INTERNAL-SCROLL） | `.nav-links` 的 `scrollWidth > clientWidth`，溢出收在导航容器里，标签仍单行 | 7 档 | 可接受 |

## 12.4 1280 的其他实测值（与第一轮一致，未回退）

| 指标 | 读到值 |
|---|---|
| `.nav-links` 右边界 vs `.inner` 内容右边界 | 1103.5 → **超出 −97px**（第一轮是 0px，现在更宽松） |
| `.nav-links` 右边界 vs `.inner` 右边界 | 1103.5 vs 1222.5 → **−119px** |
| `.nav-links` `scrollWidth / clientWidth` | **807 / 807**（无内部滚动） |
| `.inner` `scrollWidth / clientWidth` | 1180 / 1180（无横向溢出） |
| 页面横滚 | `false` |
| `.nav-links` 盒宽 | **807.08px**（正好等于 10 个链接的单行需要） |

## 12.5 390×844 移动端（复跑）

| 判据 | 读到值 | 结果 |
|---|---|---|
| 页面无横向滚动条 | `docScrollWidth 390 / clientWidth 390` | **PASS** |
| 顶栏单行 | `offsetTop = [10]`（唯一） | **PASS** |
| `.nav-links` 的 `overflow-x` | `auto` | **PASS** |
| 标签行数 | `[1,1,1,1,1,1,1,1,1,1]`（单行） | **PASS** |
| `.inner` 竖向溢出 | 0（高 60px） | **PASS** |
| 内部滚动 | 551px（允许） | 可接受 |

## 12.6 JS 错误与 favicon（复跑，无新增）

`pageerror = 0`、`console.error = 0`（18/18 通过）。`Log.entryAdded` 共 3 条：
1 条 `/favicon.ico` 404（origin 级浏览器默认请求，用全新 Chrome 复现，与页面无关）；
2 条 `search.html` 访问线上 Worker API 的 CORS + `ERR_FAILED`（本地起服务访问线上接口的环境问题）。
**改 theme.js / style.css 没有引入任何新的 JS 异常。**

## 12.7 修复前后的对比小结

| | 修复前 | 修复后 |
|---|---|---|
| 1280 标签行数 | `[2,2,2,2,2,2,2,2,2,2]`（全折行） | **`[1,1,1,1,1,1,1,1,1,1]`** |
| 1280 链接高 | 61px | **36.5px** |
| `.inner` 竖向溢出 | 1px（61 > 60） | **0** |
| 1280 宽度余量 | −52.48px | **+19.44px** |
| 681–800px 页面横滚 | 有（最糟越界 148px） | **无** |
| 折行的宽度档 | 1440→681 全部 | **无** |
| 通过页数 | 0/18 | **18/18** |

## 12.8 本轮产物

| 文件 | 说明 |
|---|---|
| `local_working_copy/web-audit/verify-nav.mjs` | 已按新判据改写（Range 数行盒 + 10 档扫描 + 折行/内部滚动分状态） |
| `local_working_copy/web-audit/verify-nav.json` | 本轮结构化结果（`summary.round = fix-followup`） |
| `local_working_copy/web-audit/verify-nav.log` | 本轮完整日志（退出码 0） |
| `local_working_copy/web-audit/shots/nav-1280-fixed.png` | 1280 顶栏：10 个标签单行 |
| `local_working_copy/web-audit/shots/nav-900-fixed.png` | 900px：单行 + 内部滚动 |
| `local_working_copy/web-audit/shots/nav-760-fixed.png` | 760px（原坏区间）：单行 + 内部滚动，页面不横滚 |
| `local_working_copy/web-audit/shots/nav-390-fixed.png` | 390px 移动端 |
| `local_working_copy/web-audit/shots/footer-1280-fixed.png` | 页脚次级入口（未受影响） |

复验命令同第 11 节；本轮退出码为 **0**（无未通过项）。

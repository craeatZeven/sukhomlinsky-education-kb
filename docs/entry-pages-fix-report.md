# 条目页 / 分面页收尾修正报告（2026-09-11）

> 范围：`web/entry.html`、`web/facets.html`、`web/facet.html`、`web/index.html`、`web/search.html`、`web/entries.html`（附带）、`web/kb.js`（注释）。
> 未改动：`scripts/build_shards.py`、`scripts/build_site.py`、`classification.json`、`taxonomy.md`；未 `git commit`。
> 所有计数一律从 `web/data/` 现读，页面上没有一个写死的数字。

## 〇、中途的需求变更（第 2 项做了两遍）

第 2 项（facets/facet 页）先按「标记已算出但未过复核门槛」写了一版并验证通过；
随后收到通知：分面标记改走逐卡判读、复核已达标（分面级微平均 F1 83.0% / 83.1%，门槛 80%；「是否有标记」一致 100%），
`facets_ready` 已变 `true`、`facets_blocked_reason` 字段已删除、分片已带卡片清单。
**于是第 2 项按「分面已就绪、可用」重写并重新验证**（本报告记录的是最终版）。
`facets_blocked_reason` 现在页面里没有任何引用（grep 为空）。
旧说法「待补」「未过门槛」在 `web/` 下已全部清零（grep 为空）。仍保留一段**过渡态兜底**文案
（`!meta.facets_ready` 或分片 `cards` 为空时才会出现），措辞只说"数据分片里还没有卡片清单"，
不涉及门槛，正常上线状态下不会渲染——目的只是数据分片没跟上时不致于显示空白。

## 一、改了哪几处（前后对比）

### 1. `web/entry.html` —— 复分标签 A18 真正列出卡片

| 位置 | 改前 | 改后 |
|---|---|---|
| 统计块（`info.tag` 分支） | 只有一句 `<span class="meta">复分标签 · 不参与主归属分区</span>`，**不给张数** | `<div class="stat"><b>${cards.length}</b><span>带此标记的卡</span></div>` + 原说明句 |
| 区小标题 | 固定 `<h2 class="section-title">主归属</h2>` | 加 `id="primaryTitle"`；A18 时文案为 **「带此标记的卡」**，普通条目仍是「主归属」 |
| `#primarySub` 说明 | 「A18 是复分标签：它本身不持卡片，主归属仍按每张卡的内容定。」 | 「…只给「谈这类孩子」的卡加标记——每张卡的主归属仍按内容定。下面列出的 **69** 张就是带此标记的卡，每行末尾标出的是那张卡自己的主归属。」（69 由 `cards.length` 算出） |
| 卡片列表 | `paged("cardList", …)`，但当时 `cards` 是空数组→列表空 | 数据层已带 69 张，现在**真的渲染**：首屏 40 行 + 「加载更多卡片」→ 69 行 |
| 空列表兜底 | 「该条目暂无主归属卡片。」 | A18 时「暂无带此标记的卡片。」；普通条目不变 |
| 同角度区（附带） | A18 无 layer（`关照` 不在 5 个角度里）→ 空副标题 + 「该角度下暂无其他条目」 | A18 时说明「关照是复分标签，不属于五个观察角度（宗旨 / 立场 / …），所以没有"同角度的其他条目"」 |
| CSV 导出的 `part` 列（附带） | 一律 `主归属` | A18 时 `带此标记` |

### 2. `web/facets.html`（最终版 = 可用状态）

| 位置 | 改前 | 改后 |
|---|---|---|
| 统计格 | `待补 / 分面标记` | `已就绪 / 分面标记`；另加 `<b>2242</b>分面标记（可多选）`（由 `meta.facets` 求和得出） |
| 顶部提示块 `#pending` | 「分面标记待补，暂不可用…数字全为 0 是因为"还没算"」 | **已就绪时整块为空**（`#pending` 内容为 `""`） |
| 分组说明 | `5 个分面（张数待补）` | `5 个分面 · 共 937 个分面标记（一张故事可落进多个分面）` |
| 每个分面卡片 | `分面标记待补` | `301 张故事 →`（真实计数） |

### 3. `web/facet.html`（最终版 = 列出该分面下的故事卡）

| 位置 | 改前 | 改后 |
|---|---|---|
| 统计格 | `—` / `待补` | `301 带此标记的故事`、`301 本页可列出的卡片`、字段格不变 |
| 列表 | 无卡片列表（`cards` 空）；无分页按钮 | 新增 `<div class="load-wrap"><button id="loadMore" class="chip">加载更多故事卡</button></div>` 与 entry.html 同款的 `paged()`（PAGE_SIZE=40），走 `KB.cardRowHTML()` 档案版式行 |
| 列表说明 | 「结构已就位：标记算出来后…」 | 「共 301 张带「自然与季节」标记的故事卡，按档案版式列出（整行可点，进卡片详情）。」 |
| 计数来源 | `facet.count`（当时分片里是占位的 0） | 取 `meta.facets` 的 `count`，回落到分片 `facet.count`；两处都是数据，不写死 |
| 已就绪判定 | `facet.ready` | `meta.facets_ready || facet.ready`（任一说可用即可用） |

### 4. `web/index.html` 第 83 行

```diff
-<span class="row-desc">故事体卡片不走条目归属：角色 / 场景 / 事件或情绪三个字段、十七个分面（分面标记待补）</span>
+<span class="row-desc">故事体卡片不走条目归属：角色 / 场景 / 事件或情绪三个字段、十七个分面（可点入看该分面下的故事）</span>
```

### 5. `web/search.html` 坏顶栏（bug 修复，只改这一处顶栏）

`<header class="site-header">`（该类名在 `style.css` 里根本不存在 → 顶栏裸奔）替换为现行 `<nav class="topnav">` 结构，
照 `index.html` 顶栏抄（类名 `topnav / inner / brand / nav-links / nav-link` 完全一致），
把 `API 检索` 标为 `active`。**未动其余 11 个页面的顶栏。**

顺带核实：同页 `<footer class="site-footer">` 的类名同样不存在，但 `style.css:222` 有裸 `footer {}` 规则，
页脚渲染正常，所以**没动**（不在本次范围）。

### 6. 附带（不改就是错的旧假设）

- `web/entries.html` A18 区：行尾 `被参见 0 →` → **`带此标记 69 张 →`**；并删掉整段陈旧说明
  （原文写「这个标记的卡片清单还没算出来…`classification.json` 没有标记字段…这里不显示张数、也不列出卡片」——现在已经不成立）。
  这一处不在用户列的 4 件事里，但验证清单第 2 条要求 entries.html 的 A18 区显示 69，所以一并修了。
- `web/kb.js`：仅更新两处**注释**（`loadFacet` 的说明由「标记未算出」改为「计数 + 该分面下的故事卡」），无逻辑改动。

## 二、渲染验证的真实结果

环境：`python -m http.server 8123`（**在仓库根 `D:\Git\sukhomlinsky-education-kb` 启动**——
页面用 `data/` 相对路径，且 `../docs/*.md` 要能落到 `/docs/`；试过 `http://127.0.0.1:8123/web/entry.html` 与
`/docs/facet-labeling-plan.md` 都是 HTTP 200）+ headless Chrome via CDP。
脚本：`local_working_copy/web-audit/verify-fixes.mjs`（复用仓库里现成的 web-audit CDP 骨架 `audit.mjs`）、
`local_working_copy/web-audit/verify-extra.mjs`（翻页 + 截图）。日志：`verify-fixes.log` / `verify-extra.log` / `verify-fixes.json`。

静态服务仍开着（后台任务），可以人工复核：
`http://127.0.0.1:8123/web/entry.html?code=A18`、`…/web/facets.html`、`…/web/facet.html?code=S6`、
`…/web/entry.html?code=A11`、`…/web/entries.html`、`…/web/search.html`。

### 1. `python scripts\validate_all.py` → `ALL OK`（exit 0）

```
=== check_kb.py ===   === audit_cards.py ===   === coverage_report.py ===
=== coverage_volumes.py ===   === build_site.py ===   === build_shards.py ===
ALL OK
EXIT=0
```
（重建后 `web/data/` 与重建前 sha256 一致——两次跑都得到 `c4a634b7…` meta.json / `f213774f…` A18.json，
说明 `build_shards.py` 是幂等的，我的页面改动不会被重建覆盖。）

### 2. CDP 渲染：6/6 PASS

```
PASS  entry-A18 列出带标记的卡   [web/entry.html?code=A18]  ready=true
  stats: "69带此标记的卡 复分标签 · 不参与主归属分区"
  title: "带此标记的卡"
  sub:   "A18 学习困难学生 是复分标签：它本身不持卡片，只给「谈这类孩子」的卡加标记—— 每张卡的主归属仍按内容定。下面列出的 69 张就是带此标记的卡，每行末尾标出的是那张卡自己的主归属。"
  rows: 40,  firstIds: ["sk-0001","sk-0002","sk-0003"],  has_sk0001: true,  bodyHas69: true

PASS  entry-A11 主归属 59 / 参见 27   [web/entry.html?code=A11]
  stats: "59主归属卡 27被参见 内容与方法所属角度"
  title: "主归属",  mainRows: 40,  crossRows: 27

PASS  entries 的 A18 区显示 69   [web/entries.html]
  rowText: "A18 学习困难学生 … 带此标记 69 张 →"
  stats:   "5观察角度 | 23条目 | 713有主归属的卡 | 416交叉参见"
  stillSaysNotComputed: false

PASS  facets 显示真实计数、无「待补」   [web/facets.html]
  stats: "3字段 17分面 673故事体卡片 2242分面标记（可多选） 已就绪分面标记"
  S6: "S6 场景 自然与季节 301 张故事 →"     S1: "…250 张故事 →"
  S4: "…207 张故事 →"                       S2: "…120 张故事 →"
  S11: "…113 张故事 →"                      group0: "5 个分面 · 共 937 个分面标记（一张故事可落进多个分面）"
  pending: ""   saysDaibu: false   saysBlocked: false   has301: true   zeroCountCards: 0

PASS  facet-S6 计数 + 列出真实故事卡   [web/facet.html?code=S6]
  stats: "场景字段 301带此标记的故事 301本页可列出的卡片"
  listSub: "共 301 张带「自然与季节」标记的故事卡，按档案版式列出（整行可点，进卡片详情）。"
  rows: 40, firstIds: ["sk-0022","sk-0068","sk-0076"], loadMore: "inline-block"
  第一行文字: "…光脚、户外与不怕淋雨：三四年级不再有人生病 case 案例 把心献给孩子… sk-0022 故事体 · 走故事分面"

PASS  search 顶栏有样式（topnav）   [web/search.html]
  nav: present, legacy(.site-header): 0
  background: rgb(44, 53, 47)   position: sticky   height: 61px   .inner: display flex / 60px
  brandColor: rgb(238, 242, 236)
  links: 首页 / 教育专题 / 主题浏览 / 541 篇故事 / 问题检索 / 思想地图 / 案例 Review / 书源 / API 检索
  activeLink: "API 检索"

==== 6/6 PASS ====   EXIT=0     （6 项均无 pageerror / console error）
```

### 3. 补充验证（翻页到位 + 截图取证）

```
A18 加载更多: {"before":40,"btnVisible":"inline-block","after":69,"btnAfter":"none",
               "uniqueIds":69,"cardsWhosePrimaryIsA18":0}
  最后一张卡行: "…practice 实践 … 287 张卡片 sk-1350 主归属 · A9 集体与同伴 ／ 参见 A5 尊严、爱与信任 读全文 →"
首页故事分面行: "故事分面 故事体卡片不走条目归属：角色 / 场景 / 事件或情绪三个字段、十七个分面（可点入看该分面下的故事） 看分面 →"
facet-S6 翻页: {"before":40,"afterAllClicks":301}
  最后一行: "…case 案例 … sk-1391 故事体 · 走故事分面 读全文 →"
search 顶栏: 滚动 600px 后 topnav 的 top = 0（真吸顶）
截图: local_working_copy/web-audit/shots/fix-entry-A18-1440.png、fix-facet-S6-1440.png、fix-index-1440.png、fix-search-1440.png
```

- A18 的 69 张**全部可达**（唯一 id 数 69，点了「加载更多」后按钮自动消失）；
  这 69 行里**没有任何一张卡的主归属是 A18**（`cardsWhosePrimaryIsA18: 0`），与「复分标签不持主归属」一致。
- S6 的 301 张全部翻得出来（唯一 id 数 301）。
- 人工看图确认：`fix-search-1440.png` 是深色 chrome 顶栏 + 9 个链接（`API 检索` 带下划线高亮）；
  `fix-entry-A18-1440.png` 顶部统计为「69 带此标记的卡」，小标题「带此标记的卡」，下面是真实卡片行；
  `fix-facet-S6-1440.png` 三个统计格为「场景 / 301 带此标记的故事 / 301 本页可列出的卡片」，下方是真实故事卡。

### 4. 文本层 grep（均为空 = 无残留）

```
Select-String -Path web\*.html,web\*.js -Pattern '待补|未过门槛|未通过独立复核|facets_blocked_reason|还没算|site-header'
→ （无输出）
```

### 5. `docs/facet-labeling-plan.md` 链接是否死链

`docs/deployment.md` 记录 Pages 的实际配置是 **Branch `master` / Path `/`（仓库根）**，
站点地址 `https://craeatzeven.github.io/sukhomlinsky-education-kb/`，网页在 `/web/` 下——
所以 `../docs/facet-labeling-plan.md` 在 Pages 上落在 `/docs/…`，**文件存在，不是死链**
（该页脚注原本就有这个链接，本次沿用；本地 `http://127.0.0.1:8123/docs/facet-labeling-plan.md` 也是 HTTP 200）。
注意 `docs/deployment.md` §注意事项 已说明：Pages 上 `.md` 是当源文件/纯文本提供，不是渲染后的页面。

## 三、没做到 / 需要你知道的

1. **`web/data/facet/<CODE>.json` 的 `count` 字段**：重建前它一直是我读到的占位 `0`（`meta.facets` 里才是真数），
   所以 `facet.html` 的计数我改成从 `meta.facets` 取、回落到分片 `count`。你这次重建后分片 `count` 已是真数
   （`S6: {"count": 301, "ready": true}`，301 张卡）——**两条路现在都通**，不用再改页面。
2. **过渡态兜底文案**：`facets.html` / `facet.html` 各留了一段"分片里还没有卡片清单"的兜底，
   只在 `facets_ready=false` 或 `cards` 为空时渲染；正常状态下 `#pending` 是空的（验证里 `pending: ""`）。
   如果你认为连这段都该删掉，说一声我就删。
3. **`search.html` 顶栏的链接集**：照 `index.html` 抄了 9 项（含 `教育专题`、`思想地图`、`案例 Review`、`书源`），
   因此该页顶栏里**不再有**原来的「覆盖」「指南」两个链接（这两页仍可从首页进入）。
   若你希望保留，我可以把它们加回这 9 项里——但那样就不再与其它页面一致了。
4. **其余 11 个页面的顶栏没动**（按要求「不要顺手统一」）；`docs/entry-pages-report.md` 里记着的 `site-header` 是审计报告的正文描述，不是代码。
5. **移动端断点只做了逻辑兜底、没逐档截图**：截图与计算样式都在 1440 宽；`style.css` 的 ≤680px 规则我没改。
6. **没有 `git commit`**（按要求）；改动都在工作区，`git status` 里可见。
7. 我**没有**改动 `scripts/build_shards.py`、`scripts/build_site.py`、`classification.json`、`taxonomy.md`；
   页面上的每个计数（69 / 301 / 2242 / 937 / 673 …）都是渲染时从 `web/data/` 现读的。

# 条目页与分面页交付报告

> 2026-09-11。构建层 + 前端数据层 + 页面三部分的新增与改动。
> 所有数字均由脚本从 `classification.json` / `taxonomy.md` 现算，页面不写死任何计数。

---

## 一、结论速览

**做完的**

1. `scripts/build_shards.py` 新增 `entry` / `layer` / `facet` 三个分片目录，`meta.json` 新增 `entries` / `layers` / `facets` / `facets_ready` / `classification` 五块；
2. `scripts/build_site.py` 的 `web/data.json` 快照带上分类字段与 `taxonomy` 块；
3. `card_index_entry()` / `card_full_entry()` 增加 `primary` / `seealso` / `primary_name` / `seealso_names`；`related` 改为优先按新分类计算，旧 topics 只作兜底；
4. `web/kb.js` 新增 `loadEntry()` / `loadLayer()` / `loadFacet()` / `entryBadge()` / `entryBadges()` / `entryText()` / `cardMetaText()`，`cardRowHTML()` 与 `cardHTML()` 的旧 topics 位置换成条目归属；
5. 新增 4 个页面 `web/entries.html` / `entry.html` / `facets.html` / `facet.html`，改写 `web/card.html` 详情页的条目归属块，`web/index.html`「看结构」新增两个入口；
6. `python scripts/validate_all.py` → **`ALL OK`**（本文件末尾附关键输出）。

**先说没做到的**（详见 §七）

- **分面标记仍未算出**：按规格填 `count: 0` + `facets_ready: false`，页面如实显示「分面标记待补，暂不可用」，没有伪造任何分面数据。
- **A18 复分标签的卡片清单拿不到**：`classification.json` 里没有标记字段（`seealso` 里从未出现 A18），所以条目页只出现 A18 这一条、张数为 0，并按规格「不编造」处理。规格 §五.3 要求的「列出全部被打标卡片」的入口**本期做不到**，需要先补标记数据。
- **你给的基准数字（718/668）与当前仓库不一致**：现在是 **713/673**（`seealso` 仍是 416 条 / 399 张卡 / 跨角度 245 条）。差异原因与并发改写风险见 §七.3。
- 其余页面顶部导航**没有动**（已做审计，见 §六.3），是否统一请你定。

---

## 二、新增 / 修改文件清单

| 文件 | 类型 | 说明 |
|---|---|---|
| `scripts/build_shards.py` | 修改 | 读 `classification.json` + `taxonomy.md`；新增 `Taxonomy` 汇总类、`clean_rule()`、`load_classification()`；`card_index_entry()` / `card_full_entry()` 带分类字段；`build_related()` 改写；写 `entry/` `layer/` `facet/` 分片 |
| `scripts/build_site.py` | 修改 | 快照每张卡带 `primary` / `seealso` / `primary_name` / `seealso_names`；新增顶层 `taxonomy` 块（23 条目 + 5 角度 + 17 分面 + `facets_ready`）；sitemap 增加 entries/facets/entry 页 |
| `web/kb.js` | 修改 | 新增 3 个加载器 + 4 个渲染/查询辅助；`cardRowHTML()` / `cardHTML()` 换掉旧 topics；`searchText()` 增加条目名 |
| `web/style.css` | 修改 | 只加 4 组类：`.badge--entry` / `.badge--see`、`.entry-attr`、`.angle-note`、`.pending-note`、`.row-entry`（沿用既有变量与尺寸，不引入新视觉语言） |
| `web/entries.html` | 新增 | 23 条目总览，按 5 个角度分组 + 复分标签单列；每个角度可展开浏览该角度全部主归属卡（点开才加载 `layer/<n>.json`） |
| `web/entry.html` | 新增 | 条目页：收录口径 + 主归属区 + **交叉参见区**（每张标出它自己的主归属）+ 同角度其他条目 + 故事体说明 |
| `web/facets.html` | 新增 | 3 字段 × 17 分面总览，显式声明分面标记待补 |
| `web/facet.html` | 新增 | 单个分面页：结构就位、内容区如实为空并说明原因 |
| `web/card.html` | 修改 | 详情页首屏徽章与 `keyfacts` 换成「这一条属于 / 还涉及哪些条目」（均可点）；相关卡片改显示主归属 |
| `web/index.html` | 修改 | 「看结构」组新增「分类条目」「故事分面」两行（原有三行与其相对顺序未动） |
| `web/latest.html` | 修改 | 目录行的元信息由旧主题名换成条目归属（旧主题不再是主信息） |
| `web/search.html` | 修改 | 同上（该页的旧主题筛选器保留） |
| `docs/entry-pages-report.md` | 新增 | 本文件 |

生成物（由 `scripts/build_shards.py` / `build_site.py` 重写，不算源码改动）：`web/data/meta.json`、`index.json`、`index/*`、`topic/*`、`entry/*`（新）、`layer/*`（新）、`facet/*`（新）、`cards/*`、`search/*`、`ids.json`、`latest.json`、`web/data.json`、`web/sitemap.xml`。

未 `git commit`（按要求）。

---

## 三、数据层实现

### 3.1 规格解析：`layer` 字段不是空的

先回答你点名要确认的那件事：**`scripts/taxonomy.py` 的 `e['layer']` 是解析得出来的，不需要猜。**
`taxonomy.md` §二 的表格本来就是 7 列（编号 / 名称 / **角度** / 判定用关键词 / 弱证据关键词 / 收录 / 不收录），`load_spec()` 把第 3 列填进了 `layer`。实测 23 条全部有值：

```
A1..A4,A19 → 宗旨    A5,A6,A21 → 立场    A8,A9,A10 → 教育关系与组织
A7,A11..A15,A17,A22,A23 → 内容与方法    A16,A20 → 衡量    A18 → 关照（e['tag'] is True）
```

**一处与你的描述不符，需要你知道**：`taxonomy.md` §一（五个观察角度）那张表**实际有 6 行**，第 6 行是「关照 / 面向哪一类具体孩子（复分标签…）/ 1」。我按「只有复分标签条目的层不算观察角度」把它剔除，所以 `meta.layers` 是 **5 项**（宗旨 / 立场 / 教育关系与组织 / 内容与方法 / 衡量，`layer/1.json`…`5.json`），A18 在 `entries` 里带 `tag: true` 单独出现，不出现在任何 `layers[].entries` 里。这与你要求的「5 项」一致，但 §一 原文是 6 行——如果以后新增条目落到「关照」，剔除逻辑仍然成立。

### 3.2 `meta.json` 新增五块

| 块 | 形状 | 说明 |
|---|---|---|
| `entries` | 23 项 `{code,name,layer,rule,count,cross,tag}` | `rule` = §二 该行「收录」列原文；`count` = 主归属卡数；`cross` = 被参见次数；A18 `count: 0`、`tag: true` |
| `layers` | 5 项 `{index,name,question,count,entries}` | `question` 取自 §一 |
| `facets` | 17 项 `{code,name,field,count}` | `count` 一律 **0**（未算出，不伪造） |
| `facets_ready` | `false` | 页面据此如实说明 |
| `classification` | `{source,total,assigned,story,seealso,seealso_cards,cross_layer}` | 现算的核对数字，写进数据而不是写死在页面 |

**角度汇总（现算）**

| # | 角度 | 回答的问题 | 条目数 | 主归属卡 | 被参见 |
|---|---|---|---|---|---|
| 1 | 宗旨 | 教育要把孩子培养成什么样的人？ | 5 | 213 | 157 |
| 2 | 立场 | 怎么看待儿童、怎么对待儿童？ | 3 | 82 | 57 |
| 3 | 教育关系与组织 | 教育在什么关系里发生、由谁承担？ | 3 | 116 | 54 |
| 4 | 内容与方法 | 教什么、怎么教？ | 9 | 268 | 128 |
| 5 | 衡量 | 怎么反馈、怎么评价？ | 2 | 34 | 20 |

**23 条目（主归属卡 / 被参见）**

| 条目 | 名称 | 角度 | count | cross |
|---|---|---|---|---|
| A1 | 全面发展与个性 | 宗旨 | 32 | 16 |
| A2 | 公民与祖国 | 宗旨 | 41 | 24 |
| A3 | 幸福与精神生活 | 宗旨 | 14 | 9 |
| A4 | 自我教育 | 宗旨 | 40 | 47 |
| A5 | 尊严、爱与信任 | 立场 | 55 | 27 |
| A6 | 了解儿童 | 立场 | 14 | 21 |
| A7 | 健康与作息 | 内容与方法 | 30 | 6 |
| A8 | 家庭与母亲 | 教育关系与组织 | 36 | 33 |
| A9 | 集体与同伴 | 教育关系与组织 | 32 | 14 |
| A10 | 教师 | 教育关系与组织 | 48 | 7 |
| A11 | 劳动与创造 | 内容与方法 | 59 | 27 |
| A12 | 自然与思维课 | 内容与方法 | 18 | 5 |
| A13 | 阅读与书籍 | 内容与方法 | 28 | 15 |
| A14 | 美与艺术 | 内容与方法 | 27 | 10 |
| A15 | 思维与智力 | 内容与方法 | 59 | 38 |
| A16 | 评价与分数 | 衡量 | 26 | 11 |
| A17 | 习惯与纪律 | 内容与方法 | 4 | 4 |
| A18 | 学习困难学生 | 关照（复分标签） | 0 | 0 |
| A19 | 道德判断与品德培养 | 宗旨 | 86 | 61 |
| A20 | 检查知识与考查 | 衡量 | 8 | 9 |
| A21 | 儿童发展与年龄阶段 | 立场 | 13 | 9 |
| A22 | 教学方法与教育艺术 | 内容与方法 | 31 | 16 |
| A23 | 学习方法与学习技能 | 内容与方法 | 12 | 7 |

（主归属合计 713；被参见合计 416。）

### 3.3 新分片

| 路径 | 内容 |
|---|---|
| `web/data/entry/<CODE>.json` | `{code,name,layer,rule,count,cards,cross}`。`cards` = 主归属卡索引条目；`cross` = 把该条目标为 seealso 的卡索引条目，每项额外带 `cross_from`（那张卡自己的主归属 code）与 `cross_from_name` |
| `web/data/layer/<n>.json` | `{index,name,question,count,entries,cards}`，`entries` 是该角度下 23 条目中的那几条（含 count/cross），`cards` 是该角度全部主归属卡 |
| `web/data/facet/<CODE>.json` | `{code,name,field,count:0,cards:[],ready:false}`（17 个） |

体积：`entry/*` 23 个文件合计 1,036,519 raw / 291,285 gzip；`layer/*` 5 个合计 635,774 / 170,052；`facet/*` 17 个合计 1,526 / 1,773。

### 3.4 索引与详情字段

`card_index_entry()` 与 `card_full_entry()` 都增加：`primary`（故事体为 `null`）、`seealso`、`primary_name`、`seealso_names`。名字直接进数据，前端不必再查表。

### 3.5 `related`（相关卡片）

改为**优先按新分类**，打分（我定的权重，规格未定，见 §七.7）：

```
+2  与本站同一 primary（两边都有 primary）
+2  它自己的 primary 出现在本卡的 seealso 里
+2  本卡的 primary 出现在它的 seealso 里
+1  两边 seealso 集合每重叠一个 code
按 (-分数, id) 排序取 6 张；不足 6 张才用旧 topics 共现补齐。
```

`related` 项现在带 `primary` / `primary_name`（`topics` 保留，供旧页面兜底）。

---

## 四、体积变化（raw / gzip）

“改动前”是本次会话开始时（改动尚未落地）在真实文件上测得的字节数。

| 文件 | 改动前 raw | 改动前 gzip | 改动后 raw | 改动后 gzip | raw 变化 | gzip 变化 |
|---|---|---|---|---|---|---|
| `web/data/meta.json` | 23,402 | 9,307 | **30,166** | **11,495** | +6,764（+28.9%） | +2,188（+23.5%） |
| `web/data/index.json` | 1,091,311 | 307,929 | **1,204,441** | **317,699** | +113,130（+10.4%） | +9,770（+3.2%） |
| `web/data.json`（快照） | 3,527,165 | 784,234 | **3,715,503** | **802,858** | +188,338（+5.3%） | +18,624（+2.4%） |
| `web/sitemap.xml` | 160,124 | — | 162,725 | — | +2,601 | — |

`index.json` 的增量做了**归因核对**：用同一份 `cards/` 分别生成「无分类字段」和「带分类字段」的索引，得到 1,091,311 / 307,929 → 1,204,441 / 317,699，**差值恰好等于上表的变化**，即 `index.json` 的 +113,130 raw / +9,770 gzip 全部来自 `primary/seealso/primary_name/seealso_names` 四个字段，与卡片正文变化无关。gzip 只涨 3.2%（名字重复度高，压缩率好），这个代价可以接受。

`meta.json` 从 9.3 KB 涨到 11.5 KB gzip，仍属首屏无压力范围；条目/角度/分面的全部元数据都在里面，`entries.html` 只靠一份 meta 就能渲染完整总览。

---

## 五、前端

### 5.1 `web/kb.js` 新增

| 名称 | 作用 |
|---|---|
| `loadEntry(code)` | 取 `data/entry/<CODE>.json` |
| `loadLayer(n)` | 取 `data/layer/<n>.json` |
| `loadFacet(code)` | 取 `data/facet/<CODE>.json` |
| `entryInfo(code)` / `entryName(code)` / `layerInfo(name)` / `tagEntries()` | 从 `meta` 里查条目、角度、复分标签，不额外发请求 |
| `entryBadge(code, opts)` | 可点条目徽章 → `entry.html?code=A11`，默认文案「A11 劳动与创造 · 59 张」，`opts.cross` 补「被参见 27」，`opts.kind='see'` 用虚线样式；`title` 属性给全量（主归属 N 张 · 被参见 M 张） |
| `entryBadges(card)` | 一张卡的主归属 + 全部参见，都是可点链接；无主归属的故事卡给「故事体 · 走故事分面 → facets.html」 |
| `entryText(card)` | 目录行用纯文字（整行已被 `<a>` 包住，不能再嵌链接）：「主归属 · A11 劳动与创造 ／ 参见 A4 自我教育、A19 道德判断与品德培养」 |
| `cardMetaText(card)` | 有新分类用新分类，没有（例如后端 API 的旧载荷只有 topics）才回落旧 topics |

`cardRowHTML()` 的元信息行末位由「旧主题名」换成 `entryText()`；`cardHTML()` 的标签区由 `topicBadge()` 换成 `entryBadges()`。`topicBadge()` 与 `KB.topicTitle()` **一行未删**（`explore.html`、`topic.html`、`coverage.html` 等旧页面仍在用），旧主题筛选与专题页全部照常工作。

`searchText()` 额外把条目编号与条目名拼进可检索文本——换分类不该让「劳动教育」这类旧词搜不到；旧 topics 仍然保留在检索文本里。

### 5.2 页面

- **`entries.html`**：按 5 个角度分组，每组给出「角度问题 + 该角度条目数 + 主归属卡数」，每条列「编号 名称 / 收录口径 / 主归属 N 张 · 被参见 M」。每组下面有个折叠块「按这个角度看全部 N 张卡」，**点开才加载** `layer/<n>.json`，一屏 20 张、可续加载（`loadLayer()` 的实际使用点）。A18 单独一个「复分标签（不参与主归属）」区，并如实说明它的标记清单还没算出来。
- **`entry.html?code=A11`**：顶部条目名 / 所属角度 / 收录口径 / 主归属张数 / 被参见次数；「主归属」区用档案版式目录行（`KB.cardRowHTML`），一屏 40 张；「交叉参见」区是重点——文案直接写明「它们的主条目是别处，但同样讲了这件事，所以查这个话题时必须一起看」，每行末位标出那张卡自己的主归属；下面是「同一角度下的其他条目」横排 chip；最后一段说明故事体走分面并链到 `facets.html`。另有导出 JSON / CSV（CSV 带 `part` 列区分主归属与参见）。
- **`facets.html` / `facet.html?code=S1`**：结构搭好，按角色 / 场景 / 事件或情绪三字段分组；两页顶部都有 `.pending-note` 明确写「分面标记待补，暂不可用」，并说明**显示为空是因为"还没算"，不是因为"没有这样的故事"**，同时链到 `docs/facet-labeling-plan.md`。分面页的列表中区在 `ready` 之后会自动填充，页面结构不用改。
- **`card.html`**：首屏徽章换成条目（故事卡显示「故事体 · 走故事分面」），`keyfacts` 的前两行是「这一条属于」「还涉及哪些条目」，全部可点；「相关卡片」由旧主题名改为主归属名。旧 topics 已从该页主信息区消失。
- **`index.html`**：「看结构」组最前面插入「分类条目」「故事分面」两行，原有分组（读内容 / 看结构 / 用起来）与既有三行的相对顺序未动。
- 所有新页面复用 `style.css` 与 `theme.js`（吸顶导航、阅读进度条、返回顶部、风格切换、移动端适配自动生效），**没有引入任何 CDN、外链字体、框架或构建工具**，也没有新增图片资源。

### 5.3 新增的 CSS（4 组，全部沿用既有变量）

`.badge--entry`（主归属徽章，实线）/ `.badge--see`（参见徽章，虚线）、`.entry-attr`、`.angle-note`、`.pending-note`（如实告知条）、`.rows .row-meta .row-entry`（目录行里的条目归属着色）。没有改任何既有选择器。

---

## 六、验收

### 6.1 `python scripts/validate_all.py` → `ALL OK`

关键输出（原样）：

```
HARD ERRORS: 0
wrote .../web/data.json (13 sources, 12 topics, 1386 cards; taxonomy: 23 entries, 5 angles, 17 facets (facets_ready=False))
shards: 1386 cards, 13 sources, 12 topics
classification: 713 论述卡有主归属 / 673 故事卡走分面；参见 416 条（399 张卡），跨角度 245 条
taxonomy: 23 条目 · 5 观察角度 · 17 故事分面（facets_ready=False）
=== check_kb.py === === audit_cards.py === === coverage_report.py ===
=== coverage_volumes.py === === build_site.py === === build_shards.py ===
ALL OK
```

### 6.2 自查（脚本化，不靠肉眼）

1. **语法**：18 个页面的全部内联 `<script>` 逐块 `node --check` → 0 失败；`web/kb.js` → OK。
2. **数据层冒烟测试**（Node + 真实分片，无 DOM）：校验 `meta.entries` 23 项且每条都有非空 `rule`、`meta.layers` 恰好 5 项且顺序为宗旨→立场→教育关系与组织→内容与方法→衡量、`meta.facets` 17 项且 `facets_ready === false`、A18 `tag===true && count===0` 且不出现在任何角度里、`index.json` 里有主归属的卡数/带参见的卡数与 `meta.classification` 完全相等、每张卡 `seealso` 与 `seealso_names` 等长、故事卡 `primary===null && seealso===[]`、23 个 `entry/*.json` 的 `cards.length`/`cross.length` 与 meta 的 `count`/`cross` 逐条相等、`cross` 每项都带 `cross_from`、每个 `facet/*.json` 都是 `ready:false + count:0 + cards:[]`、抽样 200 张卡的 `related` 都满 6 张且至少有一张与主归属或参见相关 → **SMOKE OK**。
3. **渲染回归**（headless Chrome `--dump-dom` 打真实站点）：`entries.html`、`entry.html?code=A11`、`entry.html?code=A18`、`facets.html`、`facet.html?code=S1`、`card.html?id=sk-0001`（论述卡）、`card.html?id=sk-0004`（故事卡），以及既有页面 `index / explore / topic / problem / stories / search / topics / latest` 全部正常渲染，无「数据加载失败 / 未找到」。渲染出来的文字里能读到真数字，例如条目页「59 主归属卡 / 27 被参见」、交叉参见区「另有 27 张卡把「劳动与创造」列为参见」、`latest.html` 49 行条目元信息且旧主题词 0 次。
4. HTTP 层：`data/meta.json`、`data/entry/A11.json`、`data/layer/1.json`、`data/facet/S1.json` 等分片与全部新页面均 200。

### 6.3 导航一致性审计（只审计，未改）

把全站 18 个页面的 `.nav-links` 抓出来比对，**改动前就已经有 6 种不同组合**：

| 组 | 页面 | 链接 |
|---|---|---|
| A（5 页） | cases / clusters / coverage / explore / sources | 首页 · 主题浏览 · 问题检索 · 思想地图 · 案例 Review · 书源 |
| B（3 页） | guide / latest / topics | 首页 · 教育专题 · 主题浏览 · 541 篇故事 · 问题检索 · 书源 |
| C（2 页） | problem / topic | 首页 · 主题浏览 · 思想地图 · 问题检索 · 案例 Review · 书源（顺序与 A 不同） |
| D（1 页） | card | 首页 · 主题浏览 · 思想地图 · 案例 Review · 书源（少「问题检索」） |
| E（1 页） | stories | 首页 · 主题浏览 · 541 篇故事 · 问题检索 · 思想地图 · 案例 Review · 书源 |
| F（1 页） | index | 9 个链接（最全） |
| **新页（4 页）** | entries / entry / facets / facet | 首页 · 分类条目 · 故事分面 · 主题浏览 · 书源 |
| 另类（1 页） | search | 用的是**旧版 `site-header` 版式**（`<header class="site-header">` + `<nav>`，没有 `.topnav`），而 `style.css` 里已经没有 `.site-header` 规则，所以那一页顶栏是**无样式**的；它虽然加载了 `theme.js`，但找不到 `.topnav .nav-links`，风格切换会退化成悬浮按钮 |

按你的要求，我只把新入口加进了 `index.html` 的「看结构」；**其余页面的顶栏一行未动**，避免顺手把 12 个页面重排。要不要统一（以及是否顺手修 `search.html` 的旧版式），见 §七.8。

---

## 七、没做到 / 与规格不符 / 需要你决定

1. **分面标记没有算**（按规格执行，非偏差）。`facets` 的 `count` 一律 0，`meta.facets_ready: false`，`facet/*.json` 的 `cards` 为空数组，两个页面显式写「分面标记待补，暂不可用」。`docs/facet-labeling-plan.md` 的门槛/做法已就绪，`taxonomy.py` 里也有现成的关键词命中逻辑（`classify()` 对 case 会返回 `facets`），要补随时可以补——**需要你决定由谁来跑**，因为跑完 `classification.json` 会带 `facets` 字段，届时页面会自动填充。
2. **A18 复分标签清单不可得**（与规格 §五.3 不符，原因是数据缺失）。规格要求「凡使用复分标签的条目，页面上必须有一处能直接点开、列出全部被打标卡片的入口」。当前 `classification.json` 的字段只有 `primary/seealso/claim/evidence/title/old_topics/type`（7 张人工裁定卡另有 `source`/`override_why`），**没有 `tags` 之类标记字段**，416 条 seealso 里也从未出现 A18（实测 `seealso A18: 0`）。所以 `entries.html` 的复分标签区只列出 A18 本身，并明确写「标记数据未算出，不显示张数、不列卡片——不编造」。补齐后这里会自然带上清单。
3. **你给的自检基准（718 / 668）与当前仓库不一致，当前是 713 / 673**（`seealso` 416 / 399 / 跨角度 245 与你给的一致）。原因：本次会话期间**有另一个进程在同时改这个仓库**——`classification.json`（468,701 → 530,406 字节）、`taxonomy.md`、`scripts/taxonomy.py`、`scripts/classify_llm.py`、`docs/*` 都被改过，其中 **5 张卡（`sk-1089`~`sk-1093`，云雀之歌 / 秋天 / 日出 / 黄昏 / 太阳躲进云里）从论述体改判为故事体**，所以论述体从 718 降到 713、故事体从 668 升到 673，A14 从 32 降到 27。我另外撞到一次**构建互踩**：某个并发进程正在跑 `build_shards.py`，它先删空 `web/data/cards/` 再逐张重写，我中途看到目录里只有 370 个文件（现已恢复 1386）。**所有数字都取自最后一次完整构建**；如果你希望交付报告里的数字与某个确定版本绑定，请在并发进程停掉后再跑一遍 `validate_all.py`。
4. **`rule` 不是逐字符原文**：`taxonomy.md` 表格单元格里带 `**强调**` 与 `<br>`，直接显示会露出星号与标签，所以我去掉了 `**`、把 `<br>` 换成空格、压缩连续空白，**实词一字未改**。另外要提醒：**A20 的收录口径原文里内嵌着一句历史数字**「（实测全文命中 91 张，其中 84 张原不在 A16）」，这是规格自述、可能已随逐卡判读更新而失效；我按"收录口径原文"如实照搬，页面会显示它。**要不要在规格里把这类内嵌数字改成不含数字的表述，请你决定。**
5. **`layers` 是 5 项，`taxonomy.md` §一 的表是 6 行**（第 6 行「关照」）。我按「该层全部条目都是复分标签 → 不是观察角度」的规则剔除，A18 单列。
6. **规格没点名、我自行补的字段/改动**（都可用，但请你确认是否接受）：`meta.entries[].tag`（23 项全带，不只 A18）、`meta.classification` 块、`entry/*.json` 的 `cross_from_name`、`layer/*.json` 的 `question`/`entries`、`web/data.json` 顶层 `taxonomy` 块、`sitemap.xml` 增加 `entries.html`/`facets.html`/23 个 `entry.html?code=`、`entry.html` 的 JSON/CSV 导出。
7. **`related` 的权重是我定的启发式**（§3.5）。规格只说「同 primary 的卡 + 与本卡 seealso 重叠的卡，取 6 张」，没说谁优先、同 primary 与参见重叠怎么比。如果你希望「同一主归属」绝对优先于「参见重叠」，改一行排序键即可。
8. **导航未统一**（见 §6.3）。现状是改动前就有的 6 种组合，我一行未动。要不要：①把「分类条目」加进 A/B/C/D/E 五组的顶栏；②把 `search.html` 的旧 `site-header` 换成 `.topnav`（顺带修好它无样式的顶栏）；③把 12 个页面的顶栏统一成一套。**这三件都需要你点头**，因为都会改动既有页面的版式。
9. **旧 topics 仍在这些地方出现**（有意保留，向后兼容）：`explore.html` / `search.html` / `topic.html` 的主题**筛选器**与 `topics.html`（教育专题）整个页面、`topic/*.json` 分片。它们都是"按旧标签回溯"的入口，删掉会让旧链接失效。**卡片列表与详情页的主信息区**里已经不再显示旧主题名（`cardRowHTML` / `cardHTML` / `card.html` / `latest.html` / `search.html` 结果行）。
10. **没有 `git commit`**（按要求）。`web/data/**` 有 1419 个生成文件处于改动状态，其中一部分是并发进程造成的重建。
11. 冒烟测试脚本放在仓库外（`D:\dsh\projects\smoke_kb.js`、`nav_audit.py`、`index_delta.py`），没有写进仓库——`validate_all.py` 的链路未被改动。如果你希望把数据层冒烟测试固化成 `scripts/` 里的一环（这样以后换分类会自动拦住不一致），我可以加。

# 设计台账（Design Ledger）

> 这份文件答两个问题：**站点与数据层的设计决策都记在哪、每条什么时候必须重看。**
> 原始报告仍在 `docs/` 各自的文件里（本文件是**总入口 + 复查阈值**，不复述细节）。
> 由来：2026-10-17 站点"变卡"——性能改造（2026-09-10）本身是对的，但它只在 1,386 张卡时验证过，
> 长到 2,590 张后 `index.json` 从 306 KB 涨到 **587 KB gzip**，越过了当时的隐含阈值，而**没有任何机制提醒复查**。

## 一、决策清单（每条都必须有复查阈值）

| # | 决策 | 当时依据 | **复查阈值（越线必重看）** | 当前状态 | 原始文档 |
|---|---|---|---|---|---|
| D1 | 静态分片：索引/正文分离，浏览器按需取 | 1,386 张：首屏 772 KB gzip → 分片后 306 KB | **`index.json` gzip >300 KB** 或 **卡数 >2,000** | ⚠️ **已越线**（587 KB / 2,590 张）→ 2026-10-17 处置中 | `web-performance-sharding.md` |
| D2 | 离线可用：`.json.js` 影子 + `cards-all.js` 单包 | fetch 在 `file://` 被拦、`<script src>` 不被拦 | **`cards-all.js` gzip >1.2 MB** | ⚠️ **已越线**（1.5 MB）→ 待处置 | 同上 |
| D3 | 列表页首屏只渲染一屏 | 1,351 卡一次性渲染 ≈ 19,578 节点 / 布局 4,090 ms | **单页 DOM >20,000 节点** | ⚠️ 已越线（约 2.5 倍）→ 渐进渲染 | 同上 |
| D4 | 检索走 `search/all.json` 全量语料 | 1,386 卡时 664 KB gzip 可接受 | **`search/all.json` gzip >800 KB** | ⚠️ **已越线**（1.5 MB）→ 应改按来源分片 | 同上 |
| D5 | `cards/` 是可引用层，只有人能写；AI 只读 | 层划界 | 无（原则性） | ✅ | 仓库 `AGENTS.md` |
| D6 | 案例卡（`type: case`）只进主题入口、不进 A 论断入口 | 10-15 实测：673 张 case 卡 `primary: null`，**是设计不是缺陷**；前端 `entry/A*.json` 里 0 张 case ✓ | 若前端 A 入口出现 case 卡 ⇒ 前端实现退化了 | ✅ | 本文件 §三 |
| D7 | 导航统一（六入口） | 多版本导航并存 | 新增入口前先看是否与已有六个重复 | ✅ | `topnav-unification-report.md` |
| D8 | 档案层布局（列表/检索用档案层、长文用阅读层） | 按"这一屏要干什么"取层 | 单页混用两种层时复查 | ✅ | `web-archive-layout.md` |
| D9 | id 稳定：`sk-XXXX` 只新增不改号；卡间引用只写 `[[sk-XXXX]]` | 全库 64 组标题重复 | 若必须改号 ⇒ 先全库改引用 | ✅ | 仓库 `AGENTS.md` |

## 二、2026-10-17 实测基线（gzip，用于下次对比）

| 文件 | 原始 | gzip | 谁加载 |
|---|---:|---:|---|
| `web/data/index.json` | 2,443 KB | **587 KB** | 5 个页面（全量）→ 改为渐进 |
| `web/data/index-p/01.json` | 140 KB | **39 KB** | 渐进首片（新） |
| `web/data/search/all.json` | 4,064 KB | **1,559 KB** | 检索页 |
| `web/data/cards-all.js` | 6,900 KB | **1,503 KB** | 卡片页兜底（fetch 失败才用） |
| `web/data/data.json` | 7,841 KB | 1,890 KB | **浏览器不加载**（给 agent/外部程序）|
| `web/style.css` | 122 KB | 39 KB | 全站 |
| `web/kb.js` | 31 KB | 12 KB | 全站 |

## 三、2026-10-17 处置（A+B+C）

**A（数据层，已上线）**：`kb.js` 新增 `loadIndexProgressive(onChunk)` / `loadIndexFast()`——
先取第 1 片（150 张 / 39 KB gzip）立即渲染，其余 17 片后台追加。

**B（渲染层，试点 1/5）**：`explore.html` 已改：首屏 `loadIndexFast()`，然后 `loadIndexProgressive` 每追加一片就**重跑 `applyFilter()`**。
> **语义红线**：`loadIndexPage` 上方 2026-09-27 的警告仍然成立——「只载一部分行去做筛选，会得到筛出来的不是全部，那比慢更糟」。
> 所以渐进加载**必须**每片回调后重跑渲染/筛选，绝不能"载一半就不管了"。
> 其余 4 个页面（clusters / problem / search / sources）尚未改，**同一个模式，逐页改 + 上线实测**（不批量盲改）。

**C（本文件）**：把设计决策收口并给每条加阈值。

## 四、下次复查的触发条件（照这个表看，不要凭感觉）

- `index.json` gzip 再破 300 KB（已破）· `cards-all.js` gzip >1.2 MB（已破）· `search/all.json` gzip >800 KB（已破）
- 卡数每翻一倍（1,300 → 2,600 → 5,200）⇒ 重跑一次本文件的实测基线表
- 任一页面首屏可交互 >1 秒（用 headless Chrome 抓 `Network.loadingFinished` + `Performance`，方法见 `web-performance-sharding.md` §3.1）

### 2026-10-17 · B 收敛：改 2 页、判 2 页不改（附理由）

| 页面 | loadIndex 用在哪 | 处置 | 理由 |
|---|---|---|---|
| explore.html | 首屏筛选列表 | 改（首片 + 每片重跑 applyFilter）| 筛选基于增长中的数组，语义正确 |
| problem.html | 首屏问题清单 | 改（首片 + 每片重跑 apply）| 同上 |
| search.html | 首屏检索索引 | 改（首片；其余静默追加进 SDATA.index）| 检索按需触发，下次搜即全量，无需重跑 |
| clusters.html | ensureIndex 算关系矩阵 | **不改** | 片段索引会算错关系矩阵；且已是懒加载 |
| sources.html | exportAll 导出全部卡片 | **不改** | 导出必须完整数据，渐进会导出残缺（且是用户点按钮才触发）|

结论：7 个加载 index.json 的页面里，真正该渐进的是 3 个；其余需要完整数据或已懒加载。
**不批量盲改是对的** —— 两张看起来一样的页面，loadIndex 的语义可以完全不同。

**剩余风险（D4）**：search.html 仍全量取 search/all.json（1.5 MB gzip），是当前最大单页负担，应改按来源分片（search/<source>.json 已存在）。

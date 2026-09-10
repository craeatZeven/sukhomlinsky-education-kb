# 网页性能改造：档位 A 静态分片（2026-09-10 实施并验收）

> 目标：把「首屏一次性下载整库」改成「按需取分片」，让分享出去的网页在普通网络与移动端都能秒开；同时把后端 API 作为可选增强保留。
> 相关：`docs/web-architecture-options.md`（方案对比与实测基线）、`docs/deployment.md`（部署）、`api/README.md`（后端）。

---

## 一、改之前的问题

| 指标 | 改造前 |
|---|---|
| 首屏 JS | `web/data.js` 3.31 MB 原始 / **772 KB gzip**（1386 张卡全量内联，含正文） |
| 任意页面（含首页、卡片详情） | 都要等这 772 KB 下完才渲染 |
| DOM 规模 | 一次渲染全部卡片时 19,578 节点，布局耗时 4,090 ms（1351 卡实测） |
| 详情页 | 为了显示「上一张/下一张」和「相关卡片」，也必须先加载整库 |

根因：**把「索引」和「正文」混在一个文件里**，而 90% 的浏览只需要索引。

---

## 二、改造后的数据层

新增 `scripts/build_shards.py` 生成 `web/data/`，浏览器由 `web/kb.js` 统一按需加载：

| 文件 | 内容 | 原始 | gzip | 谁在用 |
|---|---|---|---|---|
| `data/meta.json` | 书源、主题、各来源/主题计数 | 23 KB | **9.3 KB** | 所有页面（先取它拿版本号） |
| `data/index.json` | 全库索引：元数据 + 80 字摘要（无正文） | 1.09 MB | 306 KB | 浏览页（桌面 60 张/屏） |
| `data/index/<source>.json` | 按来源切分的索引 | 7 KB – 425 KB | 3 KB – 120 KB | 《做人的故事》页等 |
| `data/topic/<slug>.json` | 按主题切分的索引 | 13 KB – 453 KB | 4 KB – 130 KB | 专题页 |
| `data/cards/<id>.json` | 单卡全文 + 上一张/下一张 + 6 张相关卡 | 平均 3.2 KB | **平均 1.3 KB** | 卡片详情页、列表「展开更多原文」 |
| `data/search/all.json` | 全文检索语料 | 1.73 MB | 664 KB | 检索页本地回退、列表页 0 结果时的深度检索 |
| `data/search/<source>.json` | 按来源切分的检索语料 | 10 KB – 703 KB | 5 KB – 257 KB | 《做人的故事》页检索 |
| `data/ids.json` / `data/latest.json` | 全部 id / 最近 60 张 | 14 KB / 50 KB | 2.7 KB / 14.5 KB | 随机卡片、最近更新页 |

`web/kb.js` 负责：版本号（来自 `meta.generated`）、请求去重与缓存、**HTML 转义**（`KB.esc`）、
`ref` 里 OCR 注释的还原（`KB.refText`），以及 `loadIndex / loadIndexFor / loadTopicIndex / loadCard / loadSearch / loadLatest / loadRandomCard`。

`web/data.js` 已删除；`web/data.json`（全库快照）保留给 agent 与外部程序，浏览器不加载。

---

## 三、实测：每页真实传输量（headless Chrome，本地未压缩）

| 页面 | 改造前 | 改造后（原始） | 改造后（Pages gzip 估算） |
|---|---|---|---|
| 首页 | 3.4 MB | **75 KB**（meta + ids + 1 张卡） | ~28 KB |
| 卡片详情 | 3.4 MB | **9.6 KB**（meta + 单卡） | ~12 KB |
| 主题浏览 | 3.4 MB | 1.10 MB（索引） | ~335 KB |
| 《做人的故事》 | 3.4 MB | 431 KB（来源索引） | ~140 KB |
| 专题页 | 3.4 MB | 182 KB（主题索引） | ~70 KB |
| 最近更新 | 3.4 MB | 53 KB | ~25 KB |
| 书源 / 主题总览 | 3.4 MB | 9 KB | ~12 KB |

首屏卡片的渲染规模：主题浏览默认只渲染 **60 张（移动端 24 张）**，DOM 900 节点（改造前全量渲染 19,578 节点）。

---

## 四、验收：自动化检查（脚本在 gitignored `local_working_copy/web-audit/`）

`node local_working_copy/web-audit/audit.mjs` —— CDP 驱动 headless Chrome，18 个页面 + 4 条交互流程：

- **18/18 页面 OK**：控制台错误 0、页面异常 0、请求失败 0；
- `explore-deep-search` PASS：索引查不到的词自动加载全文语料后命中（「孜」→ 3 张，状态栏显示「已含原文全文」）；
- `stories-deep-search` PASS：《做人的故事》页同样的深度检索路径；
- `explore-expand-excerpts` PASS：列表「展开」按需拉单卡 JSON，补出 2 段原文；
- `search-static-fallback` PASS：后端不可达时自动切本地静态检索，「劳动」→ 411 命中、20/页、摘要来自原文正文。

`node local_working_copy/web-audit/metrics.mjs` —— 客观 UX 指标（1440×900 / 390×844 两档）：

| 检查项 | 结果 |
|---|---|
| 横向溢出（`scrollWidth - clientWidth`） | 全部页面 **0** |
| 首屏能否看到卡片 | 主题浏览：桌面 746 px、移动 676 px（均小于视口高度） |
| 移动端触控目标 < 40 px 的元素 | 主题浏览 43 → **0**；其余页面 0（检索页除外，已补规则） |
| 最小字号 | 12 px（仅 eyebrow / 出处等辅助文字） |

`node local_working_copy/web-audit/aesthetics.mjs` —— 机检字阶与对比度：

- 字阶收敛为 **12 / 14 / 17 / 21 / 26 / 34** 六级，相邻级差 1.17 / 1.21 / 1.24 / 1.24 / 1.31（改造前是 12/13/14/15/16/17/18/20/24/26/28，级差 1.06–1.14，肉眼分不出层级）；
- 对比度：正文 13.66:1、次要文字 5.04:1、徽章 4.99:1（均过 WCAG AA；绿色主题的 `--soft` 由 4.34:1 调深到 5.04:1）。

---

## 五、顺带修掉的三个真问题

1. **96 张卡的出处行整段消失**：`ref` 里带 `` `<!-- OCR 原PDF页段: p0400-0499 (0-based) -->` ``，直接注入 `innerHTML` 时被浏览器当成 HTML 注释吃掉，页面只剩「OCR原书页码：」。现在统一走 `KB.esc()` + `KB.refText()`。
2. **后端探测无超时**：`*.workers.dev` 在国内被屏蔽时 TCP 连接长时间挂起，检索页会一直停在「正在连接后端…」。现在 4 秒超时后自动切本地静态检索。
3. **卡片详情页标题重复**：页头大标题与卡内标题同名同义，占两块视觉空间；已删掉卡内重复标题并去掉冗余 eyebrow。

---

## 六、维护约定

- 内容更新后跑 `python scripts/validate_all.py`（已把 `build_shards.py` 并入链路：check → audit → coverage ×2 → build_site → build_shards）。
- `web/data/` 必须提交（Pages 直接从仓库取）；`web/data.json` 与 `web/data/` 都由脚本生成，不要手改。
- 新增页面时的三条规矩：**只取需要的那一片**、**文本一律过 `KB.esc`**、**新增全局字号必须落在六级字阶上**。
- 回归验证：`node local_working_copy/web-audit/audit.mjs`（页面 + 交互）与 `metrics.mjs` / `aesthetics.mjs`（UX 与字阶对比度）。

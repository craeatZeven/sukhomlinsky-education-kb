# 知识库状态总表（KB Status）

> **时点**：2026-09-11（分类体系改版后）。本文件是「一眼看全库」的总入口；各专项细节见文末文档索引。
> **用途**：新会话/新协作者先读本文件，再按需进入专项文档。
> **分类的唯一真源是 [`taxonomy.md`](../taxonomy.md)**；本文件只报规模与状态，不复述分类规则。

---

## 一、规模

| 项 | 数值 |
|---|---|
| 卡片总数 | **1386**（本文件随批次更新；实时值以 `cards/` 与 `docs/coverage-dashboard.md` 为准） |
| ├ 论述卡 | **713**（quote 259 / principle 194 / method 164 / practice 96，各自有主归属条目） |
| └ 故事卡 | **673**（全部 `type: case`，不占主归属；靠分面与挂靠条目检索） |
| 分类轴线 | **5 个观察角度 × 23 个条目（A1–A23，其中 A18 是复分标签不持卡）+ 17 个分面（S1–S17）**，见 [`taxonomy.md`](../taxonomy.md) |
| 编辑专题（另一条轴，与分类轴并存） | 12 个，见 [`topics/`](../topics/) 与站点「教育专题」页 |
| 来源 | 13 个已登记（12 个已有卡） |
| 在线站点 | https://craeatzeven.github.io/sukhomlinsky-education-kb/ |

**分类落位实测**（`classification.json`，1386 行）：22 个条目持卡（A18 只作标签）；673 张故事卡全部无主归属；
668 张有判读分面；116 张挂靠到条目（共 236 处挂靠）。旧 12 个主题没有消失，改作 `old_topics` 字段保留，
映射关系见 `taxonomy.md` §四。

**按来源**（见 `docs/coverage-dashboard.md` 实时表）：做人的故事 541 / 五卷本第2卷 272 / 五卷本第5卷 167 / 五卷本第3卷 97 / 五卷本第4卷 77 / 五卷本第1卷 67 / On Education 41 / 把心献给孩子 35 / 给教师的建议 24 / To Children I Give My Heart 22 / Each One Must Shine 16 / The Singing Feather 12。

---

## 二、三项覆盖审计（均已完成）

### 2.1 《苏霍姆林斯基讲美德故事》44 篇

- 状态：**44/44 全量盘点**——31 篇确认同源、11 篇高度可能（probable）、2 篇仅主题相关（thematic）。
- 报告：`docs/story-coverage-meide-gushi.md` + `docs/story-coverage-meide-gushi-verification.md`。
- 残留：13 篇（11 probable + 2 thematic）**需要原书才能定案**，本地无合法来源 → 暂缓。

### 2.2 113 条官方故事书目 ↔ 卡片对照

- 状态：**99/113 高置信可挂现有卡**（10 `A_verified` + 89 `H_high`），14 条 `E_none`。
- 报告：`docs/coverage-official-tales-mapping.md` + 三份 verification 报告。
- 残留：14 条 E_none 经逐条核验为「本地三源（ZuoRen / 五卷本 / singing-feather）均无对应故事」，其中 717《Бабусин борщ》有公开乌克兰语原文但本地无中文卡 → 暂缓（缺合法中文来源）。

### 2.3 五卷本逐章覆盖审计（310 个审计单位）

| 指标 | 数值 |
|---|---:|
| 审计单位 | 310 |
| 原 `gap` 行 | 143 |
| 已补（4 轮） | **143（100%）** |
| 仍空白 | 0 |
| 口径存疑 | 1（《给教师的100条建议》下篇 79） |

- 报告：`docs/coverage-volumes-chapters.md`（章节明细）、`docs/coverage-volumes-gaps-remaining.md` 及 round2/3/4 四份缺口审计。
- **勘误**：审计表有 12 张卡归属错误（6 张首轮裁定 + 6 张复查新发现，含 1 张跨作品），见 `docs/coverage-volumes-chapters-corrections.md`。

---

## 三、密度现状（加密度阶段）

| 卷 | 单位 | 1 张 | 2 张 | ≥3 张 | 全引言单位 | 无可操作卡单位 |
|---|---:|---:|---:|---:|---:|---:|
| 第 2 卷 | 166 | 约 89 | — | — | 15 → 已大幅减少 | 约 29 |
| 第 5 卷 | 68 | 3 | 36 | 29 | **2** | 11 |

- 第 2 卷的问题：**单卡 + 论断层**（唯一卡多为 principle/quote），缺的是数量与操作卡。
- 第 5 卷的问题：**已基本治好**「引言卡海」（全引言 36 → 2，quote 占比 69% → 48%）。
- 报告：`docs/vol2-density-report.md`、`docs/vol5-density-report.md`、`docs/density-reaudit-round3.md`。

**高频主题仍偏少**（下面这组是**旧 12 主题**口径的计数，见 `docs/coverage-dashboard.md`）：`assessment-grading`、`health-first`、`learning-difficulties`、`reading-and-books` 相对其他主题明显偏少。
2026-09-11 分类改版后，补卡的优先方向应以**新条目（A1–A23）**的持卡数分布为准（实测最多的 A19 有 86 张、A15 与 A11 各 59 张、A5 55 张、A10 48 张；最少的一档见 `web/data/map.json` 的 `entries`）；旧主题计数只用于追溯历史审计。

---

## 四、质量门与自动化

| 脚本 | 作用 |
|---|---|
| `scripts/validate_all.py` | 一次跑完下列脚本；输出 `ALL OK` |
| `scripts/check_kb.py` | frontmatter/来源/主题/INDEX 一致性 |
| `scripts/audit_cards.py` | 卡片质检（摘录长度、页码 ref、类型规范） |
| `scripts/coverage_report.py` | 生成 `docs/coverage-dashboard.md` + `web/coverage.json` |
| `scripts/coverage_volumes.py` | 生成 `docs/coverage-volumes.md` |
| `scripts/rebuild_index.py` | 重建 `INDEX.md` |
| `scripts/build_site.py` | 生成 `web/data.json`（全库快照，供 agent）+ `sitemap.xml` |
| `scripts/build_shards.py` | 生成 `web/data/` 浏览器分片（meta / 索引 / 单卡 / 检索语料 / 条目 / 分面） |
| `scripts/check_classification_shards.py` | **分片 ↔ `classification.json` 对账**（主归属 / 参见 / 标签 / 案例数 / 分面数 / 卡数），唯一能拦住"分片悄悄与分类脱节"的一步 |
| `scripts/check_content_contract.py` | **数据层内容契约**：原文槽位不得写"转述"、转述卡必须显式标注待补、入门卡三角色齐备、案例挂靠数从 `classification.json` 现算 |

**浏览器层回归**（需要真实 Chrome 与静态服务，进不了上面这条离线链）：[`tools/web-audit/`](../tools/web-audit/README.md)，三份脚本 ——
① `verify-hardened.mjs` 32 条行为/数据/判据（含「目录行是否真三列」与「打印时内容全部显形」）；② `scan-hidden-content.mjs` 17 个页面「滚到稳定后还有没有内容看不见」；
③ `verify-contrast-census.mjs` 三套主题 × 七个页面的文本对比度普查（先滚完全页再采样）。
跑法：`powershell -NoProfile -ExecutionPolicy Bypass -File tools\web-audit\run-audit.ps1`。

**已建立的质检手段**（这些是一次性脚本，仍在 gitignored `local_working_copy/`）：
- `verify_new_cards_verbatim.py`：新卡摘录逐段回查 OCR 全文（shingle 覆盖率）；
- `verify_verbatim.py`：严格**连续子串**复核（比 shingle 更强，用于补回的 9 条摘录）；
- `duplicate_scan.py`：全库同标题 + 摘录近重复扫描（当前：同标题组均为「同篇第二张卡」，Jaccard ≥ 0.70 的卡片对 0 组）；
- `fix_card_frontmatter.py`：批量修复 YAML 引号/字段。

**当前质量状态**：结构硬错误 0、质检警告 0、内容契约全部一致（1386 张卡 · 原文待补 11 张 · 22 个条目有入门卡 · 案例挂靠 236 处）。

---

## 五、网页

- 18 个静态页面：首页、分类条目、故事分面、主题浏览、教育专题、故事索引、问题检索、思想地图、书源、卡片详情、条目详情、分面详情、案例 Review、覆盖仪表盘、使用指南、最新卡片、**API 检索页**等；支持关键词/条目/来源/类型过滤、全文搜索、JSON/CSV 导出、引用复制、分享、打印/PDF。
- 性能实测（`docs/web-architecture-options.md` §六）：1351 张卡时首屏 607 KB gzip 级、过滤 2.8 ms、搜索 13.7 ms、**渲染全部卡片后布局 4,090 ms**（因此不一次性渲染全部，保持分页）。
- **档位 A 静态分片已实施（2026-09-10）**：浏览器不再加载全库 `data.js`（3.26 MB / 755 KB gzip），改为 `web/kb.js` + `web/data/` 分片按需加载——首页只取 meta（9 KB gzip）+ 一张随机卡，卡片详情只取单卡 JSON（约 0.9 KB），列表页取索引（305 KB gzip），全文检索语料仅在需要时加载。实测与验收见 `docs/web-performance-sharding.md`。
- **后端 API（档位 B）已实现可运行原型**（2026-09-09）：`scripts/build_db.py` → `api/kb.db`（SQLite + FTS5 trigram），`api/main.py`（FastAPI 11 个端点，同时托管 `web/`），配套前端页 `web/search.html` + `web/config.js`，容器化文件 `Dockerfile` / `docker-compose.yml`，说明见 `api/README.md`。本地实测 1386 张卡检索正常；**尚未部署到公网**。
- **Cloudflare 免运维变体（2026-09-09 已上线）**：`cloudflare/`（Workers + D1），SQL 由 `scripts/build_d1_sql.py` 生成。线上地址 **https://suk-kb-api.suk-kb.workers.dev**（D1 `suk-kb`，1386 卡 + FTS5；`/api/search?q=苏霍姆林斯基` 走 FTS5 771 命中、`q=劳动` 走 LIKE 372 命中；GitHub Pages 的 `search.html` 已连上）。CORS 已收紧为站点域名。**注意**：`*.workers.dev` 在国内网络被 DNS 污染（脚本类客户端不可达、浏览器可访问），主要受众在大陆时需绑自定义域名；`search.html` 在后端不可达时会自动回退到本地静态检索。
- 已完成：档位 A 静态分片（`web/data/` + `web/kb.js`，见 `docs/web-performance-sharding.md`）。
- **版式分而治之（2026-09-10）**：调研 24 个同类高级感站点后定版——列表页走档案版式（目录行 / 零圆角 / hairline / 深色 chrome 层），详情页保留杂志阅读（衬线大引文 + 纸感 + **700px 阅读栏宽**）；砖红限量到 4 处；详情页新增「关于本卡」溯源块。实测与验收见 `docs/web-archive-layout.md`。

---

## 六、已知缺口与阻塞

| 缺口 | 状态 |
|---|---|
| 《美德故事》13 篇 probable/thematic | **阻塞**：缺原书（合法来源） |
| 113 条官方书目 14 条 E_none | 暂缓：本地三源均无对应故事 |
| 五卷本第 2 卷约 89 个单卡单位 / 29 个无可操作卡单位 | 可继续：按 `docs/density-reaudit-round3.md` §三 逐篇诊断补卡 |
| 五卷本第 5 卷 11 个「无操作卡」篇目、2 个全引言篇目 | 可继续（篇目体量偏小者优先跳过） |
| 562 篇期刊文章 | 暂缓：合法获取渠道受限 |
| 英文/电子本页码未统一 | 暂缓：以本地文件/行号定位 |

---

## 七、文档索引

| 文档 | 内容 |
|---|---|
| [`taxonomy.md`](../taxonomy.md) | **分类唯一真源**：5 观察角度 / 23 条目 / 17 分面 / 旧主题映射 / 6 条验证门槛 / 人工裁定表 |
| [`tools/web-audit/README.md`](../tools/web-audit/README.md) | 浏览器回归验证（24 条判据 + 三主题对比度普查）与判据设计缘由 |
| `docs/review-disposition.md` | 两轮外部评审（GPT / Codex）的**逐条处置表**，含撤回的过度结论 |
| `docs/codex-final-opinion.md` / `docs/codex-rereview-opinion.md` | 两轮外部评审原文 |
| `docs/web-performance-sharding.md` / `docs/web-archive-layout.md` | 网页性能分片、版式分而治之 |
| `docs/coverage-dashboard.md` | 实时覆盖仪表盘（自动生成） |
| `docs/coverage-volumes-chapters.md` | 五卷本章节级审计（310 单位） |
| `docs/coverage-volumes-gaps-remaining*.md` | 四轮剩余缺口审计 |
| `docs/coverage-volumes-chapters-corrections.md` | 审计表归属勘误（12 张卡） |
| `docs/vol2-density-report.md` / `docs/vol5-density-report.md` / `docs/density-reaudit-round3.md` | 加密度审计 |
| `docs/zuoren-uncarded-audit.md` | 《做人的故事》541 篇漏卡审计 |
| `docs/story-coverage-meide-gushi*.md` | 44 篇美德故事覆盖 |
| `docs/coverage-official-tales-mapping*.md` | 113 条官方书目对照与核验 |
| `docs/quality-notes.md` | 逐轮质量与建卡日志 |
| `docs/roadmap.md` | 路线图与已完成项 |
| `docs/web-architecture-options.md` | 网页架构选项与性能实测 |
| `docs/copyright-policy.md` | 版权边界（公开仓库只放短摘录/转述，全文留在 gitignored 本地目录） |

---

## 八、收官核验（2026-09-09，全部 PASS）

脚本：`local_working_copy/final_verification.py`（可重跑）。核验项与结果：

| 核验项 | 结果 |
|---|---|
| 卡片总数 1386（12 个有卡来源，541/287/167/97/77/67/41/35/24/22/16/12） | PASS |
| 版权边界：单卡摘录最长 697 汉字（≤800） | PASS |
| `docs/coverage-dashboard.md` 总数一致 | PASS |
| `web/coverage.json` 总数与各来源卡片数一致 | PASS |
| `INDEX.md` 卡片条目数一致（1386） | PASS |
| `README.md` / `docs/kb-status.md` / `docs/local-holdings-index.md` / `docs/roadmap.md` 声明总数一致 | PASS |
| 三项覆盖审计 + 密度/勘误/质量日志文档齐备（14 份） | PASS |
| `local_working_copy/` 在 `.gitignore`（全文不入公开仓库） | PASS |
| 网页 18 个页面/数据文件齐备 | PASS |
| 全库重复扫描：同标题组均为「同篇第二张卡」；摘录 Jaccard ≥ 0.70 的卡片对 **0** | PASS |
| `scripts/validate_all.py` → `ALL OK`（0 硬错误 / 0 警告） | PASS |
| 线上 `web/coverage.json` 与本地一致（1386 / 各来源一致） | PASS |

---

## 九、分类改版核验（2026-09-11）

把旧 12 主题换成「5 观察角度 × 23 条目 + 17 分面」，判读走 **LLM 逐卡判断**（不是关键词打分）。
下面每个数字都有对应脚本可重跑；口径与例外都写在 `taxonomy.md` 与 `docs/review-disposition.md`。

| 核验项 | 结果 | 怎么复算 |
|---|---|---|
| 判读 vs 人工抽检（条目级 / 同范畴） | **82.8%**（159/192） / **91.1%**（175/192） | `scripts/path_test_prod.py` |
| 同一门槛下的关键词基线 | 50.5% / 63.0% —— 判读明显胜出 | 同上 |
| 两轮判读稳定性 | 条目级 85.4%、**同范畴 91.6%**（与抽检的 91.1% 收敛） | `scripts/classify_llm.py` 两轮包 |
| 分面判读 —— 抽检一致率 | **83.0% / 83.1%**（门槛 80） | `scripts/facet_compare_judge.py` |
| 分面判读 —— 关键词基线 | 61.4%（**未过门槛**，所以采用判读结果） | `scripts/facet_compare.py` |
| 分面覆盖 | 668/673（99.3%）有分面；5 张零标记（已登记为例外） | `classification.json` |
| 参见（see-also） | 416 条，落在 399 张卡上（占论述卡 56.0%），其中 245 条跨角度（58.9%） | `web/data/map.json` 的 `pairs` |
| 多词条假说 | **被证伪**：探针下 65% 的卡只该有 1 个参见、35% 一个都不该有、2 个为 0 —— 所以不强行多挂 | `docs/review-disposition.md` |
| 关系矩阵 | 22×22 = 484 格，对角线 0，非零 181 格，合计 416 = 参见总数；单格最大 14，**A19→A4 与 A19→A8 并列** | `web/data/map.json` 的 `matrix` |
| 教学案例挂靠 | 673 张故事卡分成 儿童文学 557 / **教学案例 116**；这 116 张挂到条目共 **236 处**（A11 +16、A19 +32） | `scripts/case_entries.py check` |
| 原文身份 | 1386 张卡：**11 张显式标注「原文待补」**（`excerpt_status: paraphrase` + 编者概括），**0 张静默留空**，其余 1375 张原文槽位非空 | `scripts/check_content_contract.py` |
| 依据可核验性 | 论述卡的分类依据要与卡片正文做模糊匹配（4-gram ≥ 70%），对不上的显式标 `evidence_unverified`：当前 **9 张**。注意它和上一行的 11 张**不是同一张清单**——11 张里有 2 张是 `case` 卡（`sk-0111`、`sk-0185`），本来就没有 `evidence` 字段可核，不算 unverified | `local_working_copy/diag_paraphrase_vs_unverified.py` |
| 入门卡 | 22 个持卡条目都有「为什么 / 怎么做 / 一个教学案例」三角色；A1、A20 本身没有挂靠案例，入门卡只有两张（**已登记为例外**） | 同上 |
| 路径宽度 | 按**全库**（不是按关键词预筛）算：劳动 235 / 后进生 294 / 分数 145 / 美育 470 —— 曾误报「比旧标签窄 41%」，那是**测量口径造成的假象**，已撤回 | `scripts/path_test_prod.py` |
| 浏览器回归 | 32 条判据全过 + 17 个页面无隐形内容 + 三主题 × 七页面对比度全过（采样 798 处，不达标 0） | `tools/web-audit/run-audit.ps1` |
| 隐形内容（2026-09-14 修） | 条目页与分面页曾**整页永久透明**（6+6 块、1926+863 字），线上同样；当时 24 条判据全 PASS。修 `theme.js` 的渐入为「谁被观察谁才隐藏」+ MutationObserver，并新增 `scan-hidden-content.mjs` 守住 | 见 `docs/review-disposition.md` §十一 |

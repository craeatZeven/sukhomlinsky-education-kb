# 知识库状态总表（KB Status）

> **时点**：2026-09-09。本文件是「一眼看全库」的总入口；各专项细节见文末文档索引。
> **用途**：新会话/新协作者先读本文件，再按需进入专项文档。

---

## 一、规模

| 项 | 数值 |
|---|---|
| 卡片总数 | **1386**（本文件随批次更新；实时值以 `cards/` 与 `docs/coverage-dashboard.md` 为准） |
| 来源 | 13 个已登记（12 个已有卡） |
| 主题 | 12 个 |
| 在线站点 | https://craeatzeven.github.io/sukhomlinsky-education-kb/ |

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

**高频主题仍偏少**（全库 topic 计数，见 `docs/coverage-dashboard.md`）：`assessment-grading`、`health-first`、`learning-difficulties`、`reading-and-books` 相对其他主题明显偏少，是后续补卡优先方向。

---

## 四、质量门与自动化

| 脚本 | 作用 |
|---|---|
| `scripts/validate_all.py` | 一次跑完下面四项；输出 `ALL OK` |
| `scripts/check_kb.py` | frontmatter/来源/主题/INDEX 一致性 |
| `scripts/audit_cards.py` | 卡片质检（摘录长度、页码 ref、类型规范） |
| `scripts/coverage_report.py` | 生成 `docs/coverage-dashboard.md` + `web/coverage.json` |
| `scripts/coverage_volumes.py` | 生成 `docs/coverage-volumes.md` |
| `scripts/rebuild_index.py` | 重建 `INDEX.md` |
| `scripts/build_site.py` | 生成 `web/data.json`（全库快照，供 agent）+ `sitemap.xml` |
| `scripts/build_shards.py` | 生成 `web/data/` 浏览器分片（meta / 索引 / 单卡 / 检索语料） |

**已建立的质检手段**（脚本在 gitignored `local_working_copy/`）：
- `verify_new_cards_verbatim.py`：新卡摘录逐段回查 OCR 全文（shingle 覆盖率）；
- `duplicate_scan.py`：全库同标题 + 摘录近重复扫描（当前：同标题组均为「同篇第二张卡」，Jaccard ≥ 0.70 的卡片对 0 组）；
- `fix_card_frontmatter.py`：批量修复 YAML 引号/字段。

**当前质量状态**：结构硬错误 0、质检警告 0。

---

## 五、网页

- 15 个静态页面：首页、主题浏览、问题检索、思想地图、案例 Review、书源、卡片详情、主题页、故事索引（541 篇）、覆盖仪表盘、使用指南、最新卡片、**API 检索页**等；支持关键词/主题/来源/类型过滤、全文搜索、JSON/CSV 导出、引用复制、分享、打印/PDF。
- 性能实测（`docs/web-architecture-options.md` §六）：1351 张卡时首屏 607 KB gzip 级、过滤 2.8 ms、搜索 13.7 ms、**渲染全部卡片后布局 4,090 ms**（因此不一次性渲染全部，保持分页）。
- **档位 A 静态分片已实施（2026-09-10）**：浏览器不再加载全库 `data.js`（3.26 MB / 755 KB gzip），改为 `web/kb.js` + `web/data/` 分片按需加载——首页只取 meta（9 KB gzip）+ 一张随机卡，卡片详情只取单卡 JSON（约 0.9 KB），列表页取索引（305 KB gzip），全文检索语料仅在需要时加载。实测与验收见 `docs/web-performance-sharding.md`。
- **后端 API（档位 B）已实现可运行原型**（2026-09-09）：`scripts/build_db.py` → `api/kb.db`（SQLite + FTS5 trigram），`api/main.py`（FastAPI 11 个端点，同时托管 `web/`），配套前端页 `web/search.html` + `web/config.js`，容器化文件 `Dockerfile` / `docker-compose.yml`，说明见 `api/README.md`。本地实测 1386 张卡检索正常；**尚未部署到公网**。
- **Cloudflare 免运维变体（2026-09-09 已上线）**：`cloudflare/`（Workers + D1），SQL 由 `scripts/build_d1_sql.py` 生成。线上地址 **https://suk-kb-api.suk-kb.workers.dev**（D1 `suk-kb`，1386 卡 + FTS5；`/api/search?q=苏霍姆林斯基` 走 FTS5 771 命中、`q=劳动` 走 LIKE 372 命中；GitHub Pages 的 `search.html` 已连上）。CORS 已收紧为站点域名。**注意**：`*.workers.dev` 在国内网络被 DNS 污染（脚本类客户端不可达、浏览器可访问），主要受众在大陆时需绑自定义域名；`search.html` 在后端不可达时会自动回退到本地静态检索。
- 已完成：档位 A 静态分片（`web/data/` + `web/kb.js`，见 `docs/web-performance-sharding.md`）。

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

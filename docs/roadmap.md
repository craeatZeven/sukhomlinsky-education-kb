# Roadmap

## v0.1 — 仓库骨架（已完成）
- [x] README / SKILL / INDEX / LICENSE / NOTICE / CONTRIBUTING / AGENTS
- [x] 规范与模板（schemas / templates / docs）
- [x] 书源登记
- [x] 首个主题 + 可溯源卡片

## v0.2 — 内容扩展（已完成）
- [x] 12 个主题页全部建立
- [x] 本地/公开中译本来源登记
- [x] 卡片规模到 1257 张（13 个来源）
- [x] 《做人的故事》541 篇（540 个不重复标题 + 同题《暴风雪》两篇）全部建卡
- [x] 页码尽量落实到 OCR 印刷页码；ZuoRen 541 张已逐条核对
- [ ] 术语表（glossary）待建

## v0.3 — 检索与发布（已完成主体）
- [x] GitHub Pages 静态检索站
- [x] 按主题/来源/类型过滤
- [x] 全文搜索（标题 + 中文转述 + 原文摘录 + 出处）
- [x] JSON / CSV 导出
- [x] frontmatter 校验脚本（`scripts/check_kb.py`）
- [x] 全量质量审计脚本（`scripts/audit_cards.py`）
- [x] 覆盖仪表盘（`docs/coverage-dashboard.md`）
- [ ] GitHub Actions CI（本地凭据缺 workflow scope；暂用 `scripts/validate_all.py`）

## v0.4 — 覆盖审计与内容补全（进行中）
- [x] 44 篇《美德故事》44/44 盘点（`docs/story-coverage-meide-gushi.md`）
- [x] 113 条官方故事书目盘点（`docs/coverage-official-tales.md`）
- [x] 113 条书目 ↔ 卡片全量对照与核验（`docs/coverage-official-tales-mapping.md`，99/113 高置信：10 A + 89 H；14 E_none；三份 verification 报告）
- [x] 五卷本按作品统计（`docs/coverage-volumes.md`）
- [x] 五卷本逐章覆盖审计（`docs/coverage-volumes-chapters.md`）
- [x] 五卷本剩余缺口审计（四轮）：原 143 个 gap 中 135 个已不再空白、7 个仍空白、1 个存疑（第四轮快照，`docs/coverage-volumes-gaps-remaining-round4.md`）
- [x] 剩余 7 个 gap 补齐（sk-1232–sk-1238，2026-09-09）；第 1/3/4/5 卷 gap 已连续三轮清零，第 2 卷 gap 清零
- [ ] 五卷本「加密度」：第 2 卷 166 个审计单位仅 2 个 ≥3 张卡、118 行停在 1 张卡；第 5 卷 68 篇多为每篇 1–2 张（下一阶段主线）
- [x] 第 2 卷加密度审计（`docs/vol2-density-report.md`）：166 单位 = 154 单卡 / 6 双卡 / 2 ≥3 张（口径 A），给出 20 项第二张卡清单
- [x] 审计表归属勘误（`docs/coverage-volumes-chapters-corrections.md`）：6 张卡错位，第 33/36/40/52 篇实为 0 张 → 补建 sk-1259–sk-1262
- [x] 第 2 卷密度补卡：`docs/vol2-density-report.md` §四 前 20 项全部落地（sk-1239–sk-1258，2026-09-09）；第 5 卷下一阶段优先补 method/practice/case 而非第 N 张 quote
- [ ] 第 2 卷继续加密度：仍有多数单位停在 2 张卡；第 5 卷 24 篇仍只有 1 张卡
- [x] 第 5 卷加密度审计（`docs/vol5-density-report.md`）：68 篇 = 1 张 24 / 2 张 41 / ≥3 张 3；**52 篇（76.5%）一张 method/practice/case 都没有**、36 篇（52.9%）全部卡都是 quote；推荐 20 项零 quote（method 12 / practice 5 / case 3）
- [ ] 第 5 卷密度补卡：按 §四 前 20 项补 method/practice/case（sk-1264 起）；新建卡 ref 统一写「《论文集》第 N 篇“篇名”」（旧卡 112/116 缺作品名，已造成一次静默误吸 sk-0202）
- [x] ZuoRen 漏卡审计与补卡（`docs/zuoren-uncarded-audit.md`）：目录实为 541 篇，补建 sk-1263《暴风雪》p277–278；官方书目 694 条升 H_high
- [ ] 44 篇中 11 篇 probable + 2 篇 thematic 的人工复核
- [ ] 113 条对照草稿的人工抽检；5 条 medium + 14 条 none 的后续处理
- [x] 五卷本优先 20 个 gap 章节的补卡
- [ ] 562 篇期刊文章的合法获取与逐步补卡
- [ ] 网页架构升级（可选，见 `docs/web-architecture-options.md`）：先做静态分片（档位 A），需要 API/多人写卡时再上前端+后端（档位 B）

## v0.5 — 生态化
- [ ] 作为可移植 Agent Skill 发布到 skills.sh
- [ ] 多语言（中/英）
- [ ] 社区贡献指南完善

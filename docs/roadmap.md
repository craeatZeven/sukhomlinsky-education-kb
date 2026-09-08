# Roadmap

## v0.1 — 仓库骨架（已完成）
- [x] README / SKILL / INDEX / LICENSE / NOTICE / CONTRIBUTING / AGENTS
- [x] 规范与模板（schemas / templates / docs）
- [x] 书源登记
- [x] 首个主题 + 可溯源卡片

## v0.2 — 内容扩展（已完成）
- [x] 12 个主题页全部建立
- [x] 本地/公开中译本来源登记
- [x] 卡片规模到 1069 张（13 个来源）
- [x] 《做人的故事》540/540 目录标题建卡
- [x] 页码尽量落实到 OCR 印刷页码；ZuoRen 540 张已逐条核对
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
- [x] 113 条书目 ↔ 卡片全量对照与核验（`docs/coverage-official-tales-mapping.md`，96/113 高置信：10 A + 86 H；17 E_none；三份 verification 报告）
- [x] 五卷本按作品统计（`docs/coverage-volumes.md`）
- [x] 五卷本逐章覆盖审计（`docs/coverage-volumes-chapters.md`）
- [ ] 44 篇中 11 篇 probable + 2 篇 thematic 的人工复核
- [ ] 113 条对照草稿的人工抽检；5 条 medium + 15 条 none 的后续处理
- [ ] 五卷本优先 20 个 gap 章节的补卡
- [ ] 562 篇期刊文章的合法获取与逐步补卡

## v0.5 — 生态化
- [ ] 作为可移植 Agent Skill 发布到 skills.sh
- [ ] 多语言（中/英）
- [ ] 社区贡献指南完善

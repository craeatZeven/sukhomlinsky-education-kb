# Sukhomlinsky Education KB

苏霍姆林斯基（V. A. Sukhomlinsky, 1918–1970）教育思想与案例的开源知识库。

**目标**：从苏霍姆林斯基的原著中，把教育思想、真实案例和可操作方法整理成**按教育主题检索与学习**的结构化 Markdown 知识库。

**两条使用路径**：

- 👤 人类读者：从 [`INDEX.md`](INDEX.md) 进入主题页 → 阅读思想与案例卡片。
- 🤖 AI / Agent：由根级 [`SKILL.md`](SKILL.md) 路由 → 按主题读取 `topics/` 与 `cards/`。

**在线访问**：

- GitHub 仓库：https://github.com/craeatZeven/sukhomlinsky-education-kb
- GitHub Pages：https://craeatzeven.github.io/sukhomlinsky-education-kb/

---

## 为什么做这个项目

苏霍姆林斯基的教育思想散落在《给教师的建议》《把整个心灵献给孩子》《论教育》等大量作品中。常见的“名言集”缺少上下文与案例；“整本书摘录”又难以按问题检索。

这个仓库采用：

```
sources/  → 书目与出处（无源不录的根）
cards/    → 原子卡片：原文摘录 / 案例 / 原则 / 方法 / 实践
topics/   → 主题页：按教育场景聚合卡片，并做跨书综合
```

## 当前状态

- [x] 仓库骨架与规范
- [x] 12 个主题页：学习困难学生、家校合作、劳动教育、健康第一、美育与自然、集体教育、教师成长、爱的教育、评价与分数、儿童研究、阅读与书籍、思维课与大自然
- [x] 可溯源卡片 **1019 张**（13 个来源）
- [x] 《做人的故事》目录 **540/540 篇全部建卡**，页码已与 OCR 正文页逐条核对
- [x] 覆盖审计：44 篇《美德故事》44/44 盘点、113 条官方故事书目 + 93 条卡片对照、五卷本按作品与章节级覆盖
- [x] 五卷本章节级审计：310 个审计单位（13 covered / 154 partial / 143 gap），附优先补卡清单
- [x] 全量质量审计：`python scripts/audit_cards.py`（0 硬错误 / 0 警告）
- [x] 网页检索站：[打开 `web/index.html`](web/index.html) · [GitHub Pages](https://craeatzeven.github.io/sukhomlinsky-education-kb/)
- [x] 网页支持：关键词/主题/来源/类型过滤、全文搜索、JSON/CSV 导出
- [ ] GitHub Actions CI（本地凭据缺少 workflow scope，暂用 `scripts/validate_all.py` 代替）
- [ ] 五卷本逐章覆盖审计（已有按作品统计版）
- [ ] skills.sh 发布

## 快速开始

```bash
# 给人类：直接打开 INDEX.md 或主题页
# 给 agent：告诉它先读 SKILL.md
```

### 目录速览

| 路径 | 作用 |
|---|---|
| [`INDEX.md`](INDEX.md) | 唯一索引：主题、来源、卡片清单 |
| [`SKILL.md`](SKILL.md) | Agent 入口与路由规则 |
| [`topics/`](topics/) | 按教育主题组织的主题页 |
| [`cards/`](cards/) | 原子卡片（quote/case/principle/method/practice） |
| [`sources/`](sources/) | 原书/译本书目元数据 |
| [`schemas/`](schemas/) | frontmatter 字段规范 |
| [`templates/`](templates/) | 新建 source/card/topic 的模板 |
| [`web/`](web/) | 杂志风知识检索站：主题/来源过滤、全文搜索、JSON/CSV 导出 |
| [`docs/`](docs/) | 生产流程、质量门、版权政策、路线图 |

## 质量纪律

1. **无源不录**：卡片必须能定位到具体作品与章节/页码。
2. **主题页不裸写断言**：实质判断用 `（参见 sk-XXXX）` 挂卡。
3. **Agent 与人类共用同一份索引**：README 与 SKILL.md 不重复维护内容目录。

详见 [`docs/quality-gate.md`](docs/quality-gate.md)。

## 版权与出处

- 本仓库的原创编排、主题页、中文转述/注释遵循仓库 [`LICENSE`](LICENSE)（MIT）。
- 原文摘录属于各自权利人；本项目只收录短摘录、转述与链接，不做整书转载。
- 详见 [`NOTICE.md`](NOTICE.md) 与 [`docs/copyright-policy.md`](docs/copyright-policy.md)。

## 贡献

欢迎补充主题、核对出处、改进 schema。请先读 [`CONTRIBUTING.md`](CONTRIBUTING.md) 与 [`AGENTS.md`](AGENTS.md)。

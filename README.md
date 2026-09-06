# Sukhomlinsky Education KB

苏霍姆林斯基（V. A. Sukhomlinsky, 1918–1970）教育思想与案例的开源知识库。

**目标**：从苏霍姆林斯基的原著中，把教育思想、真实案例和可操作方法整理成**按教育主题检索与学习**的结构化 Markdown 知识库。

**两条使用路径**：

- 👤 人类读者：从 [`INDEX.md`](INDEX.md) 进入主题页 → 阅读思想与案例卡片。
- 🤖 AI / Agent：由根级 [`SKILL.md`](SKILL.md) 路由 → 按主题读取 `topics/` 与 `cards/`。

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
- [x] MVP 主题：[学习困难学生（后进生）](topics/learning-difficulties.md)
- [x] 首批可溯源卡片 8 张
- [x] 本地书源全部登记：11 个唯一来源（覆盖本地 12 份文件，见 [书源盘点](docs/book-inventory.md)）
- [x] 网页原型：[打开 `web/index.html`](web/index.html)
- [ ] 更多主题（家校合作、劳动教育、美育、集体教育……）
- [ ] 中文扫描 PDF 全文 OCR 完成
- [ ] GitHub Pages 部署
- [ ] JSON/CSV 导出
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
| [`web/`](web/) | 杂志风知识检索站（单文件 HTML 原型） |
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

# Contributing

欢迎贡献：新主题、新卡片、出处核对、schema 改进、网站/脚本。

## 贡献前

1. 阅读 [`docs/production-guide.md`](docs/production-guide.md) 与 [`docs/quality-gate.md`](docs/quality-gate.md)。
2. 检查 `INDEX.md`、`topics/`、`cards/` 是否已有重复内容。
3. 如果涉及原文摘录，确认你有合法的文本来源，并遵守 [`docs/copyright-policy.md`](docs/copyright-policy.md)。

## 提交清单

- [ ] 新建/修改文件符合 [`schemas/README.md`](schemas/README.md) 的 frontmatter
- [ ] 卡片有 `source` 且 `ref` 可定位
- [ ] 新增卡片已在 `INDEX.md` 登记
- [ ] 主题页每句实质断言都挂 `（参见 sk-XXXX）`
- [ ] 主题/来源/卡片三个目录各自的 `_README.md` 命名规范已遵守

## 卡片 ID

- 全局递增 `sk-0001`、`sk-0002`……
- 文件名可带短描述，但 ID 是机器主键，不得按主题重复。

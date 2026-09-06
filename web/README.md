# web/ — 知识检索站

## 本地预览

直接双击打开 `index.html` 即可，单文件、无依赖。

## 当前能力

- 书源一览
- 主题深读
- 卡片检索（关键词 + 类型过滤）
- 杂志风精致化：吸顶导航 / 阅读进度 / 返回顶部 / 卡片 hover

## 与仓库数据的关系

- 当前 `index.html` 内嵌了一份数据快照（sources/topics/cards）。
- 数据更新后需要重新生成该快照；后续可加一个 `scripts/build_site.py` 从 Markdown 自动生成。
- 源文件：`../sources/`、`../topics/`、`../cards/`、`../INDEX.md`。

## 部署建议

- GitHub Pages：把仓库根目录或 `web/` 设为 Pages 目录即可。
- 若部署 `web/`，相对链接如 `../topics/...` 需要改为指向仓库根；正式部署前建议用构建脚本把 Markdown 链接替换为 GitHub blob 链接。

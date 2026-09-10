# web/ — 知识检索站

## 本地预览

直接双击打开 `index.html` 即可（`fetch()` 读同目录的 `data/` 分片；用本地 HTTP 服务更稳，例如 `python -m http.server 8000`）。

## 数据层：分片按需加载（档位 A）

浏览器不加载全库，而是按需取分片：

| 文件 | 内容 | 大小（gzip） | 谁在用 |
|---|---|---|---|
| `data/meta.json` | 书源、主题、计数 | ~9 KB | 所有页面 |
| `data/index.json` | 全库卡片索引（元数据 + 摘要，无正文） | ~305 KB | 浏览页 / 详情页翻页与相关推荐 |
| `data/index/<source>.json` | 按来源切分的索引 | 4–167 KB | 《做人的故事》页 |
| `data/topic/<slug>.json` | 按主题切分的索引 | 12–130 KB | 专题页 |
| `data/cards/<id>.json` | 单卡全文 | ~0.9 KB | 卡片详情页、列表「展开更多原文」 |
| `data/search/<scope>.json` | 全文检索语料 | 5–664 KB | 检索页本地回退、列表页 0 结果时的深度检索 |
| `data/latest.json`、`data/ids.json` | 最近 60 张、全部 id | ~17 KB | 最近更新页、随机卡片 |

`kb.js` 是统一的数据层（`KB.ready() / loadIndex() / loadIndexFor() / loadTopicIndex() / loadCard() / loadSearch() / loadLatest() / loadRandomCard()`），
并集中处理 HTML 转义（`KB.esc`）与 `ref` 里 OCR 注释的还原（`KB.refText`）。

## 当前能力

- 书源一览（含每个来源的卡片数，可直接跳到该来源的卡片列表）
- 主题深读
- 卡片检索：关键词 + 主题 + 来源 + 类型/标签过滤；搜索覆盖标题、中文转述、原文摘录和出处
- 当前结果导出：JSON / CSV；书源页可导出全库；专题页可导出本专题
- 使用指南页：三种用法、卡片结构、引用导出、Agent 接入
- 最近更新页：按卡片 ID 倒序查看新增内容
- 覆盖报告页：卡片量、来源分布、主题分布、已知缺口
- 键盘快捷键：在检索页按 `/` 直接聚焦搜索框
- 阅读体验：顶部阅读进度条 + 右下角返回顶部
- 卡片详情页支持复制引用、分享、打印 / 存 PDF
- 杂志风精致化：吸顶导航 / 阅读进度 / 返回顶部 / 卡片 hover

## 与仓库数据的关系

- `data/` 下的分片由 `../scripts/build_shards.py` 从 Markdown 自动生成；`data.json` 是全库快照（供 agent 取用，浏览器不加载）。
- 内容更新后执行：
  ```bash
  python ../scripts/validate_all.py     # 含 build_site.py + build_shards.py
  ```
  即可刷新网页数据。
- 源文件：`../sources/`、`../topics/`、`../cards/`、`../INDEX.md`。

## 部署建议

- GitHub Pages：把仓库根目录或 `web/` 设为 Pages 目录即可。
- 若部署 `web/`，相对链接如 `../topics/...` 需要改为指向仓库根；正式部署前建议用构建脚本把 Markdown 链接替换为 GitHub blob 链接。

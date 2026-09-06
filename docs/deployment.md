# Deployment — GitHub Pages 部署说明

## 当前网页形态

- `web/index.html`：杂志风知识检索站（人读入口）
- `web/data.js`：由 `scripts/build_site.py` 从 Markdown 自动生成
- 源数据：`sources/`、`topics/`、`cards/`、`INDEX.md`

## 本地预览

```bash
# 更新数据（每次增删卡片/主题后执行）
python scripts/build_site.py

# 直接打开
start web/index.html
```

## 部署到 GitHub Pages

1. 把仓库推到 GitHub。
2. 在仓库 Settings → Pages 中：
   - Source 选择 `Deploy from a branch`
   - Branch 选择 `main`，目录选择 `/web`
3. 访问：`https://<用户名>.github.io/<仓库名>/`

## 注意事项

- 页面内“查看来源记录”会链接到 `../sources/*.md` 等 Markdown；
  在 GitHub Pages 上这些会按纯文本/源文件提供，正式发布前可把链接改为 GitHub blob 地址。
- 如果希望仓库根目录作为 Pages（`https://<用户名>.github.io/<仓库名>/`），可在根目录放一个跳转页或把 `web/` 内容提升到根目录。
- 仓库已配置 CI（`.github/workflows/check.yml`）：每次 push 自动跑知识库校验和数据生成。

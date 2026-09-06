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

## 部署到 GitHub Pages（当前已启用）

1. 仓库已推送到：https://github.com/craeatZeven/sukhomlinsky-education-kb
2. GitHub Pages 已启用：
   - Branch：`master`
   - Path：`/`
   - 访问：https://craeatzeven.github.io/sukhomlinsky-education-kb/
3. 根目录 `index.html` 会自动跳转到 `web/index.html`。

## 注意事项

- 页面内“查看来源记录”会链接到 `../sources/*.md` 等 Markdown；
  在 GitHub Pages 上这些会按纯文本/源文件提供，正式发布前可把链接改为 GitHub blob 地址。
- 仓库曾添加 CI（`.github/workflows/check.yml`），但因当前 GitHub token 缺少 `workflow` scope 暂时从默认分支移除；
  授权 `workflow` scope 后可从 git 历史恢复该文件。
- 后续内容更新只需：
  ```bash
  python scripts/build_site.py
  git add -A && git commit -m "update"
  git push origin master
  ```

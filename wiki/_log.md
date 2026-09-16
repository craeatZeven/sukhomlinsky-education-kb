# 操作日志（append-only）

> 每行一条，前缀固定成 `## [日期] 动作 | 标题` —— 这样 `grep "^## \[" _log.md | tail -5`
> 就能取最近 5 条（Karpathy 的建议：日志能被 unix 工具直接解析）。

## [2026-09-14] init | 建立旁挂层 wiki/

- 建立 `wiki/`：`_schema.md`（宪法）/ `_log.md`（本文件）/ `index.md`（内容目录）
  / `moc/` `concepts/` `queries/` `comparisons/`
- 划界：卡片只读、AI 只写本层；个人批注进 gitignore 的 `notes/`
- 同期完成（在卡片层，属一次性迁移）：351 处卡→卡引用接成 `[[sk-XXXX]]`；
  1386 张卡补 `aliases`

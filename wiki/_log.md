# 操作日志（append-only）

> 每行一条，前缀固定成 `## [日期] 动作 | 标题` —— 这样 `grep "^## \[" _log.md | tail -5`
> 就能取最近 5 条（Karpathy 的建议：日志能被 unix 工具直接解析）。

## [2026-09-16] init | 建立旁挂层 wiki/

- 建立 `wiki/`：`_schema.md`（宪法）/ `_log.md`（本文件）/ `index.md`（内容目录）
  / `moc/` `concepts/` `queries/` `comparisons/`
- 划界：卡片只读、AI 只写本层；个人批注进 gitignore 的 `notes/`
- 同期完成（在卡片层，属一次性迁移）：351 处卡→卡引用接成 `[[sk-XXXX]]`；
  1386 张卡补 `aliases`

## [2026-09-16] moc | 生成 5 个角度页 + 22 个条目页

- 全部从 `web/data/meta.json` 与 `web/data/entry/*.json` 现算，不手写
- 为什么连条目页一起生成：`[[A11]]` 在 Obsidian 里解析不到，条目不是文件；角度页要能点进条目就得先有可解析的条目页
- 规则修正：旁挂层改用**中文文件名**（`[[宗旨]]` 读起来是话）；卡片的英文 slug 保持不动，因为 `[[sk-XXXX]]` 必须短且无歧义

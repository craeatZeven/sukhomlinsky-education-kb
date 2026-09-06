# Quality Gate — 质量门

每次新增/修改内容后，跑一遍以下检查。

## 1. Frontmatter 完整性

- source 有：`slug / title / author / rights_status / status`
- card 有：`id / type / topics / source / ref / status`
- topic 有：`slug / title / summary / card_ids / source_ids / related_topics`

## 2. 引用纪律

- 每张 card 的 `ref` 非空，且 `source` 存在于 `sources/`。
- quote 卡必须包含 `## 原文/Excerpt`。
- 非 quote 卡至少在 `## 出处核对` 中给出原文定位。

## 3. 主题页纪律

- `frontmatter.card_ids` 中的 ID 都存在。
- 正文中每个实质断言都带 `（参见 sk-XXXX）`。
- “编辑者建议/应用启示”与苏霍姆林斯基原意明确分节。

## 4. 索引一致性

- `INDEX.md` 的 topics / sources / cards 三张表与实际文件一致。
- `README.md` 与 `SKILL.md` 没有重复维护内容目录。

## 5. MVP 复核记录

| 检查项 | 结果 | 备注 |
|---|---|---|
| 8 张卡片均有 source + ref | ✅ | 来源见 INDEX |
| 卡片覆盖 ≥2 来源 | ✅ | on-education + to-children-i-give-my-heart |
| 卡片类型 ≥3 种 | ✅ | quote/case/principle/method/practice |
| 主题页每句实质断言挂卡 | ✅ | learning-difficulties |
| INDEX 与实际文件一致 | ✅ | 2026 初始 MVP |

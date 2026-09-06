# Production Guide — 内容生产流程

目标：把“作品原文”变成“可溯源的主题页 + 原子卡片”。

## 流程总览

```
1. 选书/选来源      → 登记到 sources/<slug>.md（status: registered）
2. 源素材可行性检查  → 确认某个主题在 ≥2 本来源中都有足够素材
3. 抽卡             → 逐条提取 quote/case/principle/method/practice
4. 审卡             → 核对出处、原文、类型，status: reviewed
5. 聚合主题页       → 只用 reviewed 卡片，逐句挂卡
6. 跑质量门         → 见 quality-gate.md
7. 同步 INDEX       → 更新唯一索引
```

## 步骤说明

### 1. 登记来源

用 `templates/source.md` 创建 `sources/<source-slug>.md`。至少要写：
- 书名/作者/译者/出版社/年份
- 可访问 URL 或本地工作副本标识
- `rights_status`
- 章节/页码定位方式说明

### 2. 源素材可行性检查

选主题前先统计候选词在两个来源中的出现情况。MVP 门槛：一个主题至少要有 **6 条以上素材、覆盖 2 本来源、至少包含 2 种卡片类型**。

### 3. 抽卡

- 卡片粒度：一条可独立检索的观点/案例/方法 = 一张卡。
- 引用原文保持短摘录；长原文不要放进 frontmatter，放正文 `## 原文/Excerpt`。
- `ref` 要能让别人回到原文位置：书名/章节/页码/URL anchor 至少写两个线索。

### 4. 审卡

- 原文是否确实来自登记来源？
- `type` 是否贴切（见 schemas）？
- 中文转述是否偏离原文？
- 通过后 `status: reviewed`，并填 `reviewed_by`。

### 5. 聚合主题页

主题页的正文结构固定（见 template）。实质判断必须用 `（参见 sk-XXXX）` 挂卡；没有卡支撑的句子放在“编辑者建议”小节。

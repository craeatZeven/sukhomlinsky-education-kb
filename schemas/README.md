# Schema — Frontmatter 规范

> 本文件是 frontmatter 字段的唯一权威。所有 `sources/`、`cards/`、`topics/` 文件必须遵守。

## 通用约定

- slug 用小写连字符：`learning-difficulties`
- 卡片 ID 全局递增：`sk-0001`
- 日期格式：`YYYY-MM-DD`
- 枚举值必须严格使用下文列出的值

---

## sources/<source-slug>.md

```yaml
---
slug: on-education
title: "On Education"
author: "Vasili Sukhomlinsky"
translator: "Katharine Judelson"
publisher: "Progress Publishers"
year: 1977
url: "https://archive.org/details/vasili-sukhomlinsky-on-education-progress-1977"
access_date: "YYYY-MM-DD"
rights_status: translation-license-unknown
status: registered
---
```

| 字段 | 必填 | 取值 |
|---|---|---|
| slug | ✅ | 小写连字符 |
| title | ✅ | 书名 |
| author | ✅ | 作者 |
| translator | 可选 | 译者 |
| publisher | 可选 | 出版社 |
| year | 可选 | 出版年 |
| url | 可选 | 在线来源 |
| access_date | 可选 | 核验日期 |
| rights_status | ✅ | `public-domain-verified` / `translation-license-unknown` / `in-copyright-short-quotes-only` / `unverified` |
| status | ✅ | `registered` / `partial` / `complete` |

---

## cards/<id>-<short-title>.md

```yaml
---
id: sk-0001
type: quote
title: "后进生是花园里最娇嫩的花"
lang: zh-CN
topics:
  - learning-difficulties
source: on-education
ref: "On Education, Progress Publishers 1977, p. 22 (EPUB page 23)"
url: ""
status: reviewed
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
reviewed_by: ""
---
```

### type 判定规则

| 值 | 判定 |
|---|---|
| `quote` | 直接引文；正文必须有 `## 原文/Excerpt` |
| `case` | 书中具体人物/事件/学校经历的叙事 |
| `principle` | 可被引文支撑的价值判断/教育立场 |
| `method` | 有步骤、可迁移的操作方法 |
| `practice` | 作者/学校实际使用、可观察的实践形态 |

一条内容同时命中多类时：优先按主形态选一类，另在正文 `## 说明` 中注明关联类型。

### 正文固定结构

```
## 原文/Excerpt        # 至少 quote 必填
## 中文转述/说明
## 教育场景/应用
## 出处核对
```

原文与转述分离，原文不进 frontmatter。

---

## topics/<topic-slug>.md

```yaml
---
slug: learning-difficulties
title: "学习困难学生"
aliases:
  - 后进生
summary: "一句话定位"
card_ids:
  - sk-0001
source_ids:
  - on-education
related_topics: []
status: reviewed
updated: "YYYY-MM-DD"
---
```

### 正文固定结构

```
## 核心判断
## 典型教育场景
## 可操作方法
## 相关卡片
## 跨书综合
## 编辑者建议（可选）
## 待验证/缺口
```

实质断言必须用 `（参见 sk-XXXX）` 挂卡；无卡支撑的判断放“编辑者建议”。

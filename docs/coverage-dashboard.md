# 覆盖仪表盘 Coverage Dashboard

> 由 `scripts/coverage_report.py` 自动生成；只读卡片后写本文件。
> 用途：一眼看清每个来源的卡片量、页码覆盖和当前缺口。

## 总览

- 卡片总数：**980**
- 来源数：**12**
- 主题数：**12**
- 《做人的故事》：**540 张卡 / 540 个目录标题**

## 来源覆盖

| 来源 | 卡片数 | 含印刷页码 ref |
|---|---:|---:|
| 做人的故事（`zuo-ren-de-gu-shi-zh`） | 540 | 540/540 |
| 苏霍姆林斯基选集（五卷本）第5卷（`xuan-ji-zh-vol5`） | 109 | 109/109 |
| 苏霍姆林斯基选集（五卷本）第3卷（`xuan-ji-zh-vol3`） | 52 | 51/52 |
| 苏霍姆林斯基选集（五卷本）第2卷（`xuan-ji-zh-vol2`） | 51 | 45/51 |
| On Education（`on-education`） | 41 | 0/41 |
| 苏霍姆林斯基选集（五卷本）第4卷（`xuan-ji-zh-vol4`） | 41 | 41/41 |
| 苏霍姆林斯基选集（五卷本）第1卷（`xuan-ji-zh-vol1`） | 38 | 36/38 |
| 把心献给孩子（`ba-xin-xian-gei-hai-zi-zh`） | 35 | 0/35 |
| 给教师的建议（`gei-jiao-shi-de-jian-yi-zh`） | 23 | 23/23 |
| To Children I Give My Heart（`to-children-i-give-my-heart`） | 22 | 0/22 |
| Each One Must Shine: The Educational Legacy of V. A. Sukhomlinsky（`each-one-must-shine`） | 16 | 0/16 |
| The Singing Feather (会唱歌的羽毛)（`singing-feather`） | 12 | 0/12 |

## 卡片类型

| 类型 | 数量 |
|---|---:|
| `case` | 588 |
| `quote` | 256 |
| `principle` | 79 |
| `method` | 35 |
| `practice` | 22 |

## 主题分布

| 主题 | 卡片数 |
|---|---:|
| 爱的教育（`love-education`） | 370 |
| 儿童研究（`child-study`） | 270 |
| 家校合作（`family-school`） | 223 |
| 美育与自然（`aesthetic-nature-education`） | 218 |
| 集体教育（`collective-education`） | 195 |
| 劳动教育（`labor-education`） | 171 |
| 教师成长（`teacher-growth`） | 133 |
| 思维课与大自然（`thinking-and-nature`） | 107 |
| 学习困难学生（`learning-difficulties`） | 64 |
| 阅读与书籍（`reading-and-books`） | 51 |
| 健康第一（`health-first`） | 36 |
| 评价与分数（`assessment-grading`） | 33 |

## 当前已知缺口

- 《做人的故事》540 个目录标题已全部建卡；页码已与 OCR 正文页逐条核对（含 OCR 异体字/错字映射）。
- 《苏霍姆林斯基讲美德故事》44 篇中，已确认同源 15 篇；其余继续用关键词核正文。
- 113 篇官方故事：标题已对齐，全文覆盖尚未逐一标注。
- 562 篇期刊文章：仅第五卷 68 篇已覆盖；其余受合法获取渠道限制，暂缓。
- 英文/电子本（On Education、To Children I Give My Heart、Each One Must Shine、Singing Feather、把心献给孩子）：暂用本地文件/行号定位，未统一到印刷页码。

## 维护命令

```bash
python scripts/validate_all.py
python scripts/check_kb.py
python scripts/audit_cards.py
python scripts/coverage_report.py
python scripts/build_site.py
```

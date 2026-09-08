# 覆盖仪表盘 Coverage Dashboard

> 由 `scripts/coverage_report.py` 自动生成；只读卡片后写本文件。
> 用途：一眼看清每个来源的卡片量、页码覆盖和当前缺口。

## 总览

- 卡片总数：**1206**
- 来源数：**12**
- 主题数：**12**
- 《做人的故事》：**540 张卡 / 540 个目录标题**

## 来源覆盖

| 来源 | 卡片数 | 含印刷页码 ref |
|---|---:|---:|
| 做人的故事（`zuo-ren-de-gu-shi-zh`） | 540 | 540/540 |
| 苏霍姆林斯基选集（五卷本）第2卷（`xuan-ji-zh-vol2`） | 159 | 45/159 |
| 苏霍姆林斯基选集（五卷本）第5卷（`xuan-ji-zh-vol5`） | 116 | 109/116 |
| 苏霍姆林斯基选集（五卷本）第3卷（`xuan-ji-zh-vol3`） | 97 | 51/97 |
| 苏霍姆林斯基选集（五卷本）第4卷（`xuan-ji-zh-vol4`） | 77 | 41/77 |
| 苏霍姆林斯基选集（五卷本）第1卷（`xuan-ji-zh-vol1`） | 67 | 36/67 |
| On Education（`on-education`） | 41 | 0/41 |
| 把心献给孩子（`ba-xin-xian-gei-hai-zi-zh`） | 35 | 0/35 |
| 给教师的建议（`gei-jiao-shi-de-jian-yi-zh`） | 24 | 23/24 |
| To Children I Give My Heart（`to-children-i-give-my-heart`） | 22 | 0/22 |
| Each One Must Shine: The Educational Legacy of V. A. Sukhomlinsky（`each-one-must-shine`） | 16 | 0/16 |
| The Singing Feather (会唱歌的羽毛)（`singing-feather`） | 12 | 0/12 |

## 卡片类型

| 类型 | 数量 |
|---|---:|
| `case` | 637 |
| `quote` | 260 |
| `principle` | 176 |
| `method` | 99 |
| `practice` | 34 |

## 主题分布

| 主题 | 卡片数 |
|---|---:|
| 爱的教育（`love-education`） | 459 |
| 儿童研究（`child-study`） | 373 |
| 家校合作（`family-school`） | 272 |
| 美育与自然（`aesthetic-nature-education`） | 259 |
| 集体教育（`collective-education`） | 242 |
| 劳动教育（`labor-education`） | 203 |
| 教师成长（`teacher-growth`） | 201 |
| 思维课与大自然（`thinking-and-nature`） | 168 |
| 学习困难学生（`learning-difficulties`） | 99 |
| 阅读与书籍（`reading-and-books`） | 80 |
| 健康第一（`health-first`） | 51 |
| 评价与分数（`assessment-grading`） | 40 |

## 当前已知缺口

- 《做人的故事》540 个目录标题已全部建卡；页码已与 OCR 正文页逐条核对（含 OCR 异体字/错字映射）。
- 《苏霍姆林斯基讲美德故事》44 篇已全量盘点：31 篇确认同源、11 篇高度可能、2 篇仅主题相关；详见 `docs/story-coverage-meide-gushi.md`。
- 113 条官方故事书目已盘点并完成全量核验：98/113 高置信可挂现有卡（10 A + 88 H；15 条 E_none）；另用本地全文补建 sk-1085–sk-1091 等故事卡。
- 五卷本已按作品统计（`docs/coverage-volumes.md`），并完成章节级覆盖审计与三轮剩余缺口审计：原 143 个 gap 中 115 个已不再空白、27 个仍空白、1 个口径存疑；详见 `docs/coverage-volumes-chapters.md` 与 `docs/coverage-volumes-gaps-remaining-round3.md`。
- 562 篇期刊文章：仅第五卷 68 篇已覆盖；其余受合法获取渠道限制，暂缓。
- 英文/电子本（On Education、To Children I Give My Heart、Each One Must Shine、Singing Feather、把心献给孩子）：暂用本地文件/行号定位，未统一到印刷页码。

## 维护命令

```bash
python scripts/validate_all.py
python scripts/check_kb.py
python scripts/audit_cards.py
python scripts/coverage_report.py
python scripts/coverage_volumes.py
python scripts/build_site.py
```

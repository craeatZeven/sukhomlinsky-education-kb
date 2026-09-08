# 本地已有全文资产盘点（2026-09-08）

> 用途：把“已经合法拿到并可检索”的材料整理成一张总表；难找的 450 篇期刊文章暂不追。
> 所有本地 OCR/全文文件都在 gitignored `local_working_copy/`，不入 GitHub。

## 一、全文/OCR 资产

| 资产 | 版本/来源 | 本地文件 | 规模 | 卡片数 |
|---|---|---|---|---|
| 苏霍姆林斯基选集（五卷本）第1卷 | 教育科学出版社，中文扫描 OCR | `ocr/mineru-range/merged/苏霍姆林斯基选集（五卷本）第1卷.txt` | 1.39 MB | 38 |
| 苏霍姆林斯基选集(五卷本)第2卷 | 同上 | `.../第2卷.txt` | 1.40 MB | 51 |
| 苏霍姆林斯基选集（五卷本）第3卷 | 同上 | `.../第3卷.txt` | 1.59 MB | 53 |
| 苏霍姆林斯基选集(五卷本)第4卷 | 同上 | `.../第4卷.txt` | 1.46 MB | 41 |
| 苏霍姆林斯基选集（五卷本）第5卷 | 同上（68篇论文集） | `.../第5卷.txt` | 1.43 MB | 109 |
| 给教师的建议 | 杜殿坤编译，教育科学 | `.../苏霍姆林斯基-给教师的建议.txt` | 1.02 MB | 23 |
| 做人的故事 | 诸惠芳等译，人民教育 2015，读秀图像 OCR | `zuoren-gushi-full-ocr.md` / `zuoren-gushi-ocr-pages.jsonl` | 443页 / 24.2万字 | 540（540/540 标题已建卡） |
| On Education | Progress 1977 英文 | 本地 EPUB/文本（见 source） | — | 41 |
| To Children I Give My Heart | 英文公开版 | 本地 PDF/txt | — | 22 |
| Each One Must Shine | Alan Cockerill 英文 | 本地 txt | — | 16 |
| The Singing Feather | 英文儿童故事集，Archive.org | `singing-feather.txt` | 16 KB | 12 |
| 把心献给孩子（中文） | EPUB 抽取 | 本地 EPUB | — | 35 |

## 二、可检索的书目/索引资产

| 文件 | 内容 | 规模 |
|---|---|---|
| `official-bibliography-1987.txt` | 1987官方传记书目全文 | 633 KB |
| `bibliography-1987-entries.csv` | 结构化 1082 条 | 1082 行 |
| `articles-562-coverage.csv` / `articles-485-availability.csv` | 562篇文章覆盖/可获得性 | 562 行 |
| `tales-113-coverage.csv` / `tales-113-inventory.md` | 113篇故事标题对齐/清单 | 113 条 |
| `zuoren-story-index.csv` | 《做人的故事》540个标题→首次页码 | 540 行（527个已定位） |
| `content-matrix.csv/md` | 卡片内容矩阵 | 447 卡（已随建卡更新） |
| `story-title-matches.txt` | 44篇美德故事在五卷本中的精确命中 | — |
| `story-title-zuoren-candidates.txt` | 44篇 vs 《做人的故事》候选映射 | — |

## 三、未纳入的临时文件

`local_working_copy/tmp_*.html/txt/pdf`（koob、studfile、multiurok 等来源）是早期试探下载，**来源授权不明，不计入正式资产，也不用于建卡**。需要时再单独评估或删除。

## 四、当前覆盖口径

- 卡片总数：1049（13 sources / 12 topics）
- 核心著作：五卷本 + 给教师的建议 + 做人的故事 已形成可检索中文全文池
- 《做人的故事》：540/540 个目录标题均已建卡（含 OCR 异题/异体字按正文校订；507「狼良的牙齿」按正文题名「狼的牙齿」建卡；323「会唱歌的羽毛」另有 ZuoRen 中文原版卡 sk-0982）
- 儿童故事：44 篇美德故事已全量盘点——31 篇确认同源、11 篇高度可能、2 篇仅主题相关（见 `docs/story-coverage-meide-gushi.md`）
- 五卷本：已按作品统计卡片来源分布（见 `docs/coverage-volumes.md`），并完成章节级覆盖审计（见 `docs/coverage-volumes-chapters.md`）：310 个审计单位中 13 covered / 154 partial / 143 gap
- 562篇文章：仅第5卷68篇（77条目）已覆盖；其余暂缓
- 113条官方故事书目：已盘点，并完成“条目↔卡片”对照草稿：92/113 高置信可挂现有卡（20 条抽样复核后修正 1 条；见 `docs/coverage-official-tales.md`、`docs/coverage-official-tales-mapping.md`、`docs/coverage-official-tales-mapping-verification.md`）

## 五、下一步（整理向）

1. 《做人的故事》540 个标题已全部建卡；后续只做按需修订（页码/异文/主题归类）；
2. 44 篇美德故事：优先人工复核 11 篇 probable 和 2 篇 thematic；
3. 113 条官方书目：人工抽检 93 条高置信映射，补齐 5 条 medium 与 15 条 none；
4. 五卷本：按 `docs/coverage-volumes-chapters.md` 的优先清单，先补 20 个高价值 gap 章节；
5. 定期重建 `scripts/check_kb.py` + `scripts/build_site.py`，保持索引与网页同步。

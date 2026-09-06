# 书源盘点 Book Inventory

> 本页登记已纳入知识库体系的全部本地苏霍姆林斯基资料与补充公版/公开全文来源。
> 绝对路径不进入公开仓库；本地工作副本映射见 `local_working_copy/source-map.md`（已 gitignore）。

## 本地书源（12 份文件 → 10 个唯一书源）

| 本地文件名 | 对应 source slug | 语言 | 可读性/处理状态 |
|---|---|---|---|
| On Education - Sukhomlinsky.epub | `on-education` | EN | ✅ 已抽纯文本 |
| To Children I Give My Heart.txt | `to-children-i-give-my-heart` | EN | ✅ 纯文本 |
| To Children I Give My Heart.pdf | `to-children-i-give-my-heart` | EN | ✅ 有文字层（备用） |
| 把心献给孩子(...).epub | `ba-xin-xian-gei-hai-zi-zh` | ZH | ✅ 已抽纯文本 |
| 苏霍姆林斯基-给教师的建议.pdf | `gei-jiao-shi-de-jian-yi-zh` | ZH | ⚠️ 扫描版，待 OCR |
| 苏霍姆林斯基教育箴言.pdf | `jiao-yu-zhen-yan-zh` | ZH | ✅ OCR 完成（318 页） |
| 苏霍姆林斯基选集（五卷本）第1卷.pdf | `xuan-ji-zh-vol1` | ZH | ⚠️ 扫描版，待 OCR |
| 苏霍姆林斯基选集（第一卷）.pdf | `xuan-ji-zh-vol1` | ZH | ⚠️ 疑似与上一条重复 |
| 苏霍姆林斯基选集(五卷本)第2卷.pdf | `xuan-ji-zh-vol2` | ZH | ⚠️ 扫描版，待 OCR |
| 苏霍姆林斯基选集（五卷本）第3卷.pdf | `xuan-ji-zh-vol3` | ZH | ⚠️ 扫描版，待 OCR |
| 苏霍姆林斯基选集(五卷本)第4卷.pdf | `xuan-ji-zh-vol4` | ZH | ⚠️ 扫描版，待 OCR |
| 苏霍姆林斯基选集（五卷本）第5卷.pdf | `xuan-ji-zh-vol5` | ZH | ⚠️ 扫描版，待 OCR |

## 补充公开全文/可获取来源

| 书目 | slug | 说明 |
|---|---|---|
| Each One Must Shine: The Educational Legacy of V. A. Sukhomlinsky (Alan Cockerill, 2009) | `each-one-must-shine` | Archive.org 有全文文本；当前环境直连超时，待网络可用后下载 |

## 已知待办

- [x] 《苏霍姆林斯基教育箴言》318 页 OCR 完成（EasyOCR）
- [x] MinerU 3.4.5 安装并验证通过（pipeline + OCR 中文）
- [x] MinerU 模型缓存已迁至 D 盘（避免 C 盘占满）
- [ ] 《给教师的建议》574 页 OCR（MinerU 后台任务 `pwsh-15` 进行中）
- [ ] 五卷本第 1–5 卷 OCR（MinerU 排队中，共约 4607 页）
- [ ] 核对“选集（第一卷）”与“选集（五卷本）第1卷”是否同版
- [ ] 下载 Each One Must Shine 全文文本
- [ ] 建立各中文书“目录/章节/页码”索引

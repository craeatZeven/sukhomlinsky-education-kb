# tools/web-audit —— 网页回归验证（唯一权威）

这个目录里是**唯一**能证明「网页还正常」的自动化证据。它不测数据（数据由
`python scripts/validate_all.py` 这条离线链负责），它测的是**浏览器里真正渲染出来的东西**：
真实 Chrome、真实 `web/data/*.json`、真实布局与颜色。

## 怎么跑

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File tools\web-audit\run-audit.ps1
```

脚本会自己在仓库根起一个 `python -m http.server 8123`，依次跑两个验证，再关掉服务。
不需要先手动起服务。

- 退出码 `0` = 全通过；`2` = 有判据没过；`1` = 验证脚本自身崩了。
- 结果 JSON 落在 `tools/web-audit/out/`（已 gitignore，属于运行产物）。
- 可调环境变量：`KB_ROOT`（默认从脚本位置推两级上去）、`AUDIT_BASE`（默认 `http://127.0.0.1:8123/`）、
  `AUDIT_CHROME`、`KB_PYTHON`。

单独跑其中一个：

```powershell
$env:AUDIT_BASE='http://127.0.0.1:8123/'; node tools\web-audit\verify-hardened.mjs
```

## 两份脚本各自管什么

### `verify-hardened.mjs` —— 24 条判据

| 分区 | 条数 | 在防什么 |
|---|---|---|
| 检索 | 3 | 自然问句真的命中对应预设问题、命中卡真的是讲那件事的、总数如实显示（不是把每页 30 当总数） |
| 地图 | 4 | 延迟索引 + 连点两次不错配（竞态）、窄屏与桌面的板块顺序 |
| 移动导航 | 3 | 每个链接文字是**单行**、没有越界、锚点跳转后标题停在顶栏正下方 |
| 入门卡 | 3 | 三张按角色挑（为什么 / 怎么做 / 一个教学案例）、互不重复、真的落在**首屏内** |
| 相关案例 | 2 | 张数从 `classification.json` **现算**（不从被测分片反推）、与主归属重叠的部分有披露 |
| 对比度 | 6 | 三套主题各自主题一致、三档齐全且达 WCAG AA 4.5:1 |
| 原文待补标记 | 1 | 标记存在且**真的可见**（不在被裁剪的段落里） |
| 原文身份 | 1 | 没有卡片把「转述/非直引」写进原文摘录槽位（独立扫 `web/data.json`） |
| 通用 | 1 | 全流程无 JS 异常 |

每份结果都带 `dataVersion`（`classification.json` 与 `web/data.json` 的 sha256 前 12 位 + `meta.generated`）。
看到一份结果而不知道它对应哪份数据，等于没有证据。

### `verify-contrast-census.mjs` —— 3 主题 × 7 页面对比度普查

`green` / `paper` / `dark` 三套主题，跑 `index / entries / entry?code=A11 / clusters / facets / card?id=sk-0001 / problem`
七个页面，对 `h1 h2 h3 p .meta .angle-note .section-sub .row-title .row-desc .row-go .badge .chip .ref .cn a`
逐类采样（每类前 6 个），按 WCAG AA 判定（小字 4.5:1，大字/粗体 3:1）。
七个页面 × 三套主题 = 21 个组合；最近一次运行共采样 **798 处**文本（这个数字随页面内容浮动，
不要把它当门槛，门槛是"任何一处不达标就 FAIL"）。

## 为什么这些判据长这样（不是形式主义）

这份脚本是**第二轮复审逐条逼出来的**（`docs/codex-rereview-opinion.md` §A）。原来的检查会假通过：

- 案例张数的 expected 来自**同一个分片** → 上游和分片同时丢数据也照样 PASS；
  现在一律从 `classification.json` / `web/data.json` 现算。
- 只断言 `rows > 0` → 返回任意无关卡也能过；现在核对**具体 ID**。
- 查移动导航查的是**盒子 top 的数量**，不是文字行数 → flex 换行不溢出，永远测不出来；现在用 `Range` 量行数。
- 入门卡只比 `startTop < primaryTop` → 两张都在屏幕下面也能过；现在断言真的在**首屏内**。
- 对比度找不到某档**直接跳过**，不让整体失败；现在缺档即失败。

这套判据**真的抓到过东西**，不是摆设：

- `.bar` 类名撞车 → 地图比例条高度被算成 0，**肉眼完全看不见**，而所有宽度检查全是 PASS。
- 三主题普查才发现的两处真实不达标：`.chip--primary` 在 dark 主题只有 2.39:1（修到 7.32）、
  `.row-go` 在 paper 主题 4.36:1（修到 5.22）。只验一套主题的话这两处会一直躺在那里。
- 顶栏 10 个标签在中等宽度换行成两行 —— `scrollWidth` 检查测不到（flex 是换行，不是溢出）。

## 与 `local_working_copy/web-audit/` 的关系

`local_working_copy/` 里还留着几十个早前几轮用过的一次性探针（`_dbg-*.mjs`、已被取代的
`verify-*.mjs`、参考站截图等）。那些**不再维护**，保留只为可追溯。真正要长期跑的就是这里两份。
`local_working_copy/` 在 `.gitignore` 里，所以那份副本在全新 clone 里根本不存在 —— 这正是把它们
搬进版本库的原因：一个项目不能只有一台机器上才有回归证据。

## 加新判据时

判据必须**能真的失败**：先想清楚"什么样的错误会让它 FAIL"，再用那个错误试一次。
这个项目在这一点上翻过车 —— 曾经有一条 `hasCase === caseSectionShown` 的同义反复判据，
两边同时为 false 时照样 PASS，结果放过了一次 `case_entries` 被整体清空（116 条）的事故。

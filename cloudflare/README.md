# Cloudflare Workers + D1 版后端（免运维）

> 与 `api/`（FastAPI 版）**接口形状完全一致**，`web/search.html` 不用改代码，只改 `web/config.js` 里的 `apiBase`。
> 选它是因为：无需服务器、免费额度足够、全球边缘节点、数据库用托管 SQLite（D1）。

## 零、当前部署状态（2026-09-09 已上线）

| 项 | 值 |
|---|---|
| Worker 地址 | **https://suk-kb-api.suk-kb.workers.dev** |
| 版本 ID | `d324cabb-dec3-420b-b5c2-8c9804abbde3` |
| D1 数据库 | `suk-kb` · id `e8883afd-c7e5-4b9b-bb84-fa3be965a3c8` · 区域 WNAM |
| workers.dev 子域 | `suk-kb` |
| 数据量 | 1386 卡 / 2970 主题关联 / FTS5 1386 行 |
| CORS | 已收紧为 `https://craeatzeven.github.io` |
| 前端接线 | `web/config.js` 的 `apiBase` 已指向该地址；Pages 上的 `search.html` 实测已连上后端 |

**线上实测（2026-09-09）**：

| 检查 | 结果 |
|---|---|
| `/api/health` | `{"status":"ok","cards":1386,"backend":"cloudflare-workers-d1"}` |
| `/api/meta` | 1386 卡 / 12 来源 / 12 主题 |
| `/api/search?q=劳动` | `like-short-query` · 372 命中 |
| `/api/search?q=苏霍姆林斯基` | `fts-trigram` · 771 命中 |
| `/api/search?q=劳动 教育` | 336 命中 |
| `/api/random`、`/api/coverage` | 正常 |
| GitHub Pages `search.html` | 显示「后端已连接 · 共 1386 张卡」，渲染 20 条/页、70 页 |

> ⚠️ **网络注意**：本机用 Python/curl 访问 `*.workers.dev` 会失败（DNS 被污染到 75.126.150.210 / 67.228.235.93，TLS 握手被重置），但 **Chrome 能正常打开**（浏览器自带 DoH）。
> 也就是说：**浏览器/用户能访问，脚本类客户端在国内网络可能不行**。
> 如果主要受众在中国大陆，建议给 Worker 绑一个**自定义域名**（见下节末尾），`*.workers.dev` 在国内普遍被屏蔽。

```
cards/*.md ──scripts/build_d1_sql.py──▶ cloudflare/{schema.sql,data.sql,schema_fts.sql,coverage.json}
                                              │  wrangler d1 execute --file
                                              ▼
                                        D1（托管 SQLite）
                                              │  env.DB
                                        Worker（cloudflare/src/index.js）
                                              ▼
                                    https://suk-kb-api.<你的子域>.workers.dev/api/*
```

---

## 一、部署（约 10 分钟，全部命令在 `cloudflare/` 目录下执行）

> **在 Windows 上跑，不要用 WSL。** 本仓库在 `D:\Git\sukhomlinsky-education-kb`，
> PowerShell 里 `cd D:\Git\sukhomlinsky-education-kb\cloudflare`；
> 本机 Python 是 `D:\python\python.exe`（WSL 里既没有 `python` 命令，npm 还配着一个不通的代理）。

```bash
cd D:\Git\sukhomlinsky-education-kb\cloudflare
npm install                       # 安装 wrangler（首次；本机已装好可跳过）

# 1) 生成 SQL（在仓库根目录执行）
D:\python\python.exe ..\scripts\build_d1_sql.py --fts

# 2) 登录 Cloudflare（浏览器授权，只需一次）
npx wrangler login

# 3) 创建 D1 数据库，把输出里的 database_id 填进 wrangler.toml
npx wrangler d1 create suk-kb

# 4) 建表 + 导入数据（1386 张卡，约 3.1 MB）
npx wrangler d1 execute suk-kb --remote --file=./schema.sql --yes
npx wrangler d1 execute suk-kb --remote --file=./data.sql --yes

# 5) 可选：FTS5 全文索引（若这步报错，跳过即可——Worker 会自动回退 LIKE 检索）
npx wrangler d1 execute suk-kb --remote --file=./schema_fts.sql --yes

# 6) 上线
npx wrangler deploy
```

部署完会打印一个地址，形如 `https://suk-kb-api.<你的子域>.workers.dev`。验证：

```bash
curl https://suk-kb-api.<你的子域>.workers.dev/api/health
curl "https://suk-kb-api.<你的子域>.workers.dev/api/search?q=劳动&size=3"
```

## 二、把前端接上

编辑 `web/config.js`：

```js
window.KB_CONFIG = { apiBase: "https://suk-kb-api.<你的子域>.workers.dev" };
```

然后 commit + push。GitHub Pages 上的 `search.html` 就会走这个后端（页面本身仍是静态托管，只有检索/分页走 API）。

**同时把 CORS 收紧**：编辑 `cloudflare/wrangler.toml` 的 `CORS_ORIGIN`，从 `"*"` 改成
`"https://craeatzeven.github.io"`，再 `npx wrangler deploy` 一次。

## 三、本地预览（不需要 Cloudflare 账号）

```bash
cd D:\Git\sukhomlinsky-education-kb\cloudflare
npm install                 # 安装 wrangler（首次；本机已装好可跳过）
npm run db:schema:local     # 本地 D1：建表
npm run db:data:local       # 导入 1386 张卡
npm run db:fts:local        # 可选：FTS5 索引
npm run dev                 # http://127.0.0.1:8787
```

**本地实测（2026-09-09，wrangler 4.130.0）**：`cards=1386 / card_topics=2970 / cards_fts=1386`；
`/api/health` 返回 `{"status":"ok","cards":1386,"backend":"cloudflare-workers-d1"}`；
检索结果与 FastAPI 版**逐项一致**（`劳动` 372、`教育` 1243、`苏霍姆林斯基` 771 走 FTS5、`劳动 教育` 336、`情感教育` 9）；
`web/search.html` 把 `apiBase` 指向该 Worker 后跨源渲染正常（20 条/页，70 页）。

> ⚠️ 踩坑记录：D1 单条 SQL 语句有大小上限，`data.sql` 按 60 KB 分批会报 `SQLITE_TOOBIG`，
> 现已改为**按字符数动态分批（≤25 KB/条）**，`data.sql` 95 条语句、`schema_fts.sql` 65 条语句，导入正常。

## 四、接口

与 `api/README.md` 的接口表一致：`/api/health`、`/api/meta`、`/api/search`、`/api/cards/{id}`、
`/api/cards?ids=`、`/api/random`、`/api/related/{id}`、`/api/sources[/{slug}]`、
`/api/topics[/{slug}]`、`/api/coverage`。

检索策略（`src/index.js`）：

1. 查询词**全部 ≥3 字**且 D1 支持 FTS5 → `MATCH` + `bm25` 排序（`mode: fts-trigram`）；
2. 含 **1–2 字**中文词（劳动/教育）→ 长词用 FTS 缩小集合、短词用 LIKE 过滤（`mode: fts+like`）；
3. D1 不支持 FTS5（或探测失败）→ 全部 LIKE（`mode: like*`）。

> D1 对 FTS5 的支持取决于其 SQLite 版本；本 Worker 在第一次请求时探测一次，
> 探测失败自动降级，**不会因为 FTS 不可用而报错**。

## 五、成本与限制（免费额度，2025 年档位）

| 项 | 免费额度 | 本库消耗 |
|---|---|---|
| Worker 请求 | 10 万次/天 | 每次检索 1 个请求 |
| D1 读行数 | 500 万行/天 | 一次 LIKE 检索约扫 1386 行 → 约 3600 次检索/天 |
| D1 存储 | 5 GB | 约 5 MB（data.sql 3.4 MB + FTS 2 MB） |

超过免费额度会按量计费；公开分享前建议加 Cloudflare 的 Rate limiting 规则（免费版可配 1 条）。

## 六、更新数据（每次补卡后）

```bash
python scripts/build_d1_sql.py --fts
cd cloudflare
npx wrangler d1 execute suk-kb --remote --file=./schema.sql --yes      # 清表重建
npx wrangler d1 execute suk-kb --remote --file=./data.sql --yes
npx wrangler d1 execute suk-kb --remote --file=./schema_fts.sql --yes  # 可选
npx wrangler deploy
```

> `schema.sql` 里带 `DROP TABLE`，重复导入是幂等的（先清后建）。

## 七、不提交到仓库的产物

`cloudflare/` 下这几类是**构建产物**，已加入 `.gitignore`：
`node_modules/`、`data.sql`、`schema_fts.sql`、`coverage.json`、`.wrangler/`。
`schema.sql`、`wrangler.toml`、`package.json`、`src/index.js`、`README.md` 是源码，随仓库提交。

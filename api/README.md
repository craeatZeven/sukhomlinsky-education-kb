# 知识库后端 API（FastAPI + SQLite FTS5）

> 状态：**可运行的本地/自托管原型**（2026-09-09 实测通过：1386 张卡，检索/分页/聚合/相关卡全部正常）。
> 本目录不属于 GitHub Pages 静态站；Pages 上仍跑纯静态版，二者可并存。

---

## 一、它是什么

把仓库里的 `cards/*.md` 构建成一个**只读 SQLite 数据库**（含 FTS5 全文索引），用 FastAPI 暴露 JSON 接口，
同时把 `web/` 静态站挂在同一个进程上——一个端口就能同时提供「网页 + API」，便于自托管与分享。

```
cards/*.md ──scripts/build_db.py──▶ api/kb.db（SQLite + FTS5 trigram）
                                        │
                          api/main.py（FastAPI）
                                        ├── /api/*      给前端与第三方调用
                                        └── /            托管 web/ 静态站
```

## 二、本地跑起来

```bash
# 1) 建库（每次改卡后重跑；只读库，可随时删除重建）
python scripts/build_db.py                # 默认输出 api/kb.db，并自动做一次自检

# 2) 起服务
pip install -r api/requirements.txt
uvicorn api.main:app --host 127.0.0.1 --port 8000

# 3) 打开
#    网页（含 API 检索页）：http://127.0.0.1:8000/search.html
#    接口文档（Swagger）：   http://127.0.0.1:8000/docs
```

本机环境实测可用版本：Python 3.10.10 / SQLite 3.39.4（FTS5 trigram 可用）/ fastapi 0.141 / uvicorn 0.49。

## 三、接口

| 方法 | 路径 | 说明 |
|---|---|---|
| GET | `/api/health` | 健康检查（返回卡片数、数据库路径） |
| GET | `/api/meta` | 总数 + 来源/主题/类型聚合 |
| GET | `/api/search?q=&source=&topic=&type=&page=&size=` | 检索 + 过滤 + 分页；返回 `mode`/`total`/`pages`/`items`（含 `snippet`） |
| GET | `/api/cards/{id}` | 单卡（含完整摘录） |
| GET | `/api/cards?ids=a,b,c` | 批量取卡 |
| GET | `/api/random` | 随机一卡 |
| GET | `/api/related/{id}?limit=8` | 同主题 / 同来源的相关卡 |
| GET | `/api/sources`、`/api/sources/{slug}` | 来源列表 / 某来源的卡 |
| GET | `/api/topics`、`/api/topics/{slug}` | 主题列表 / 某主题的卡 |
| GET | `/api/coverage` | 转发 `web/coverage.json` |

### 检索说明（重要）

FTS5 使用 **trigram 分词**（中文按 3 字滑窗），因此：

- 查询词 **≥3 字** → 走 FTS5（`bm25` 排序，`mode: fts-trigram`）；
- 查询词 **1–2 字**（「劳动」「教育」「兴趣」这类高频词）→ 自动回退 `LIKE` 子串扫描（`mode: like-short-query`，1386 行毫秒级）；
- **多词**按空格切分，做 AND 关系；长词用 FTS 缩小集合、短词再 LIKE 过滤（`mode: fts+like`）。

实测样例（1386 张卡）：

| 查询 | 模式 | 命中 |
|---|---|---:|
| `劳动` | like-short-query | 372 |
| `教育` | like-short-query | 1243 |
| `苏霍姆林斯基` | fts-trigram | 771 |
| `劳动 教育` | like-short-query | 336 |
| `怎样培养真正的人` | fts-trigram | 119 |
| `情感教育` | fts-trigram | 9 |

> 若日后要更好的中文分词，可选方案：构建期用 jieba 预分词 + `unicode61` 分词器；或用 SQLite 的 `simple` 扩展。
> 当前方案零依赖、可复现，先满足需求。

## 四、前端怎么接

- `web/search.html` 是配套的「API 检索页」：服务端检索 + 分页 + 聚合 + 摘要 + 导出本页 JSON/CSV。
- `web/config.js` 里 `apiBase`：
  - 留空 `""` → 与页面同源（页面由本服务托管时用这个）；
  - 填后端地址（如 `https://kb-api.example.workers.dev`）→ 前端在 GitHub Pages、后端在别处时用这个。
- 若 `apiBase` 指向的服务不可用，`search.html` 会显示明确的错误提示，不影响其它静态页。

## 五、自托管 / 部署选项

| 方案 | 命令/要点 | 适用 |
|---|---|---|
| 本机 | 见第二节 | 自己用、局域网分享 |
| Docker | `docker compose up -d --build` → `http://<主机>:8000` | 有一台 VPS 就够 |
| Cloudflare Workers + D1 | 需要把 `kb.db` 导入 D1，并把接口改写成 Workers 路由（本目录未提供，属后续工作） | 免运维、有免费额度 |
| 反向代理 + HTTPS | Nginx/Caddy 反代 8000 端口，设置 `KB_CORS_ORIGINS=https://你的前端域名` | 公开分享 |

**分享前务必注意**：
1. `KB_CORS_ORIGINS` 不要长期留 `*`，改成你的前端域名；
2. 这是**只读**接口，没有写入路径，但公网暴露仍需加限流/防滥用（Cloudflare 免费版即可）；
3. 公开仓库里不要放数据库文件（`api/kb.db` 已加入 `.gitignore`，构建期生成）。

## 六、与静态站的关系

| | 静态站（GitHub Pages） | 后端 API |
|---|---|---|
| 托管 | GitHub Pages，零运维 | 需要自托管或 serverless |
| 首屏数据 | `web/data/` 分片按需加载：首页 9 KB gzip、卡片详情 ~12 KB、浏览页索引 306 KB gzip（2026-09-10 起，见 `docs/web-performance-sharding.md`） | 索引 ~几十 KB + 按需取卡 |
| 检索 | 浏览器内过滤（1386 张时 8–14 ms）；正文全文检索语料按需加载 | 服务端 FTS5 + 分页 + 聚合 |
| 可被程序调用 | 只能下载整包 `data.json` | 有 REST 接口 |
| 一次性渲染全量 | 布局约 **4,090 ms**（1351 张实测），因此移动端只渲染 24 张 | 不需要（服务端分页） |

两者不冲突：Pages 继续跑静态版，API 版作为 `search.html` 这条路径。

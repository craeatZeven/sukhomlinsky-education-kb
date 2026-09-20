# 全文检索接口（C 方案）

`api/fulltext.py` —— 把 `local_working_copy/fulltext/corpus.db`（书全文原子层，31,198 单元 / 616 万字）
以**只给命中片段**的方式提供出来。

## 为什么是这个形态（版权边界）
`NOTICE.md`：公开仓库只收短摘录，完整全文留在本地。所以：
- 单条片段上限 **180 字**（context 接口 420 字）
- 每次查询最多 **50 条**，最多翻 **5 页**
- **没有**按书/按页导出全文的接口，也没有能把全书捞完的翻页路径
- 想通读整本，只能去读纸本 —— 这是有意的

## 起服务
```
python -c "import uvicorn; uvicorn.run('api.main:app', host='127.0.0.1', port=8787)"
# 或沿用既有习惯： uvicorn api.main:app --host 127.0.0.1 --port 8000
```

## 接口
| 接口 | 说明 |
|---|---|
| `GET /api/fulltext/health` | 库在不在、多少单元、多少字、有哪些书 |
| `GET /api/fulltext/search?q=&limit=&page=&book=&min_len=` | 命中列表（片段 + 书/页/小节 + 单元号） |
| `GET /api/fulltext/context?unit=&q=` | 单条多一点上下文（仍 ≤420 字） |

`q` 至少 2 字；`limit` ≤50；`page` ≤5。

## 实测（2026-09-20）
- `health` → `{"ok":true,"units":31198,"chars":6159488,"books":[…12 本…]}`
- `search?q=集体舆论` → 4 条命中，片段带上下文（如第1卷 p791，《教师的人格在集体…》）
- 闸门：`limit=999` / `page=9` 被校验拒（422）；不存在的 unit → 404

## 还没做
站点前端还没接这个接口。接线要处理三件事：
① API 基址可配置（默认 `http://127.0.0.1:8787`）；
② 公用站点上 API 不可达时的**优雅降级**（回落到现有的卡片检索）；
③ 命中结果在页面上如何呈现（片段 + 「第几卷第几页」，并说明「全文在本地」）。
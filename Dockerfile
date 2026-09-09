# 知识库 API + 静态站（单进程托管）
# 构建：docker build -t suk-kb-api .
# 运行：docker run --rm -p 8000:8000 suk-kb-api
FROM python:3.11-slim

WORKDIR /app

COPY api/requirements.txt api/requirements.txt
RUN pip install --no-cache-dir -r api/requirements.txt

COPY scripts/ scripts/
COPY cards/ cards/
COPY sources/ sources/
COPY topics/ topics/
COPY web/ web/
COPY api/ api/

# 构建期生成只读 SQLite（含 FTS5 trigram 索引）
RUN python scripts/build_db.py --out /app/api/kb.db

ENV KB_DB=/app/api/kb.db \
    KB_CORS_ORIGINS=*

EXPOSE 8000
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]

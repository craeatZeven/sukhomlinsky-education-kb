-- 苏霍姆林斯基教育知识库 · Cloudflare D1 schema
-- 生成脚本：scripts/build_d1_sql.py
DROP TABLE IF EXISTS card_topics;
DROP TABLE IF EXISTS cards;
DROP TABLE IF EXISTS cards_fts;

CREATE TABLE cards (
  id TEXT PRIMARY KEY,
  type TEXT,
  title TEXT,
  source TEXT,
  ref TEXT,
  excerpt TEXT,
  excerpts_json TEXT,
  cn TEXT,
  topics_json TEXT,
  tags_json TEXT,
  created TEXT,
  updated TEXT,
  file TEXT
);
CREATE TABLE card_topics (
  card_id TEXT NOT NULL,
  topic TEXT NOT NULL
);
CREATE INDEX idx_cards_source ON cards(source);
CREATE INDEX idx_cards_type ON cards(type);
CREATE INDEX idx_card_topics_topic ON card_topics(topic);
CREATE INDEX idx_card_topics_card ON card_topics(card_id);

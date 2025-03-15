CREATE KEYSPACE IF NOT EXISTS ocr_data 
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

USE ocr_data;

CREATE TABLE IF NOT EXISTS user_auth (
    username TEXT PRIMARY KEY,
    password TEXT
);

CREATE TABLE IF NOT EXISTS documents (
    id UUID,
    user_id TEXT,
    documents TEXT,
    created_at TIMESTAMP,
    PRIMARY KEY(user_id, created_at)
);

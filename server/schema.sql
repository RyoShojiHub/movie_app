CREATE TABLE IF NOT EXISTS videos (
    id TEXT PRIMARY KEY,
    video_name TEXT,
    video_file_path TEXT,
    thumbnail_file_path TEXT,
    uploaded_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
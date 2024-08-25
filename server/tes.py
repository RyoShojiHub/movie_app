import os
import sqlite3
from server.database import get_db_connection

# データベース接続
connection = get_db_connection()
cursor = connection.cursor()

# データの挿入クエリ
insert_query = '''
INSERT INTO videos (id, video_name, video_file_path, thumbnail_file_path, uploaded_at)
VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)
'''

# ファイル名だけを保存
data = [
    ('1', 'Sample Video 1', 'video1.mp4', 'thumbnail1.png'),
    ('2', 'Sample Video 2', 'video2.mp4', 'thumbnail2.png'),
]

# データを挿入
cursor.executemany(insert_query, data)
connection.commit()

# 接続を閉じる
connection.close()

print("データが追加されました。")

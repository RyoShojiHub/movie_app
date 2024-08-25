import sqlite3
from server.database import get_db_connection

# データベース接続
connection = get_db_connection()
cursor = connection.cursor()

# 全てのデータを削除
delete_query = "DELETE FROM videos"
cursor.execute(delete_query)
connection.commit()

# 接続を閉じる
connection.close()

print("データが削除されました。")

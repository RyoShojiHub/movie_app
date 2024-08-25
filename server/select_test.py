'''
テスト用だから後でこのpythonファイル消していいよ
'''

import os
import sqlite3
from server.database import get_db_connection

connection = get_db_connection()
cursor = connection.cursor()
cursor.execute("SELECT * FROM videos")

rows = cursor.fetchall()

for r in rows:
    print(r)

connection.close()
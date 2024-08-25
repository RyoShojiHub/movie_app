import sqlite3
import os

BASE_PATH = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_PATH, 'database', 'app.db')


def get_db_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row # 行を辞書形式で返すように設定
    return connection


def init_db():
    connection = get_db_connection()
    with open(os.path.join(BASE_PATH, 'schema.sql')) as f:
        connection.executescript(f.read())
    connection.commit()
    connection.close()

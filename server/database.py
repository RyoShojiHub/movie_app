import sqlite3
import os

BASE_PATH = os.path.dirname(__file__)
DB_PATH = os.path.join(BASE_PATH, 'database', 'app.db')


def get_db_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row  # 行を辞書形式で返すように設定
    return connection


def init_db():
    connection = get_db_connection()
    with open(os.path.join(BASE_PATH, 'schema.sql')) as f:
        connection.executescript(f.read())
    connection.commit()
    connection.close()


def get_alldata():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM videos')
    all_data = cursor.fetchall()
    conn.close()
    return all_data


def insert_data(id, video_name, video_file_path, thumbnail_file_path):
    insert_query = '''
    INSERT INTO videos (id, video_name, video_file_path, thumbnail_file_path, uploaded_at)
    VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)
    '''
    data = (id, video_name, video_file_path, thumbnail_file_path)

    conn = get_db_connection()
    try:
        conn.execute(insert_query, data)
        conn.commit()
        print('データ追加成功')
    except Exception as e:
        return e
    finally:
        conn.close()
    return True


def delete_data(id):
    delete_query = '''
    DELETE FROM videos WHERE id=?;
    '''

    conn = get_db_connection()
    try:
        conn.execute(delete_query, (id,))
        conn.commit()
    except Exception as e:
        return e
    finally:
        conn.close()
    return True


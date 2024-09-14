import requests
import os

# clientディレクトリの絶対パスを取得し、URL.txtのパスを設定
client_dir = os.path.dirname(os.path.abspath(__file__))
url_file_path = os.path.join(client_dir, 'URL.txt')

# サーバのURL
with open(url_file_path, 'r') as f:
    URL = f.readline().strip()


def get_video_data():
    response = requests.get(URL)
    return response.json()

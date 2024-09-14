import requests
import os

from PIL import Image
from io import BytesIO

# サーバのURL
with open('URL.txt', 'r') as f:
    URL = f.readline().strip()


def get_video_data():
    response = requests.get(URL)
    return response.json()




import requests
import os

from PIL import Image
from io import BytesIO

URL = 'http://127.0.0.1:5000'


def get_video_data():
    response = requests.get(URL)
    return response.json()




import os

from flask import Blueprint, jsonify, url_for, send_from_directory

from server import database

home_bp = Blueprint('home', __name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.join(BASE_DIR, '..')
THUMBNAIL_FOLDER = os.path.join(BASE_DIR, 'thumbnails')


@home_bp.route('/', methods=['GET'])
def home():
    video_datas = database.get_alldata()

    video_list = []
    for video_data in video_datas:
        video_info = {
            'video_id': video_data['id'],
            'video_name': video_data['video_name'],
            'thumbnail_file_path': url_for('home.get_thumbnail', filename=video_data['thumbnail_file_path'], _external=True),
            'video_file_path': url_for('stream.stream_video', filename=video_data['video_file_path'],_external=True)
        }
        video_list.append(video_info)

    return jsonify(video_list)


@home_bp.route('/thumbnail/<filename>', methods=['GET'])
def get_thumbnail(filename):
    return send_from_directory(THUMBNAIL_FOLDER, filename)

from flask import Blueprint, request, jsonify
import os
import uuid

from server import database


upload_bp = Blueprint('upload', __name__)

VIDEO_FOLDER = os.path.join(os.path.dirname(__file__), '..', 'videos')
THUMBNAIL_FOLDER = os.path.join(os.path.dirname(__file__), '..', 'thumbnails')

# フォルダがない場合作成する
os.makedirs(VIDEO_FOLDER, exist_ok=True)
os.makedirs(THUMBNAIL_FOLDER, exist_ok=True)

@upload_bp.route('/', methods=['POST'])
def upload_video():
    print('アップロードのリクエスト受け取り')
    video_file = request.files.get('video')
    thumbnail_file = request.files.get('thumbnail')
    video_name = request.form.get('title')
    if not video_file or not thumbnail_file or not video_name:
        return jsonify({"error": "Missing required fields"}), 400

    # UUIDを生成してサーバに保存するファイル名を作成
    video_id = str(uuid.uuid4())
    video_filename = f"{video_id}.mp4"
    thumbnail_filename = f"{video_id}.png"

    video_path = os.path.join(VIDEO_FOLDER, video_filename)
    thumbnail_path = os.path.join(THUMBNAIL_FOLDER, thumbnail_filename)

    try:
        video_file.save(video_path)
        thumbnail_file.save(thumbnail_path)
    except Exception as e:
        return jsonify({"error": f"File saving failed: {e}"}), 500

    # データベースに情報を保存
    result = database.insert_data(video_id, video_name, video_filename, thumbnail_filename)
    if result is not True:
        return jsonify({"error": f"Database Error: {result}"}), 500

    return jsonify({"message": "Video upload successfully"}), 201

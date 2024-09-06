from flask import Blueprint, request, jsonify, send_file
import os

from server.database import get_db_connection

stream_bp = Blueprint('stream', __name__)

VIDEO_FOLDER = os.path.join(os.path.dirname(__file__), '..', 'videos')


@stream_bp.route('/<filename>', methods=['GET'])
def stream_video(filename):
    video_file_path = os.path.join(VIDEO_FOLDER, filename)

    if not os.path.isfile(video_file_path):
        print("File not found: ", video_file_path)
        return jsonify({"error": "File not found"}), 404

    try:
        return send_file(video_file_path, mimetype='video/mp4', as_attachment=False)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

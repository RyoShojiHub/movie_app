from flask import Blueprint, request, jsonify, send_file
import os

from server.database import get_db_connection

stream_bp = Blueprint('stream', __name__)

VIDEO_FOLDER = os.path.join(os.path.dirname(__file__), '..', 'videos')


@stream_bp.route('/stream/<filename>', methods=['GET'])
def stream_video(filename):
    video_file_path = os.path.join(VIDEO_FOLDER, filename)
    video_id = request.json.get('video_id')

    if not video_id:
        return jsonify({"error: Missing video_id"}), 404

    try:
        return send_file(video_file_path, as_attachment=False)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

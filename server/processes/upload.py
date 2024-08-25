from flask import Blueprint, request, jsonify
import os

upload_bp = Blueprint('upload', __name__)

VIDEO_FOLDER = os.path.join(os.path.dirname(__file__), '..', 'videos')
SHUMBNAIL_FOLDER = os.path.join(os.path.dirname(__file__), '..', 'thumbnails')

@upload_bp.route('/', methods=['POST'])
def upload_video():
    pass
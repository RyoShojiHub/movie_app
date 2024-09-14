import os
import sys

from flask import Flask

# どこからでも実行できるようにパスを調整
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

from server.database import init_db
from server.processes import home
from server.processes import stream
from server.processes import upload

app = Flask(__name__)

app.register_blueprint(home.home_bp, url_prefix='/')
app.register_blueprint(upload.upload_bp, url_prefix='/upload')
app.register_blueprint(stream.stream_bp, url_prefix='/stream')

if __name__ == '__main__':
    init_db()  # データベース初期化
    app.run(debug=True)

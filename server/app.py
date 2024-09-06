from flask import Flask

from database import init_db
from processes import home
from processes import stream
from processes import upload


app = Flask(__name__)

app.register_blueprint(home.home_bp, url_prefix='/')
app.register_blueprint(upload.upload_bp, url_prefix='/upload')
app.register_blueprint(stream.stream_bp, url_prefix='/stream')

if __name__ == '__main__':
    init_db()  # データベース初期化
    app.run(debug=True)

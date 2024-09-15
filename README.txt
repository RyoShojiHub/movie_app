概要:
movie_appはpythonを使用した動画管理アプリケーションで、サーバ側では動画の削除、ユーザ側では動画のアップロードや再生が可能です。
就職活動で提出するポートフォリオの一環として制作しました。


使用方法:
VLC media Playerが必要なため、以下のサイトからダウンロードしてください。
パスの設定等は必要ありません。
https://www.videolan.org/vlc/index.ja.html

プロジェクトのルートディレクトリに移動し、必要なパッケージをインストールします。
cd movie_app
pip install -r requirements.txt

サーバを起動します。
python server\main.py

クライアントを起動します(必要に応じてclient\URL.txtのIPアドレスを書き換えてください)。
python client\main.py


動画の削除:
動画の削除はサーバ側で以下のコマンドを実行して行ってください。
python server\delete_movie.py

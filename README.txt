概要:
movie_appは、pythonを使用した動画管理アプリケーションで、サーバ側では動画の削除、ユーザ側では動画のアップロードや再生が可能です。
就職活動で提出するポートフォリオの一環として制作しました。


使用方法:
必要なパッケージをインストールします。
pip install -r requirements.txt

プロジェクトのルートディレクトリに移動し、サーバを起動します。
cd movie_app
python server\main.py

クライアントを起動します
python client\main.py


動画の削除:
動画の削除は以下のプログラムからおこなってください。
python server\delete_movie.py

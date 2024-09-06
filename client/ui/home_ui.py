import requests
from io import BytesIO
import tkinter as tk
from PIL import Image, ImageTk

from client import api_client


class HomeUI(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack(fill=tk.BOTH, expand=True)
        self.create_upload_button()
        self.display_home()

    def create_upload_button(self):
        upload_button = tk.Button(self, text="アップロード", command=self.go_to_upload)
        upload_button.pack(side=tk.TOP, pady=10)

    def display_home(self):
        row_frame = None
        video_data = api_client.get_video_data()
        for i, video in enumerate(video_data):
            title = video['video_name']
            thumbnail_url = video['thumbnail_file_path']
            video_file_path = video['video_file_path']

            if i % 4 == 0:
                row_frame = tk.Frame(self)
                row_frame.pack(side=tk.TOP, pady=10)

            try:
                img_data = requests.get(thumbnail_url).content
                img = Image.open(BytesIO(img_data))
                img = img.resize((150, 100))
                tk_img = ImageTk.PhotoImage(img)
            except Exception as e:
                print('Error: {}'.format(e))
                continue

            frame = tk.Frame(row_frame, )
            frame.pack(side=tk.LEFT, padx=10)

            # 画像ラベルを作成
            img_label = tk.Label(frame, image=tk_img)
            img_label.image = tk_img
            img_label.pack(side=tk.TOP)

            # タイトルラベルを作成
            title_label = tk.Label(frame, text=title)
            title_label.pack(side=tk.TOP)

            img_label.bind("<Button-1>", lambda event, url=video_file_path: self.on_thumbnail_click(url))

    def on_thumbnail_click(self, video_path):
        # 動画再生画面に切り替え、指定された動画を再生
        self.master.show_frame("VideoPlayerUI")  # VideoPlayerUIに切り替える
        self.master.frames["VideoPlayerUI"].play_video(video_path)  # 動画再生メソッドを呼び出す

    def go_to_upload(self):
        self.master.show_frame("UploadFormUI")

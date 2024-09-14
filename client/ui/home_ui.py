import os.path

import requests
from io import BytesIO
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

from client import api_client

# uiディレクトリの絶対パス
UI_DIR = os.path.dirname(os.path.abspath(__file__))


class HomeUI(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill=tk.BOTH, expand=True)

        # 各種ボタンを配置するフレーム
        self.button_frame = tk.Frame(self, bg="white")
        self.button_frame.pack(fill=tk.X, anchor=tk.N)
        self.create_buttons(self.button_frame)

        # スクロール可能なキャンバスとコンテンツ配置
        self.canvas = tk.Canvas(self)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.scrollable_frame = self.create_scroll_area(self.canvas)
        self.display_home()

    def create_buttons(self, frame):
        # アップロードボタンの設定
        upload_icon = PhotoImage(file=os.path.join(UI_DIR, "icon01.png"))
        upload_button = tk.Button(
            frame,
            text=" 動画のアップロード",
            image=upload_icon,
            compound=tk.LEFT,
            command=self.go_to_upload,
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            activebackground="#45a049",
            activeforeground="white",
            relief="raised",
            bd=3,
            padx=10,
            pady=5,
            cursor="hand2",
        )
        upload_button.image = upload_icon
        upload_button.pack(side=tk.LEFT, padx=20, pady=10)

        # 更新ボタンの設定
        refresh_icon = PhotoImage(file=os.path.join(UI_DIR, "icon02.png"))
        refresh_button = tk.Button(
            frame,
            text=" 更新",
            image=refresh_icon,
            compound=tk.LEFT,
            command=self.display_home,
            font=("Arial", 12, "bold"),
            bg="#42A5F5",  # ボタンの背景色
            fg="white",  # テキストの色
            activebackground="#1E88E5",  # ホバー時の背景色
            activeforeground="white",  # ホバー時のテキスト色
            relief="raised",
            bd=3,
            padx=10,
            pady=5,
            cursor="hand2",
        )
        refresh_button.image = refresh_icon
        refresh_button.pack(side=tk.LEFT, padx=10, pady=10)

    def create_scroll_area(self, canvas):
        # スクロール可能なフレームの作成
        scrollable_frame = tk.Frame(canvas, bg="blue")
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        scrollbar = tk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.configure(yscrollcommand=scrollbar.set)

        # スクロール領域の自動更新
        scrollable_frame.bind(
            "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        self.master.bind("<MouseWheel>", self.on_mouse_wheel)

        return scrollable_frame

    def display_home(self):
        # 既存の内容をクリア
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        main_frame = tk.Frame(self.scrollable_frame, bg="white")
        main_frame.pack(fill=tk.BOTH, expand=True)

        row_frame = None
        video_data = api_client.get_video_data()
        for i, video in enumerate(video_data):
            title = video['video_name']
            thumbnail_url = video['thumbnail_file_path']
            video_file_path = video['video_file_path']
            uploaded_date = video['uploaded_at']

            if i % 4 == 0:
                row_frame = tk.Frame(main_frame, bg="white")
                row_frame.pack(side=tk.TOP, padx=10, pady=20, anchor=tk.W)

            try:
                img_data = requests.get(thumbnail_url).content
                img = Image.open(BytesIO(img_data))
                img = img.resize((288, 162))
                tk_img = ImageTk.PhotoImage(img)
            except Exception as e:
                print('Error: {}'.format(e))
                continue

            content_frame = tk.Frame(row_frame, bg="white", cursor="hand2")
            content_frame.pack(side=tk.LEFT, padx=10, anchor=tk.W)

            # 画像ラベルを作成
            img_label = tk.Label(content_frame, image=tk_img, bg="white")
            img_label.image = tk_img
            img_label.pack(side=tk.TOP)
            img_label.bind("<Button-1>", lambda event, url=video_file_path: self.on_thumbnail_click(url))

            # タイトルと日付用のフレーム
            title_frame = tk.Frame(content_frame, height=30, width=280, bg="white")
            title_frame.pack(side=tk.TOP, fill=tk.X)

            # タイトルラベルを作成
            title_label = tk.Label(
                title_frame,
                font=("Arial", 12, "normal"),
                text=title,
                height=2,
                anchor=tk.NW,
                justify="left",
                wraplength=280,
                bg="white",
            )
            title_label.pack(side=tk.TOP, anchor=tk.NW)
            title_label.bind("<Button-1>", lambda event, url=video_file_path: self.on_thumbnail_click(url))

            # 投稿日付
            date_label = tk.Label(title_frame, text=uploaded_date, bg="white")
            date_label.pack(side=tk.TOP, anchor=tk.NW)
            date_label.bind("<Button-1>", lambda event, url=video_file_path: self.on_thumbnail_click(url))

    def on_mouse_wheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def on_thumbnail_click(self, video_path):
        self.master.show_frame("VideoPlayerUI")  # VideoPlayerUIに切り替える
        self.master.frames["VideoPlayerUI"].play_video(video_path)  # 動画再生メソッドを呼び出す

    def go_to_upload(self):
        self.master.show_frame("UploadFormUI")

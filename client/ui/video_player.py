import tkinter as tk
import vlc
import os
import ctypes


class VideoPlayerUI(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="white")
        self.master = master
        self.pack(fill=tk.BOTH, expand=True)

        # 各種ボタンの配置
        self.button_frame = tk.Frame(self, bg="white")
        self.button_frame.pack(fill=tk.X, pady=10)
        self.create_buttons(self.button_frame)

        # 動画再生用のキャンバス
        self.canvas = tk.Canvas(self, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.player = None

    def create_buttons(self, frame):
        # 戻るボタン
        back_button = tk.Button(
            frame,
            text="ホームに戻る",
            command=self.go_home,
            bg="#FF7043",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=10,
            pady=5,
            relief="raised",
            cursor="hand2"
        )
        back_button.pack(side=tk.LEFT, padx=5)

    def play_video(self, video_path):
        if self.player:
            self.player.stop()

        # VLCメディアプレーヤーのセットアップ
        self.player = vlc.MediaPlayer(video_path)
        self.player.set_hwnd(self.canvas.winfo_id())  # Windows用の設定
        self.player.play()

    def go_home(self):
        # プレーヤーを停止してホーム画面に戻る
        if self.player:
            self.player.stop()
        self.master.show_frame("HomeUI")  # ホーム画面に切り替える

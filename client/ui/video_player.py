import tkinter as tk
import vlc
import os
import ctypes


class VideoPlayerUI(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack(fill=tk.BOTH, expand=True)
        self.player = None
        self.create_ui()

    def create_ui(self):
        # 戻るボタン
        button_frame = tk.Frame(self)
        button_frame.pack(fill=tk.X, pady=10)
        back_button = tk.Button(
            button_frame,
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

        # 動画再生用のキャンバス
        self.canvas = tk.Canvas(self, bg="black")
        self.canvas.pack(fill=tk.BOTH, expand=True)

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
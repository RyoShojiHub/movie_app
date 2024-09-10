import tkinter as tk
from tkinter import filedialog, messagebox
import requests


class UploadFormUI(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.video_path = None
        self.thumbnail_path = None
        self.create_form()

    def create_form(self):
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

        # タイトル入力フィールド
        title_label = tk.Label(self, text="動画タイトル:", font=("Arial", 12))
        title_label.pack(pady=5)
        self.title_entry = tk.Entry(self, width=50, font=("Arial", 10))
        self.title_entry.pack(pady=5)

        # 動画ファイル選択ボタン
        video_button = tk.Button(
            self,
            text="動画ファイルを選択",
            command=self.select_video,
            bg="#42A5F5",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=10,
            pady=5,
            relief="raised",
            cursor="hand2"
        )
        video_button.pack(pady=10)
        self.video_label = tk.Label(self, text="選択された動画ファイル: なし", font=("Arial", 10))
        self.video_label.pack()

        # サムネイル選択ボタン
        thumbnail_button = tk.Button(
            self,
            text="サムネイルを選択",
            command=self.select_thumbnail,
            bg="#42A5F5",
            fg="white",
            font=("Arial", 10, "bold"),
            padx=10,
            pady=5,
            relief="raised",
            cursor="hand2"
        )
        thumbnail_button.pack(pady=10)
        self.thumbnail_label = tk.Label(self, text="選択されたサムネイル: なし", font=("Arial", 10))
        self.thumbnail_label.pack()

        # アップロードボタン
        upload_button = tk.Button(
            self,
            text="アップロード",
            command=self.upload_video,
            bg="#66BB6A",
            fg="white",
            font=("Arial", 12, "bold"),
            padx=10,
            pady=5,
            relief="raised",
            cursor="hand2"
        )
        upload_button.pack(pady=20)

    def select_video(self):
        # 動画ファイルを選択するダイアログを表示
        self.video_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
        if self.video_path:
            self.video_label.config(text=f"選択された動画ファイル: {self.video_path}")

    def select_thumbnail(self):
        # サムネイル画像を選択するダイアログを表示
        self.thumbnail_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
        if self.thumbnail_path:
            self.thumbnail_label.config(text=f"選択されたサムネイル: {self.thumbnail_path}")

    def upload_video(self):
        # フォームデータを取得
        video_title = self.title_entry.get()
        if not video_title or not self.video_path or not self.thumbnail_path:
            messagebox.showerror("エラー", "すべてのフィールドを入力してください")
            return

        # サーバにデータをアップロード
        try:
            with open(self.video_path, 'rb') as video_file, open(self.thumbnail_path, 'rb') as thumbnail_file:
                files = {
                    'video': video_file,
                    'thumbnail': thumbnail_file
                }
                data = {'title': video_title}
                response = requests.post('http://127.0.0.1:5000/upload', files=files, data=data)
                if response.status_code == 201:
                    messagebox.showinfo("成功", "動画のアップロードに成功しました")
                    self.go_home()
                else:
                    messagebox.showerror("エラー", f"アップロードに失敗しました: {response.json().get('error')}")
        except Exception as e:
            messagebox.showerror("エラー", f"ファイルのアップロード中にエラーが発生しました: {e}")


    def go_home(self):
        self.master.show_frame("HomeUI")  # ホーム画面に切り替える

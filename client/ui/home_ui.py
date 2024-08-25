import requests
from io import BytesIO
import tkinter as tk
from PIL import Image, ImageTk


class HomeUi(tk.Frame):
    def __init__(self):
        super().__init__()

    def display_home(self, video_data):
        row_frame = None
        for i, video in enumerate(video_data):
            title = video['video_name']
            thumbnail_url = video['thumbnail_file_path']
            video_file_path = video['video_file_path']

            if i % 3 == 0:
                row_frame = tk.Frame(self)
                row_frame.pack(side=tk.TOP, pady=10)

            try:
                img_data = requests.get(thumbnail_url).content
                img = Image.open(BytesIO(img_data))
                tk_img = ImageTk.PhotoImage(img)

                frame = tk.Frame(row_frame)
                frame.pack(side=tk.LEFT, padx=10)

                img_label = tk.Label(frame, image=tk_img)
                img_label.image = tk_img
                img_label.pack(side=tk.TOP)

                title_label = tk.Label(frame, text=title)
                title_label.pack(side=tk.TOP)

                frame.bind("<Button-1>", lambda url=video_file_path: self.master.play_video(url))

            except Exception as e:
                print('Error: {}'.format(e))

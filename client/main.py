import tkinter as tk

from ui.home_ui import HomeUI
from ui.upload_form import UploadFormUI
from ui.video_player import VideoPlayerUI


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Video App')
        self.geometry("1280x800")
        self.frames = {}
        self.create_frames()
        self.show_frame("HomeUI")

    def create_frames(self):
        self.frames["HomeUI"] = HomeUI(self)
        self.frames["VideoPlayerUI"] = VideoPlayerUI(self)
        self.frames["UploadFormUI"] = UploadFormUI(self)

        # 全フレームを重ねて配置
        for frame in self.frames.values():
            frame.pack(fill=tk.BOTH, expand=True)

    def show_frame(self, frame_name):
        # 表示されているフレームを非表示にする
        for frame in self.frames.values():
            frame.pack_forget()

        # 指定されたフレームを前面に表示
        frame = self.frames[frame_name]
        frame.pack(fill=tk.BOTH, expand=True)


if __name__ == '__main__':
    app = App()
    app.mainloop()

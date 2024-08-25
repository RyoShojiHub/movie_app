import tkinter as tk

from ui import video_player
from ui import home_ui
from ui import upload_form
import api_client


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Video App')
        self.geometry("1280x800")
        self.home_frame = home_ui.HomeUi()
        self.video_player_frame = video_player.VideoPlayer()
        self.upload_form_frame = upload_form.UploadForm()

        self.show_home()

    def show_home(self):
        self.clear_frames()
        video_data = api_client.get_video_data()
        self.home_frame.display_home(video_data)
        self.home_frame.pack(fill=tk.BOTH, expand=True)

    def show_upload_form(self):
        self.clear_frames()
        self.upload_form_frame.pack(fill=tk.BOTH, expand=True)

    def clear_frames(self):
        self.home_frame.pack_forget()
        self.video_player_frame.pack_forget()
        self.upload_form_frame.pack_forget()


if __name__ == '__main__':
    app = App()
    app.mainloop()

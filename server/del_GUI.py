import os
import tkinter as tk
from tkinter import messagebox

import database

VIDEO_FOLDER = os.path.join(os.path.dirname(__file__), 'videos')
THUMBNAIL_FOLDER = os.path.join(os.path.dirname(__file__), 'thumbnails')


def main():
    root = tk.Tk()
    root.title('動画削除')
    root.geometry("800x600")
    root.resizable(width=False, height=False)

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
    video_listbox = tk.Listbox(frame, width=80, height=25, font=('Consolas', 12), yscrollcommand=scrollbar.set)
    scrollbar.config(command=video_listbox.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    video_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    load_videos(video_listbox)
    video_listbox.pack()

    delete_button = tk.Button(root, text="選択した動画を削除", command=lambda: delete_selected_video(video_listbox))
    delete_button.pack(pady=10)

    root.mainloop()


def load_videos(listbox):
    data = database.get_alldata()
    listbox.delete(0, tk.END)
    for row in data:
        text = f"{row['id']} - {row['video_name']} - {row['uploaded_at']}"
        listbox.insert(tk.END, text)


def delete_selected_video(listbox):
    selected_index = listbox.curselection()
    if not selected_index:
        messagebox.showwarning("警告", "削除する動画を選択してください。")
        return

    selected_item = listbox.get(selected_index)
    video_id = selected_item.split(' - ')[0]  # IDを取得

    confirm = messagebox.askyesno("確認", "この動画を削除しますか？")
    if not confirm:
        return

    data = database.get_alldata()
    video_data = next((row for row in data if row['id'] == video_id), None)

    if video_data:
        # ファイルパスを作成
        video_path = os.path.join(VIDEO_FOLDER, video_data['video_file_path'])
        thumbnail_path = os.path.join(THUMBNAIL_FOLDER, video_data['thumbnail_file_path'])

        # ファイルの削除
        if os.path.exists(video_path):
            os.remove(video_path)
        else:
            print("動画ファイルが存在しません。")

        if os.path.exists(thumbnail_path):
            os.remove(thumbnail_path)
        else:
            print("サムネイルファイルが存在しません。")

    result = database.delete_data(video_id)
    if result is not True:
        messagebox.showerror("エラー", f"削除中にエラーが発生しました: {result}")
        return

    load_videos(listbox)
    messagebox.showinfo("完了", "動画が削除されました。")


if __name__ == '__main__':
    main()

import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess

# Function to open file dialog and download
def download_video(video_type):
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Error", "Please enter a valid URL")
        return

    folder_selected = filedialog.askdirectory(title="Select Export Folder")
    if not folder_selected:
        return

    format_option = {
        'video': 'bestvideo+bestaudio/best',
        'playlist': '--yes-playlist',
        'short': 'bestvideo+bestaudio/best'
    }

    command = [
        'yt-dlp', '-P', folder_selected, '-f', 'bestvideo+bestaudio/best', '--merge-output-format', 'mp4', url
    ]

    if video_type == 'playlist':
        command.insert(3, '--yes-playlist')

    try:
        subprocess.run(command, check=True)
        messagebox.showinfo("Success", "Download completed!")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to download. Please check the URL and try again.")

# GUI setup
root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("400x200")
root.configure(bg="#fffffc")

# URL entry box
url_label = tk.Label(root, text="YouTube URL:", bg="#fdffb6", fg="#5a5a5a")
url_label.pack(pady=5)

url_entry = tk.Entry(root, width=50, bg="#caffbf", fg="#5a5a5a", insertbackground="#5a5a5a")
url_entry.pack(pady=5)

# Button frame
button_frame = tk.Frame(root, bg="#fffffc")
button_frame.pack(pady=10)

video_button = tk.Button(button_frame, text="Video", bg="#9bf6ff", fg="#5a5a5a", command=lambda: download_video('video'))
video_button.grid(row=0, column=0, padx=5)

playlist_button = tk.Button(button_frame, text="Playlist", bg="#a0c4ff", fg="#5a5a5a", command=lambda: download_video('playlist'))
playlist_button.grid(row=0, column=1, padx=5)

short_button = tk.Button(button_frame, text="Short", bg="#bdb2ff", fg="#5a5a5a", command=lambda: download_video('short'))
short_button.grid(row=0, column=2, padx=5)

root.mainloop()

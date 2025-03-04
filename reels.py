from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as font
from tkinter import messagebox
import yt_dlp

root = Tk()
root.title("Instagram Reel Downloader")
root.minsize(600, 500)
root.maxsize(600, 500)

FONT = font.Font(family="Times New Roman", size=18, weight="bold")

def download(link):
    try:
        if link:
            ydl_opts = {
                'outtmpl': f"reel_{int(time.time())}.mp4",
                'format': 'bestvideo+bestaudio/best',
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
            messagebox.showinfo("Status", "Reel downloaded successfully")
        else:
            messagebox.showwarning("Empty field", "Please fill out the field")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")

canvas = Canvas(root, height=500, width=600)
canvas.pack()

frame = Frame(root, bg="white")
frame.place(relwidth=1, relheight=1)

label1 = Label(frame, text="Download Reels in a Click!", font=FONT, bd=5, fg="#0d1137", bg="white")
label1.place(relx=0.25, rely=0.1, relheight=0.1)

FONT_SMALL = font.Font(family="Times New Roman", size=12, weight="bold")
label2 = Label(frame, text="Enter link address:", font=FONT_SMALL, bd=5, fg="#e52165", bg="white")
label2.place(relx=0.25, rely=0.25, relheight=0.1)

entry = Entry(frame, font=FONT_SMALL, fg="#fbad50")
entry.place(relx=0.25, rely=0.35, relwidth=0.5, relheight=0.05)

button1 = Button(root, text="Download", font=FONT_SMALL, bg="pink", fg="black", command=lambda: download(entry.get()))
button1.place(relx=0.4, rely=0.45, relwidth=0.2, relheight=0.06)

root.mainloop()

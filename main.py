import pygame
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter.filedialog import askdirectory
import os

root = tk.Tk()
root.title("Music Player")
root.geometry("900x680")
directory = askdirectory()
os.chdir(directory)
songlist = os.listdir()
playlist = tk.Listbox(root, font="Helvetica 16 italic",
                      bg="DeepSkyBlue3", selectmode=tk.SINGLE)
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=BOTH)
playlist.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=playlist.yview)
for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos = pos+1

pygame.init()
pygame.mixer.init()


def PlayM():
    pygame.mixer.music.load(playlist.get(tk.ACTIVE))
    var.set(playlist.get(tk.ACTIVE))
    pygame.mixer.music.play()


def ExitM():
    pygame.mixer.music.stop()


def PauseM():
    pygame.mixer.music.pause()


def ResumeM():
    pygame.mixer.music.unpause()


play = Image.open(r'F:\Python Projects\Music Player\image\play.png')
stop = Image.open(r'F:\Python Projects\Music Player\image\stop.png')
pause = Image.open(r'F:\Python Projects\Music Player\image\pause.png')
resume = Image.open(r'F:\Python Projects\Music Player\image\Resume.png')


play = play.resize((110, 110))
stop = stop.resize((110, 110))
pause = pause.resize((110, 110))
resume = resume.resize((110, 110))
play_img = ImageTk.PhotoImage(play)
stop_img = ImageTk.PhotoImage(stop)
pause_img = ImageTk.PhotoImage(pause)
resume_img = ImageTk.PhotoImage(resume)

# Creating buttons
play_btn = tk.Button(root, width=5, height=95, font="Cambria 20",
                     text="Play Music", image=play_img, command=PlayM, bg="DeepSkyBlue4", fg="white")

stop_btn = tk.Button(root, width=5, height=95, font="Cambria 20",
                     text="Stop Music", image=stop_img, command=ExitM, bg="DeepSkyBlue4", fg="white")

pause_btn = tk.Button(root, width=5, height=95, font="Cambria 20",
                      text="Pause Music", image=pause_img, command=PauseM, bg="DeepSkyBlue4", fg="white")

resume_btn = tk.Button(root, width=5, height=95, font="Cambria 20",
                       image=resume_img, command=ResumeM, bg="DeepSkyBlue4", fg="white")

var = tk.StringVar()
songtitle = tk.Label(root, font="Helvetica 13 bold", textvariable=var)
Label(root, text="Developed By Nilesh Kr", font="lucida 10",
      bg="grey", fg="white").pack(fill=X, pady=7)
songtitle.pack()
play_btn.pack(fill="x")
stop_btn.pack(fill="x")
pause_btn.pack(fill="x")
resume_btn.pack(fill="x")
playlist_label = tk.Label(root, text="Select Any Song To Play", font="Times 19 bold",
                          bg="DeepSkyBlue4")
playlist_label.pack(fill="both")
playlist.pack(fill="both", expand="yes")
root.mainloop()

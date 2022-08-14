from ctypes import resize
from tkinter import *;
from tkinter import Tk;
from tkinter import filedialog
from tkinter.font import BOLD
from turtle import bgcolor;
from pygame import mixer;
import os;

#Creating window
root = Tk()
root.title('Music Player')
root.geometry("900x600")
root.configure(bg="#0f1a2b")
root.resizable(0, 0);
mixer.init()



def addMusic():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)

        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)


def playMusic():
    musicName = Playlist.get(ACTIVE)
    print(musicName[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()



#Background
frame = Frame(root, width=100, height=100)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

logoImage = PhotoImage(file="bg.png")
Label(frame, image=logoImage, bg="#0f1a2b").pack()


#Button
Button(root, text="Play", width=10, height=2, bg="white", bd=0, command=playMusic).place(x = 100, y = 400)

Button(root, text="Stop", width=10, height=2, bg="white", bd=0, command=mixer.music.stop).place(x=30, y=500)

Button(root, text="Resume", width=10, height=2, bg="white", bd=0, command=mixer.music.unpause).place(x=115, y=500)


Button(root, text="Pause", width=10, height=2, bg="white", bd = 0, command=mixer.music.pause).place(x=200, y = 500)


#music
Label(root, text="Menu", foreground="white", bg="#0f1a2b", font=("arial", 25)).pack(padx=20, pady=50, side=RIGHT)


frameMusic = Frame(root, bd=2, relief= RIDGE)
frameMusic.place(x=330, y=350, width=560, height=250)

Button(root, text="Add Music", width=20, height=2, font=("times new roman", 12, "bold"), fg="Black", bg="#21b3de", command=addMusic).place(x=330, y=300)

Scroll = Scrollbar(frameMusic)
Playlist = Listbox(frameMusic, width=100, font=("times new roman", 10), bg="#333333", fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=LEFT, fill=BOTH)

root.mainloop()








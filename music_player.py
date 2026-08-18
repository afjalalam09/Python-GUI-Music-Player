import os
from tkinter import *
from tkinter import filedialog
from pygame import mixer

# Initialize Tkinter & Pygame Mixer
root = Tk()
root.title("TuneCast Player")
root.geometry("400x550")
root.configure(bg="#1E1E1E") # Modern Dark Theme
root.resizable(False, False)
mixer.init()

# --- Application Logic (Functions) ---

def AddMusic():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        Playlist.delete(0, END) # Clears the old playlist when a new folder is selected
        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)

def PlayMusic():
    try:
        music_name = Playlist.get(ACTIVE)
        mixer.music.load(music_name)
        mixer.music.play()
        # Displays the first 30 characters of the song name
        status_label.config(text=f"Playing: {music_name[:30]}...", fg="#00FF00")
    except:
        status_label.config(text="Please select a valid song", fg="#FF4444")

def StopMusic():
    mixer.music.stop()
    status_label.config(text="Stopped", fg="#FF4444")

def PauseMusic():
    mixer.music.pause()
    status_label.config(text="Paused", fg="#FFA500")

def ResumeMusic():
    mixer.music.unpause()
    status_label.config(text="Resumed playing...", fg="#00FF00")

# --- UI Design Section ---

# App Title
Label(root, text="🎵 TuneCast Player", font=("Helvetica", 20, "bold"), bg="#1E1E1E", fg="#FF9500").pack(pady=20)

# Browse Button
Button(root, text="📂 Browse Music Folder", font=("Helvetica", 12, "bold"), bg="#333333", fg="white", bd=0, cursor="hand2", command=AddMusic).pack(pady=5, ipadx=10, ipady=5)

# Playlist Box setup with Scrollbar
Frame_Music = Frame(root, bd=0)
Frame_Music.pack(pady=15)

Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=40, height=12, font=("Helvetica", 11), bg="#2C2C2C", fg="white", selectbackground="#FF9500", selectforeground="black", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=LEFT, fill=BOTH)

# Real-time Status Label
status_label = Label(root, text="Ready to Play", font=("Helvetica", 10), bg="#1E1E1E", fg="grey")
status_label.pack(pady=10)

# Controls Frame setup
controls_frame = Frame(root, bg="#1E1E1E")
controls_frame.pack(pady=10)

# Button Styling Variables
btn_font = ("Helvetica", 18)
btn_bg = "#333333"

# Modern Unicode Control Buttons
Button(controls_frame, text="⏹", font=btn_font, bg=btn_bg, fg="#FF4444", bd=0, width=4, cursor="hand2", command=StopMusic).grid(row=0, column=0, padx=5)
Button(controls_frame, text="⏯", font=btn_font, bg=btn_bg, fg="#FFA500", bd=0, width=4, cursor="hand2", command=ResumeMusic).grid(row=0, column=1, padx=5)
Button(controls_frame, text="▶", font=btn_font, bg=btn_bg, fg="#00FF00", bd=0, width=4, cursor="hand2", command=PlayMusic).grid(row=0, column=2, padx=5)
Button(controls_frame, text="⏸", font=btn_font, bg=btn_bg, fg="#FFA500", bd=0, width=4, cursor="hand2", command=PauseMusic).grid(row=0, column=3, padx=5)

# Run Application
root.mainloop()
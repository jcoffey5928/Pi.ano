from tkinter import *
from tkinter import ttk
from keyboard import Keyboard

class Gui:
    def __init__(self, master, controller):
        self.master = master
        self.master.title('Piano')
        self.master.resizable(False, False)

        self.controller = controller
        self.song = self.controller.getCurrentSong().getTitle()
        self.songText = StringVar()
        self.songText.set(self.song)
        self.key = self.controller.getCurrentKey()
        self.keyText = StringVar()
        self.keyText.set(f"Key: {self.key}")
        self.lightColor = Keyboard.KEY_COLORS.get(self.key) 

        self.style = ttk.Style()
        self.style.configure("TFrame", background="black")
        self.style.configure("Pl.TButton", background="green", padding=6)
        self.style.configure("Pr.TButton", background="grey", padding=6)
        self.style.configure("N.TButton", background="grey", padding=6)
        self.style.configure("S.TLabel", textvariable=self.songText, background="black", foreground="white", font=("Consolas", 14), anchor="center")
        self.style.configure("K.TLabel", textvariable=self.keyText, background="black", foreground=self.lightColor, font=("Consolas", 14, "bold"), anchor="center")

        self.createInfoFrame()
        self.createControlFrame()

    def createInfoFrame(self):
        contentFrame = ttk.Frame(self.master, style="TFrame")
        contentFrame.pack()
        self.songLabel = ttk.Label(contentFrame, textvariable=self.songText, width=50, style="S.TLabel").grid(row=0, column=0)
        self.keyLabel = ttk.Label(contentFrame, textvariable=self.keyText, style="K.TLabel").grid(row=1,column=0)

    def createControlFrame(self):
        buttonFrame = ttk.Frame(self.master, style="TFrame")
        buttonFrame.pack()
        playButton = ttk.Button(buttonFrame, command=self.playSong, text="Play", style="Pl.TButton").grid(row=0, column=0)
        prevButton = ttk.Button(buttonFrame, command=self.prevSong, text="Previous", style="Pr.TButton").grid(row=0, column=1)
        nextButton = ttk.Button(buttonFrame, command=self.nextSong, text="Next", style="N.TButton").grid(row=0, column=2)

    def playSong(self):
        #TODO Implement color changing text that follows the song keys
        self.controller.playSong()

    def prevSong(self):
        # TODO Implement prevSong
        print("Prev Song")

    def nextSong(self):
        self.controller.nextSong()
        self.song = self.controller.getCurrentSong()
        print(f"prev key: {self.key}; prev color: {self.lightColor}")
        self.song = self.controller.getCurrentSong().getTitle()
        self.songText.set(self.song)
        self.key = self.controller.getCurrentKey()
        self.keyText.set(f"Key: {self.key}")
        self.lightColor = Keyboard.KEY_COLORS.get(self.key) 
        print(f"current key: {self.key}; current colorr: {self.lightColor}")
        self.style.configure("K.TLabel", foreground = self.lightColor)

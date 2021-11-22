from tkinter import *
from tkinter import ttk
from keyboard import Keyboard

class Gui:
    def __init__(self, master, controller):
        self.master = master
        self.controller = controller

        self.master.title('Piano')
        self.master.resizable(True, True)

        self.style = ttk.Style()
        self.style.configure("TButton", background="blue", padding=6)
        self.style.configure("TLabel", background="grey", font=("Consolas", 14))
        self.style.configure("TFrame", background="red")

        self.createInfoFrame()
        self.createControlFrame()

    def createInfoFrame(self):
        note = self.controller.getCurrentSong()
        lightColor = Keyboard.KEY_COLORS.get(note) 
        contentFrame = ttk.Frame(self.master)
        contentFrame.pack()
        label = ttk.Label(contentFrame, text=note, foreground=lightColor).grid(row=0, column=1)

    def createControlFrame(self):
        buttonFrame = ttk.Frame(self.master)
        buttonFrame.pack()
        nextButton = ttk.Button(buttonFrame, command=self.controller.nextSong, text="Next").grid(row=0, column=1)

    def nextSong(self):
        print('Button pushed. Playing the next song')
        self.controller.nextSong()
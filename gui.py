from tkinter import *
from tkinter import ttk

class Gui:
    def __init__(self, master, controller):
        self.controller = controller
        self.master = master

        self.master.title('Piano')
        self.master.resizable(True, True)

        self.style = ttk.Style()
        self.style.configure("TButton", background="blue", padding=6)
        self.style.configure("TLabel", background="grey", font=("Consolas", 14))
        self.style.configure("TFrame", background="red")


        self.createInfoFrame()
        self.createControlFrame()

    def createInfoFrame(self):
        self.note = "C5"
        self.lightColor = "green"
        self.contentFrame = ttk.Frame(self.master)
        self.contentFrame.pack()
        self.label = ttk.Label(self.contentFrame, text=self.note, foreground=self.lightColor).grid(row=0, column=1)

    def createControlFrame(self):
        self.buttonFrame = ttk.Frame(self.master)
        self.buttonFrame.pack()
        self.nextButton = ttk.Button(self.buttonFrame, command=self.nextSong, text="Next").grid(row=0, column=1)

    def nextSong(self):
        print('Button pushed. Playing the next song')

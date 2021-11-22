from tkinter import *
from tkinter import ttk

class Gui:
    def __init__(self, master):
        master.title('Piano')
        master.resizable(True, True)

        self.style = ttk.Style()
        self.style.configure("TButton", background="blue", padding=6)
        self.style.configure("TLabel", background="grey", font=("Consolas", 14))
        self.style.configure("TFrame", background="red")


        self.note = "C5"
        self.color = "green"

        self.contentFrame = ttk.Frame(master)
        self.contentFrame.pack()
        self.label = ttk.Label(self.contentFrame, text=self.note, foreground=self.color).grid(row=0, column=1)

        self.buttonFrame = ttk.Frame(master)
        self.buttonFrame.pack()
        self.nextButton = ttk.Button(self.buttonFrame, text="Next").grid(row=0, column=1)


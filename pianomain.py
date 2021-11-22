from pianoapp import PianoApp
from gui import Gui
from tkinter import *
from tkinter import ttk

def main():
    app = PianoApp()
    root = Tk()
    gui = Gui(root)
    root.mainloop()
    app.run()

def main():
    app = PianoApp()
    app.run()

if __name__ == "__main__": main()

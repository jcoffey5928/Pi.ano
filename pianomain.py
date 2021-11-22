from pianoapp import PianoApp
from gui import Gui
from tkinter import *
from tkinter import ttk

def main():
    root = Tk()
    gui = Gui(root)
    app = PianoApp()

    root.mainloop()

    app.run()

if __name__ == "__main__": main()

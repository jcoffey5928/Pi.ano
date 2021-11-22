<<<<<<< HEAD
#from pianoapp import PianoApp
from gui import Gui
from tkinter import *
from tkinter import ttk

def main():
    #app = PianoApp()
    root = Tk()
    gui = Gui(root)
    root.mainloop()
    #app.run()
=======
from pianoapp import PianoApp

def main():
    app = PianoApp()
    app.run()
>>>>>>> parent of 445dd7f... Gui testing

if __name__ == "__main__": main()

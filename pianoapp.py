#!/usr/bin/env python3

from songparser import SongParser
from songcontroller import SongController
from song import Song
from gui import Gui
from tkinter import *
from tkinter import ttk
from time import sleep
import os

class PianoApp:
    def __init__(self):
        self.songList = []
        self.controller = None

    def run(self):
        self.gatherFiles()
        if (len(self.songList) != 0):
            self.controller = SongController(self.songList)
            root = Tk()
            gui = Gui(root, self.controller)
            root.mainloop()
        else:
            print("NO SONG FILES FOUND")

    def gatherFiles(self):
        for fileName in os.listdir("songs"):
            if fileName.endswith('.sg'):
                file = os.path.join("songs", fileName)
                song = Song('')
                parser = SongParser(song)
                parser.parse(file)
                self.songList.append(song)

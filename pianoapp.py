#!/usr/bin/env python3

from gpiozero import TonalBuzzer
from songparser import SongParser
from songcontroller import SongController
from song import Song
from light import Light
from gui import Gui
from tkinter import *
from tkinter import ttk
from time import sleep
import os

class PianoApp:
    def __init__(self):
        self.songList = []
        self.controller = None
        self.buzzer = TonalBuzzer(2)
        self.light = Light(12, 19, 13)
        self.light.turnOff()

    def run(self):
        self.gatherFiles()
        self.controller = SongController(self.songList)
        root = Tk()
        gui = Gui(root, self.controller)

        root.mainloop()
        #self.playSongs()

    def gatherFiles(self):
        for fileName in os.listdir("songs"):
            if fileName.endswith(".sg"):
                file = os.path.join("songs", fileName)
                song = Song('')
                parser = SongParser(song)
                parser.parse(file)
                self.songList.append(song)
        

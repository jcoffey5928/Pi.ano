from gpiozero import TonalBuzzer
from songparser import SongParser
from songcontroller import SongController
from song import Song
from time import sleep
import os

class PianoApp:
    def __init__(self):
        self.songList = []
        self.controller = None
        self.buzzer = TonalBuzzer(2)

    def run(self):
        self.gatherFiles()

        self.controller = SongController(self.songList)

        self.playSongs()

    def gatherFiles(self):
        for fileName in os.listdir("songs"):
            if fileName.endswith(".sg"):
                file = os.path.join("songs", fileName)
                song = Song('')
                parser = SongParser(song)
                parser.parse(file)
                self.songList.append(song)
        
    # Used for testing
    def playSongs(self):
        for song in self.songList:
            print(song.title, end ='')
            song.play(self.buzzer)
            sleep(2)
            print()

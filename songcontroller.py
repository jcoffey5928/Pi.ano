#!/usr/bin/env python3
#Name: songcontroller.py
#Purpose: Controls the flow of the songs. It will progress the song note by note if the keyboard input is correct.
#         It will track the current position of the song and remember this position if the song is to be played 
#         for the next 3 notes or if the entire song is played. 
#Developer: Jonathan Coffey

from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from light import Light
from keyboard import Keyboard
from time import sleep

class SongController:
     
    def __init__(self, songList):
        self.songList = songList
        self.currentSong = songList[0]
        self.currentKey = self.currentSong.notes[0][0]
        self.currentDelay = self.currentSong.notes[0][1]
        self.keyPlayed = None
        self.buzzer = TonalBuzzer(2)
        self.light = Light(12, 19, 13)
        self.light.turnOff()

    def isKeyCorrect(self, currentKey):
        return currentKey == Keyboard.keyPlayed

    def playSong(self, gui):
        print(self.currentSong.title, end ='')
        #self.currentSong.play(self.buzzer, self.light)
        for i in self.currentSong.keys:
            key = i[0]
            delay = i[1]
            print(key)
            self.buzzer.play(Tone(key))
            self.light.onWithDelay(Keyboard.KEY_COLORS.get(key), float(delay))
            self.light.turnOff()
            sleep(float(delay))
            self.buzzer.stop()
            sleep(0.1)
        self.light.turnOff()
        print()

    def nextSong(self):
        currentIndex = self.songList.index(self.currentSong)
        if (currentIndex + 1 < len(self.songList)):
            self.currentSong = self.songList[currentIndex + 1]
        else:
            self.currentSong = self.songList[0]
        self.reset()
    
    def prevSong(self):
        currentIndex = self.songList.index(self.currentSong)
        print(len(self.songList))
        if (currentIndex - 1 >= 0):
            self.currentSong = self.songList[currentIndex - 1]
        else:
            self.currentSong = self.songList[len(self.songList) - 1]
        self.reset()
        
    def reset(self):
        self.currentKey = self.currentSong.notes[0][0]
        self.currentDelay = self.currentSong.notes[0][1]
        self.keyPlayed = None
        

    # Used for testing all songs
    def playSongs(self):
        for song in self.songList:
            print(song.title, end ='')
            song.play(self.buzzer, self.light)
            sleep(2)
            print()

    def getCurrentSong(self):
        return self.currentSong
    
    def getCurrentKey(self):
        return self.currentKey

#!/usr/bin/env python3
#Name: songcontroller.py
#Purpose: Controls the flow of the songs. It will progress the song note by note if the keyboard input is correct.
#         It will track the current position of the song and remember this position if the song is to be played 
#         for the next 3 notes or if the entire song is played. 
#Developer: Jonathan Coffey

from keyboard import Keyboard
from time import sleep

class SongController:
     
    def __init__(self, songList):
        self.songList = songList
        self.currentSong = songList[0]
        self.currentKey = self.currentSong.notes[0][0]
        self.currentDelay = self.currentSong.notes[0][1]
        self.keyPlayed = None

    def isKeyCorrect(self, currentKey):
        return currentKey == Keyboard.keyPlayed

    def nextSong(self):
        print('changing to the next song')
        currentIndex = self.songList.index(self.currentSong)
        if (currentIndex + 1 < len(self.songList)):
            self.currentSong = self.songList[currentIndex]
        else:
            self.currentSong = self.songList[0]
        self.reset()
    
    def reset(self):
        self.currentKey = self.currentSong.notes[0][0]
        self.currentDelay = self.currentSong.notes[0][1]
        self.keyPlayed = None
        

    # Used for testing
    def playSongs(self):
        for song in self.songList:
            print(song.title, end ='')
            song.play(self.buzzer, self.light)
            sleep(2)
            print()

    def getCurrentSong(self):
        return self.currentSong
#!/usr/bin/env python3
#Name: song.py
#Purpose: Class which simply creates a song that with a title and notes in the file.
#Developer: Jonathan Coffey

from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from time import sleep
from light import Light
from keyboard import Keyboard

class Song: 
    def __init__(self, title):
        self.title = title
        self.notes = [] # Each element is an array of size 2. [0] = the key, [1] = pause time

    # TODO Implement a preview from the current position in learning mode.
    def playThreeNotes(self, pos):
        for i in self.notes[pos:pos+3]:
            key = i[0]
            delay = i[1]
            print(key)
            sleep(float(delay))

    def getTitle(self):
        return self.title


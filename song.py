
from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from time import sleep
from light import Light
from keyboard import Keyboard

class Song: 
    def __init__(self, title):
        self.title = title
        self.notes = [] # Each element is an array of size 2. [0] = the note, [1] = pause time

    def play(self, buzzer, light):
        for i in self.notes:
            note = i[0]
            delay = i[1]
            print(note)
            buzzer.play(Tone(note))
            light.onWithDelay(Keyboard.KEY_COLORS.get(note), float(delay))
            light.turnOff()
            sleep(float(delay))
            buzzer.stop()
            sleep(0.1)
        light.turnOff()

    def playThreeNotes(self, pos):
        for i in self.notes[pos:pos+3]:
            note = i[0]
            delay = i[1]
            print(note)
            sleep(float(delay))

    def getTitle(self):
        return self.title


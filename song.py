
from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from time import sleep
from light import Light
from keyboard import Keyboard

class Song: 
    def __init__(self, title):
        self.title = title
        self.keys = [] # Each element is an array of size 2. [0] = the key, [1] = pause time

    def play(self, buzzer, light):
        for i in self.keys:
            key = i[0]
            delay = i[1]
            print(key)
            buzzer.play(Tone(key))
            light.onWithDelay(Keyboard.KEY_COLORS.get(key), float(delay))
            light.turnOff()
            sleep(float(delay))
            buzzer.stop()
            sleep(0.1)
        light.turnOff()

    def playThreeNotes(self, pos):
        for i in self.keys[pos:pos+3]:
            key = i[0]
            delay = i[1]
            print(key)
            sleep(float(delay))

    def getTitle(self):
        return self.title


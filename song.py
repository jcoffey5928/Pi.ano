
from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from time import sleep

class Song: 
    def __init__(self, title):
        self.title = title
        self.notes = [] # Each element is an array of size 2. [0] = the note, [1] = pause time

    def play(self, buzzer):
        for i in self.notes:
            print(i[0])
            buzzer.play(Tone(i[0]))
            sleep(float(i[1]))
            buzzer.stop()
            sleep(0.1)

    def playThreeNotes(self, pos):
        for i in self.notes[pos:pos+3]:
            print(i[0])
            sleep(float(i[1]))


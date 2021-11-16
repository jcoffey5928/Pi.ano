from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from time import sleep

buzzer = TonalBuzzer(2)

buzzer.play(Tone("E5"))
sleep(0.75)
buzzer.play(Tone("D5"))
sleep(0.75)
buzzer.play(Tone("C5"))
sleep(0.75)
buzzer.play(Tone("D5"))
sleep(0.75)
buzzer.play(Tone("E5"))
sleep(0.75)
buzzer.play(Tone("E5"))
sleep(0.75)
buzzer.play(Tone("E5"))
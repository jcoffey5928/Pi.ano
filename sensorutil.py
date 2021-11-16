from gpiozero import LED
from gpiozero import Button
from gpiozero import Buzzer
from time import sleep

class SensorUtil:


    @staticmethod
    def LEDOnAndWait(pin, sec):
        LED(pin).on()
        sleep(sec)

    @staticmethod
    def LEDOffAndWait(pin, sec):
        LED(pin).off()
        sleep(sec)

    @staticmethod
    def BuzzerOnAndWait(pin, sec):
        Buzzer(pin).on()
        sleep(sec)

    @staticmethod
    def BuzzerOffAndWait(pin, sec):
        Buzzer(pin).off()
        sleep(sec)



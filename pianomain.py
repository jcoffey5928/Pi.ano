#!/usr/bin/env python3

from pianoapp import PianoApp
import RPi.GPIO as GPIO

def main():
    app = PianoApp()
    try:
        app.run()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

if __name__ == "__main__": main()

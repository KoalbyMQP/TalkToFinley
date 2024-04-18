from serial import Serial
import RPi.GPIO as GPIO
import time
import signal

pin = 17  #change pin

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
def main():
    signal.signal(signal.SIGINT, onExit)
    GPIO.output(pin, False)
    time.sleep(10)
    GPIO.output(pin, True)

def onExit(self, sig, frame):
    GPIO.output(pin, True)
    exit(0)
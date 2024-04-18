from serial import Serial
import RPi.GPIO as GPIO
import time
import signal

pin = 17  # change pin
previous_state = False  # global variable to store previous state

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

def main():
    global previous_state  # use the global variable

    signal.signal(signal.SIGINT, onExit)

    # Toggle the state based on the previous state
    if previous_state:
        GPIO.output(pin, False)
        previous_state = False
    else:
        GPIO.output(pin, True)
        previous_state = True

def onExit(sig, frame):  # Remove self parameter
    GPIO.output(pin, True)
    exit(0)
import RPi.GPIO as GPIO
import time

RED = 2
GREEN = 3
BLUE = 4

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

GPIO.output(RED, 0)
GPIO.output(GREEN, 0)
GPIO.output(BLUE, 0)

def setRGB(a, b, c):
    GPIO.output(RED, a)
    GPIO.output(GREEN, b)
    GPIO.output(BLUE, c)


while True:
    setRGB(1,1,1)
    time.sleep(0.5)
    setRGB(0,0,0)
    time.sleep(0.5)


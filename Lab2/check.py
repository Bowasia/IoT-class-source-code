import RPi.GPIO as GPIO
import time

RED = 3
GREEN = 2
BLUE = 4

BUTTON = 26
LED_OUT = 19

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_OUT, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.output(LED_OUT, False)
GPIO.output(RED, 1)
GPIO.output(GREEN, 1)
GPIO.output(BLUE, 1)

i = 0

def setRGB(a, b, c):
    GPIO.output(RED, a)
    GPIO.output(GREEN, b)
    GPIO.output(BLUE, c)
    #time.sleep(1);

def num2list(n):
    bi = format(n, '03b')
    l = [int(x) for x in bi]
    return l


while True:
    #GPIO.output(LED_OUT, True)
    #time.sleep(0.5);
    #GPIO.output(LED_OUT, False)
    #time.sleep(0.5);
    #c = GPIO.input(button)

    if (GPIO.input(BUTTON)):
        if (i > 7):
            i = 0;
        arr = num2list(i)
        print(arr)
        setRGB(arr[0], arr[1], arr[2]);
        i += 1;
        time.sleep(0.7)

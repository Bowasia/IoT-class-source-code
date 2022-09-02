import  RPi.GPIO as GPIO
import  time

RED = 2
GREEN = 3
BLUE = 4
BUTTON = 26
i = 0;

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

GPIO.setup (RED, GPIO.OUT)
GPIO.setup (GREEN, GPIO.OUT)
GPIO.setup (BLUE, GPIO.OUT)
GPIO.setup (BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.output(RED, 1)
GPIO.output(GREEN, 1)
GPIO.output(BLUE, 1)

def setRGB(a,b,c):
    GPIO.output(RED, a)
    GPIO.output(GREEN, b)
    GPIO.output(BLUE, c)
    #time.sleep(1);

def num2list(n):
    bi = format(n, '03b')
    l = [int(x) for x in bi]
    return l
    
while True:
    if (GPIO.input(BUTTON)):
        if (i > 7):
            i = 0;
        arr = num2list(i)
        print(arr)
        setRGB(arr[0],arr[1],arr[2]);
        i += 1;
        time.sleep(0.7)


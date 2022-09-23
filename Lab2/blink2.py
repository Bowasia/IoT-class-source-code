import RPi.GPIO as GPIO
import time
import _thread

RED = 3
GREEN = 2
BLUE = 4
BUTTON = 26
LED_RED = 19
LED_GREEN = 13
i = 0;

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(LED_GREEN, GPIO.OUT)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.output(LED_RED, False)
GPIO.output(LED_GREEN, False)
GPIO.output(RED, 1)
GPIO.output(GREEN, 1)
GPIO.output(BLUE, 1)

pwm = GPIO.PWM(LED_GREEN, 100)

def thread_green():
    counter = 10
    pwm.start(counter)
    while 1:
        if counter > 100:
            counter = 10
        pwm.ChangeDutyCycle(counter)
        time.sleep(2)
        counter += 10

def setRGB(a, b, c):
    GPIO.output(RED, a)
    GPIO.output(GREEN, b)
    GPIO.output(BLUE, c)
    #time.sleep(1);

def num2list(n):
    bi = format(n, '03b')
    l = [int(x) for x in bi]
    return l

def button_irq(ch):
    global   i
    if (i > 7):
        i = 0;
    arr = num2list(i)
    print(arr)
    setRGB(arr[0], arr[1], arr[2]);
    i += 1;
    time.sleep(0.7)


GPIO.add_event_detect(BUTTON, GPIO.RISING, callback=button_irq, bouncetime=200)

_thread.start_new_thread(thread_green,())

while True:
    GPIO.output(LED_RED, True)
    time.sleep(0.5);
    GPIO.output(LED_RED, False)
    time.sleep(0.5);



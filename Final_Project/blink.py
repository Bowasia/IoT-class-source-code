import  RPi.GPIO as GPIO
import  time
import  requests
import  mysql.connector

#mydb = mysql.connector.connect(
        #host="localhost",
        #user="id17516185_admin",
        #password="Raspberry@1234",
        #database="id17516185_aquatek"
        #)

#mycursor = mydb.cursor()

#mycursor.execute("SELECT * FROM UserInput")

#myresult = mycursor.fetchall()

status = "off"
http_address = "https://cingalese-flames.000webhostapp.com/api/UserInput/update.php?"

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

#def all_from_db():
    #mycursor = mydb.cursor()
    #mycursor.execute("SELECT * FROM UserInput")
    #myresult = mycursor.fetchall()
    #return myresult



#print("Original data")
#for i in all_from_db():
    #print(x)

while True:
    if (GPIO.input(BUTTON)):
        if (i % 2 == 0):
            text = "off"
        else:
            text = "on"
        request_string = http_address + "id=4&" + "Camera=" + str(text)
        response = requests.get(request_string)
        print("Camera = " + text + "\n" + "response =")
        print(response.text, "\n")
        #print("After update:")
        #for i in all_from_db():
            #print(i)
        if (i > 7):
            i = 0;
        arr = num2list(i)
        print(arr)
        setRGB(arr[0],arr[1],arr[2]);
        i += 1;
        time.sleep(0.7)


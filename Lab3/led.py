import  RPi.GPIO as GPIO
import  time
import paho.mqtt.client as paho

broker = "iotkmitl.ddns.net"
port = 9001

RED = 2
GREEN = 3
BLUE = 4
#BUTTON = 26
LED = 26
i = 0;

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

GPIO.setup (LED, GPIO.OUT)

GPIO.output(LED, 0)

def on_message(mosq, obj, msg):
    global message
    print(msg.payload.decode("utf-8"))
    message = msg.payload.decode("utf-8")
    if (message == "on"):
        GPIO.output(LED, 1)
    else:
        GPIO.output(LED, 0)



def on_subscribe(mosq, obf, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_publish(client, userdata, result):
    print("data published\n")

client1 = paho.Client("control13", transport="websockets")
client1.username_pw_set(username="kmitlcie", password="ciehasmoney")

client1.on_publish = on_publish
client1.on_subscribe = on_subscribe
client1.on_message = on_message

client1.connect(broker, port)
#ret = client1.publish("apple", "on")

client1.subscribe("apple", 0)
client1.loop_forever()

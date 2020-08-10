import time
import paho.mqtt.client as paho
from random import randrange

broker = "broker"


def on_connect(c, ud, flags, rc):
    if rc == 0:
        print("Client connected")
    else:
        print("Client not connected")


def on_message(client, userdata, message):
    time.sleep(1)
    print("received message =", str(message.payload.decode("utf-8")))


client = paho.Client("node1")
client.on_message = on_message

print("connecting to broker ", broker)
client.connect(broker)  # connect
client.subscribe("home/t1")  # subscribe
client.loop_start()  # start loop to process received messages

time.sleep(2)
while True:
    generated_num = randrange(100)
    print("\nGenerated num was: ", generated_num)
    client.publish("home/t2", generated_num)
    time.sleep(5)

client.disconnect()  # disconnect
client.loop_stop()  # stop loop

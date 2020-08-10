import time
import paho.mqtt.client as paho

broker = "192.168.1.13"


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

client.loop_forever()  # start loop to process received messages

print("subscribing ")

client.disconnect()  # disconnect
client.loop_stop()  # stop loop

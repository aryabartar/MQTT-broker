import time
import paho.mqtt.client as paho

broker = "192.168.1.13"


def on_message(client, userdata, message):
    time.sleep(1)
    print("received message =", str(message.payload.decode("utf-8")))


client = paho.Client("node2")
# client.on_message = on_message

print("connecting to broker ", broker)
client.connect(broker)  # connect
client.loop_start()  # start loop to process received messages

while True:
    client.publish("home/t1", "on")
    time.sleep(1)

client.disconnect()
client.loop_stop()

import time
import paho.mqtt.client as paho

broker = "192.168.1.13"


def on_message(client, userdata, message):
    number = int(message.payload.decode("utf-8"))
    if number > 50:
        print("Detected above 50!")
        client.publish("home/t1", "Above 50!")
    else:
        print("Detected below 50.")
        client.publish("home/t1", "Below 50!")


client = paho.Client("node2")
client.on_message = on_message

print("connecting to broker ", broker)
client.connect(broker)  # connect
client.subscribe("home/t2")  # subscribe
client.loop_forever()  # start loop to process received messages

client.disconnect()
client.loop_stop()

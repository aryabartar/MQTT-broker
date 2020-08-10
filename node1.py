import paho.mqtt.client as mqtt
import time


def on_log(client, userdata, level, buf):
    print("log: " + buf)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected, OK")
    else:
        print("Bad connection!", rc)


def on_disconnect(client, userdata, flags, rc=0):
    print("Disconnected result code " + str(rc))


broker = "broker"
client = mqtt.Client("node1")

client.on_connect = on_connect
client.on_log = on_log

print("Connecting to broker ", broker)
client.connect(broker)
client.loop_start()

client.publish("hello2")
client.publish("test", "hello2")

time.sleep(4)

client.loop_stop()
client.disconnect()

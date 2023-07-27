import paho.mqtt.client as mqtt
import json

host=  "localhost"
port = 1883
#topic = "test-topic"
topic = "vasco"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print(json.loads(msg.payload))

def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host, port)
    client.loop_forever()

if __name__ == '__main__':
    main()
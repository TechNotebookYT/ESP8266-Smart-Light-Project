import time
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        global connected
        connected = True
        print("Connected")
    else:
        print("Unable To Connect")

def on_message(client, userdata, msg):
    message = str(msg.payload.decode('utf-8'))
    print(message)

client = mqtt.Client()
broker = 'PI IP'
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, 1883, 60)

last_value = ''

client.loop_start()

while True:
    with open('mqtt.txt', 'r+') as file:
        contents = file.read()
        if contents == '0.0':
            if last_value != 0.0:
                last_value = 0.0
                print(last_value)
                file.truncate(0)
                client.publish('ESP8266 Topic', '0')
                print('published')
        elif contents == '0.1':
            if last_value != 0.1:
                last_value = 0.1
                print(last_value)
                file.truncate(0)
                client.publish('ESP8266 TOPIC', '1')
                print('published')

client.loop_stop()

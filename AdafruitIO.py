import time
import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        global connected
        connected = True
        print("Connected")
    else:
        print("Unable To Connect")
        

connected = False
message_received = False

def on_message(client, userdata, msg):
    message = str(msg.payload.decode('utf-8'))
    print(message)
    with open('mqtt.txt', 'w') as file:
        file.write(message)

client = mqtt.Client()
broker = 'io.adafruit.com'
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set('USER','KEY')
client.connect(broker, 1883, 60)


client.loop_start()
client.subscribe('TOPIC')

while connected != True or message_received != True:
    time.sleep(0.2)

client.loop_forever()

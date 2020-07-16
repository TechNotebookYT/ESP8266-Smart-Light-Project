while True:

    try:

        import time

        import paho.mqtt.client as mqtt

        import requests



        token = 'TOKEN HERE'

        url = f'https://api.telegram.org/bot{token}/getUpdates'



        response = {}

        last_sent = 0

        on_options = ['on', '1']

        off_options = ['off', '0']

        verified_sender = #SENDER HERE

        broker_address = 'IP ADDR'
        
        topic = 'TOPIC HERE'



        connected = False





        def on_connect(client, userdata, flags, rc):

            if rc == 0:

                connected = True

                print("Connected")

            else:

                print("Not Able To Connect")





        def toggle(state):

            client.connect(broker_address)

            client.loop_start()

            client.publish(topic, state)

            print('publish')

            client.loop_stop()





        client = mqtt.Client("client-win")  # create new instance

        client.on_connect = on_connect

        client.connect(broker_address, keepalive=60)



        while True:

            response = requests.post(url).json()['result'][-1]

            if response != {} and response != "{'ok':true,'result':[]}":

                sender = response['message']['from']['id']

                date = response['message']['date']

                if sender == verified_sender:

                    if date != last_sent:

                        message = str(response['message']['text'])

                        last_sent = date

                        if message.lower() in on_options:

                            toggle(1)

                        elif message.lower() in off_options:

                            toggle(0)



                elif sender != verified_sender:

                    print('An un-verified Person is sending a message to the bot! Rejecting Request')



                else:

                    print('Unexpected Error! Continuing On')

                time.sleep(1.5)

    except IndexError:

        time.sleep(15)

    except KeyboardInterrupt:
        exit()


import paho.mqtt.client as mqtt
import hiveclient
import apihandler
import time

subscribers: list = []

def on_connect(client: mqtt.Client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    client.subscribe(hiveclient.TOPIC_SUBSCRIBE)

def on_publish(client, userdata, mid, reason_code, properties):
    print("mid: " + str(mid))
    
def on_message(client: mqtt.Client, userdata, msg: mqtt.MQTTMessage):
    coords = str(msg.payload, encoding='utf-8').split(' ')
    print('Received ', coords)
    if coords not in subscribers:
        subscribers.append(coords)

publisher = hiveclient.get_client()
hiveclient.connect(publisher)

publisher.on_connect = on_connect
publisher.on_publish = on_publish
publisher.on_message = on_message

publisher.loop_start()

while True:
    if publisher.is_connected:
        for coord in subscribers:
            result = apihandler.get_weather(coord[0], coord[1])
            msg: str = result['weather'][0]['description']
            publisher.publish(hiveclient.TOPIC_WEATHER, msg.encode('utf-8'))
        time.sleep(10)

publisher.loop_stop()
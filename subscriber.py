import paho.mqtt.client as mqtt
import hiveclient

coord = '-22.651156126816506 -42.01691522039935'

def on_connect(client: mqtt.Client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    client.subscribe(hiveclient.TOPIC_WEATHER)

def on_subscribe(client: mqtt.Client, userdata, mid, granted_qos, properties=None):
    client.publish(hiveclient.TOPIC_SUBSCRIBE, bytearray(coord, encoding='utf-8'))
    
def on_publish(client, userdata, mid, reason_code, properties):
    print("mid: " + str(mid))

def on_message(client, userdata, msg: mqtt.MQTTMessage):
    print(msg.payload.decode('utf-8'))

subscriber = hiveclient.get_client()
subscriber.on_connect = on_connect
subscriber.on_message = on_message
subscriber.on_subscribe = on_subscribe
hiveclient.connect(subscriber)

subscriber.loop_forever()
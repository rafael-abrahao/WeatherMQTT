import paho.mqtt.client as mqtt
from paho.mqtt.enums import MQTTErrorCode
from dataclasses import dataclass

TOPIC_WEATHER = 'topic/weather'
TOPIC_SUBSCRIBE = 'topic/subscribe'

__broker_address = '...' #colocar endereço do broker
__port = 8883

#colocar os dados de um usuário cadastrado no hive
__username = '...'
__password = '...' 

def get_client(username = __username, password = __password):
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
    client.username_pw_set(username, password)
    return client


def connect(client: mqtt.Client) -> MQTTErrorCode:
    return client.connect(__broker_address, __port)

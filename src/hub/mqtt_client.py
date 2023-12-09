import paho.mqtt.client as mqtt
from utils import config

class MqttClient:
    def __init__(self):
        self.client = mqtt.Client()

    def connect(self, host, port):
        self.client.connect(host, port)

    def subscribe(self, topic):
        self.client.subscribe(topic)

    def on_message(self, handler):
        self.client.on_message = handler

    def loop_forever(self):
        self.client.loop_forever()

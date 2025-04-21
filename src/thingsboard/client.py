from paho.mqtt import client as mqtt
import json
import time
from utils.config import load_config

class ThingsBoardClient:
    def __init__(self):
        self.config = load_config()
        self.client = mqtt.Client()
        self.access_token = self.config['THINGSBOARD_ACCESS_TOKEN']
        self.client.on_connect = self.on_connect
        self.client.on_publish = self.on_publish

    def on_connect(self, client, userdata, flags, rc):
        print("Connected to ThingsBoard with result code: " + str(rc))

    def on_publish(self, client, userdata, mid):
        print("Data published with message ID: " + str(mid))

    def connect(self):
        self.client.username_pw_set(self.access_token)
        self.client.connect(self.config['MQTT_BROKER'], self.config['MQTT_PORT'], 60)
        self.client.loop_start()

    def publish(self, telemetry_data):
        topic = "v1/devices/me/telemetry"
        payload = json.dumps(telemetry_data)
        result = self.client.publish(topic, payload)
        return result

    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()
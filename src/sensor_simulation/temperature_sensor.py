from paho.mqtt import client as mqtt
import json
import random
import time

class TemperatureSensor:
    def __init__(self, broker, port, topic, access_token):
        self.broker = broker
        self.port = port
        self.topic = topic
        self.access_token = access_token
        self.client = mqtt.Client()
        self.client.username_pw_set(access_token, password=None)

    def connect(self):
        self.client.connect(self.broker, self.port)

    def publish_temperature(self):
        while True:
            temperature = round(random.uniform(15.0, 30.0), 2)  # Simulate temperature between 15 and 30 degrees Celsius
            payload = json.dumps({"temperature": temperature})
            self.client.publish(self.topic, payload)
            print(f"Published temperature: {payload} to topic: {self.topic}")
            time.sleep(5)  # Publish every 5 seconds

    def start(self):
        self.connect()
        self.client.loop_start()
        self.publish_temperature()

if __name__ == "__main__":
    # Example usage
    broker = "mqtt.thingsboard.io"  # Replace with your MQTT broker
    port = 1883
    topic = "v1/devices/me/telemetry"
    access_token = "YOUR_ACCESS_TOKEN"  # Replace with your ThingsBoard device access token

    sensor = TemperatureSensor(broker, port, topic, access_token)
    sensor.start()
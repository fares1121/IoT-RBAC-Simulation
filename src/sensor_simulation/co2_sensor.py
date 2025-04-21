from paho.mqtt import client as mqtt
import json
import time
import os

class CO2Sensor:
    def __init__(self, broker, port, topic, access_token):
        self.broker = broker
        self.port = port
        self.topic = topic
        self.access_token = access_token
        self.client = mqtt.Client()

    def connect(self):
        self.client.connect(self.broker, self.port)

    def publish_co2_data(self):
        while True:
            co2_level = self.simulate_co2_level()
            payload = {
                "co2": co2_level
            }
            self.client.publish(self.topic, json.dumps(payload), qos=1)
            print(f"Published CO2 level: {co2_level} ppm")
            time.sleep(5)  # Publish every 5 seconds

    def simulate_co2_level(self):
        # Simulate CO2 level (in ppm)
        return round(400 + (100 * (time.time() % 60) / 60), 2)

if __name__ == "__main__":
    broker = os.getenv("MQTT_BROKER", "broker.hivemq.com")
    port = int(os.getenv("MQTT_PORT", 1883))
    topic = os.getenv("THINGSBOARD_TOPIC", "v1/devices/me/telemetry")
    access_token = os.getenv("THINGSBOARD_ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")

    co2_sensor = CO2Sensor(broker, port, topic, access_token)
    co2_sensor.connect()
    co2_sensor.publish_co2_data()
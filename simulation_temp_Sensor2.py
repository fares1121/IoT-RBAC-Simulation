import paho.mqtt.client as mqtt
import json
import time
import random
from paho.mqtt.client import CallbackAPIVersion

# MQTT Configuration
BROKER = "192.168.1.64"
PORT = 1883
TOPIC = "v1/devices/me/telemetry"
CLIENT_ID = "temp.id"
USERNAME = "dev1"
PASSWORD = "dev11pass"

# Create MQTT client with correct callback API version
client = mqtt.Client(
    client_id=CLIENT_ID,
    protocol=mqtt.MQTTv311,
    transport="tcp",
    callback_api_version=CallbackAPIVersion.VERSION1
)
client.username_pw_set(USERNAME, PASSWORD)

# Callback for connection
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected successfully to ThingsBoard MQTT broker.")
    else:
        print(f"Connection failed with code {rc}")

client.on_connect = on_connect

# Connect to MQTT broker
client.connect(BROKER, PORT, 60)
client.loop_start()

try:
    while True:
        # Generate random telemetry data
        payload = {
            "temperature": round(random.uniform(20.0, 30.0), 2)
        }

        # Publish to ThingsBoard
        client.publish(TOPIC, json.dumps(payload), qos=1)
        print(f"Published: {payload}")

        # Wait for 5 seconds
        time.sleep(5)

except KeyboardInterrupt:
    print("\nSimulation stopped by user.")

finally:
    client.loop_stop()
    client.disconnect()

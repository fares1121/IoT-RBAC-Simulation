from sensor_simulation.temperature_sensor import TemperatureSensor
from sensor_simulation.co2_sensor import CO2Sensor
from thingsboard.client import ThingsBoardClient
from utils.config import load_config

def main():
    # Load configuration
    config = load_config()

    # Initialize ThingsBoard client
    tb_client = ThingsBoardClient(config['thingsboard']['host'], config['thingsboard']['access_token'])

    # Initialize sensors
    temperature_sensor = TemperatureSensor(tb_client, config['sensors']['temperature'])
    co2_sensor = CO2Sensor(tb_client, config['sensors']['co2'])

    # Start publishing data
    temperature_sensor.start()
    co2_sensor.start()

if __name__ == "__main__":
    main()
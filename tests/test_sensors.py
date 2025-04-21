import unittest
from src.sensor_simulation.temperature_sensor import TemperatureSensor
from src.sensor_simulation.co2_sensor import CO2Sensor

class TestSensorSimulation(unittest.TestCase):

    def setUp(self):
        self.temp_sensor = TemperatureSensor()
        self.co2_sensor = CO2Sensor()

    def test_temperature_sensor_publish(self):
        temperature_data = self.temp_sensor.publish_data()
        self.assertIsInstance(temperature_data, dict)
        self.assertIn('temperature', temperature_data)
        self.assertIsInstance(temperature_data['temperature'], float)

    def test_co2_sensor_publish(self):
        co2_data = self.co2_sensor.publish_data()
        self.assertIsInstance(co2_data, dict)
        self.assertIn('co2', co2_data)
        self.assertIsInstance(co2_data['co2'], float)

if __name__ == '__main__':
    unittest.main()
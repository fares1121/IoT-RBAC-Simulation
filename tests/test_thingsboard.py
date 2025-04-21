import unittest
from src.thingsboard.client import ThingsBoardClient
from src.thingsboard.api import ThingsBoardAPI

class TestThingsBoard(unittest.TestCase):

    def setUp(self):
        self.client = ThingsBoardClient("http://demo.thingsboard.io", "YOUR_ACCESS_TOKEN")
        self.api = ThingsBoardAPI(self.client)

    def test_device_registration(self):
        device_name = "Test Device"
        device_type = "default"
        response = self.api.register_device(device_name, device_type)
        self.assertIn("id", response)

    def test_publish_telemetry(self):
        device_id = "YOUR_DEVICE_ID"
        telemetry_data = {"temperature": 25, "co2": 400}
        response = self.api.publish_telemetry(device_id, telemetry_data)
        self.assertEqual(response.status_code, 200)

    def test_get_device(self):
        device_id = "YOUR_DEVICE_ID"
        response = self.api.get_device(device_id)
        self.assertEqual(response["id"], device_id)

    def test_invalid_access(self):
        invalid_client = ThingsBoardClient("http://demo.thingsboard.io", "INVALID_TOKEN")
        with self.assertRaises(Exception):
            invalid_client.get_devices()

if __name__ == '__main__':
    unittest.main()
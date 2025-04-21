def register_device(access_token, device_name):
    import requests

    url = "http://demo.thingsboard.io/api/device"
    headers = {
        "Content-Type": "application/json",
        "X-Authorization": f"Bearer {access_token}"
    }
    payload = {
        "name": device_name,
        "type": "sensor"
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.json()

def publish_telemetry(access_token, device_id, telemetry_data):
    import requests

    url = f"http://demo.thingsboard.io/api/v1/{access_token}/telemetry"
    payload = telemetry_data

    response = requests.post(url, json=payload)
    return response.status_code

def get_device_data(access_token, device_id):
    import requests

    url = f"http://demo.thingsboard.io/api/device/{device_id}/telemetry"
    headers = {
        "X-Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)
    return response.json()
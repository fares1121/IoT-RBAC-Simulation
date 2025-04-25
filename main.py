import json
import requests
import os

# ThingsBoard configuration
THINGSBOARD_HOST = '192.168.1.64'
BASE_URL = f'http://{THINGSBOARD_HOST}:8080'
LOGIN_URL = f'{BASE_URL}/api/auth/login'

# User credentials
USERS = [
    {"role": "Admin", "username": "Alice@group9.com", "password": "alice123"},
    {"role": "Operator", "username": "Bob@group9.com", "password": "bob123"},
    {"role": "Viewer", "username": "Charlie@group9.com", "password": "charlie123"}
]

def log_to_file(filename, title, message):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"[{title}] {message}\n")

def log_json_to_file(filename, title, json_data):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"\n=== {title} ===\n")
        f.write(json.dumps(json_data, indent=4))
        f.write("\n")

def authenticate(username, password, logfile):
    try:
        response = requests.post(LOGIN_URL, json={'username': username, 'password': password})
        response.raise_for_status()
        token = response.json()['token']
        log_to_file(logfile, "INFO", f"{username} - Authenticated successfully")
        return token
    except requests.RequestException as e:
        log_to_file(logfile, "ERROR", f"{username} - Authentication failed: {e}")
        return None

def get_user_info(jwt, username, logfile):
    headers = {'X-Authorization': f'Bearer {jwt}'}
    try:
        response = requests.get(f'{BASE_URL}/api/auth/user', headers=headers)
        response.raise_for_status()
        user_info = response.json()
        log_json_to_file(logfile, f"{username} - User Profile", user_info)
        return {
            'authority': user_info.get('authority'),
            'customer_id': user_info.get('customerId', {}).get('id'),
            'user_id': user_info.get('id', {}).get('id')
        }
    except requests.RequestException as e:
        log_to_file(logfile, "ERROR", f"{username} - Failed to retrieve user profile: {e}")
        return None

def get_devices(jwt, role_info, username, logfile):
    headers = {'X-Authorization': f'Bearer {jwt}'}
    authority = role_info['authority']
    customer_id = role_info['customer_id']

    if authority == "TENANT_ADMIN":
        url = f'{BASE_URL}/api/tenant/devices?pageSize=100&page=0'
        log_to_file(logfile, "INFO", f"{username} - Using /tenant/devices")
    elif authority == "CUSTOMER_USER":
        url = f'{BASE_URL}/api/customer/{customer_id}/devices?pageSize=100&page=0'
        log_to_file(logfile, "INFO", f"{username} - Using /customer/{customer_id}/devices")
    else:
        log_to_file(logfile, "WARN", f"{username} - Unsupported authority type: {authority}")
        return []

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json().get('data', [])
        log_to_file(logfile, "INFO", f"{username} - Retrieved {len(data)} device(s)")
        for d in data:
            log_to_file(logfile, "DEVICE", f"{d['name']} (ID: {d['id']['id']})")
        return data
    except requests.RequestException as e:
        log_to_file(logfile, "ERROR", f"{username} - Failed to retrieve devices: {e}")
        return []

def get_telemetry(jwt, device_id, username, logfile):
    headers = {'X-Authorization': f'Bearer {jwt}'}
    url = f'{BASE_URL}/api/plugins/telemetry/DEVICE/{device_id}/values/timeseries'
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        telemetry = response.json()
        if telemetry:
            log_json_to_file(logfile, f"{username} - Telemetry for Device {device_id}", telemetry)
        else:
            log_to_file(logfile, "WARN", f"{username} - No telemetry found for device {device_id}")
    except requests.RequestException as e:
        log_to_file(logfile, "ERROR", f"{username} - Failed to get telemetry: {e}")

# === MAIN EXECUTION ===

if __name__ == "__main__":
    os.makedirs("logs", exist_ok=True)

    for user in USERS:
        logfile = f"logs/{user['role'].lower()}_log.txt"
        open(logfile, 'w').close()  # Clear previous log
        print(f"\nLogging for {user['role']} ({user['username']}) -> {logfile}")

        jwt = authenticate(user['username'], user['password'], logfile)
        if jwt:
            role_info = get_user_info(jwt, user['username'], logfile)
            if role_info:
                devices = get_devices(jwt, role_info, user['username'], logfile)
                for device in devices:
                    get_telemetry(jwt, device['id']['id'], user['username'], logfile)

# Setup Guide for IoT RBAC Simulation Project

## Introduction
This guide provides step-by-step instructions for setting up the IoT RBAC Simulation project, which simulates an IoT sensor network with Role-Based Access Control (RBAC) using ThingsBoard and Python.

## Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.x
- pip (Python package installer)

## Step 1: Create a ThingsBoard Account and Device
1. Visit [ThingsBoard Demo](https://demo.thingsboard.io) or deploy a local instance of ThingsBoard.
2. Create a free user account.
3. Navigate to **Devices** > **+ Add new device**.
4. After creating the device, click on it, open the **Details** tab, and copy the **Access Token** for later use.

## Step 2: Clone the Repository
Clone the project repository to your local machine using the following command:
```
git clone <repository-url>
cd iot-rbac-simulation
```

## Step 3: Install Required Python Packages
Install the necessary Python packages using pip:
```
pip install -r requirements.txt
```

## Step 4: Configure Settings
1. Open the `config/settings.json` file.
2. Add your ThingsBoard access token and MQTT broker details in the appropriate fields.

## Step 5: Create a Dashboard in ThingsBoard
1. Go to **Dashboards** > **+ Create new dashboard**.
2. Open the dashboard and click **Edit** > **Add Widget**.
3. Assign the device you created as a data source for each widget.

## Step 6: Implement RBAC in ThingsBoard
1. Navigate to **Security** > **Roles**.
2. Create the following roles:
   - **Admin**: Full access to all devices and dashboard controls.
   - **Operator**: Can view and operate dashboards but cannot configure devices.
   - **Viewer**: Read-only access.
3. Create users under **Security** > **Users**, assigning them to the appropriate role.

## Step 7: Run the Simulation
1. In the terminal, navigate to the `src` directory:
```
cd src
```
2. Run the main application:
```
python main.py
```

## Step 8: Verify Access Control
Manually log in as different users to verify that each role's permissions are enforced:
- **Admin** can modify dashboards and add devices.
- **Operator** can interact with dashboards but not change settings.
- **Viewer** can only observe data.

## Conclusion
You have successfully set up the IoT RBAC Simulation project. You can now simulate sensor data and test the role-based access control features. For further development, consider implementing additional features as outlined in the project documentation.
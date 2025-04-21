# IoT RBAC Simulation

## Introduction
This project simulates an IoT sensor network focused on environmental monitoring, implementing a Role-Based Access Control (RBAC) system to secure access to sensor data. The system utilizes ThingsBoard for data visualization and management, while Python is used to simulate sensor data.

## Project Structure
- **src/**: Contains the main application code.
  - **sensor_simulation/**: Simulates temperature and CO₂ sensors.
  - **thingsboard/**: Handles interactions with the ThingsBoard platform.
  - **rbac/**: Implements the RBAC system for access control.
  - **utils/**: Contains utility functions and configuration settings.
  - **main.py**: The entry point of the application.
  
- **tests/**: Contains unit tests for the application components.
  
- **config/**: Holds configuration files, including settings for ThingsBoard and MQTT.
  
- **docs/**: Documentation files, including architecture and setup guides.
  
- **requirements.txt**: Lists required Python packages for the project.

- **.env.example**: Example environment variables needed for the project.

## Setup Instructions
1. **Create a ThingsBoard Account and Device**
   - Visit [ThingsBoard Demo](https://demo.thingsboard.io) or deploy a local instance.
   - Create a free user account.
   - Navigate to Devices > + Add new device.
   - After creation, copy the Access Token from the Details tab.

2. **Install Required Python Packages**
   - Run the following command to install the necessary packages:
     ```
     pip install -r requirements.txt
     ```

3. **Configure Environment Variables**
   - Copy `.env.example` to `.env` and fill in the required values, including ThingsBoard access tokens and MQTT broker details.

4. **Run the Application**
   - Execute the main script to start the sensor simulations and publish data to ThingsBoard:
     ```
     python src/main.py
     ```

## Usage
- The application simulates temperature and CO₂ sensors that publish data to ThingsBoard.
- Users with different roles (Admin, Operator, Viewer) can access the dashboard with varying permissions.

## Testing
- Unit tests are provided in the `tests/` directory. Run the tests to ensure the functionality of the application:
  ```
  pytest tests/
  ```

## Conclusion
This project demonstrates a secure and scalable approach to managing IoT sensor data with role-based access control, providing a foundation for future enhancements and real-world applications.
# Architecture Overview of IoT RBAC Simulation

## Introduction
This document provides an overview of the architecture for the IoT RBAC (Role-Based Access Control) simulation project. The system is designed to simulate an IoT sensor network for environmental monitoring while enforcing secure access control through defined user roles.

## System Components
The architecture consists of the following key components:

1. **Simulated Sensors**: 
   - Python scripts simulate temperature and CO₂ sensors. These sensors publish telemetry data to the ThingsBoard platform using the MQTT protocol.

2. **ThingsBoard**: 
   - An open-source IoT platform that manages the data from the sensors. It provides visualization tools and dashboards for monitoring sensor data and implements the RBAC system to control user access.

3. **User Roles**: 
   - The system defines three user roles: Admin, Operator, and Viewer. Each role has specific permissions that dictate what actions users can perform within the ThingsBoard interface.

## Architecture Diagram
[Insert Architecture Diagram Here]

The diagram illustrates the flow of data from the simulated sensors to the ThingsBoard platform and the interaction of users with the system based on their roles.

## Data Flow
1. **Sensor Simulation**:
   - The temperature and CO₂ sensors generate data at defined intervals and publish it to ThingsBoard.

2. **Data Management**:
   - ThingsBoard receives the data and stores it for visualization and analysis. Users can access this data based on their assigned roles.

3. **Role-Based Access Control**:
   - The RBAC system ensures that users can only perform actions permitted by their roles. For example:
     - Admins can modify dashboards and add devices.
     - Operators can view and interact with dashboards but cannot change settings.
     - Viewers have read-only access to the data.

## Conclusion
The architecture of the IoT RBAC simulation project effectively integrates simulated sensors, a robust IoT platform, and a secure access control mechanism. This design not only facilitates environmental monitoring but also ensures that sensitive data is protected from unauthorized access.
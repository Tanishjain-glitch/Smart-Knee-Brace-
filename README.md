
# Smart Pneumatic Knee Brace

This project is an IoT-based smart pneumatic knee brace designed to assist in rehabilitation by monitoring gait, detecting anomalies, and providing adaptive support through real-time sensor feedback and AI processing.

## Features
- Real-time knee angle and movement analysis using MPU6050 and flex sensor
- BLE communication to mobile app for remote monitoring
- AI model for anomaly detection based on gait patterns
- Pneumatic actuator control based on dynamic input
- Web server visualization (Flask + MQTT)
- Temperature monitoring for inflammation detection

## Directories
- `firmware/`: Arduino code for ESP8266 to handle sensors and actuators
- `ai_model/`: AI scripts and models for anomaly detection
- `mobile_app_ble/`: Codebase for BLE-enabled Android/iOS application
- `python_server/`: MQTT broker interface and visualization backend

---
**Status**: Provisional Patent Filed

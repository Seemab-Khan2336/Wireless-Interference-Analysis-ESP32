# Bluetooth & Wi-Fi Jamming Analysis (RF Interference Study) 📡🛡️

This project explores the security and stability of wireless networks under heavy RF interference. By utilizing an **ESP32** and an **nRF24L01** module, we simulate signal congestion to study how Bluetooth (FHSS) and Wi-Fi (DSSS/OFDM) handle "Availability" threats in the shared 2.4 GHz spectrum.

## 🎯 Project Objectives
* **Analyze Protocol Resilience:** Compare how Bluetooth's frequency hopping behaves vs. Wi-Fi's fixed-channel communication under noise.
* **Hardware Implementation:** Interface ESP32 with nRF24L01 via SPI communication.
* **Signal Monitoring:** Real-time visualization of Wi-Fi signal strength degradation during interference events.
* **Mitigation Research:** Identify defensive strategies like dual-band usage and adaptive channel selection.

## 🛠️ Hardware Requirements
* **ESP32 WROOM-32U:** Main microcontroller for logic and timing.
* **nRF24L01+ PA/LNA:** External antenna module for RF signal transmission.
* **Push Button:** For toggling between Channel Hopping and Sequential modes.
* **Power Supply:** Stable 3.3V/5V source for the high-power antenna.

## 💻 Software Features
* **Live Signal Monitor (`new2.py`):** A Python script that uses `matplotlib` and `subprocess` to graph real-time Wi-Fi signal strength percentages.
* **Firmware:** Logic for SPI communication and RF channel manipulation (implemented in Arduino IDE/C++).

## 📊 Results Summary
* **Bluetooth:** Showed better short-range resilience due to Frequency Hopping Spread Spectrum (FHSS).
* **Wi-Fi:** Experienced significant throughput drop and connection instability when the noise floor increased.

## 📂 Project Structure
* `new2.py`: Python script for real-time Wi-Fi signal visualization.
* `Report_NS_Project.docx`: Comprehensive technical report on experimental observations.
* `Bluetooth & Wi-fi jamming.pptx`: Presentation slides detailing system architecture and hardware pins.

## 🎓 Academic Info
Developed as a **Network Security** project at the **University of Wah** by:
* Awais Asif (UW-23-CY-BS-010)
* Seemab Khan (UW-23-CY-BS-005)
* Rubaiqa Pervez (UW-23-CY-BS-020)

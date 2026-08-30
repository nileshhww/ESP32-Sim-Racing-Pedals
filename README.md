# ESP32 Sim Racing Pedals 🏎️

A DIY 3-pedal sim racing setup built using an **ESP32**, **Hall effect sensors**, and a **load cell**.

The project combines custom hardware, embedded C++ firmware, sensor processing, and a Python vJoy bridge to turn the pedals into a PC game-controller input.

## 🚗 Project Overview

I designed and built these pedals for use with PC sim racing games such as **Assetto Corsa**.

The ESP32 reads the **throttle, brake, and clutch** inputs, processes the sensor values, and sends them to the PC through serial communication. A Python bridge then converts the data into virtual joystick inputs using **vJoy**.

The goal was to achieve smooth and accurate pedal control with a close to **1:1 relationship between physical pedal movement and in-game input**.

## 🔧 Hardware

- ESP32
- Hall effect sensors
- Load cell
- HX711 load-cell amplifier
- Push buttons for gear shifting
- DIY pedal mechanism

## 💻 Software & Technologies

- **Arduino IDE**
- **C++ / Arduino**
- **Python**
- **vJoy**
- **Serial Communication**

## ⚙️ Current Features

- 🎮 Throttle input
- 🛑 Load-cell based brake input
- 🦶 Clutch input
- 📏 Dead-zone handling
- 🔄 1:1 pedal input-to-output response
- ⚡ ESP32-based sensor processing
- ⬆️ Gear-up button
- ⬇️ Gear-down button
- 🖥️ PC controller output through vJoy
- 🔧 Custom-built hardware and firmware

## 📁 Project Structure

ESP32-Sim-Racing-Pedals/
│
├── ESP32-Sim-Racing-Pedals.ino
├── vjoy_bridge.py
└── README.md

## 🚧 Future Improvements

- Advanced calibration system
- Adjustable sensitivity curves
- Improved sensor filtering
- Save calibration settings to ESP32 flash
- USB HID support
- Improved pedal mechanics

- ## 📸 Project

More photos, wiring details, and project documentation will be added soon.

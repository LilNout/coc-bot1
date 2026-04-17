# Clash of Clans Auto Farm Bot

A Python-based bot for automating resource collection and other tasks in Clash of Clans using ADB and OpenCV.

## Features

- **Resource Collection**: Automatically detects and taps on gold mines, elixir collectors, and dark elixir drills.
- **ADB Integration**: Uses Android Debug Bridge for interaction with the device.
- **Computer Vision**: Uses OpenCV template matching to identify game elements.

## Prerequisites

- Python 3.x
- ADB (Android Debug Bridge) installed and added to PATH.
- An Android device or emulator with Clash of Clans installed.
- USB Debugging enabled on the device.

## Installation

1. Clone the repository.
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Setup

### 1. Template Images

The bot relies on template images to identify game elements. You need to capture small screenshots of the elements you want to detect (e.g., a full gold collector) and place them in the `templates/` directory.

Expected templates:
- `templates/gold_collector.png`
- `templates/elixir_collector.png`
- `templates/dark_elixir_collector.png`

### 2. Device Connection

Ensure your device is connected and recognized by ADB:
```bash
adb devices
```

## Usage

Run the bot using:
```bash
python main.py
```

If you have multiple devices connected, specify the device ID:
```bash
python main.py --device <device_id>
```

## Disclaimer

Using bots in Clash of Clans may violate Supercell's Terms of Service and can lead to your account being banned. Use this bot at your own risk. This project is for educational purposes only.

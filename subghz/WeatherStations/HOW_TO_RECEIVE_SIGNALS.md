# How to Receive TCM220063 Weather Station Signals

Since you want to **receive** weather station signals rather than transmit them, here are the proper methods for capturing TCM220063 data with your Flipper Zero.

## 🎯 **Method 1: Weather Station App (Automatic Decoding)**

The Weather Station app by @Skorpionm is the **best option** for receiving and decoding live weather signals.

### How it Works:
- **No "read mode"** - the app continuously listens
- **Automatic protocol detection** - recognizes Nexus-TH signals
- **Real-time decoding** - displays temperature, humidity, etc.
- **Works with live signals only** - not for playing back saved files

### Setup:
1. **Install**: https://lab.flipper.net/apps/sub_ghz_weather_station
2. **Open the app** on your Flipper Zero
3. **Position Flipper** within 5-20 meters of your TCM220063 station
4. **Wait patiently** - signals transmit every 60 seconds
5. **Watch the display** for automatic decoding

### What You'll See:
```
┌─────────────────────┐
│   Nexus-TH          │
│                     │
│  Temperature: 21.3°C│
│  Humidity:    68%   │
│  Channel:     0     │
│  ID:          90    │
│  Battery:     OK    │
│                     │
│  Signal: ████░░     │
│  RSSI: -45 dBm      │
└─────────────────────┘
```

---

## 🎯 **Method 2: Sub-GHz Read RAW (Manual Capture)**

Use the standard Sub-GHz app to capture raw signals for analysis.

### Setup:
1. **Sub-GHz** → **Read RAW**
2. **Configure frequency**: 433.92 MHz
3. **Set modulation**: AM650 (AM 650kHz)
4. **Position Flipper** near weather station
5. **Press record** and wait up to 60 seconds
6. **Save the captured signal**

### Settings:
- **Frequency**: 433920000 Hz (433.92 MHz)
- **Modulation**: AM650 or OOK270Async
- **Sample Rate**: Default is fine
- **Recording Time**: At least 70 seconds to catch a transmission

### Analysis:
After capturing, you can:
- **View signal** in the Flipper's spectrum analyzer
- **Export to computer** for analysis with tools like rtl_433
- **Compare with provided sample files**

---

## 🎯 **Method 3: Sub-GHz Frequency Analyzer**

Use the built-in frequency analyzer to detect when signals are being transmitted.

### How to Use:
1. **Sub-GHz** → **Frequency Analyzer**
2. **Navigate to 433.92 MHz**
3. **Watch for signal spikes** every 60 seconds
4. **Note the exact frequency** (may vary slightly)
5. **Switch to Read RAW** when you see activity

This helps you:
- **Confirm your weather station is transmitting**
- **Find the exact frequency** (sometimes slightly off from 433.92)
- **Time your captures** for maximum success

---

## 🎯 **Method 4: Third-Party Tools (Advanced)**

If you have additional hardware, these tools can help:

### RTL-SDR + rtl_433:
- **Hardware**: RTL-SDR dongle (~$25)
- **Software**: rtl_433 (free)
- **Command**: `rtl_433 -f 433.92M -s 1024k`
- **Advantage**: Continuous monitoring, detailed analysis

### HackRF + GQRX:
- **Hardware**: HackRF One (~$300)
- **Software**: GQRX (free)
- **Advantage**: Wide frequency range, waterfall display

---

## 📍 **Positioning Tips for Best Reception**

### Flipper Position:
- **Distance**: 2-20 meters from weather station
- **Line of sight**: Avoid walls, metal objects
- **Height**: Weather stations often mounted high - try elevated positions
- **Orientation**: Point Flipper's screen toward the station

### Environmental Factors:
- **Time of day**: Less RF interference at night
- **Weather**: Rain/snow can affect signal propagation  
- **Buildings**: Urban environments have more interference
- **Other devices**: Turn off WiFi, Bluetooth on nearby devices

---

## ⏰ **Timing is Critical**

### TCM220063 Transmission Pattern:
- **Interval**: Every 60 seconds (±5 seconds)
- **Duration**: ~500ms transmission time
- **Pattern**: Consistent timing, but can drift slightly

### Capture Strategy:
1. **Start capture** and wait the full 70 seconds
2. **Don't move** the Flipper during capture
3. **Try multiple captures** if first attempt fails
4. **Note the time** when signals are detected for future captures

---

## 🔧 **Troubleshooting Reception Issues**

### No Signals Detected:

**Check the Basics:**
- ✅ **Battery in weather station** - replace if low
- ✅ **Frequency setting** - exactly 433.92 MHz
- ✅ **Distance** - try closer (2-5 meters)
- ✅ **Timing** - wait full 60+ seconds

**Advanced Troubleshooting:**
- **Test with frequency analyzer** first
- **Try different modulation** (AM650, OOK270)
- **Check for interference** (turn off other 433 MHz devices)
- **Verify weather station** is actually transmitting (check display updates)

### Weak Signals:
- **Move closer** to weather station
- **Raise Flipper higher** (weather stations often mounted high)
- **Try different angles** - RF propagation can be directional
- **Wait for night time** - less RF interference

### Intermittent Reception:
- **Weather station battery** may be low
- **RF interference** from other devices
- **Environmental factors** (weather, obstacles)
- **Temperature effects** on electronics

---

## 🌟 **What to Do After Successful Capture**

### With Weather Station App:
- **Data is automatically decoded** and displayed
- **Note the values** for comparison with actual weather
- **Monitor over time** to see data patterns

### With Raw Captures:
- **Compare with sample files** in this repository
- **Use the Python decoder** script to analyze data
- **Create your own .sub files** from captures
- **Share interesting captures** with the community

### Analysis Tools:
- **decode_tcm220063.py** script in this repository
- **Flipper Zero desktop app** for signal analysis
- **rtl_433** for detailed protocol decoding
- **Online signal analysis** tools

---

## 📊 **Expected Signal Characteristics**

When you successfully capture a TCM220063 signal:

### Timing Pattern:
```
Preamble: 12 bits alternating (sync pattern)
Sync:     4 bits (frame start marker)
Data:     32 bits (actual weather data)
Gap:      20ms silence
Repeat:   Usually 2-3 times per transmission
```

### Data Content:
- **Channel ID**: Usually 0 (4 bits)
- **Sensor ID**: Fixed per device (8 bits)
- **Temperature**: -40°C to +60°C (12 bits)
- **Humidity**: 0-100% (8 bits)

### Signal Strength:
- **Close range** (2m): -30 to -20 dBm
- **Medium range** (10m): -50 to -40 dBm  
- **Long range** (30m): -70 to -60 dBm

---

## 💡 **Pro Tips**

### For Beginners:
1. **Start with Weather Station app** - easiest to use
2. **Position close** to weather station initially
3. **Be patient** - signals only transmit every 60 seconds
4. **Try multiple times** - success rate improves with practice

### For Advanced Users:
1. **Combine methods** - use analyzer + raw capture
2. **Create custom scripts** from your captures
3. **Monitor multiple channels** if your station supports them
4. **Set up automated monitoring** with external SDR tools

### For Troubleshooting:
1. **Test with provided sample files** first
2. **Verify your weather station** is working (check display)
3. **Try different times** of day for better RF conditions
4. **Compare with online weather** to validate decoded data

---

**Remember**: The goal is to **receive and decode** live weather data, not to play back saved files. The Weather Station app is specifically designed for this purpose and will give you the best results!
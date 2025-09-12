# Quick Setup Guide: Weather Station App + TCM220063

This guide helps you set up the TCM220063 weather station with the Weather Station app by @Skorpionm.

## ⚡ Quick Setup (5 minutes)

### Step 1: Install Weather Station App
**Option A - Via Flipper Lab (Recommended):**
1. Visit: https://lab.flipper.net/apps/sub_ghz_weather_station
2. Click **"Install on Flipper"**
3. Connect your Flipper Zero and follow the installation

**Option B - Via qFlipper:**
1. Download the latest `.fap` file from the releases
2. Copy to `/ext/apps/Sub-GHz/` on your Flipper Zero
3. Restart your Flipper Zero

### Step 2: Copy Weather Data File
1. **Download** `TCM220063_WeatherApp.sub` from this repository
2. **Copy to your Flipper Zero**: `/ext/subghz/TCM220063_WeatherApp.sub`

### Step 3: Use the App
1. **Open** the **Weather Station** app on your Flipper
2. **Navigate** to **"Read"** mode  
3. **Press OK** to start scanning for weather signals
4. **Alternatively**, load the `.sub` file to test with sample data

## 🎯 What You'll See

When the app detects TCM220063 signals, it will display:
```
┌─────────────────────┐
│   Nexus-TH          │
│                     │
│  Temperature: 20.5°C│
│  Humidity:    65%   │
│  Channel:     0     │
│  ID:          90    │
│                     │
│  Signal: ████░░     │
└─────────────────────┘
```

## 🔧 Testing Your Setup

### Test with Sample Data:
1. **Load file**: Navigate to **"Saved"** → **"TCM220063_WeatherApp.sub"**
2. **Press Play**: The app should decode and display the weather data
3. **Try different packets**: Use the navigation to test various temperature/humidity combinations

### Test with Real Weather Station:
1. **Set to Read mode**
2. **Hold Flipper near** your actual TCM220063 weather station
3. **Wait up to 60 seconds** (station transmits every minute)
4. **Check the display** for decoded data

## ✅ Supported Weather Data

The app will automatically decode:
- **Temperature**: -40°C to +60°C (0.1°C precision)
- **Humidity**: 0-100% (1% precision)  
- **Channel**: 0-2 (usually 0 for TCM220063)
- **Battery Status**: Shows low battery warnings
- **Signal Strength**: Visual indicator

## 🚨 Troubleshooting

### App Not Detecting Signals:
1. **Check frequency**: Ensure 433.92 MHz is supported
2. **Check distance**: Stay within 5-20 meters of weather station
3. **Wait for transmission**: TCM220063 transmits every 60 seconds
4. **Check antenna position**: Point towards the weather station

### App Not Decoding Data:
1. **Verify protocol**: TCM220063 uses Nexus-TH protocol
2. **Check file format**: Use `TCM220063_WeatherApp.sub` (optimized version)
3. **Update app**: Ensure Weather Station app v1.8 or later

### No Weather Station App in Menu:
1. **Check installation**: App should be in **Apps** → **Sub-GHz** → **Weather Station**
2. **Restart Flipper**: Hold power button, restart
3. **Check SD card**: Ensure `/ext/apps/Sub-GHz/` exists

## 🌟 Pro Tips

### For Best Reception:
- **Position Flipper** with screen facing the weather station
- **Avoid obstacles** between Flipper and weather station  
- **Try different heights** (weather stations often mounted high)

### For Testing:
- **Use multiple packets** from the .sub file to simulate different conditions
- **Record your own** signals using **"Read RAW"** mode first
- **Compare timing** with provided sample data

### Creating Custom Data:
- **Use the Python script**: `decode_tcm220063.py --encode --temp 25.0 --humidity 60 --flipper`
- **Generate new packets** for any temperature/humidity combination
- **Add to .sub file** for extended testing scenarios

## 📱 Alternative Apps

If Weather Station app isn't available, you can also try:
- **Universal RF Remote**: May detect signals but won't decode them
- **Sub-GHz Read RAW**: For capturing your own weather station signals
- **Spectrum Analyzer**: To verify the 433.92 MHz frequency

## 🔗 Useful Links

- **Weather Station App**: https://lab.flipper.net/apps/sub_ghz_weather_station
- **Flipper Lab**: https://lab.flipper.net/ 
- **TCM220063 Manual**: Check Tchibo website for original documentation
- **Awesome Flipper**: https://awesome-flipper.com/ (more apps and resources)

---

**Need help?** Check the main README.md file for detailed technical information and additional troubleshooting options.

**App by**: @Skorpionm  
**Version**: 1.8+  
**Compatible with**: Flipper Zero firmware v0.74.2+
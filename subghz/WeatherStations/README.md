# Weather Station Sub-GHz Scripts for Flipper Zero

This directory contains Sub-GHz scripts for various weather stations that can be used with the Flipper Zero device and compatible weather applications.

## Tchibo Weather Station TCM220063

### Available Files
- **`TCM220063_WeatherApp.sub`** - ⭐ **RECOMMENDED**: Optimized for Weather Station app by @Skorpionm
- **`TCM220063.sub`** - Standard Sub-GHz file for general use
- **`TCM220063.txt`** - Text format with protocol documentation
- **`decode_tcm220063.py`** - Python utility for encoding/decoding data packets
- **`README.md`** - This documentation file

### Overview
The **TCM220063** is a wireless weather station sold by Tchibo that transmits temperature and humidity data via 433.92 MHz radio frequency.

### Device Specifications
- **Model**: TCM220063 (Tchibo/TCM brand)
- **Frequency**: 433.92 MHz
- **Modulation**: OOK (On-Off Keying)
- **Protocol**: Nexus Weather Protocol variant
- **Transmission Interval**: Every 60 seconds
- **Range**: Up to 100 meters (line of sight)
- **Power**: 2x AA batteries

### Data Format
The weather station transmits 36-bit packets containing:
- **Preamble**: 12 bits (alternating pattern for synchronization)
- **Sync Word**: 4 bits (frame synchronization)
- **Data Payload**: 32 bits structured as:
  - Bits 0-3: Channel ID (0-2, typically 0)
  - Bits 4-11: Rolling code/Random ID (changes on battery replacement)
  - Bits 12-23: Temperature (12-bit signed, 0.1°C resolution, +40°C offset)
  - Bits 24-31: Humidity (8-bit, 0-100% range)

### Temperature Calculation
The temperature is encoded as: `Raw Value = (Temperature + 40.0) × 10`

**Examples:**
- Raw value 605 → (60.5 - 40.0) = 20.5°C
- Raw value 450 → (45.0 - 40.0) = 5.0°C
- Raw value 235 → (23.5 - 40.0) = -16.5°C

## How to Use

### Method 1: Weather Station App by @Skorpionm ⭐ **BEST OPTION**
This is the recommended method as it provides automatic decoding and a proper weather display interface.

**Quick Start:**
1. **Install app**: https://lab.flipper.net/apps/sub_ghz_weather_station
2. **Copy file**: `TCM220063_WeatherApp.sub` → `/ext/subghz/`
3. **Open Weather Station app** → **Read** mode
4. **Load and play** the .sub file
5. **View decoded weather data** in real-time

### Method 2: Standard Sub-GHz App
1. **Copy the Script:**
   ```
   Copy TCM220063.sub to your Flipper Zero SD card:
   /ext/subghz/TCM220063.sub
   ```

2. **Load in Flipper Zero:**
   - Navigate to: **Sub-GHz** → **Saved**
   - Select `TCM220063.sub`
   - Choose **Emulate** to transmit the recorded signals

3. **Testing:**
   - Point your Flipper Zero towards compatible weather receivers
   - The transmitted data will appear as sensor readings
   - Try different packets for various temperature/humidity values

### Method 2: Using Weather Station App by @Skorpionm ⭐ RECOMMENDED
The **Weather Station app** by @Skorpionm has native support for Nexus-TH protocol (which TCM220063 uses):

**Installation:**
1. **Install Weather Station App**: https://lab.flipper.net/apps/sub_ghz_weather_station
   - Or via Flipper Lab: Search for "Weather Station" by @Skorpionm
2. **Copy optimized script**: Use `TCM220063_WeatherApp.sub` (optimized for this app)
3. **Place in**: `/ext/subghz/TCM220063_WeatherApp.sub`

**Usage:**
1. **Open Weather Station app** on your Flipper Zero
2. **Go to "Read" mode** 
3. **Load the .sub file** and play it
4. **The app automatically decodes** Nexus-TH signals and displays:
   - Temperature (°C)
   - Humidity (%)
   - Channel ID
   - Signal strength
5. **Real-time display** with proper units and formatting

**Supported Protocols in Weather Station App:**
- ✅ **Nexus-TH** (TCM220063 protocol)
- inFactory-TH, ThermoPRO-TX4, GT-WT02, Acurite series, Oregon series, and many more

**App Version:** v1.8+ (supports external CC1101 radio modules)

### Method 3: Capturing Real Data
To capture your own weather station signals:

1. **Sub-GHz → Read RAW**
2. **Set frequency** to 433.92 MHz
3. **Set modulation** to AM650
4. **Hold near** your TCM220063 weather station
5. **Wait** for transmission (every 60 seconds)
6. **Save** the captured signal

## Script Contents

The `TCM220063.sub` file contains:
- **4 example packets** with different temperature/humidity values
- **Complete protocol documentation**
- **Raw timing data** for accurate signal reproduction
- **Low battery indicator example**

### Example Packets Included:
1. **Packet 1**: 20.5°C, 65% humidity
2. **Packet 2**: 21.0°C, 63% humidity  
3. **Packet 3**: 19.8°C, 68% humidity
4. **Packet 4**: Low battery indicator example

## Compatibility

### Compatible Receivers:
- Original TCM220063 base station
- rtl_433 software with Nexus protocol support
- Other weather station receivers using 433.92 MHz
- Weather monitoring software that supports this protocol

### Flipper Zero Requirements:
- **Firmware**: v0.74.2 or later recommended
- **Sub-GHz module**: Must support 433.92 MHz
- **Storage**: Minimal space required (~2KB per file)

## Technical Notes

### Signal Characteristics:
- **Bit Timing**: ~1ms per bit (1 kHz data rate)
- **Manchester Encoding**: Used for data representation
- **Pulse Width**: 500µs for short pulses, 1500µs for long pulses
- **Frame Gap**: 20ms between packet repetitions

### Protocol Analysis:
The Nexus protocol used by this device is well-documented and supported by various SDR tools like rtl_433. The signal structure follows standard weather station patterns with:
- Clear preamble for receiver synchronization
- Consistent timing for reliable decoding
- Error detection through data validation

## Troubleshooting

### If the script doesn't work:
1. **Check frequency**: Ensure 433.92 MHz is set correctly
2. **Verify modulation**: Should be OOK/ASK
3. **Distance**: Stay within 10-50 meters for testing
4. **Timing**: Some receivers are sensitive to timing variations
5. **Interference**: Avoid areas with heavy 433 MHz traffic

### Capturing Your Own Signals:
If the provided script doesn't match your specific device:
1. Use Sub-GHz **Read RAW** mode
2. Capture multiple transmissions
3. Compare timing patterns
4. Create custom script based on your captures

## Legal Notice

⚠️ **Important**: This script is for educational and testing purposes only.
- Only use on devices you own
- Respect local RF regulations
- Some regions restrict 433 MHz transmissions
- Don't interfere with commercial weather services

## Contributing

If you have improvements or additional weather station scripts:
1. Test thoroughly with actual hardware
2. Document the protocol details
3. Include example data packets
4. Add compatibility information

## References

- [rtl_433 Nexus Protocol Documentation](https://github.com/merbanan/rtl_433)
- [Flipper Zero Sub-GHz Documentation](https://docs.flipperzero.one/sub-ghz)
- [Weather Station Protocol Analysis](https://www.sigidwiki.com/wiki/Weather_Station)

---
**Version**: 1.0  
**Last Updated**: September 2025  
**Compatibility**: Flipper Zero firmware v0.74.2+
#!/usr/bin/env python3
"""
TCM220063 Weather Station Data Decoder

This script helps decode weather data packets from the Tchibo TCM220063
weather station for use with Flipper Zero Sub-GHz scripts :)

Usage:
    python decode_tcm220063.py [hex_data]

Example:
    python decode_tcm220063.py 0x5A25D41
"""

import sys
import argparse

def decode_weather_packet(data):
    """
    Decode a 32-bit weather data packet from TCM220063
    
    Args:
        data: 32-bit integer or hex string
    
    Returns:
        dict: Decoded weather data
    """
    if isinstance(data, str):
        if data.startswith('0x') or data.startswith('0X'):
            data = int(data, 16)
        else:
            data = int(data, 16)
    
    # Extract fields from 32-bit data
    channel = (data >> 28) & 0x0F        # Bits 28-31 (top 4 bits)
    rolling_id = (data >> 20) & 0xFF     # Bits 20-27 (8 bits)
    temp_raw = (data >> 8) & 0xFFF       # Bits 8-19 (12 bits)
    humidity = data & 0xFF               # Bits 0-7 (8 bits)
    
    # Calculate temperature (signed 12-bit with offset)
    if temp_raw & 0x800:  # Check sign bit
        temp_raw = temp_raw - 4096  # Convert from unsigned to signed
    
    temperature = (temp_raw / 10.0) - 40.0
    
    return {
        'channel': channel,
        'rolling_id': rolling_id,
        'temperature': temperature,
        'humidity': humidity,
        'temp_raw': temp_raw
    }

def encode_weather_packet(channel, rolling_id, temperature, humidity):
    """
    Encode weather data into a 32-bit packet for TCM220063
    
    Args:
        channel: Channel ID (0-15)
        rolling_id: Rolling code (0-255)
        temperature: Temperature in Celsius
        humidity: Humidity percentage (0-100)
    
    Returns:
        int: 32-bit encoded packet
    """
    # Convert temperature to raw value
    temp_raw = int((temperature + 40.0) * 10)
    
    # Handle negative temperatures (12-bit signed)
    if temp_raw < 0:
        temp_raw = temp_raw + 4096
    
    # Ensure values are in valid ranges
    channel = max(0, min(15, channel))
    rolling_id = max(0, min(255, rolling_id))
    temp_raw = max(0, min(4095, temp_raw))
    humidity = max(0, min(255, humidity))
    
    # Pack into 32-bit value
    packet = (channel << 28) | (rolling_id << 20) | (temp_raw << 8) | humidity
    
    return packet

def generate_flipper_raw_data(packet, repeat=2):
    """
    Generate RAW_Data line for Flipper Zero .sub file
    
    Args:
        packet: 32-bit data packet
        repeat: Number of times to repeat the packet
    
    Returns:
        str: RAW_Data line for .sub file
    """
    # Convert packet to binary string (32 bits)
    binary = format(packet, '032b')
    
    # Add preamble (12 bits alternating) and sync (4 bits)
    preamble = '101010101010'  # 12 bits alternating
    sync = '1100'              # 4 bits sync word
    full_data = preamble + sync + binary
    
    # Convert to Manchester encoding and timing
    raw_data = []
    
    for bit in full_data:
        if bit == '1':
            # Long pulse followed by short gap
            raw_data.extend(['1500', '-500'])
        else:
            # Short pulse followed by long gap
            raw_data.extend(['500', '-1500'])
    
    # Add frame gap
    raw_data.append('-20000')
    
    # Repeat if requested
    timing_str = ' '.join(raw_data)
    if repeat > 1:
        timing_str = timing_str.replace('-20000', '') + (' ' + timing_str) * (repeat - 1)
    
    return f"RAW_Data: {timing_str}"

def main():
    parser = argparse.ArgumentParser(description='Decode/Encode TCM220063 weather data')
    parser.add_argument('data', nargs='?', help='Hex data to decode (e.g., 0x5A25D41)')
    parser.add_argument('--encode', action='store_true', help='Encode mode')
    parser.add_argument('--channel', type=int, default=0, help='Channel (0-15)')
    parser.add_argument('--id', type=int, default=90, help='Rolling ID (0-255)')
    parser.add_argument('--temp', type=float, default=20.0, help='Temperature in Celsius')
    parser.add_argument('--humidity', type=int, default=65, help='Humidity percentage')
    parser.add_argument('--flipper', action='store_true', help='Generate Flipper Zero RAW_Data')
    
    args = parser.parse_args()
    
    if args.encode:
        # Encode mode
        packet = encode_weather_packet(args.channel, args.id, args.temp, args.humidity)
        print(f"Encoded packet: 0x{packet:08X}")
        
        # Decode it back to verify
        decoded = decode_weather_packet(packet)
        print(f"Channel: {decoded['channel']}")
        print(f"Rolling ID: {decoded['rolling_id']} (0x{decoded['rolling_id']:02X})")
        print(f"Temperature: {decoded['temperature']:.1f}°C")
        print(f"Humidity: {decoded['humidity']}%")
        
        if args.flipper:
            print("\nFlipper Zero RAW_Data:")
            print(generate_flipper_raw_data(packet))
    
    elif args.data:
        # Decode mode
        try:
            decoded = decode_weather_packet(args.data)
            print(f"Decoded weather data from {args.data}:")
            print(f"Channel: {decoded['channel']}")
            print(f"Rolling ID: {decoded['rolling_id']} (0x{decoded['rolling_id']:02X})")
            print(f"Temperature: {decoded['temperature']:.1f}°C")
            print(f"Humidity: {decoded['humidity']}%")
            print(f"Raw temp value: {decoded['temp_raw']}")
            
            if args.flipper:
                packet = int(args.data, 16) if isinstance(args.data, str) else args.data
                print("\nFlipper Zero RAW_Data:")
                print(generate_flipper_raw_data(packet))
                
        except ValueError as e:
            print(f"Error decoding data: {e}")
    
    else:
        # Show examples
        print("TCM220063 Weather Station Data Decoder")
        print("=" * 40)
        print("\nExample usage:")
        print("  Decode: python decode_tcm220063.py 0x5A25D41")
        print("  Encode: python decode_tcm220063.py --encode --temp 21.5 --humidity 70")
        print("  Generate Flipper data: python decode_tcm220063.py --encode --temp 20.0 --flipper")
        print("\nExample data packets:")
        
        examples = [
            (0x005A25D41, "20.5°C, 65% humidity"),
            (0x005A262F, "21.0°C, 63% humidity"), 
            (0x005A2564, "19.8°C, 68% humidity")
        ]
        
        for packet, desc in examples:
            decoded = decode_weather_packet(packet)
            print(f"  0x{packet:08X} -> {desc}")

if __name__ == "__main__":
    main()
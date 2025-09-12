# Monitor IR Scripts for Flipper Zero

This collection contains infrared remote control scripts for various monitor brands to be used with the Flipper Zero device.

## Available Monitor Brands

- **Samsung_Monitor.ir** - Samsung LCD/LED monitors
- **LG_Monitor.ir** - LG LCD/LED monitors  
- **Dell_Monitor.ir** - Dell LCD/LED monitors
- **ASUS_Monitor.ir** - ASUS LCD/LED monitors
- **BenQ_Monitor.ir** - BenQ LCD/LED monitors
- **Acer_Monitor.ir** - Acer LCD/LED monitors
- **HP_Monitor.ir** - HP LCD/LED monitors
- **Universal_Monitor.ir** - Generic codes that work across multiple brands

## How to Use

1. **Copy to Flipper Zero:**
   - Transfer the appropriate `.ir` file to your Flipper Zero's SD card
   - Place it in the `infrared` folder: `/ext/infrared/`

2. **Load the Script:**
   - On your Flipper Zero, go to: **Infrared** → **Saved Remotes**
   - Select the monitor brand file you copied

3. **Test the Commands:**
   - Point your Flipper Zero at the monitor
   - Try the "Power" button first to test compatibility
   - Use other commands like Menu, Source, Brightness controls, etc.

## Common Commands Available

All monitor scripts include these basic functions:

- **Power** - Turn monitor on/off
- **Menu** - Open/close monitor menu
- **Up/Down/Left/Right** - Navigate menu options
- **Enter** - Select/confirm menu option
- **Source** - Switch input source (HDMI, VGA, etc.)
- **Auto** - Auto-adjust display settings
- **Exit** - Exit menu/go back
- **Brightness_Up/Down** - Adjust screen brightness

### Brand-Specific Functions

Some brands include additional specialized commands:

- **Samsung:** Contrast controls
- **LG:** Settings, Home button
- **ASUS:** ECO Mode, Splendid (color modes)
- **BenQ:** ECO mode, Display modes
- **Acer:** ECO Mode, Empowering key
- **HP:** Info display, My Display settings
- **Universal:** Multiple power/menu variants, volume controls

## Troubleshooting

If your monitor doesn't respond:

1. **Try Universal_Monitor.ir first** - Contains common codes that work across brands
2. **Check your monitor model** - Some newer/older models may use different codes
3. **Distance and angle matter** - Point directly at the monitor's IR receiver
4. **Try multiple power variants** - The Universal script has several power button codes

## Technical Details

- **Protocol:** Most scripts use NEC protocol (38kHz)
- **Format:** Standard Flipper Zero IR file format
- **Compatibility:** Works with Flipper Zero firmware v0.74.2 and later

## Notes

- These IR codes are based on common remote control patterns for each brand
- Not all commands may work with every monitor model within a brand
- Some monitors may require specific model codes - you can capture your original remote using Flipper Zero's "Learn New Remote" feature
- Modern monitors with only touch controls or no IR receiver will not work with these scripts

## Contributing

If you have IR codes for monitor models not covered here, or improvements to existing codes, please contribute them to the repository.

## Disclaimer

These scripts are provided as-is for educational and legitimate use only. Always ensure you have permission to control the devices you're targeting.
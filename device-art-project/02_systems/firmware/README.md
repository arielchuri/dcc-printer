# DCC Printer Firmware Installation & Deployment Guide

This directory contains the production-grade CircuitPython 9.x firmware for the **DCC Printer** Device Art project.

---

## 1. Quick Installation on Raspberry Pi Pico

1. **Mount Pico**: Connect the Raspberry Pi Pico to your computer via USB while holding the `BOOTSEL` button. It will mount as a drive named `RPI-RP2`.
2. **Install CircuitPython 9.x**: Copy the latest CircuitPython `.uf2` file for Raspberry Pi Pico to `RPI-RP2`. The board will reboot and mount as `CIRCUITPY`.
3. **Copy Firmware**: Copy [code.py](code.py) to the root of `CIRCUITPY`:
   ```bash
   cp code.py /Volumes/CIRCUITPY/code.py
   ```
4. **Copy Libraries**: In the `CIRCUITPY/lib/` folder, ensure the following Adafruit CircuitPython bundle libraries are installed:
   - `adafruit_character_lcd/`
   - `adafruit_ds3231.mpy`
   - `adafruit_bus_device/`

---

## 2. Parent Architecture Reference

- Full system operational state machine and display screens: [../../../../firmware.md](../../../firmware.md)
- Complete DCC generator tables and 32-column receipt formatting: [../../../../dcc-tables.md](../../../dcc-tables.md)
- Circuit schematic and star grounding details: [../circuit_schematic.md](../circuit_schematic.md)

# 3D CAD Models & Mechanical Asset Crosswalk

**Course:** PSAM 2230 Device Art (Fall 2026)  
**Deliverable:** Milestone 3 CAD Assets & Component Modeling  
**Non-Duplication Policy:** All 3D STEP CAD models are referenced via local placeholder files in `assets/models/` and direct relative links to the primary repository models in `../../models/`.

---

## 1. 3D STEP & STL Component Model Inventory

All models are provided in both **STEP AP214** (parametric solid CAD) and **STL** (mesh format optimized for Tinkercad drag-and-drop import under the 25 MB / 300k polygon limits):

| Component | Format | STEP File Link | STL File Link (Tinkercad) | Spec Notes |
| :--- | :---: | :--- | :--- | :--- |
| **Cashino CSN-A2 Thermal Printer** | AP214 / STL | [cashino_csn_a2_printer.step](../../models/cashino_csn_a2_printer.step) (37 KB) | [cashino_csn_a2_printer.stl](../../models/cashino_csn_a2_printer.stl) (55 KB) | [Info](../assets/models/cashino_csn_a2_printer.md) |
| **Raspberry Pi Pico** | AP214 / STL | [pico_rp2040.step](../../models/pico_rp2040.step) (1.6 MB) | [pico_rp2040.stl](../../models/pico_rp2040.stl) (2.2 MB) | [Info](../assets/models/pico_rp2040.md) |
| **8-Way Rotary Switch (Adafruit #2925)** | AP214 / STL | [adafruit_2925_rotary_switch.step](../../models/adafruit_2925_rotary_switch.step) (352 KB) | [adafruit_2925_rotary_switch.stl](../../models/adafruit_2925_rotary_switch.stl) (772 KB) | [Info](../assets/models/adafruit_2925_rotary_switch.md) |
| **Anodized Knob (Adafruit #5527)** | AP214 / STL | [adafruit_5527_knob.step](../../models/adafruit_5527_knob.step) (64 KB) | [adafruit_5527_knob.stl](../../models/adafruit_5527_knob.stl) (92 KB) | [Info](../assets/models/adafruit_5527_knob.md) |
| **Triangle Button (Adafruit #4186–#4190)** | AP214 / STL | [adafruit_4190_triangle_button.step](../../models/adafruit_4190_triangle_button.step) (56 KB) | [adafruit_4190_triangle_button.stl](../../models/adafruit_4190_triangle_button.stl) (80 KB) | [Info](../assets/models/adafruit_4190_triangle_button.md) |
| **2.1mm DC Jack (Adafruit #610)** | AP214 / STL | [adafruit_610_dc_jack.step](../../models/adafruit_610_dc_jack.step) (87 KB) | [adafruit_610_dc_jack.stl](../../models/adafruit_610_dc_jack.stl) (409 KB) | [Info](../assets/models/adafruit_610_dc_jack.md) |
| **Toggle Switch (Adafruit #3221)** | AP214 / STL | [adafruit_3221_toggle_switch.step](../../models/adafruit_3221_toggle_switch.step) (662 KB) | [adafruit_3221_toggle_switch.stl](../../models/adafruit_3221_toggle_switch.stl) (1.7 MB) | [Info](../assets/models/adafruit_3221_toggle_switch.md) |
| **LCD 1602 Display Screen** | AP214 / STL | [lcd1602.step](../../models/lcd1602.step) (855 KB) | [lcd1602.stl](../../models/lcd1602.stl) (2.1 MB) | [Info](../assets/models/lcd1602.md) |
| **PCF8574 I2C Backpack** | AP214 / STL | [lcd1602_i2c_backpack.step](../../models/lcd1602_i2c_backpack.step) (6.3 MB) | [lcd1602_i2c_backpack.stl](../../models/lcd1602_i2c_backpack.stl) (6.5 MB) | [Info](../assets/models/lcd1602_i2c_backpack.md) |
| **DS3231 Precision RTC** | AP214 / STL | [ds3231_rtc.step](../../models/ds3231_rtc.step) (8.1 MB) | [ds3231_rtc.stl](../../models/ds3231_rtc.stl) (6.8 MB) | [Info](../assets/models/ds3231_rtc.md) |

---

## 2. Mechanical Stackup & Header Clearance Geometry

The 3D CAD modeling verified the critical internal clearance constraints between the top control panel and the internal thermal paper roll cavity:

### LCD 1602 + PCF8574 Backpack Clearance
- **Bezel Projection:** The metal bezel projects $6.8\text{ mm}$ upward from the front of the display PCB.
- **Glass / Window Aperture:** $64.5\text{ mm} \times 16.0\text{ mm}$ viewing window fits flush inside the top panel cutout.
- **Header Selection Optimization:**
  - As detailed in the [lcd1602-i2c-module.pdf](../../lcd1602-i2c-module.pdf) engineering drawing, straight pin headers require at least **$30.0\text{ mm}$** of internal enclosure clearance to avoid pinching the female DuPont wiring harness.
  - By modeling and utilizing **Right-Angle (Bent 90°)** headers parallel to the PCB surface, the total internal component depth drops to only **$14.5\text{ mm}$**.
  - This 15.5 mm reduction in required clearance allows the top console to be positioned directly above the thermal printer's paper bay without mechanical collisions.

### DS3231 Real-Time Clock Placement
- **Chassis Mounting:** Mounted vertically along the left interior sidewall using M2.5 nylon hex standoffs ($8.0\text{ mm}$ height).
- **Coin Cell Battery Clearance:** The coin cell holder requires a vertical clearance envelope of $14.0\text{ mm}$ from the PCB face for battery insertion and removal.

---

## 3. Related Design Documents

- **2D Laser Cut Production Sheet:** [enclosure_laser_cut.svg](enclosure_laser_cut.svg)
- **Comprehensive Mechanical Specifications:** [milestone_03_enclosure.md](milestone_03_enclosure.md)
- **Original CAD Directory:** [../../models/](../../models/)

# DS3231 + AT24C32 RTC Module Technical Datasheet

The technical datasheet and battery modification guide for the DS3231 precision real-time clock breakout module is located in the root repository.

- **Direct GitHub PDF Link:** [ds3231-rtc-module.pdf](../../../ds3231-rtc-module.pdf)
- **HTML Vector Source:** [ds3231-datasheet.html](../../../ds3231-datasheet.html)
- **Key Specifications:**
  - PCB Dimensions: $38.0 \times 22.0\text{ mm}$ (Height $14.0\text{ mm}$ with CR2032 holder)
  - Accuracy: $\pm 2\text{ ppm}$ from 0°C to +40°C ($\approx \pm 1\text{ minute/year}$)
  - Interface: I2C (`0x68` for DS3231, `0x57` for AT24C32 EEPROM)
  - Modification: Cut diode D1 for safe disposable CR2032 coin cell operation

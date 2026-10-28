# Bill of Materials (BOM) & Component Audit

**Course:** PSAM 2230 Device Art (Fall 2026)  
**Project:** DCC Printer Capstone  
**Status:** All Primary Electronics In-Hand & Verified  
**Parent Specifications:** [dcc-printer.md](../../dcc-printer.md)

---

## 1. Electronics & Transducers BOM

| Item | Component | Specification | Qty | Source / Vendor | Part / CAD Link | Status | Unit Cost |
| :---: | :--- | :--- | :---: | :--- | :--- | :---: | :---: |
| **01** | **Microcontroller** | Raspberry Pi Pico (RP2040, 2MB Flash, Dual-Core M0+) | 1 | Raspberry Pi / Adafruit | [Adafruit #4864](https://www.adafruit.com/product/4864)<br>[CAD Model](../../models/pico_rp2040.step) | In Hand | $4.00 |
| **02** | **Thermal Printer** | Cashino CSN-A2 Panel Mount (58mm roll, TTL UART 9600, 5V–9V ≥2A) | 1 | Cashino / Amazon | [Datasheet PDF](../../cashino-printer.pdf) | In Hand | $38.50 |
| **03** | **Character Display** | LCD1602 (16x2 Chars) with PCF8574 $I^2C$ Backpack (Bent 90° Header) | 1 | AliExpress / Amazon | [Vector Datasheet](../../lcd1602-i2c-module.pdf)<br>[CAD Model](../../models/lcd1602.step) | In Hand | $3.20 |
| **04** | **Real-Time Clock** | DS3231 Precision RTC Module (Battery-backed with CR2032) | 1 | AliExpress / Amazon | [Vector Datasheet](../../ds3231-rtc-module.pdf)<br>[CAD Model](../../models/ds3231_rtc.step) | In Hand | $2.80 |
| **05** | **Rotary Selector** | Adafruit #2925 8-Way Rotary Selector Switch (SP8T, 9mm Bushing) | 1 | Adafruit #2925 | [Product Link](https://www.adafruit.com/product/2925)<br>[CAD Model](../../models/adafruit_2925_rotary_switch.step) | In Hand | $2.50 |
| **06** | **Control Knob** | Adafruit #5527 Anodized Knurled Aluminum Knob ($\varnothing 20 \times 15.5\text{ mm}$, M4 screw) | 1 | Adafruit #5527 | [Product Link](https://www.adafruit.com/product/5527)<br>[CAD Model](../../models/adafruit_5527_knob.step) | In Hand | $2.25 |
| **07** | **Trigger Button** | Adafruit #4186–#4190 Illuminated Triangle Arcade Pushbutton (M24, 5V LED) | 1 | Adafruit #4190 | [Product Link](https://www.adafruit.com/product/4190)<br>[CAD Model](../../models/adafruit_4190_triangle_button.step) | In Hand | $3.95 |
| **08** | **Power Input** | Adafruit #610 2.1mm DC Barrel Jack (5.5mm OD, Panel Mount) | 1 | Adafruit #610 | [Product Link](https://www.adafruit.com/product/610)<br>[CAD Model](../../models/adafruit_610_dc_jack.step) | In Hand | $1.25 |
| **09** | **Main Power Switch** | Adafruit #3221 Heavy Duty SPST Bat Toggle Switch (12mm Bushing) | 1 | Adafruit #3221 | [Product Link](https://www.adafruit.com/product/3221)<br>[CAD Model](../../models/adafruit_3221_toggle_switch.step) | In Hand | $2.50 |
| **10** | **Buffer Capacitor** | $1000\mu\text{F}$ 16V Low-ESR Radial Electrolytic Capacitor | 1 | Course Kit / DigiKey | Placed across printer 5V rail | In Hand | $0.45 |

---

## 2. Enclosure Materials & Fasteners

| Item | Component / Material | Specification / Finish | Qty | Vendor / Source | Application | Status | Est. Cost |
| :---: | :--- | :--- | :---: | :--- | :--- | :---: | :---: |
| **11** | **Enclosure Panels** | 3.0mm (1/8") Matte Black Cast Acrylic Sheet ($12" \times 12"$) | 2 | Canal Plastics Center | Laser-cut top, front, sides, rear, bottom panels | Need to Cut | $16.00 |
| **12** | **Accent Trim** | 3.0mm (1/8") Smoked Bronze Cast Acrylic | 1 | Canal Plastics Center | Screen bezel frame and accent spacers | In Studio | $8.00 |
| **13** | **Machine Fasteners** | M3 $\times$ 12mm Stainless Socket-Head Cap Screws (Black Oxide) | 16 | McMaster-Carr | T-slot panel joinery & component mounting | In Hand | $4.50 |
| **14** | **Captive Hardware** | M3 Square & Hex Zinc-Plated Steel Nuts | 16 | McMaster-Carr | Captured inside T-slots for rigid assembly | In Hand | $2.20 |
| **15** | **PCB Standoffs** | M2.5 $\times$ 8mm Nylon Hex Standoffs + Screws | 8 | McMaster-Carr | Mounting Pico and RTC securely | In Hand | $3.50 |
| **16** | **Wiring Loom** | 22 AWG Silicone Flexible Hookup Wire (Red, Black, Yellow, Green) | 1 | Course Kit / Adafruit | Interconnects & star-ground harness | In Hand | $4.00 |
| **17** | **Thermal Paper** | 58mm $\times$ 30mm BPA-Free Direct Thermal Paper Rolls | 5 | Cashino / Office Supply | Consumable print stock | In Hand | $6.50 |

---

## 3. Financial Summary

- **Total Electronic Transducers:** $59.15
- **Total Enclosure & Hardware:** $44.70
- **Total Project Cost:** **$103.85**

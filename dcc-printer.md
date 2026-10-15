# DCC Printer (Dungeon Crawl Classics Thermal Receipt Generator)

An electromechanical gaming artifact and tabletop prop that prints procedurally generated *Dungeon Crawl Classics* (DCC) RPG tables, 0-level characters, and creatures onto 58mm thermal paper.

---

## 1. Bill of Materials & Component Specifications

| Component | Description | Reference | Specifications |
| :--- | :--- | :--- | :--- |
| **Thermal Printer** | Cashino CSN-A2 Panel | [cashino.pdf](cashino-printer.pdf) | 58mm roll (48mm print width) |
| | Panel Mount Printer | | TTL UART 9600, 5V–9V (≥2A) |
| **Rotary Switch** | SR16A-18-15KQ | [rotary.pdf](rotary-switch-SR16A-18-15KQ.pdf) | 1-pole 8-position selector |
| | 8-Position Switch | | 15mm round knurled shaft |
| **Knob** | Pointer Control Knob | [knob.pdf](knob.pdf) | Knurled shaft pointer |
| | Metal / Plastic | | Position indicator line |
| **Trigger Button** | Illuminated Triangle | [button.jpg](triangle-button.jpg) | Momentary microswitch |
| | Arcade Pushbutton | | Integrated PWM glow LED |
| **Microcontroller** | Raspberry Pi Pico | Standard 40-pin DIP | Dual-core Cortex-M0+ |
| | RP2040 Board | | CircuitPython runtime |
| **OLED Display** | SSD1306 Monochrome | I2C (Address `0x3C`) | 128x32 or 128x64 display |
| | 0.91" / 0.96" Screen | | Mode & status screen |
| **Real-Time Clock** | DS3231 Precision RTC | I2C (Address `0x68`) | Battery-backed clock |
| | Module with CR2032 | | Receipt real-time stamp |
| **Power Socket** | 5.5 x 2.1mm DC Jack | Panel Mount | 5V DC input rated |
| | Barrel Connector | | 3.0A minimum capacity |
| **Power Switch** | Latching SPST Switch | In-line 5V DC line | Main system power cut-off |
| | Rocker / Toggle | | Rated for ≥3A DC |

---

## 2. Documentation Modules

The project specifications and engineering guides are divided into modular documents:

1. **[Wiring & Power Architecture](wiring.md)**:
   - Full system schematic and interconnect diagram.
   - GPIO pinout table for the Raspberry Pi Pico.
   - Dual-rail power distribution (5V high-current & 3.3V logic).
   - In-depth guide: **Understanding Low-Impedance Star Grounding** (physics of ground bounce, noise immunity, decoupling).

2. **[DCC Generator Tables & Receipt Layouts](dcc-tables.md)**:
   - Specifications for the 8 rotary switch positions:
     1. DCC RPG (0-Level Funnel)
     2. MCC RPG (0-Level Seeker Funnel)
     3. Umerica (0-Level Survivor Funnel)
     4. X-Crawl Classics (0-Level Athlete Funnel)
     5. DCC Lankhmar (0-Level Citizen Funnel)
     6. DCC Empire of the East (0-Level Villager Funnel)
     7. DCC Dying Earth (Jack Vance 0-Level Wayfarer Funnel)
     8. Beast-o-Matic (Procedural Random Monster)
   - 58mm thermal print area constraints (32-character column limit).
   - Reusable 32-column ASCII art headers (Horned Demon Skull, Monster Head, Radioactive Skull).
   - Sample formatted receipt mockups.

3. **[Firmware & Operational Flow](firmware.md)**:
   - System state machine (Mermaid diagram).
   - SSD1306 OLED interface screens (Idle, Printing, Error).
   - CircuitPython software architecture, debouncing, and ESC/POS UART driver loop.

---

## 3. Hardware Assembly Checklist

- [ ] Solder 40-pin header pins to the Raspberry Pi Pico.
- [ ] Connect I2C bus (`GP0` SDA, `GP1` SCL) with shared 3.3V power to SSD1306 and DS3231.
- [ ] Connect UART1 TX (`GP4`) to Cashino RX and UART1 RX (`GP5`) to Cashino TX.
- [ ] Wire rotary switch positions 1–8 to pins `GP6` through `GP13` with rotary common to logic GND.
- [ ] Wire triangle button microswitch to `GP14` and button LED anode to `GP15` (PWM).
- [ ] Install 470µF–1000µF capacitor across the Cashino power connector.
- [ ] Establish **low-impedance star ground** from DC power jack negative terminal.

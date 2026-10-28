# Circuit Schematic & Power Architecture

**Course:** PSAM 2230 Device Art (Fall 2026)  
**Deliverable:** Milestone 2 Electrical Schematic & Interconnect Documentation  
**Primary Specification Reference:** [wiring.md](../../wiring.md)

---

## 1. Raspberry Pi Pico GPIO Pinout Allocation

| Pico Physical Pin | GPIO Identifier | Peripheral Subsystem | Connected Signal / Component | Electrical Spec |
| :---: | :---: | :---: | :--- | :--- |
| **Pin 1** | `GP0` | `I2C0 SDA` | LCD1602 SDA & DS3231 SDA | 3.3V Logic, $4.7\text{k}\Omega$ onboard pull-up |
| **Pin 2** | `GP1` | `I2C0 SCL` | LCD1602 SCL & DS3231 SCL | 3.3V Logic, $4.7\text{k}\Omega$ onboard pull-up |
| **Pin 6** | `GP4` | `UART1 TX` | Cashino CSN-A2 RX (Data In) | 3.3V TTL Serial, 9600 Baud |
| **Pin 7** | `GP5` | `UART1 RX` | Cashino CSN-A2 TX (Status Return) | 3.3V TTL Serial, 9600 Baud |
| **Pin 9** | `GP6` | Digital In | Alpha Rotary Switch Position 1 (DCC) | Internal Pull-Up, Active LOW |
| **Pin 10** | `GP7` | Digital In | Alpha Rotary Switch Position 2 (MCC) | Internal Pull-Up, Active LOW |
| **Pin 11** | `GP8` | Digital In | Alpha Rotary Switch Position 3 (Umerica) | Internal Pull-Up, Active LOW |
| **Pin 12** | `GP9` | Digital In | Alpha Rotary Switch Position 4 (X-Crawl) | Internal Pull-Up, Active LOW |
| **Pin 14** | `GP10` | Digital In | Alpha Rotary Switch Position 5 (Lankhmar) | Internal Pull-Up, Active LOW |
| **Pin 15** | `GP11` | Digital In | Alpha Rotary Switch Position 6 (Empire East) | Internal Pull-Up, Active LOW |
| **Pin 16** | `GP12` | Digital In | Alpha Rotary Switch Position 7 (Dying Earth) | Internal Pull-Up, Active LOW |
| **Pin 17** | `GP13` | Digital In | Alpha Rotary Switch Position 8 (Beast-o-Matic)| Internal Pull-Up, Active LOW |
| **Pin 19** | `GP14` | Digital In | Triangle Button Microswitch NO Contact | Internal Pull-Up, Active LOW |
| **Pin 20** | `GP15` | `PWM Out` | Triangle Button LED Anode (+) | 1000 Hz PWM Sinusoidal Glow |
| **Pin 36** | `3V3_OUT` | Regulated Out | Power for LCD1602 logic & DS3231 RTC | Max 300 mA available |
| **Pin 38** | `GND` | Digital Ground | Logic Ground Return to Star Ground Hub | Heavy trace connection |
| **Pin 39** | `VSYS` | Main Power In | 5.0V Regulated DC from Power Switch | Feeds onboard buck-boost SMPS |

---

## 2. Low-Impedance Star Grounding & Noise Decoupling Architecture

> [!IMPORTANT]
> The thermal print head and stepper motor in the Cashino CSN-A2 printer draw intermittent pulse currents reaching **1.8A to 2.2A** during solid black ASCII banner printing. Without proper grounding separation, common-impedance ground coupling causes ground bounce voltage spikes exceeding 0.8V, resetting the Pico microcontroller.

### Central Star Topology
To isolate the digital logic plane from heavy motor and thermal discharge currents:
1. **Physical Star Hub**: The negative terminal of the 5.5 x 2.1mm DC power jack acts as the single, authoritative **Star Ground Point**.
2. **Dedicated Heavy-Gauge Return**: A 20 AWG stranded copper wire runs directly from the star point to the Cashino printer's ground terminal.
3. **Decoupling Reservoir**: A $1000\mu\text{F}$ 16V low-ESR electrolytic capacitor is soldered directly across the printer's power input lugs to buffer instantaneous current transients.
4. **Isolated Logic Ground**: A separate ground lead runs from the star point to Pico `Pin 38 (GND)`. All switches, buttons, and I2C sensors return exclusively through the Pico's clean ground plane.

---

## 3. Circuit Schematic Diagram Link

- For the full ASCII wiring map and comprehensive grounding physics analysis, see the parent document:  
  **[wiring.md](../../wiring.md)**
- For the ZS-042 DS3231 circuit schematic diagram, see:  
  **[ds3231_schematic.jpg](../../ds3231_schematic.jpg)**
- For the PCF8574 I2C Backpack schematic and pin connections, see:  
  **[lcd1602-i2c-module.pdf](../../lcd1602-i2c-module.pdf)**

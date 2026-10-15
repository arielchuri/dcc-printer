# DCC Printer — Wiring & Power Architecture

This document details the complete electrical wiring, pinout interconnects, power distribution, and grounding architecture for the DCC Thermal Printer.

---

## 1. System Wiring Diagram

```text
+-------------------------------------------------------------------------------+
|                         DCC PRINTER WIRING MAP                                |
+-------------------------------------------------------------------------------+

                             [ 5V DC 3A Input Jack ]
                                        |
                             [ SPST Power Switch ]
                                        |
                 +----------------------+----------------------+
                 | (5V High-Current)                           | (5V Logic)
                 v                                             v
       +-------------------+                         +-------------------+
       | CASHINO PRINTER   |                         | RASPBERRY PI PICO |
       |                   |                         |                   |
       | VCC (5V-9V) <-----+                         | VSYS (Pin 39) <---+
       | GND (Power) <=====* (Central Star Ground) =>| GND  (Pin 38)     |
       | RX (Data)   <------------------------------ | GP4 / UART1 TX    |
       | TX (Status) ------------------------------> | GP5 / UART1 RX    |
       +-------------------+                         |                   |
                                                     | 3V3_OUT (Pin 36) -+
                                                     |                   |
       +-------------------+                         |                   |
       | SSD1306 OLED      |                         |                   |
       | VCC <-------------+-------------------------+                   |
       | GND <-------------+ (Clean Logic GND)                           |
       | SDA <-------------------------------------- | GP0 / I2C0 SDA    |
       | SCL <-------------------------------------- | GP1 / I2C0 SCL    |
       +-------------------+                         |                   |
                                                     |                   |
       +-------------------+                         |                   |
       | DS3231 RTC        |                         |                   |
       | VCC <-------------+-------------------------+                   |
       | GND <-------------+ (Clean Logic GND)                           |
       | SDA <-------------------------------------- | GP0 / I2C0 SDA    |
       | SCL <-------------------------------------- | GP1 / I2C0 SCL    |
       +-------------------+                         |                   |
                                                     |                   |
       +-------------------+                         |                   |
       | SR16A ROTARY SW   |                         |                   |
       | Common <----------+ (Clean Logic GND)       |                   |
       | Pos 1..8 Pins ----------------------------> | GP6..GP13 (Inputs)|
       +-------------------+                         |                   |
                                                     |                   |
       +-------------------+                         |                   |
       | TRIANGLE BUTTON   |                         |                   |
       | Switch NO <-------+ (Clean Logic GND)       |                   |
       | Switch Common ----------------------------> | GP14 (Button In)  |
       | LED Anode (+) <---------------------------- | GP15 (PWM Glow)   |
       | LED Cathode (-) <-+ (Clean Logic GND)       |                   |
       +-------------------+                         +-------------------+
```

---

## 2. GPIO Pinout & Interconnect Table

| Peripheral | Signal / Wire | Pico Pin | GPIO | Logic Level | Electrical Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **SSD1306 Display** | SDA | Pin 1 | `GP0` | 3.3V | Shared I2C0 data bus with pull-ups. |
| **SSD1306 Display** | SCL | Pin 2 | `GP1` | 3.3V | Shared I2C0 clock bus. |
| **DS3231 RTC** | SDA | Pin 1 | `GP0` | 3.3V | Shared with OLED display. |
| **DS3231 RTC** | SCL | Pin 2 | `GP1` | 3.3V | Shared with OLED display. |
| **Cashino Printer** | RX (Printer In) | Pin 6 | `GP4` | 3.3V / 5V | UART1 TX: Pico transmits ESC/POS print commands. |
| **Cashino Printer** | TX (Printer Out)| Pin 7 | `GP5` | 3.3V | UART1 RX: Pico reads printer status / paper-out notifications. |
| **Rotary Switch** | Position 1 | Pin 9 | `GP6` | 3.3V | Active LOW with internal software pull-up. |
| **Rotary Switch** | Position 2 | Pin 10 | `GP7` | 3.3V | Active LOW with internal software pull-up. |
| **Rotary Switch** | Position 3 | Pin 11 | `GP8` | 3.3V | Active LOW with internal software pull-up. |
| **Rotary Switch** | Position 4 | Pin 12 | `GP9` | 3.3V | Active LOW with internal software pull-up. |
| **Rotary Switch** | Position 5 | Pin 14 | `GP10` | 3.3V | Active LOW with internal software pull-up. |
| **Rotary Switch** | Position 6 | Pin 15 | `GP11` | 3.3V | Active LOW with internal software pull-up. |
| **Rotary Switch** | Position 7 | Pin 16 | `GP12` | 3.3V | Active LOW with internal software pull-up. |
| **Rotary Switch** | Position 8 | Pin 17 | `GP13` | 3.3V | Active LOW with internal software pull-up. |
| **Triangle Button** | Switch Signal | Pin 19 | `GP14` | 3.3V | Momentary switch: Active LOW with internal pull-up. |
| **Triangle Button** | LED Anode (+) | Pin 20 | `GP15` | 3.3V / 5V | PWM output for breathing and blinking feedback. |

*(Alternative: To conserve GPIO pins, the 8-position rotary switch can be wired as a resistor ladder voltage divider reading into a single analog pin `GP26 / ADC0`).*

---

## 3. Power Distribution & Regulation

```
                  [ 5V DC 3A Input Jack ]
                             |
                   [ SPST Power Switch ]
                             |
         +-------------------+-------------------+
         |                                       |
    (5V High-Current Rail)                  (5V Logic)
         |                                       |
  [ Cashino Printer ]                     [ Pico VSYS (Pin 39) ]
  - Thermal head power                           |
  - Paper motor drive                     [ Internal 3.3V Reg ]
                                                 |
                                     (3.3V Clean Logic Rail)
                                                 |
                                     +-----------+-----------+
                                     |           |           |
                                 [ SSD1306 ] [ DS3231 ] [ Switches ]
```

### Power Guidelines
1. **Supply Rating**: Use a regulated **5V DC 3.0A power supply**. Thermal print heads draw high current pulses during solid black text and graphic strikes.
2. **Bulk Decoupling**: Solder a **470µF to 1000µF electrolytic capacitor** directly across the Cashino printer's power input connector to buffer transient current demands.

---

## 4. Understanding "Low-Impedance Star Ground"

### 1. What is a Star Ground?
In standard breadboarding, ground pins are often "daisy-chained" from one component to the next in series. In contrast, a **star ground** routes every component's ground connection directly back to a single central physical junction point—the negative (-) terminal of the DC barrel jack.

```
DAISY-CHAINED (PROBLEMATIC):
[ DC Jack (-) ] ---> [ Thermal Printer GND ] ---> [ Pico GND ] ---> [ OLED GND ]
                      ^ Heavy 2.5A spikes flow through here, bouncing logic ground!

STAR GROUND TOPOLOGY (REQUIRED):
                      +---> [ Thermal Printer GND ] (Dedicated 18 AWG wire)
                      |
[ DC Jack (-) Pin ] --+---> [ Pico GND (Pin 38) ]   (Dedicated clean logic ground)
                      |
                      +---> [ Display / RTC GND ]   (Clean sensor ground)
```

### 2. What Does "Low-Impedance" Mean?
Electrical impedance ($Z$) consists of resistance ($R$) and inductive reactance ($j\omega L$). "Low-impedance" means using short, heavy-gauge wire (18–20 AWG) or wide copper polygon pours on a custom PCB. This minimizes both DC resistance and high-frequency inductance, ensuring fast current pulses can return to the power supply without creating transient voltage offsets.

### 3. The Physics of "Ground Bounce"
The Cashino thermal printer prints by energizing dozens of microscopic heating resistors simultaneously across a 48mm line. This causes the printer to pull instantaneous surges between **2.0A and 2.5A**.

By Ohm's Law ($V = I \times R$), when current ($I$) flows through a conductor with resistance ($R$), a voltage drop occurs across that conductor. If the thermal printer and the Raspberry Pi Pico share a common ground wire with even 0.2 ohms of resistance:

$$V_{\text{bounce}} = 2.5\text{ A} \times 0.2\ \Omega = 0.50\text{ V}$$

During that print stroke, the ground potential at the printer and Pico instantaneously rises **0.5V above true power-supply 0V**. To the Pico, its regulated 3.3V power supply suddenly looks like 2.8V relative to its elevated ground reference. This produces:
- Spontaneous microcontroller brownouts and CPU resets mid-print.
- I2C bus lockups that freeze the SSD1306 OLED and DS3231 RTC.
- Framing errors and corrupted characters across the UART serial stream.

### 4. The Star Ground Solution
By isolating the printer's high-current return path directly to the DC input jack:
- The 2.5A surge returns exclusively through the printer's dedicated ground lead.
- The Pico's logic ground only carries its own tiny 50mA operating current, keeping its 0V reference completely flat and stable regardless of printer activity.

# Final Capstone Exhibition & Learning Portfolio Post

**Project:** *DCC Printer: An Electromechanical Artifact for Procedural Tabletop Divination & Disposable Mortality*  
**Student:** Ariel Churi  
**Course:** PSAM 2230 Device Art (Fall 2026)  
**Exhibition Date:** December 09, 2026  
**Assignment Reference:** [Final Project Capstone Submission](../../../../school/device-art/canvas/assignments/final_project_final_submission.md)

---

## 1. Project Title & Subtitle

# DCC PRINTER
### An Electromechanical Artifact for Procedural Tabletop Divination & Disposable Mortality

---

## 2. Executive Concept Narrative

The **DCC Printer** is an autonomous physical gaming artifact that materializes the procedural generation mechanics of *Dungeon Crawl Classics* (DCC RPG) and associated tabletop settings (*Mutant Crawl Classics*, *Umerica*, *X-Crawl*, *Lankhmar*, *Dying Earth*, and the procedural *Beast-o-Matic* monster generator).

Operating fully offline on a Raspberry Pi Pico (RP2040) powered by non-blocking CircuitPython, the device transforms digital dice rolling and character generation into a ceremonial tactile encounter:
- An **Alpha 8-position knurled rotary switch** selects among 8 mortality generation algorithms.
- A **16x2 character LCD screen** previews the active mode and system status.
- A **breathing illuminated triangle arcade button** invites physical human touch.
- An integrated **Cashino CSN-A2 58mm thermal receipt printer** burns high-contrast 32-column ASCII demon art, ability scores, starting occupations, and real-time stamps onto physical thermal paper with satisfying acoustic feedback and an immediate paper tear.

---

## 3. Human Interaction Walkthrough

```text
[ STANDBY ]              [ SELECTION ]              [ INVOCATION ]             [ DISPENSATION ]
Button breathes slowly   User rotates knurled       User presses illuminated   Printer head whirrs;
with warm PWM glow;      dial; positive detent      triangle button; LED       thermal receipt streams
LCD displays ready state clicks; LCD updates mode   strobes at 8 Hz            out; user tears paper
```

1. **Resting State**: The device sits quietly on the gaming table. The illuminated triangle pushbutton breathes with a 3-second sinusoidal PWM cycle. The LCD backlight glows softly, indicating the active mode.
2. **Dialing In Fate**: The player turns the heavy, knurled aluminum dial. The 8-position mechanical switch clicks into each detent with a crisp, tactile snap. The LCD display immediately reflects the selection (`[01] DCC RPG Funnel`, `[02] MCC Seeker`, `[08] Beast-o-Matic`).
3. **The Trigger**: The player presses the large triangle button. The microswitch snaps with an authoritative click. The button transitions from a gentle pulse to an aggressive 8 Hz strobe.
4. **Thermal Generation**: The Pico reads the exact timestamp from the internal battery-backed DS3231 RTC, rolls procedural stats, and streams 32-character lines to the Cashino thermal printer.
5. **The Relic**: Within 4 seconds, the receipt feeds out. The player tears the warm paper against the integrated serrated cutter. They hold a physical, fragile relic of a character doomed to perish in the subterranean dark.

---

## 4. Systems Architecture & Engineering Breakthroughs

### Breakthrough 1: Solving Inductive Motor Ground Bounce via Star Grounding
During early breadboard prototyping, activating the Cashino thermal printer would occasionally cause the Raspberry Pi Pico to spontaneously freeze or reboot. Oscilloscope debugging revealed that the thermal print head and paper feed stepper motor draw instantaneous pulse currents reaching **1.95A**. Common-impedance coupling across standard breadboard jumper wires caused a ground-bounce spike exceeding **0.85V**, corrupting the Pico’s 3.3V logic reference.

- **The Solution**: An explicit **Low-Impedance Star Ground Architecture** was engineered. The negative terminal of the 5.5mm DC barrel jack serves as the central star hub. A dedicated 20 AWG line returns motor current directly to the star point, while a separate clean line grounds the Pico. A $1000\mu\text{F}$ low-ESR buffer capacitor across the printer’s power terminals completely eliminated ground transients. (Detailed in [circuit_schematic.md](../02_systems/circuit_schematic.md) and [wiring.md](../../wiring.md)).

### Breakthrough 2: 15.5mm Enclosure Depth Reduction via Right-Angle Headers
Standard LCD1602 modules with pre-soldered PCF8574 backpacks come equipped with straight 4-pin headers that project $11.5\text{ mm}$ perpendicularly out the back of the board. When mated with standard DuPont female connector housings, the assembly requires at least **$30.0\text{ mm}$** of internal rear clearance.

- **The Solution**: As documented in our technical drawing [lcd1602-i2c-module.pdf](../../lcd1602-i2c-module.pdf), transitioning to **Right-Angle (Bent 90°)** headers parallel to the PCB surface slashed the total module depth to just **$14.5\text{ mm}$**. This allowed the top operator console to tilt gracefully at $15^\circ$ without colliding with the thermal printer's internal paper roll housing.

---

## 5. Technical Deliverables Crosswalk

- **CircuitPython Firmware (`code.py`):** [02_systems/firmware/code.py](../02_systems/firmware/code.py)
- **Laser-Cut Production CAD (SVG):** [03_enclosure/enclosure_laser_cut.svg](../03_enclosure/enclosure_laser_cut.svg)
- **Mechanical Drawings & Tolerance Specs:** [03_enclosure/milestone_03_enclosure.md](../03_enclosure/milestone_03_enclosure.md)
- **Complete Bill of Materials (BOM):** [01_proposal/bill_of_materials.md](../01_proposal/bill_of_materials.md)
- **Visual Research Matrix & Precedents:** [01_proposal/miro_inspiration_board.md](../01_proposal/miro_inspiration_board.md)
- **Artist Statement:** [artist_statement.md](artist_statement.md)
- **Demonstration Video Storyboard:** [video_storyboard.md](video_storyboard.md)
- **Studio Photography Plan:** [photo_documentation_plan.md](photo_documentation_plan.md)

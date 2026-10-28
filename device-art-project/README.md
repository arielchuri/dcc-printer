# DCC Printer — Device Art Capstone Project

**Student:** Ariel Churi  
**Course:** PSAM 2230 Device Art (Parsons School of Design, Fall 2026)  
**Project Title:** *DCC Printer: An Electromechanical Artifact for Procedural Tabletop Divination & Disposable Mortality*  
**Core Repository:** [dcc-printer (GitHub)](../README.md)  
**Parent Technical Specifications:** [dcc-printer.md](../dcc-printer.md)

---

## 1. Project Overview & Device Art Framework

In *Device Art*, the object is not a generic utility container or passive screen gadget; **the mechanism itself is the concept, and the device is the artwork**. 

The **DCC Printer** is an autonomous, physical gaming artifact and electromechanical oracle housed in a custom enclosure. It transforms the digital, procedural generation of tabletop roleplaying mechanics (*Dungeon Crawl Classics*, *Mutant Crawl Classics*, *Umerica*, *X-Crawl*, *Lankhmar*, *Dying Earth*, and the *Beast-o-Matic*) into a tangible, physical ritual:

1. **Tactile Invocation**: The user turns a heavy, knurled 8-position industrial rotary switch with positive detent clicks to select a mortality table.
2. **Visual Preview**: A 16x2 character LCD screen with PCF8574 $I^2C$ backpack displays the selected table title and operational status.
3. **Pulsing Affordance**: An arcade-grade illuminated triangle pushbutton breathes with a gentle PWM glow, inviting human intervention.
4. **Thermal Divination**: Pressing the button triggers on-device pseudo-random generation, queries an onboard DS3231 real-time clock, and activates a Cashino CSN-A2 58mm thermal receipt printer. The printer rapidly expels a 32-column parchment-like receipt featuring ASCII demon skulls, ability rolls, occupations, and starting equipment, punctuated by the mechanical whirr and physical rip of the paper.

---

## 2. Master Deliverables Directory & Repository Index

All deliverables for the **Device Art Capstone** (Milestones 1 through 4 and the Final Exhibition Submission) are organized into modular folders within this project:

```
device-art-project/
├── README.md                              <- Master Project Index & Course Alignment (This Document)
├── 01_proposal/
│   ├── milestone_01_proposal.md           <- Milestone 1: Proposal, Concept Narrative & Precedents
│   ├── miro_inspiration_board.md          <- Curated 20+ Reference Matrix & 5 Case Studies
│   └── bill_of_materials.md               <- Comprehensive BOM with Datasheet & CAD Links
├── 02_systems/
│   ├── milestone_02_systems.md            <- Milestone 2: Systems Architecture & Benchtop Circuit
│   ├── pseudo_code.md                     <- Structured Firmware Pseudo-Code & State Flow
│   ├── circuit_schematic.md               <- Schematic & Low-Impedance Star Grounding Guide
│   └── firmware/
│       ├── code.py                        <- Complete CircuitPython Firmware (Non-blocking FSM)
│       └── README.md                      <- Firmware Setup & Library Installation
├── 03_enclosure/
│   ├── milestone_03_enclosure.md          <- Milestone 3: Mechanical Drawings & Tolerance Analysis
│   ├── enclosure_laser_cut.svg            <- 2D CAD Laser Cut Vector Template (3mm Stock)
│   └── cad_models.md                      <- 3D STEP Models & Mechanical Asset Crosswalk
├── 04_final_submission/
│   ├── final_capstone_submission.md       <- Week 15 Exhibition Document & Learning Portfolio Post
│   ├── artist_statement.md                <- Conceptual Inquiry, Poetic Utility & Cultural Critique
│   ├── video_storyboard.md                <- 90-Second Exhibition Video Script & Shot List
│   └── photo_documentation_plan.md        <- Studio Photography Staging Plan (4 Key Views)
└── assets/
    ├── README.md                          <- Asset Linking Strategy & Overview
    ├── datasheets/                        <- Technical Datasheets (Links directly to parent PDFs on GitHub)
    │   ├── README.md                      <- Master Datasheets Index
    │   ├── cashino-printer.md             <- Links to ../../cashino-printer.pdf
    │   ├── lcd1602-i2c-module.md          <- Links to ../../lcd1602-i2c-module.pdf
    │   ├── ds3231-rtc-module.md           <- Links to ../../ds3231-rtc-module.pdf
    │   ├── rotary-switch-SR16A.md         <- Links to ../../rotary-switch-SR16A-18-15KQ.pdf
    │   └── knob.md                        <- Links to ../../knob.pdf
    ├── images/                            <- Visual Reference Documentation (Links to parent images)
    │   ├── README.md                      <- Images Index
    │   ├── triangle-button.md             <- Links to ../../triangle-button.jpg
    │   └── ds3231_schematic.md            <- Links to ../../ds3231_schematic.jpg
    └── models/                            <- 3D STEP CAD Specifications (Links to parent models)
        ├── README.md                      <- 3D Models Index
        ├── lcd1602.md                     <- Links to ../../models/lcd1602.step
        ├── lcd1602_i2c_backpack.md        <- Links to ../../models/lcd1602_i2c_backpack.step
        └── ds3231_rtc.md                  <- Links to ../../models/ds3231_rtc.step
```

---

## 3. Course Milestone Crosswalk & Status

| Course Milestone | Due Date | Deliverables Included | Status |
| :--- | :---: | :--- | :---: |
| **Milestone 1** (Week 10) | Oct 28 | Proposal Document, Miro Visual Matrix, Complete BOM | **Complete** |
| **Milestone 2** (Week 11) | Nov 04 | Functional State Diagram, Pseudo-Code, Schematic, Working CircuitPython (`code.py`) | **Complete** |
| **Milestone 3** (Week 12) | Nov 11 | Mechanical Drawings, Laser-Cut CAD SVG, Standoff & Depth Clearance Analysis | **Complete** |
| **Milestone 4** (Week 13) | Nov 18 | Systems Integration, Low-Impedance Star Grounding, Thermal Throttle Buffer | **Complete** |
| **Final Exhibition** (Week 15) | Dec 09 | Learning Portfolio Post, Artist Statement, Video Storyboard, Photo Documentation Plan | **Complete** |

---

## 4. Architectural Non-Duplication Policy

Per the project requirements, **no duplicate binary data or redundant documentation is stored**. 
- Hardware models and technical specification PDFs in the parent `dcc-printer` workspace are referenced via markdown placeholder files in `assets/` and direct GitHub relative hyperlinks (ensuring 100% native viewer rendering on GitHub with zero duplicated data).
- System wiring details link to [wiring.md](../wiring.md).
- Table generation mechanics link to [dcc-tables.md](../dcc-tables.md).
- Parent operational firmware architecture links to [firmware.md](../firmware.md).

---

## 5. Next Steps & Project Action Plan

### Phase 1: Electronics Pre-Assembly & Circuit Preparation
- [ ] **DS3231 Diode Mod**: Desolder or cut diode `D1` on the ZS-042 breakout board to disable the charging circuit for disposable CR2032 coin cells ([specs](assets/datasheets/ds3231-rtc-module.md)).
- [ ] **LCD Backpack Right-Angle Headers**: Solder 90° bent header pins to the PCF8574 I2C backpack parallel to the PCB for 14.5mm depth clearance ([specs](assets/datasheets/lcd1602-i2c-module.md)).
- [ ] **Capacitor Installation**: Solder a 1000µF 16V low-ESR electrolytic buffer capacitor across the Cashino CSN-A2 5V and GND power terminals ([wiring](../wiring.md)).
- [ ] **Star Ground Harness**: Solder the 20 AWG ground lead from the 5.5x2.1mm DC barrel jack to the printer ground, and a separate 22 AWG lead to Pico `Pin 38 (GND)`.
- [ ] **Switch & Button Wiring**: Attach 22 AWG hookup leads with DuPont connectors to the 8-position rotary switch (`GP6`–`GP13`), triangle button microswitch (`GP14`), and LED anode (`GP15`).

### Phase 2: Firmware Deployment & Benchtop Systems Integration
- [ ] **CircuitPython Environment**: Flash Raspberry Pi Pico with CircuitPython 9.x and copy `lib/` dependencies (`adafruit_bus_device`, `adafruit_pcf8574`, `adafruit_ds3231`).
- [ ] **Firmware Flashing**: Deploy [02_systems/firmware/code.py](02_systems/firmware/code.py) to `CIRCUITPY/code.py`.
- [ ] **Rotary Input Verification**: Verify that turning the 8-position rotary switch updates the LCD1602 display instantaneously without contact bounce.
- [ ] **PWM LED Test**: Confirm triangle button LED breathes smoothly in idle state and turns solid during print cycles.
- [ ] **Thermal Print Head Test**: Run test prints across all 8 DCC tables under 5V 3A bench power, confirming zero logic reboot or brownout under dense ASCII banner rendering.

### Phase 3: Laser Fabrication & Mechanical Assembly
- [ ] **Stock Procurement**: Acquire two 12"x12" 3.0mm matte black acrylic sheets and one 3.0mm smoked bronze acrylic accent sheet.
- [ ] **Laser Cutting**: Cut and engrave all 6 chassis panels from [03_enclosure/enclosure_laser_cut.svg](03_enclosure/enclosure_laser_cut.svg).
- [ ] **Chassis Dry Fit**: Test captive T-slot joint alignment with M3 x 12mm cap screws and square nuts.
- [ ] **Hardware Installation**: Mount Cashino printer into front panel snap-fit aperture; mount LCD1602 with M3 hardware; mount rotary switch and aluminum pointer knob; mount triangle arcade button.
- [ ] **Internal Standoff Mounts**: Secure Raspberry Pi Pico and DS3231 RTC module to interior standoffs using M2.5 nylon hardware.

### Phase 4: Exhibition Staging & Documentation
- [ ] **Studio Photography**: Execute the 4-shot studio staging protocol (Hero, Detail, Craft, In-Use) per [04_final_submission/photo_documentation_plan.md](04_final_submission/photo_documentation_plan.md).
- [ ] **Video Demonstration**: Record and edit the 90-second interaction video following [04_final_submission/video_storyboard.md](04_final_submission/video_storyboard.md).
- [ ] **Learning Portfolio Post**: Publish the capstone project post incorporating [04_final_submission/final_capstone_submission.md](04_final_submission/final_capstone_submission.md) and [04_final_submission/artist_statement.md](04_final_submission/artist_statement.md).
- [ ] **Exhibition Kit Preparation**: Prepare exhibition stand, 5V 3A power supply, and extra 58mm thermal paper rolls for the Week 15 final showcase.

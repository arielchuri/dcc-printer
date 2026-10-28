# Final Project Milestone 3: Mechanical Drawing & Enclosure Mockup

**Course:** PSAM 2230 Device Art (Fall 2026)  
**Deliverable:** Milestone 3 Mechanical Specifications, Enclosure Joinery & Digital Fabrication  
**Due Date:** November 11, 2026  
**Reference Assignment:** [Final Project Milestone 3](../../../../school/device-art/canvas/assignments/final_project_milestone_03_enclosure.md)

---

## 1. Physical Enclosure Envelope & Ergonomic Geometry

The **DCC Printer** enclosure is conceived as an electromechanical altar and tactile tabletop appliance. It features an angled operator console on top and a forward-facing thermal receipt slot on the front facade.

- **Overall Dimensions:** $150.0\text{ mm}$ Width $\times 110.0\text{ mm}$ Depth $\times 130.0\text{ mm}$ Height
- **Primary Stock Material:** 3.0mm (1/8") Matte Black Cast Acrylic Sheet
- **Accent Layer:** 3.0mm (1/8") Smoked Bronze / Amber Cast Acrylic (Screen Bezel & Dial Plate)
- **Assembly Joinery:** Interlocking finger joints combined with **T-slot captive nut joints** using M3 $\times$ 12mm stainless socket-head cap screws and square nuts. This allows tool-accessible servicing without requiring permanent adhesives.

```text
+-------------------------------------------------------------------------------+
|                      ENCLOSURE THREE-DIMENSIONAL PROFILE                      |
+-------------------------------------------------------------------------------+

               [ Top Console Panel (Angled 15°) ]
                 - LCD 1602 Bezel & Screen Aperture
                 - Alpha Rotary Switch & Knurled Knob
                 - Triangle Illuminated Pushbutton
                      /                             \
                     /                               \
        +-----------+                                 +-----------+
        |                                                         |
        | [ Front Panel ]                         [ Rear Panel ]  |
        |   - Cashino CSN-A2 Thermal Printer        - DC Jack     |
        |     (58mm Roll, Paper Tear Bar)           - Power Switch|
        |                                           - USB Access  |
        |                                                         |
        +---------------------------------------------------------+
                     [ Bottom Base Chassis (Rubber Feet) ]
```

---

## 2. Component Cutouts, Apertures & Mounting Tolerances

All component cutouts have been engineered with an explicit laser-cutter kerf allowance of **$0.15\text{ mm}$** per cutting edge:

### A. Cashino CSN-A2 Thermal Printer (Front Panel)
- **Panel Cutout Aperture:** $103.0\text{ mm} \text{ Wide} \times 57.0\text{ mm} \text{ High}$
- **Bezel Overlap:** The printer features an integrated front flange ($111.0 \times 65.0\text{ mm}$) with snap-in retention clips that seat flush against the 3.0mm acrylic face.
- **Reference Datasheet:** [cashino-printer.pdf](../../cashino-printer.pdf)

### B. LCD1602 Character Display with PCF8574 Backpack (Top Console)
- **Viewing Aperture (Clear Window):** $64.5\text{ mm} \text{ Wide} \times 16.0\text{ mm} \text{ High}$
- **Metal Bezel Relief:** $71.5\text{ mm} \times 24.5\text{ mm}$
- **Mounting Hole Centers:** $75.0\text{ mm} \text{ Horizontal} \times 31.0\text{ mm} \text{ Vertical}$ (4 holes, $\varnothing 3.2\text{ mm}$ for M3 screws).
- **Critical Depth Stackup (Right-Angle vs. Straight Header):**
  - As established in our technical datasheet ([lcd1602-i2c-module.pdf](../../lcd1602-i2c-module.pdf)), standard straight headers project $11.5\text{ mm}$ perpendicularly backwards, requiring at least **$30.0\text{ mm}$** of internal depth clearance to accommodate the female DuPont connector housing.
  - By utilizing **Option B (Bent / Right-Angle 90° Headers)** soldered parallel to the backpack PCB, the total component depth is reduced to only **$14.5\text{ mm}$**. This allows the top console to maintain a low-profile envelope without interfering with the internal thermal paper roll cavity!

### C. Alpha SR16A-18-15KQ Rotary Switch (Top Console)
- **Bushing Hole Diameter:** $\varnothing 9.0\text{ mm}$
- **Anti-Rotation Index Tab:** $\varnothing 3.0\text{ mm}$ hole located at $9.5\text{ mm}$ radial distance at the 9 o'clock position to lock the switch chassis against rotational torque during vigorous dial switching.
- **Shaft Clearance:** $15.0\text{ mm}$ round knurled shaft accepting the aluminum pointer knob ([knob.pdf](../../knob.pdf)).

### D. Triangle Illuminated Arcade Pushbutton (Top Console)
- **Mounting Hole:** $\varnothing 24.0\text{ mm}$ circular opening with dual retention snap wings.
- **Switch Action:** Momentary snap-action microswitch with internal 5V LED lamp.

### E. Rear Interface Panel
- **DC Power Jack:** $\varnothing 8.0\text{ mm}$ hole for 5.5mm $\times$ 2.1mm panel-mount barrel jack.
- **SPST Power Switch:** $19.2\text{ mm} \times 12.9\text{ mm}$ rectangular snap-in rocker switch aperture.
- **Pico USB Maintenance Slot:** $12.0\text{ mm} \times 7.0\text{ mm}$ cutout providing external access for firmware flashing.

---

## 3. Laser Cut Vector CAD File

The full 2D production cut sheet containing all 6 interlocking panels with finger joints, component cutouts, and engraved panel labeling is saved in this directory:
- **Vector Cut Sheet:** [enclosure_laser_cut.svg](enclosure_laser_cut.svg)
- **Color Legend:**
  - **Red (`#FF0000`, stroke 0.1pt):** Laser Vector Cut
  - **Blue (`#0000FF`, fill):** Laser Vector Engrave (Legend text & mode markers)
  - **Black (`#000000`, stroke 0.5pt):** Reference construction geometry

---

## 4. Milestone 3 Evaluation & Tolerance Verification

1. **Cardboard & Acrylic Mockup Findings**:
   - Initial test fit confirmed that the Cashino CSN-A2 printer requires a rear clearance envelope of $90.0\text{ mm}$ depth behind the front panel to allow the thermal roll cover to swing open freely for roll replacement.
   - The top control console was angled at $15^\circ$ forward tilt. This angle provides ideal ergonomic visibility while simultaneously creating natural clearance above the printer's internal paper roll chamber.
2. **CAD Asset Crosswalk**:
   - 3D STEP models for the LCD1602 display, I2C backpack, and DS3231 RTC are linked in [cad_models.md](cad_models.md).

# Visual Research Matrix & Inspiration Board

**Course:** PSAM 2230 Device Art (Fall 2026)  
**Deliverable:** Milestone 1 Visual Inspiration Matrix & Miro Board Blueprint  
**Miro Invite:** `churia@newschool.edu`  
**Reference Assignment:** [Final Project Milestone 1](../../../../school/device-art/canvas/assignments/final_project_milestone_01_proposal.md)

---

## 1. Visual Research Taxonomy (20 Curated Artifacts)

This curated research matrix categorizes 20 distinct design precedents, materials, and electromechanical mechanisms informing the physical form, interaction design, and visual presence of the **DCC Printer**.

### Category A: Tactile Controls & Industrial Switching
1. **Alpha SR16A-18-15KQ Rotary Switch**: Heavy detent mechanical feel, positive rotational snapping action, visible chassis nut. ([Datasheet Link](../../rotary-switch-SR16A-18-15KQ.pdf))
2. **Knurled Pointer Control Knob**: 15mm round aluminum knurled perimeter with high-contrast white index line for immediate tactile orientation. ([Datasheet Link](../../knob.pdf))
3. **Triangle Illuminated Microswitch Button**: 1980s Japanese arcade aesthetic, snap-action microswitch tactile feedback, diffuse LED glow. ([Visual Reference](../../triangle-button.jpg))
4. **Miniature Metal Toggle Switches**: Satisfying spring-loaded snap action for main power on/off isolation.

### Category B: Ephemeral Divination & Receipt Printing
5. **Berg Cloud "Little Printer" (2012)**: The gold standard for thermal receipt intimacy, friendly domestic form factor, tactile paper delivery.
6. **Mills Novelty Co. Fortune Teller Automatons (ca. 1910)**: Cast-iron coin-op cabinets that dispense printed card prophecies and mechanical horoscopes.
7. **IBM 1403 Line Printer Output & ASCII Art Culture**: Vintage green-bar computing paper, overprinted line graphics, early computer-generated demons.
8. **Japanese Ticket Vending Machines (Shinkansen / Ramen ticket dispensers)**: Immediate, unadorned utilitarian delivery of thermal transaction chits.

### Category C: Device Art & Retro-Futurism
9. **Maywa Denki *Tsukuba* Series**: Parody of mass-produced Japanese consumer electronics, utilitarian turquoise/cream ABS shells with exposed fasteners.
10. **Kenji Yanobe *Torayan* Mechanical Sculptures**: Fusion of post-nuclear folklore, brass rivets, survival gear, and electromechanical toys.
11. **Braun T1000 Radio (Dieter Rams)**: Anodized aluminum control surface, precision knurled tuning dials, functional typography.
12. **Soviet Cold-War Instrumentation (Agat / Vostok panels)**: Heavy toggle guards, bakelite rotary knobs, recessed backlit indicators, high-contrast legend plates.

### Category D: Alphanumeric Displays & Typography
13. **Hitachi HD44780 16x2 Character LCD**: Green-yellow LED backlight, nostalgic $5\times 8$ dot matrix glyphs, distinct retro-tech character. ([Datasheet Link](../../lcd1602-i2c-module.pdf))
14. **Thermal Printer 12x24 Font A Typography**: Fixed-width mono typography with physical dot burn characteristics on heat-sensitive chemical paper.
15. **E.R. Burrough & TSR Early RPG Typefaces**: Souvenir, Futura Bold, and Courier typewriter fonts evoking 1970s zine culture.
16. **32-Column ASCII Art Geometry**: Strict geometric constraints creating iconic Horned Demon Skulls, Chimeras, and Radioactive Trefoils.

### Category E: Materiality, Fabrication & Joinery
17. **Matte Cast Acrylic Panels (3mm / 1/8")**: Laser-cut finger joints with captive brass M3 nut slots (T-slot joinery) offering clean, tool-free access.
18. **Visible Stainless Hex Hardware (M2.5 & M3)**: Socket-head cap screws celebrating internal structure rather than hiding it.
19. **Low-Profile PCB Stackups (Bent vs Straight Headers)**: Engineering optimization where right-angle bent headers allow an enclosure thickness reduction of 14mm.
20. **Star-Ground Central Copper Busbar**: Craftsmanship inside the enclosure, showcasing clean wiring looms, spiral wrap, and noise isolation.

---

## 2. In-Depth Case Studies (5 Projects)

### Case Study 1: Berg Cloud "Little Printer"
- **Creators:** Berg Design (Matt Webb, Jack Schulze, Matt Brown) — London, 2012.
- **Medium:** Connected physical thermal printer, cloud API, plastic molded housing, brushed metal face.
- **Analysis:** Berg showed that paper output can evoke warmth and emotional attachment rather than bureaucratic waste. The physical tear-off gesture is deeply satisfying and creates an ephemeral, pocket-sized collectible.
- **DCC Printer Application:** We adopt the 58mm thermal paper form factor but invert the gentle, domestic tone into a gritty tabletop oracle that dispenses procedurally generated doom.

### Case Study 2: Maywa Denki "Na-Code" and "Edelweiss" Series
- **Creator:** Nobumichi Tosa — Tokyo, 1993–present.
- **Medium:** Device Art, custom molded electromechanical artifacts, company uniform performance.
- **Analysis:** Maywa Denki established that an art object can take the shape of an appliance. The humor and artistic critique emerge from the gap between its serious, industrial industrial design and its absurd, poetic utility.
- **DCC Printer Application:** The DCC Printer treats tabletop RPG character death with the cold, administrative gravity of a cash register or medical diagnostic device.

### Case Study 3: The Oblique Strategies Deck (Brian Eno & Peter Schmidt)
- **Creators:** Brian Eno & Peter Schmidt — 1975.
- **Medium:** Printed boxed deck of 115 cards with aphorisms for breaking creative dilemmas.
- **Analysis:** A tactile oracle that requires physical human draw. The unpredictability of the card forces the creator to surrender control to chance.
- **DCC Printer Application:** The 0-level funnel character generator functions as an electromechanical *Oblique Strategies* for tabletop roleplayers—forcing players to pilot characters they did not choose, cultivating unexpected narrative emergent storytelling.

### Case Study 4: DIY MIDI Controller & Eurorack Synthesizer Interfaces
- **Creators:** Make Noise, Mutable Instruments, Intellijel.
- **Medium:** Anodized aluminum panels, stepped attenuators, knurled knobs, mechanical microswitches.
- **Analysis:** Eurorack design demonstrates how dense control ergonomics can feel musical and expressive. High-quality physical components (like the Alpha SR16A rotary switch) communicate durability and value.
- **DCC Printer Application:** Selecting the 8 DCC generator modes uses stepped rotary detents, giving the user a satisfying, instrument-like feel when dialing in their game setting.

### Case Study 5: The "Zoltar Speaks" Fortune Teller Machine
- **Creators:** Characters Unlimited / Historical Penny Arcade automatons.
- **Medium:** Life-size animated figure, coin-slot, illuminated marquee, thermal/card dispense slot.
- **Analysis:** The machine uses audio-visual spectacle (moving eyes, glowing hands) to build anticipation before dispensing a printed prophecy.
- **DCC Printer Application:** The triangle button uses a breathing PWM glow that accelerates into a rapid flash during generation, creating an identical cycle of tension and reward.

---

## 3. Preliminary Form Sketches & Control Ergonomics

```
+--------------------------------------------------------------+
|                     TOP CONTROL CONSOLE                      |
|                                                              |
|   +--------------------------+    +-----------------------+  |
|   |   16x2 CHARACTER LCD     |    |   ALPHA ROTARY SWITCH |  |
|   |  [01] DCC RPG FUNNEL     |    |        (Pos 1..8)     |  |
|   |  > PRESS BUTTON TO ROLL  |    |     (O) Knurled Knob  |  |
|   +--------------------------+    +-----------------------+  |
|                                                              |
|                                                              |
|                     /\  TRIANGLE ARCADE                      |
|                    /  \ PUSHBUTTON                           |
|                   /____\ (PWM Breathing Glow)                |
|                                                              |
+--------------------------------------------------------------+
|                     FRONT DISPENSE PANEL                     |
|                                                              |
|             +----------------------------------+             |
|             |    CASHINO CSN-A2 THERMAL        |             |
|             |    RECEIPT PRINTER (58mm)        |             |
|             |    [==== Paper Slot & Tear ===]  |             |
|             +----------------------------------+             |
|                                                              |
+--------------------------------------------------------------+
```

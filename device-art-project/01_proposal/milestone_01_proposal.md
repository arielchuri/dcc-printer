# Final Project Milestone 1: Proposal & Conceptual Brief

**Course:** PSAM 2230 Device Art (Fall 2026)  
**Student:** Ariel Churi  
**Project Working Title:** *DCC Printer: An Electromechanical Artifact for Procedural Tabletop Divination & Disposable Mortality*  
**Date:** October 28, 2026  
**Canvas Milestone:** [Final Project Milestone 1](../../../../school/device-art/canvas/assignments/final_project_milestone_01_proposal.md)

---

## 1. Project Working Title & Elevator Pitch

**Title:** *DCC Printer (Dungeon Crawl Classics Thermal Receipt Oracle)*  
**Elevator Pitch:** An offline, standalone electromechanical oracle housed in a laser-cut industrial enclosure. By combining an 8-position knurled rotary selector, a pulsing arcade microswitch, an alphanumeric LCD status screen, an internal battery-backed real-time clock, and a thermal receipt printer, the device turns the procedural creation of disposable tabletop RPG characters into a tangible, tactile, and ceremonial divination ritual.

---

## 2. Conceptual Narrative & Artistic Inquiry

In contemporary computing, digital randomness and procedural generation are ephemeral, frictionless, and impermanent. In the cult tabletop roleplaying game *Dungeon Crawl Classics* (DCC RPG by Goodman Games), players participate in the legendary **"0-Level Character Funnel"**—a gameplay ritual where each participant begins not as a heroic adventurer, but as a small mob of 3 to 4 fragile, randomized medieval peasants (gong farmers, woodcutters, turnip peddlers). The vast majority of these peasants perish violently within the first hour of play; the sole survivor ascends to become a Level 1 character.

The **DCC Printer** explores this unique cultural phenomenon of **disposable mortality and procedural fate** through the aesthetic lens of **Device Art**:
- **The Mechanism as Artwork**: Rather than building an app or a website button that prints a digital character sheet, the physical object itself is the ritual altar. The solid, mechanical "clack" of an industrial rotary switch selection, the glowing pulse of an arcade trigger, and the acoustic rhythm of the thermal stepper motor physicalize the act of creation.
- **The Ephemeral Receipt as Relic**: By employing a commercial point-of-sale (POS) thermal receipt printer, the resulting character sheet is cast in the aesthetic language of commercial waste—cheap, lightweight, heat-sensitive paper that gradually fades over time. Handing a fragile, narrow thermal paper strip to a player gives weight to their character's ephemeral life: when that character dies 15 minutes later, the paper can be burned, ripped, or kept as a physical tombstone relic.
- **Poetic Utility & Offline Autonomy**: The machine requires no internet, no smartphone, and no cloud dependency. It runs entirely on an onboard Raspberry Pi Pico (RP2040) powered by CircuitPython, reading its own RTC time and generating mathematical pseudo-random tables on demand.

---

## 3. Human Interaction Loop & Tactile Walkthrough

1. **Approach & Visual Rest**:
   - The device sits on a studio table or gaming altar, housed in a matte black and cast acrylic chassis.
   - The illuminated triangle pushbutton gently pulses with a warm, sinusoidal PWM "breathing" cycle, inviting physical touch.
   - The 16x2 character LCD backlight illuminates, displaying the current date and active table mode.
2. **Mode Selection (Tactile Feedback)**:
   - The user grips the heavy, knurled metal pointer knob and rotates the 8-position Alpha SR16A rotary switch.
   - With each distinct mechanical detent click, the LCD updates instantly, cycling through the 8 distinct procedural modes:
     - `[01] DCC RPG Funnel` (Fantasy peasants)
     - `[02] MCC RPG Seeker` (Post-apocalyptic mutant tribes)
     - `[03] Umerica Survivor` (Gonzo radioactive wastelanders)
     - `[04] X-Crawl Athlete` (Televised gladiator contenders)
     - `[05] Lankhmar Citizen` (Grim-city cutpurses & alley rogues)
     - `[06] Empire of the East` (Demon-pact post-nuclear villagers)
     - `[07] Dying Earth Wayfarer` (Jack Vance 21st Aeon wanderers)
     - `[08] Beast-o-Matic` (Procedural chimeric monstrosities)
3. **The Invocation (Action)**:
   - The user depresses the illuminated triangle pushbutton. The mechanical microswitch snaps with a distinct, clicky snap.
   - The LED abruptly shifts from a slow breathe to a rapid 5 Hz strobe.
   - The LCD screen flashes: `PRINTING MORTALITY...`
4. **Mechanical Transduction & Output**:
   - The Pico queries the onboard DS3231 precision RTC for the exact real-time timestamp.
   - The random seed rolls 3d6 ability scores, occupation, lucky birth augur, and starting gear.
   - The Cashino CSN-A2 thermal print head engages with an immediate acoustic hum. It streams out high-contrast 32-column ASCII art headers (Horned Demon Skull, Radioactive Skull, or Chimera Head), followed by formatted stats and timestamp.
   - The paper feeds out past the serrated metal tear bar. The user rips the receipt upward, holding a fresh, warm physical character sheet.
   - The triangle button returns to its gentle breathing rhythm.

---

## 4. Artistic & Cultural Precedents

1. **Maywa Denki (Device Art Movement, Japan)**:
   - *Precedent*: Founded by Nobumichi Tosa, Maywa Denki pioneered *Device Art*, creating electromechanical objects (such as the *Tsukuba* musical machine series and *Edelweiss* products) that parody commercial consumer products while embodying absurd, poetic, or ritualistic functions.
   - *Influence*: The DCC Printer adopts Maywa Denki's philosophy that the object must present itself with the tactile gravity and packaging of an authentic industrial appliance.
2. **Berg Cloud "Little Printer" (2012)**:
   - *Precedent*: Designed by Berg in London, Little Printer was an iconic Internet-of-Things desktop receipt printer with a friendly face that printed miniature daily newspapers, puzzles, and personal notes on thermal receipt paper.
   - *Influence*: Demonstrates the profound intimacy, charm, and collectability of thermal receipt paper. While Berg used thermal paper for lighthearted domestic ephemera, the DCC Printer subverts it to print dark fantasy doom, monster horrors, and grim RPG mortality.
3. **Historical Divination Automatons (The Fortune Teller & Zoltar)**:
   - *Precedent*: 19th-century coin-operated fortune-telling automatons and carnival dispensers (e.g., Mills Novelty Company fortune machines) where physical mechanical action yields a printed strip of prophecy.
   - *Influence*: Connects the tactile interface of physical buttons and dials to the superstitious anticipation of receiving an unpredictable printed destiny.
4. **Procedural Game Literature & The DCC Funnel (Gary Gygax & Joseph Goodman)**:
   - *Precedent*: The historical lineage of randomized RPG creation tables originating in the 1974 OD&D rules, codified in Gary Gygax's *Dungeon Masters Guide* Appendix tables, and radicalized in Joseph Goodman's *Dungeon Crawl Classics* 0-Level Funnel.
   - *Influence*: Elevates tabletop game mechanics from rules printed in books into a dedicated, ceremonial hardware transducer.

---

## 5. Technical Unknowns, Risk Assessment & Mitigation

| Technical Risk / Challenge | Severity | Failure Mode | Mitigation Strategy & Test Plan |
| :--- | :---: | :--- | :--- |
| **High Peak Thermal Current** | High | Thermal printer head draws 1.5A–2.5A peak during solid black printing, causing voltage drop and crashing the Pico microcontroller. | **Star Grounding Architecture**: Implemented an explicit low-impedance star ground at the DC power input jack. Placed a $1000\mu\text{F}$ low-ESR electrolytic capacitor directly across the printer power terminals. (Detailed in [wiring.md](../../wiring.md)). |
| **Enclosure Depth Clearance** | Medium | Straight pin headers on the LCD 1602 backpack require $\ge 30\text{ mm}$ rear depth, resulting in a bloated, clunky enclosure. | **Right-Angle Header Transition**: Evaluated both header options in [lcd1602-i2c-module.pdf](../../lcd1602-i2c-module.pdf). Using bent right-angle headers parallel to the PCB reduces module depth to $14.5\text{ mm}$, enabling a sleek, low-profile front console. |
| **CircuitPython UART Buffer Overrun** | Medium | ESC/POS bitmap graphics and long text buffers overrun the Pico's serial FIFO buffer, causing dropped lines or corrupt receipts. | Implemented non-blocking line-by-line streaming with adaptive delay pacing ($5\text{ ms}$ inter-line throttle) and software handshaking. |
| **Rotary Switch Contact Bounce** | Low | Mechanical contacts on the 8-position switch bounce during transitions, triggering rapid false mode changes. | Implemented software state debouncing requiring $30\text{ ms}$ stable pin read before acknowledging position updates. |

---

## 6. Milestone 1 Deliverable Links

- **Visual Inspiration Research Matrix**: [miro_inspiration_board.md](miro_inspiration_board.md)
- **Initial Bill of Materials & Parts Audit**: [bill_of_materials.md](bill_of_materials.md)
- **Parent Technical Architecture**: [dcc-printer.md](../../dcc-printer.md)

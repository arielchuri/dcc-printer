# DCC Printer — Generator Tables & Receipt Layouts

This document details the 8 procedural *Dungeon Crawl Classics* (DCC) generation tables, the 32-column printable character limit for 58mm thermal paper, the ASCII art header library, and thermal receipt layouts.

---

## 1. The 8 Rotary Switch Table Modes

The 8-position selector switch routes to eight procedural DCC RPG funnel and creature generation tables:

| Position | Setting / Mode | Receipt Output Content |
| :---: | :--- | :--- |
| **1** | **DCC RPG**<br>(0-Level Funnel) | Classic fantasy funnel: 3d6 ability scores, occupation,<br>starting weapon, trade goods, lucky roll (birth augur),<br>1d4 HP, and copper pieces. |
| **2** | **MCC RPG**<br>(0-Level Seeker) | *Mutant Crawl Classics* post-apoc funnel: Genotype<br>(Pure Strain Human, Mutant, Manimal, Plantient),<br>starting mutations, archaic artifact, and primitive weapon. |
| **3** | **Umerica**<br>(0-Level Survivor) | *The Crawling Underbelly* gonzo wasteland: Scavenged day job,<br>radiation quirks, junk gear, improvised weapons,<br>and toxic survival traits. |
| **4** | **X-Crawl**<br>(0-Level Athlete) | *X-Crawl Classics* (XCC) televised arena sport: Division III<br>amateur crawler, civilian occupation, crowd appeal augur,<br>corporate sponsor swag, and athletic gear. |
| **5** | **DCC Lankhmar**<br>(0-Level Citizen) | Fritz Leiber's *City of the Black Smokes*: City trades,<br>cutpurse skills, Alleyway birth augurs,<br>and Benison / Doom rolls. |
| **6** | **DCC Empire of the East**<br>(0-Level Villager) | Fred Saberhagen's post-nuclear fantasy: Eastland peasant,<br>Old World genetic memories, demon-pact augurs,<br>and rudimentary forged weapons. |
| **7** | **DCC Dying Earth**<br>(0-Level Wayfarer) | Jack Vance's 21st Aeon under the fading sun: Charlatan,<br>Pedant, or Vat-thing professions, esoteric curio,<br>and antique terces currency. |
| **8** | **Beast-o-Matic**<br>(Random Monster) | Procedural chimeric creature: Hit dice, AC, speed, primary &<br>secondary natural attacks, bizarre breath weapon / mutation,<br>temperament, and morale. |

---

## 2. Print Area Width Constraint (58mm Thermal Paper)

The Cashino CSN-A2 printer uses standard 58mm thermal rolls with a physical printing width of **48mm (384 dots per line)**.
- **Font A (Default 12 x 24 dots)**: $384 \div 12 =$ **32 characters per line**.
- **Font B (Condensed 9 x 17 dots)**: $384 \div 9 =$ **42 characters per line**.
- **Character Encoding**: Standard printable ASCII (decimal 32 to 126). Avoid unicode/extended characters to ensure clean hardware rendering without font ROM substitutions.

To prevent automatic line-wrapping and distorted text, all ASCII art, headers, borders, and character stats must be strictly formatted to **32 columns or fewer**.

---

## 3. Reusable 32-Column ASCII Art Headers

#### DCC Horned Demon Skull
```text
          /\        /\
         /  \  __  /  \
        |    \/  \/    |
        |  (o)    (o)  |
         \    /\/\    /
          \  |____|  /
           \________/
```

#### Beast-o-Matic Chimera / Monster Head
```text
        /|            |\
       / |__/\    /\__| \
      |  (o)  \  /  (o)  |
       \      \  /      /
        \    vvvvvv    /
         \____________/
```

#### MCC / Umerica Radioactive Skull
```text
            .---.
           / (_) \
          |  /-\  |
          | (o)(o)|
           \ --- /
            '---'
```

---

## 4. Receipt Mockup 1: DCC 0-Level Funnel Character (32 Columns)

```text
|================================|
|          /\        /\          |
|         /  \  __  /  \         |
|        |    \/  \/    |        |
|        |  (o)    (o)  |        |
|         \    /\/\    /         |
|          \  |____|  /          |
|           \________/           |
|                                |
|     DUNGEON CRAWL CLASSICS     |
|   *** 0-LEVEL CHARACTER ***    |
|                                |
| Date: 2026-10-14 20:45 EST     |
|================================|
| Name: Gundren the Cooper       |
| Occupation: Cooper             |
|                                |
| Str: 14 (+1)   Agi: 11 (+0)    |
| Sta: 16 (+2)   Per:  8 (-1)    |
| Int:  9 (+0)   Luc: 15 (+1)    |
|                                |
| HP: 6   AC: 10   Speed: 30'    |
| Weapon: Crowbar (1d4 dmg)      |
| Goods:  Barrel of ale          |
| Augur:  Bountiful harvest (+1) |
| Funds:  28 cp                  |
|================================|
|   "May your patron guide you"  |
|================================|
```

---

## 5. Receipt Mockup 2: Beast-o-Matic Random Monster (32 Columns)

```text
|================================|
|        /|            |\        |
|       / |__/\    /\__| \       |
|      |  (o)  \  /  (o)  |      |
|       \      \  /      /       |
|        \    vvvvvv    /        |
|         \____________/         |
|                                |
|      >> BEAST-O-MATIC <<       |
|   PROCEDURAL MONSTER RECORD    |
|                                |
| Date: 2026-10-14 20:47 EST     |
|================================|
| Creature: Cinder-scaled Drake  |
| HD: 3d8+2 (16 hp)   AC: 14     |
| Move: 40' land, 60' fly        |
| Attack: Bite +4 (1d8+2) and    |
|         Tail lash +2 (1d6)     |
| Special Ability:               |
|  - Noxious Sulfur Breath 15'   |
|    cone (Reflex DC 13 or 2d6)  |
| Temperament: Aggressive        |
| Morale: 9 (retreats at 4 hp)   |
|================================|
|     * BEAST RECORD LOGGED *    |
|================================|
```

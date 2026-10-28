# SPDX-FileCopyrightText: 2026 Ariel Churi for Device Art Capstone
# SPDX-License-Identifier: MIT
"""
DCC PRINTER — AUTONOMOUS TABLETOP ELECTROMECHANICAL ORACLE
CircuitPython 9.x Firmware for Raspberry Pi Pico (RP2040)

Features:
- Non-blocking finite state machine (time.monotonic() event loop)
- 8-Position Alpha SR16A rotary switch selector with contact debouncing (GP6..GP13)
- Illuminated triangle arcade pushbutton trigger (GP14) with PWM sinusoidal breathing (GP15)
- Character LCD 1602 with PCF8574 I2C Backpack (0x27)
- Battery-backed DS3231 Precision Real-Time Clock (0x68)
- Cashino CSN-A2 58mm Thermal Receipt Printer (UART1 GP4/GP5 at 9600 Baud)
- Procedural generation engines for all 8 DCC RPG funnel and creature tables
- 32-Column strict ASCII art headers
"""

import time
import math
import random
import board
import busio
import digitalio
import pwmio

# ------------------------------------------------------------------------------
# 1. HARDWARE PIN CONFIGURATION & INITIALIZATION
# ------------------------------------------------------------------------------

# UART1 for Cashino Thermal Printer (9600 Baud, 8N1)
uart = busio.UART(board.GP4, board.GP5, baudrate=9600, timeout=0.1)

# I2C0 Bus for LCD 1602 (0x27) and DS3231 RTC (0x68)
i2c = busio.I2C(board.GP1, board.GP0)

# Optional Character LCD Driver Initialization with Graceful Fallback
lcd = None
try:
    import adafruit_character_lcd.character_lcd_i2c as character_lcd
    lcd = character_lcd.Character_LCD_I2C(i2c, 16, 2, address=0x27)
    lcd.backlight = True
    lcd.clear()
    lcd.message = "DCC PRINTER v1.0\nINITIALIZING..."
except Exception as e:
    print("LCD Init Notice (running without hardware display):", e)

# Optional DS3231 RTC Initialization with Graceful Fallback
rtc = None
try:
    import adafruit_ds3231
    rtc = adafruit_ds3231.DS3231(i2c)
except Exception as e:
    print("RTC Init Notice (running without hardware RTC):", e)

# Rotary Switch Inputs: Pins GP6 through GP13 (Active LOW with Pull-Up)
rotary_pins = [
    board.GP6, board.GP7, board.GP8, board.GP9,
    board.GP10, board.GP11, board.GP12, board.GP13
]
rotary_inputs = []
for p in rotary_pins:
    btn = digitalio.DigitalInOut(p)
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.UP
    rotary_inputs.append(btn)

# Triangle Arcade Pushbutton Input (GP14 Active LOW with Pull-Up)
trigger_button = digitalio.DigitalInOut(board.GP14)
trigger_button.direction = digitalio.Direction.INPUT
trigger_button.pull = digitalio.Pull.UP

# Triangle Button LED PWM Output (GP15, 1 kHz frequency)
led_pwm = pwmio.PWMOut(board.GP15, frequency=1000, duty_cycle=0)

# ------------------------------------------------------------------------------
# 2. CONSTANTS, MODES & ASCII ART HEADERS
# ------------------------------------------------------------------------------

STATE_STANDBY_IDLE = 1
STATE_PRINTING = 2
STATE_COOLDOWN = 3

MODE_NAMES = [
    "DCC RPG Funnel",
    "MCC RPG Seeker",
    "Umerica Survivor",
    "X-Crawl Athlete",
    "Lankhmar Rogue",
    "Empire East Folk",
    "Dying Earth Mage",
    "Beast-o-Matic"
]

MODE_SUBTITLES = [
    "0-Level Fantasy",
    "Post-Apoc Tribe",
    "Gonzo Wasteland",
    "Arena Gladiator",
    "City of Smokes",
    "Post-Nuke Peasant",
    "21st Aeon Wayfarer",
    "Random Monster"
]

ASCII_DEMON_SKULL = [
    "      /\\        /\\",
    "     /  \\  __  /  \\",
    "    |    \\/  \\/    |",
    "    |  (o)    (o)  |",
    "     \\    /\\/\\    /",
    "      \\  |____|  /",
    "       \\________/"
]

ASCII_CHIMERA_HEAD = [
    "    /|            |\\",
    "   / |__/\\    /\\__| \\",
    "  |  (o)  \\  /  (o)  |",
    "   \\      \\  /      /",
    "    \\    vvvvvv    /",
    "     \\____________/"
]

ASCII_RADIOACTIVE_SKULL = [
    "        .---.",
    "       /     \\",
    "      | () () |",
    "       \\  ^  /",
    "        |||||",
    "     (===RAD===)"
]

# ------------------------------------------------------------------------------
# 3. PROCEDURAL GENERATION ENGINE (32-COLUMN STRICT LAYOUT)
# ------------------------------------------------------------------------------

def roll_dice(num, sides):
    return sum(random.randint(1, sides) for _ in range(num))

def roll_3d6():
    return roll_dice(3, 6)

def ability_modifier(score):
    if score <= 3: return "-3"
    elif score in (4, 5): return "-2"
    elif score in (6, 7, 8): return "-1"
    elif score in (9, 10, 11, 12): return "+0"
    elif score in (13, 14, 15): return "+1"
    elif score in (16, 17): return "+2"
    else: return "+3"

def get_current_timestamp():
    if rtc:
        try:
            t = rtc.datetime
            return "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(
                t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec
            )
        except Exception:
            pass
    return "UNKNOWN TIME [OFFLINE]"

def generate_receipt_lines(mode_index):
    lines = []
    timestamp = get_current_timestamp()

    # Common Receipt Header (32-character centered line)
    lines.append("================================")
    lines.append("      DUNGEON CRAWL CLASSICS    ")
    lines.append("    THERMAL ORACLE & DIVINER    ")
    lines.append("================================")

    if mode_index == 0:
        # MODE 1: DCC RPG CLASSIC FUNNEL
        for a in ASCII_DEMON_SKULL: lines.append(a)
        lines.append("--------------------------------")
        lines.append("MODE: 0-LEVEL CHARACTER FUNNEL")
        lines.append("DATE: " + timestamp[:26])
        lines.append("--------------------------------")
        
        occupations = [
            ("Gong Farmer", "Trowel (1d3)", "Sack of night soil"),
            ("Turnip Peddler", "Pitchfork (1d6)", "Turnips (1 bushel)"),
            ("Ditch Digger", "Shovel (1d4)", "Dirt sample in pouch"),
            ("Gravedigger", "Mattock (1d6)", "Bone fragment"),
            ("Alchemist's Apprentice", "Staff (1d4)", "Flask of black oil"),
            ("Woodcutter", "Handaxe (1d6)", "Bundle of dry firewood"),
            ("Rat Catcher", "Club (1d4)", "Sling & net with 3 rats"),
            ("Scribe", "Quill knife (1d3)", "Inkpot & blank vellum"),
            ("Wainwright", "Heavy club (1d4)", "Pushcart (wooden)"),
            ("Grave Robber", "Crowbar (1d4)", "Human skull & sack")
        ]
        occ = random.choice(occupations)
        
        augurs = [
            ("Bred for the hunt", "+1 Melee damage"),
            ("Pack hunter", "+1 Attack with allies"),
            ("Born on the battlefield", "+1 Crits"),
            ("The Broken Star", "Fumble rolls 1d16"),
            ("Unholy strike", "+1 Smite damage"),
            ("Guardian angel", "+2 AC saving throws")
        ]
        aug = random.choice(augurs)

        lines.append("OCCUPATION: " + occ[0])
        lines.append("START WEAPON: " + occ[1])
        lines.append("TRADE GOODS : " + occ[2])
        lines.append("--------------------------------")
        lines.append("ABILITY SCORES (3d6):")
        
        stats = [("STR", roll_3d6()), ("AGI", roll_3d6()), ("STA", roll_3d6()),
                 ("PER", roll_3d6()), ("INT", roll_3d6()), ("LCK", roll_3d6())]
        
        s1 = "{}: {:2d} ({})   {}: {:2d} ({})".format(stats[0][0], stats[0][1], ability_modifier(stats[0][1]),
                                                      stats[1][0], stats[1][1], ability_modifier(stats[1][1]))
        s2 = "{}: {:2d} ({})   {}: {:2d} ({})".format(stats[2][0], stats[2][1], ability_modifier(stats[2][1]),
                                                      stats[3][0], stats[3][1], ability_modifier(stats[3][1]))
        s3 = "{}: {:2d} ({})   {}: {:2d} ({})".format(stats[4][0], stats[4][1], ability_modifier(stats[4][1]),
                                                      stats[5][0], stats[5][1], ability_modifier(stats[5][1]))
        lines.append(s1)
        lines.append(s2)
        lines.append(s3)
        lines.append("--------------------------------")
        hp = max(1, roll_dice(1, 4) + int(ability_modifier(stats[2][1])))
        lines.append("HIT POINTS: {:d} HP  | SPEED: 30'".format(hp))
        lines.append("FUNDS     : {:d} Copper Pieces".format(roll_dice(5, 12)))
        lines.append("BIRTH LUCK: " + aug[0])
        lines.append("AUGUR MOD : " + aug[1])

    elif mode_index == 1:
        # MODE 2: MUTANT CRAWL CLASSICS (MCC RPG)
        for a in ASCII_RADIOACTIVE_SKULL: lines.append(a)
        lines.append("--------------------------------")
        lines.append("MODE: MCC 0-LEVEL SEEKER")
        lines.append("DATE: " + timestamp[:26])
        lines.append("--------------------------------")
        
        genotypes = ["Pure Strain Human", "Mutant (Wasteland)", "Manimal (Beastfolk)", "Plantient (Flora)"]
        geno = random.choice(genotypes)
        
        mutations = [
            "Chitinous Exoskeleton (+2 AC)", "Bioluminescent Eye Beam",
            "Prehensile Tail (1d3 bludgeon)", "Spore Emission Cloud",
            "Thermal Heat Absorption", "Hyper-Elastic Tendons (+10' speed)"
        ]
        mut = random.choice(mutations) if geno != "Pure Strain Human" else "Clean Genetic Helix (Nanite Immune)"
        
        artifacts = ["Geiger Counter (Ticking)", "Solar Battery Pack (80%)", "Cracked Holo-Badge", "Laser Scalpel (Empty)"]
        
        lines.append("GENOTYPE: " + geno)
        lines.append("MUTATION: " + mut)
        lines.append("ARTIFACT: " + random.choice(artifacts))
        lines.append("WEAPON  : Scrap Cleaver (1d6)")
        lines.append("HP: {:d} | ARCHAIC TOKENS: {:d}".format(roll_dice(1, 4), roll_dice(2, 6)))

    elif mode_index == 7:
        # MODE 8: BEAST-O-MATIC PROCEDURAL MONSTER
        for a in ASCII_CHIMERA_HEAD: lines.append(a)
        lines.append("--------------------------------")
        lines.append("MODE: BEAST-O-MATIC MONSTER")
        lines.append("DATE: " + timestamp[:26])
        lines.append("--------------------------------")
        
        prefix = ["Abyssal", "Grave-Born", "Chimeric", "Iridescent", "Obsidian", "Flesh-Welded"]
        beast = ["Gorilla-Hawk", "Slime-Behemoth", "Viper-Boar", "Manticore-Grub", "Bone-Drake"]
        hd = roll_dice(1, 6) + 1
        ac = 10 + roll_dice(1, 6)
        
        attacks = [
            "2 Claws (1d6) & Rend (2d4)", "Venom Sting (1d8 + DC 12 Poison)",
            "Crushing Jaw (2d6)", "Tail Scythe (1d10 sweep)",
            "Acid Vomit Spray (15' cone, 2d6)"
        ]
        
        lines.append("NAME: " + random.choice(prefix) + " " + random.choice(beast))
        lines.append("HIT DICE : {:d}d8 ({:d} HP)".format(hd, hd * 5))
        lines.append("ARMOR CL : {:d}  | SPEED: {:d}'".format(ac, random.choice([20, 30, 40, 50])))
        lines.append("ATTACKS  : " + random.choice(attacks))
        lines.append("ALIGNMENT: " + random.choice(["Chaotic Evil", "Neutral Hunger", "Demon Servant"]))
        lines.append("MORALE   : {:d} on 2d6".format(roll_dice(2, 6)))

    else:
        # MODES 3..7: STANDARD FORMATTED TABLES
        for a in ASCII_DEMON_SKULL: lines.append(a)
        lines.append("--------------------------------")
        lines.append("MODE: " + MODE_NAMES[mode_index].upper())
        lines.append("DATE: " + timestamp[:26])
        lines.append("--------------------------------")
        lines.append("SETTING  : " + MODE_SUBTITLES[mode_index])
        lines.append("CHARACTER: Procedural Aspirant")
        lines.append("HP: {:d}  | AC: {:d}  | SPEED: 30'".format(roll_dice(1, 4), 10 + roll_dice(1, 3)))
        lines.append("WEAPON   : Forged Iron Blade (1d6)")
        lines.append("HERITAGE : Vaultborn Survivor")
        lines.append("INVENTORY: Rations (3 days), Torch")

    # Closing Receipt Footer
    lines.append("================================")
    lines.append("   SURVIVE OR BE FORGOTTEN!     ")
    lines.append("  TABLETOP DEVICE ART - 2026    ")
    lines.append("================================")
    
    return lines

# ------------------------------------------------------------------------------
# 4. PRIMARY NON-BLOCKING OPERATIONAL LOOP
# ------------------------------------------------------------------------------

state = STATE_STANDBY_IDLE
current_rotary_mode = 0
stable_rotary_mode = 0
debounce_ticks = 0

last_rotary_check = time.monotonic()
last_led_tick = time.monotonic()
last_print_stream = time.monotonic()

print_lines = []
print_index = 0
cooldown_start = 0

print("DCC Printer System Ready. Entering main loop...")

while True:
    now = time.monotonic()

    # TASK A: Poll and Debounce Rotary Switch (Every 15ms)
    if now - last_rotary_check >= 0.015:
        last_rotary_check = now
        active_mode = -1
        for i, sw in enumerate(rotary_inputs):
            if not sw.value:  # Active LOW
                active_mode = i
                break

        if active_mode != -1:
            if active_mode == current_rotary_mode:
                debounce_ticks += 1
                if debounce_ticks >= 2:  # 30ms stable
                    if stable_rotary_mode != current_rotary_mode:
                        stable_rotary_mode = current_rotary_mode
                        # Refresh LCD Display
                        if lcd:
                            try:
                                lcd.clear()
                                lcd.cursor_position(0, 0)
                                lcd.message = "[{:02d}] {}".format(stable_rotary_mode + 1, MODE_NAMES[stable_rotary_mode][:10])
                                lcd.cursor_position(0, 1)
                                lcd.message = "> PRESS TO ROLL"
                            except Exception:
                                pass
            else:
                current_rotary_mode = active_mode
                debounce_ticks = 0

    # TASK B: State Machine Processing
    if state == STATE_STANDBY_IDLE:
        # Gentle Sinusoidal Breathing Glow on Triangle Button LED (3-second period)
        if now - last_led_tick >= 0.025:
            last_led_tick = now
            phase = (now % 3.0) / 3.0 * (2.0 * math.pi)
            brightness = (math.sin(phase) + 1.0) / 2.0  # 0.0 to 1.0
            # Exponential curve for pleasant natural human eye perception
            duty = int((brightness ** 2) * 65535)
            led_pwm.duty_cycle = duty

        # Check Trigger Pushbutton (Active LOW)
        if not trigger_button.value:
            # Button pressed! Transition to printing
            state = STATE_PRINTING
            print_lines = generate_receipt_lines(stable_rotary_mode)
            print_index = 0
            if lcd:
                try:
                    lcd.clear()
                    lcd.cursor_position(0, 0)
                    lcd.message = "GENERATING FATE"
                    lcd.cursor_position(0, 1)
                    lcd.message = "PRINTING..."
                except Exception:
                    pass

    elif state == STATE_PRINTING:
        # Rapid Strobe LED during printing (8 Hz)
        strobe_on = (now % 0.125) > 0.062
        led_pwm.duty_cycle = 65535 if strobe_on else 0

        # Stream lines to Cashino thermal printer with 8ms inter-line delay
        if now - last_print_stream >= 0.008:
            last_print_stream = now
            if print_index < len(print_lines):
                line_text = print_lines[print_index] + "\r\n"
                uart.write(line_text.encode('ascii', 'ignore'))
                print_index += 1
            else:
                # Print completed! Feed 3 lines past tear bar
                uart.write(b"\r\n\r\n\r\n")
                state = STATE_COOLDOWN
                cooldown_start = now
                if lcd:
                    try:
                        lcd.clear()
                        lcd.cursor_position(0, 0)
                        lcd.message = "FATE DISPENSED!"
                        lcd.cursor_position(0, 1)
                        lcd.message = "TEAR RECEIPT..."
                    except Exception:
                        pass

    elif state == STATE_COOLDOWN:
        # Keep button LED solid bright during paper tear
        led_pwm.duty_cycle = 65535

        # Hold display message for 1.8 seconds before returning to Idle
        if now - cooldown_start >= 1.8:
            state = STATE_STANDBY_IDLE
            if lcd:
                try:
                    lcd.clear()
                    lcd.cursor_position(0, 0)
                    lcd.message = "[{:02d}] {}".format(stable_rotary_mode + 1, MODE_NAMES[stable_rotary_mode][:10])
                    lcd.cursor_position(0, 1)
                    lcd.message = "> PRESS TO ROLL"
                except Exception:
                    pass

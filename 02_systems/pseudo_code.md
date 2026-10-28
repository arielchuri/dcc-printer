# Firmware Pseudo-Code & Operational Flow

**Course:** PSAM 2230 Device Art (Fall 2026)  
**Deliverable:** Milestone 2 Firmware Pseudo-Code  
**Target Runtime:** CircuitPython 9.x on Raspberry Pi Pico (RP2040)

---

## 1. High-Level System Pseudo-Code

```text
================================================================================
DCC PRINTER PSEUDO-CODE (NON-BLOCKING EVENT-DRIVEN FSM)
================================================================================

GLOBAL CONSTANTS & ENUMS:
  STATE_BOOT_INIT     = 0
  STATE_STANDBY_IDLE  = 1
  STATE_PRINTING      = 2
  STATE_COOLDOWN      = 3

  MODE_NAMES = [
    "DCC RPG Funnel",
    "MCC RPG Seeker",
    "Umerica Survivor",
    "X-Crawl Athlete",
    "Lankhmar Rogue",
    "Empire East Folk",
    "Dying Earth Wayfarer",
    "Beast-o-Matic"
  ]

INITIALIZATION (Run Once at Boot):
  Initialize UART1 on (TX=GP4, RX=GP5) at 9600 Baud
  Initialize I2C0 bus on (SDA=GP0, SCL=GP1) at 100 kHz
  
  Initialize LCD1602 at I2C address 0x27:
    Set columns = 16, rows = 2
    Turn backlight ON
    Display: "DCC PRINTER v1.0", "INITIALIZING..."

  Initialize DS3231 RTC at I2C address 0x68
  
  Initialize Rotary Switch Pins GP6..GP13:
    Configure each as DigitalIn with PULL_UP
    
  Initialize Triangle Pushbutton on GP14:
    Configure as DigitalIn with PULL_UP
    
  Initialize Button LED on GP15:
    Configure as PWMOut with frequency = 1000 Hz, duty_cycle = 0

  Initialize Non-Blocking Timers:
    last_rotary_poll   = time.monotonic()
    last_led_update    = time.monotonic()
    last_print_tick    = time.monotonic()
    active_state       = STATE_STANDBY_IDLE
    current_mode_index = 0
    stable_mode_index  = 0
    debounce_counter   = 0

MAIN LOOP (Runs Continuously):
  current_time = time.monotonic()

  ------------------------------------------------------------------------------
  TASK 1: POLL & DEBOUNCE 8-POSITION ROTARY SWITCH (Every 10ms)
  ------------------------------------------------------------------------------
  If (current_time - last_rotary_poll) >= 0.010 seconds:
    last_rotary_poll = current_time
    raw_detected_mode = -1
    
    For i from 0 to 7:
      If read_pin(GP6 + i) == LOW:
        raw_detected_mode = i
        break
        
    If raw_detected_mode != -1:
      If raw_detected_mode == current_mode_index:
        debounce_counter = debounce_counter + 1
        If debounce_counter >= 3: # 30ms stable reading
          If stable_mode_index != current_mode_index:
            stable_mode_index = current_mode_index
            Trigger Event: ROTARY_MODE_CHANGED(stable_mode_index)
      Else:
        current_mode_index = raw_detected_mode
        debounce_counter = 0

  ------------------------------------------------------------------------------
  TASK 2: STATE MACHINE LOGIC
  ------------------------------------------------------------------------------
  SWITCH (active_state):

    CASE STATE_STANDBY_IDLE:
      # A. Update Triangle Button LED breathing pulse (4-second cycle)
      If (current_time - last_led_update) >= 0.020 seconds:
        last_led_update = current_time
        angle = (current_time % 4.0) / 4.0 * (2 * PI)
        brightness = (sin(angle) + 1.0) / 2.0  # Normalized 0.0 to 1.0
        duty = uint16(brightness * 65535)
        set_pwm_duty(GP15, duty)

      # B. Handle Screen Refresh on Mode Change
      If Event ROTARY_MODE_CHANGED:
        LCD.clear()
        LCD.set_cursor(0, 0)
        LCD.print("MODE [0" + (stable_mode_index + 1) + "]:")
        LCD.set_cursor(0, 1)
        LCD.print(MODE_NAMES[stable_mode_index])

      # C. Poll Triangle Pushbutton (Active LOW)
      If read_pin(GP14) == LOW:
        # User pressed the trigger!
        active_state = STATE_PRINTING
        print_stage = 0
        print_timer = current_time
        LCD.clear()
        LCD.print("ROLLING FATE...")
        LCD.set_cursor(0, 1)
        LCD.print("PRINTING...")

    CASE STATE_PRINTING:
      # A. Fast Strobe LED (10 Hz blink)
      strobe_phase = (current_time % 0.1) > 0.05
      set_pwm_duty(GP15, strobe_phase ? 65535 : 0)

      # B. Execute Table Generation & Thermal Print Stream
      If print_stage == 0:
        # Step 1: Read RTC Timestamp
        now = RTC.get_datetime()
        timestamp_str = format("{YYYY}-{MM}-{DD} {HH}:{MM}:{SS}", now)
        
        # Step 2: Roll Procedural Content based on stable_mode_index
        output_buffer = GenerateProceduralReceipt(stable_mode_index, timestamp_str)
        print_line_index = 0
        print_stage = 1

      Else If print_stage == 1:
        # Step 3: Stream lines to Cashino printer with 5ms inter-line delay
        If (current_time - last_print_tick) >= 0.005 seconds:
          last_print_tick = current_time
          If print_line_index < length(output_buffer):
            line = output_buffer[print_line_index]
            UART.write(line + "\r\n")
            print_line_index = print_line_index + 1
          Else:
            # All lines printed; feed 3 blank lines for paper tear clearance
            UART.write("\r\n\r\n\r\n")
            print_stage = 2
            cooldown_timer = current_time

      Else If print_stage == 2:
        # Step 4: Finish job
        LCD.clear()
        LCD.print("FATE COMPLETE")
        LCD.set_cursor(0, 1)
        LCD.print("TAKE RECEIPT")
        active_state = STATE_COOLDOWN
        cooldown_timer = current_time

    CASE STATE_COOLDOWN:
      # Keep LED steady on during receipt tear
      set_pwm_duty(GP15, 65535)
      
      # Wait 1.5 seconds non-blocking before returning to IDLE
      If (current_time - cooldown_timer) >= 1.5 seconds:
        active_state = STATE_STANDBY_IDLE
        # Restore resting screen
        LCD.clear()
        LCD.print("MODE [0" + (stable_mode_index + 1) + "]:")
        LCD.set_cursor(0, 1)
        LCD.print(MODE_NAMES[stable_mode_index])

================================================================================
END MAIN LOOP
================================================================================
```

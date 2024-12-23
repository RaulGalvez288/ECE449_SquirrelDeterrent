import gpiod
import time

# GPIO setup
CHIP = "gpiochip0"  # GPIO chip name for Raspberry Pi
RELAY_PIN = 27  # GPIO pin for the relay

# Configure GPIO
chip = gpiod.Chip(CHIP)  # Access the GPIO chip
line = chip.get_line(RELAY_PIN)  # Get the specific GPIO line (pin)
line.request(consumer="relay_control", type=gpiod.LINE_REQ_DIR_OUT, default_vals=[1])

try:
    start_time = time.time()  # Record the start time
    print("Floodlight is on")
    while time.time() - start_time < 5:  # Run the loop for 5 seconds
        line.set_value(1)  # Activate relay

except KeyboardInterrupt:
    print("Script stopped by the user")

finally:
    # Ensure the relay is OFF before cleanup
    line.set_value(0)  # Set relay to OFF (HIGH)
    line.release()  # Release the GPIO line
    print("Floodlight is off")

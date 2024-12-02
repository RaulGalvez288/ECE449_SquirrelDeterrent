import gpiod
import time

# GPIO setup
CHIP = "gpiochip0"  # Default GPIO chip for Raspberry Pi 5
RELAY_PIN = 17  # GPIO pin number (Broadcom numbering)

# Configure GPIO
chip = gpiod.Chip(CHIP)  # Access the GPIO chip
line = chip.get_line(RELAY_PIN)  # Get the specific line (pin)
line.request(consumer="relay_control", type=gpiod.LINE_REQ_DIR_OUT, default_vals=[1])  # Request the pin as output, default HIGH (off)

try:
    start_time = time.time()  # Record the start time
    while time.time() - start_time < 10:  # Run the loop for 10 seconds
        # Turn the relay on (active LOW)
        line.set_value(1)  # Activate relay


except KeyboardInterrupt:
    print("Script stopped by the user")

finally:
    line.set_value(0)  # Set relay to OFF (HIGH)
    line.release()  # Release the GPIO line
    print("GPIO cleanup done")

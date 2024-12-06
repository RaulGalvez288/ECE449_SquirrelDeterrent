import gpiod
import time

# GPIO setup
CHIP = "gpiochip0"  # GPIO chip name for Raspberry Pi
PIN1 = 22  # GPIO pin for direction 1
PIN2 = 23  # GPIO pin for direction 2

def init():
    global chip, line1, line2
    chip = gpiod.Chip(CHIP)  # Access the GPIO chip
    line1 = chip.get_line(PIN1)  # Get the GPIO line for PIN1
    line2 = chip.get_line(PIN2)  # Get the GPIO line for PIN2
    # Request the GPIO lines as output, defaulting to LOW
    line1.request(consumer="motor_control", type=gpiod.LINE_REQ_DIR_OUT, default_vals=[0])
    line2.request(consumer="motor_control", type=gpiod.LINE_REQ_DIR_OUT, default_vals=[0])

def forward(sec):
    line1.set_value(1)  # Set PIN1 HIGH
    line2.set_value(0)  # Set PIN2 LOW
    time.sleep(sec)

def reverse(sec):
    line1.set_value(0)  # Set PIN1 LOW
    line2.set_value(1)  # Set PIN2 HIGH
    time.sleep(sec)

def cleanup():
    try:
        # Ensure both GPIO pins are set to LOW
        line1.set_value(0)  # Ensure PIN1 is LOW
        line2.set_value(0)  # Ensure PIN2 is LOW
    except Exception as e:
        print(f"Error during GPIO cleanup: {e}")
    finally:
        # Release GPIO lines
        line1.release()
        line2.release()
        print("GPIO cleanup done")

# Main program
try:
    init()
    seconds = 0.25
    start = time.time()
    while (time.time() - start) < 5:
        print("forward")
        forward(seconds)
        print("reverse")
        reverse(seconds)
        print("forward")
        forward(seconds)
        print("reverse")
        reverse(seconds)

except KeyboardInterrupt:
    print("Program interrupted by user.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    cleanup()

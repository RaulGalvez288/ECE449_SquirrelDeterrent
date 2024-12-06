import time
import gpiod
import subprocess
import signal
import sys
from threading import Thread

# GPIO setup
CHIP = "gpiochip0"  # GPIO chip name for Raspberry Pi 5
PIR_PIN = 2  # GPIO pin connected to the PIR sensor
SWITCH_PIN = 12  # GPIO pin for detecting either GND or 5V

# Access the GPIO chip and configure the PIR sensor and switch line
chip = gpiod.Chip(CHIP)
pir_line = chip.get_line(PIR_PIN)
switch_line = chip.get_line(SWITCH_PIN)

pir_line.request(consumer="pir_sensor", type=gpiod.LINE_REQ_DIR_IN)  # Set PIR as input
switch_line.request(consumer="switch_detector", type=gpiod.LINE_REQ_DIR_IN)  # Set switch pin as an input

# Global flag for the loop
condition = True

def signal_handler(sig, frame):
    """
    Handle termination signals.
    Triggered by:
    - SIGINT: Ctrl+C
    - SIGTERM: System termination commands like kill
    """
    global condition
    print("\nCtrl+C detected. Exiting the program...")
    condition = False  # Stop the loop

# Register the signal handler for Ctrl+C and SIGTERM
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

def run_floodlight():
    print("Activating Floodlight...")
    subprocess.run(["python3", "/home/pi/Desktop/Sensing/Light/Floodlight.py"], check=False)

def capture_image():
    print("Capturing image...")
    subprocess.run(["python3", "/home/pi/Desktop/Sensing/Camera/capture_image.py"], check=False)

def run_all_deterrents():
    print("Running deterrents...")
    subprocess.run(["python3", "/home/pi/Desktop/Sensing/Run_all_deterrents.py"], check=False)

try:
    start = time.time()
    print("Waiting for motion... Press Ctrl+C to quit.")
    while condition:
        print(f"PIR Sensor State: {pir_line.get_value()}")  # Print the PIR GPIO state
        print(f"Switch Pin State: {switch_line.get_value()}")  # Print the input GPIO state

        if pir_state:
            print("Motion detected!")
            # Start Floodlight and capture image concurrently
            floodlight_thread = Thread(target=run_floodlight)
            capture_thread = Thread(target=capture_image)
            
            floodlight_thread.start()
            capture_thread.start()

            floodlight_thread.join()
            capture_thread.join()

            # Check if the switch pin is HIGH (5V) to activate deterrents
            if switch_state:
                time.sleep(1)
                print("Running deterrents.")
                deterrents_thread = Thread(target=run_all_deterrents)
                deterrents_thread.start()
                deterrents_thread.join()

        # Sleep for a short duration to prevent busy-waiting
        time.sleep(0.5)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    pir_line.release()  # Release the PIR sensor line
    switch_line.release()  # Release the input line
    print("GPIO cleanup complete.")

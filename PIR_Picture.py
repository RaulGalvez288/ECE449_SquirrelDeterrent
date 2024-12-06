import time
import gpiod
import subprocess
import signal
import sys
from threading import Thread

# GPIO setup
CHIP = "gpiochip0"  # GPIO chip name for Raspberry Pi 5
PIR_PIN = 2  # GPIO pin connected to the PIR sensor
INPUT_PIN = 12  # GPIO pin for detecting 5V input

# Access GPIO chip and configure the PIR sensor and input line
chip = gpiod.Chip(CHIP)
pir_line = chip.get_line(PIR_PIN)
input_line = chip.get_line(INPUT_PIN)

pir_line.request(consumer="pir_sensor", type=gpiod.LINE_REQ_DIR_IN)  # Set PIR as input
input_line.request(consumer="input_detector", type=gpiod.LINE_REQ_DIR_IN)  # Set input pin as input

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
    """
    Run the Floodlight.py script.
    """
    print("Activating Floodlight...")
    subprocess.run(["python3", "/home/pi/Desktop/Sensing/Light/Floodlight.py"], check=False)

def capture_image():
    """
    Run the capture_image.py script.
    """
    print("Capturing image...")
    subprocess.run(["python3", "/home/pi/Desktop/Sensing/Camera/capture_image.py"], check=False)

def run_all_deterrents():
    """
    Run the Run_all_deterrents.py script.
    """
    print("Running all deterrents...")
    subprocess.run(["python3", "/home/pi/Desktop/Sensing/Run_all_deterrents.py"], check=False)

try:
    start = time.time()
    print("Waiting for motion... Press Ctrl+C to quit.")
    for i in range(1):
        print(i)
        pir_state = pir_line.get_value()  # Read the PIR sensor state
        input_state = input_line.get_value()  # Read the input pin state

        print(f"PIR Sensor State: {pir_state}")  # Print the PIR GPIO state
        print(f"Input Pin State: {input_state}")  # Print the input GPIO state

        if pir_state:
            print("Motion detected!")

            # Start Floodlight and capture image concurrently
            floodlight_thread = Thread(target=run_floodlight)
            capture_thread = Thread(target=capture_image)
            
            floodlight_thread.start()
            capture_thread.start()

            floodlight_thread.join()
            capture_thread.join()

            # Check if input pin is HIGH (5V) to activate deterrents
            time.sleep(2)
            print("Input pin is HIGH. Running deterrents.")
            deterrents_thread = Thread(target=run_all_deterrents)
            deterrents_thread.start()
            deterrents_thread.join()

        # Sleep for a short duration to prevent busy-waiting
        time.sleep(2)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    pir_line.release()  # Release the PIR sensor line
    input_line.release()  # Release the input line
    print("GPIO cleanup complete.")

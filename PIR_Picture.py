import time
import RPi.GPIO as GPIO
import subprocess
import signal
import sys

# Setup the PIR sensor
PIR_PIN = 2  # Adjust to the GPIO pin connected to your PIR sensor
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

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

# Register the signal handler for Ctrl+C
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

try:
    print("Waiting for motion... Press Ctrl+C to quit.")
    while condition:
        pir_state = GPIO.input(PIR_PIN)
        print(f"PIR Sensor State: {pir_state}")  # Print the raw GPIO state
        
        if pir_state:
            print("Motion detected!")

            # Call the image capturing scripts
            # Adding 'check=False' prevents exceptions from stopping the program if the script fails
            subprocess.run(["python3", "/home/pi/Desktop/Sensing/Light/Floodlight.py"], check=False)
            subprocess.run(["python3", "/home/pi/Desktop/Sensing/Camera/capture_image.py"], check=False)

        # Small sleep to avoid busy-waiting; replace with event-based logic if possible
        for _ in range(5):  # Break the delay into smaller chunks
            if not condition:  # Check the `condition` flag during the delay
                break
            time.sleep(0.1)  # Sleep in 0.1-second increments

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    GPIO.cleanup()  # Clean up GPIO on exit
    print("GPIO cleanup complete.")

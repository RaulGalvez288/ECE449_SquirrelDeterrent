import time
import RPi.GPIO as GPIO
import subprocess

# Setup the PIR sensor
PIR_PIN = 2  # Change this to the GPIO pin you connected to the OUT pin of the PIR sensor
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

try:
    print("Waiting for motion...")
    while True:
        print(f"PIR Sensor State: {GPIO.input(PIR_PIN)}")  # Print the raw GPIO state
        if GPIO.input(PIR_PIN):
            print("Motion detected!")

            # Call the image capturing script
            subprocess.run(["python3", "/home/pi/Desktop/Sensing/Light/Floodlight.py"])
            subprocess.run(["python3", "/home/pi/Desktop/Sensing/yolov7/run_detection.py"])  # Change to the correct path
            # subprocess.run(["python3", "/home/pi/Desktop/Sensing/Run_all_deterrents.py"])  # Change to the correct path

            # Wait a few seconds to avoid capturing multiple images for the same motion
            time.sleep(5)  # Adjust the delay as needed

except KeyboardInterrupt:
    print("Program stopped by User")

finally:
    GPIO.cleanup()  # Clean up GPIO on normal exit

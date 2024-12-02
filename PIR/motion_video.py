import time
import RPi.GPIO as GPIO
import subprocess

# Setup the PIR sensor
PIR_PIN = 4  # Change this to the GPIO pin you connected to the OUT pin of the PIR sensor
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

try:
    print("Waiting for motion...")
    while True:
        if GPIO.input(PIR_PIN):
            print("Motion detected!")
            # Call the video recording script
            subprocess.run(["python3", "/home/pi/Desktop/Sensing/Camera/capture_video.py"])  # Change to the correct path

            # Wait a few seconds to avoid multiple triggers for the same motion
            time.sleep(5)  # Adjust the delay as needed

except KeyboardInterrupt:
    print("Program stopped by User")

finally:
    GPIO.cleanup()  # Clean up GPIO on normal exit

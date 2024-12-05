import time
import subprocess

# Setup the PIR sensor
try:
    print("Waiting for motion...")
    while True:
        print("Motion detected!")

        # Call the image capturing script
        subprocess.run(["python3", "/home/pi/Desktop/Sensing/Light/Floodlight.py"])
        subprocess.run(["python3", "/home/pi/Desktop/Sensing/Camera/capture_image.py"], check=False)
        # subprocess.run(["python3", "/home/pi/Desktop/Sensing/Run_all_deterrents.py"])  # Change to the correct path

        # Wait a few seconds to avoid capturing multiple images for the same motion
        time.sleep(5)  # Adjust the delay as needed

except KeyboardInterrupt:
    print("Program stopped by User")

finally:
    GPIO.cleanup()  # Clean up GPIO on normal exit

import os
import cv2
from datetime import datetime
import subprocess
import time

# Number of photos to capture
num_photos = 1

# Define directory path template
base_directory = "/home/pi/Desktop/Sensing/Detection"

# Initialize the webcam
cap = cv2.VideoCapture(0)

for i in range(num_photos):
    # Capture the image
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture image")
        continue

    # Generate date and time strings
    current_time = datetime.now()
    date_str = current_time.strftime("%m_%d_%y")  # e.g., '10_28_24' for October 28, 2024
    time_str = current_time.strftime("%H_%M_%S")  # e.g., '15_30_00' for 3:30:00 PM

    # Create directory for today's date if it doesn't exist
    date_directory = os.path.join(base_directory, date_str)
    os.makedirs(date_directory, exist_ok=True)

    # Define the path for the photo
    photo_path = os.path.join(date_directory, f"{time_str}.png")

    # Save the captured image
    cv2.imwrite(photo_path, frame)
    print(f"Image {i+1} captured and saved as {photo_path}")

    # Wait a short period before taking the next photo
    time.sleep(1)

# Release the webcam
cap.release()
cv2.destroyAllWindows()

# Run detect.py on the captured images
print("Running detect.py on captured images...")
subprocess.run(["python3", "detect.py", "--source", date_directory])

print("Detection complete.")

import os
from datetime import datetime
import cv2

# Initialize the webcam (0 is usually the built-in camera; use 1 if an external webcam)
cap = cv2.VideoCapture(0)

# Check if the webcam opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
else:
    # Generate the current date strings
    current_time = datetime.now()

    # Day in MMDDYY format
    day_str = current_time.strftime("%m_%d_%y")  # e.g., '101723' for October 17, 2023

    # Time in HHMMSS format
    time_str = current_time.strftime("%H_%M_%S")  # e.g., '113533' for 11:35:33

    # Create a directory based on the day the photo was taken
    directory_path = os.path.expanduser(f"/home/pi/Desktop/Sensing/Detection/{day_str}")
    os.makedirs(directory_path, exist_ok=True)  # Create the directory if it doesn't exist

    # File path with the time the photo was taken
    file_path = os.path.join(directory_path, f"{time_str}.png")

    # Capture an image from the webcam
    ret, frame = cap.read()
    if ret:
        # Save the captured image to the specified file path
        cv2.imwrite(file_path, frame)
        print(f"Image captured and saved as {file_path}")
    else:
        print("Error: Could not capture image.")

    # Release the webcam
    cap.release()

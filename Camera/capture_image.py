import os
from datetime import datetime
import cv2  # OpenCV for capturing images
import time

start_time = time.time()

# Set the parameters
weights = '/home/pi/Desktop/Sensing/yolov7/yolov7-tiny.pt'
timestamp = datetime.now().strftime('%m_%d_%Y')
output_dir = f'/home/pi/Desktop/Sensing/Detection/images/{timestamp}'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Function to capture an image using OpenCV (for USB cameras or Raspberry Pi Camera Module with OpenCV)
def capture_image():
    source_image = os.path.join(output_dir, f'{datetime.now().strftime("%H_%M_%S")}.jpg')
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        exit()

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Adjust the resolution
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    ret, frame = cap.read()

    if ret:
        cv2.imwrite(source_image, frame)
        print(f"Image saved as {source_image}")
    else:
        print("Error: Failed to capture image.")

    cap.release()
    return source_image
capture_image()
print("Captured an image")
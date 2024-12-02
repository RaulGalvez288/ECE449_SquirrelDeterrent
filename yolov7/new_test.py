import cv2
import numpy as np
import RPi.GPIO as GPIO
import time
from datetime import datetime

# Set up GPIO for deterrents
DETERRENT_PIN = 18  # Adjust the GPIO pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(DETERRENT_PIN, GPIO.OUT)

# Load YOLO model (update paths to your YOLOv7 model weights and config)
weights_path = "yolov7-tiny.weights"
config_path = "yolov7-tiny.cfg"
class_names_path = "coco.names"

# Load class names
with open(class_names_path, "r") as f:
    class_names = [line.strip() for line in f.readlines()]

# Load the network
net = cv2.dnn.readNet(weights_path, config_path)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

# Initialize the camera
camera = cv2.VideoCapture(0)  # Use 0 for Pi Camera Module or USB webcam
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Log file setup
log_file = "squirrel_detection_log.txt"

def trigger_deterrent():
    GPIO.output(DETERRENT_PIN, GPIO.HIGH)
    time.sleep(1)  # Keep deterrent active for 1 second
    GPIO.output(DETERRENT_PIN, GPIO.LOW)

def detect_objects(frame):
    # Prepare the image for YOLO
    blob = cv2.dnn.blobFromImage(frame, 1/255, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    layer_names = net.getUnconnectedOutLayersNames()
    detections = net.forward(layer_names)

    squirrel_detected = False

    # Process detections
    for detection in detections:
        for obj in detection:
            scores = obj[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > 0.5 and class_names[class_id] == "squirrel":  # Replace with correct label
                squirrel_detected = True

    return squirrel_detected

def log_detection():
    # Log the detection timestamp to the file
    with open(log_file, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"Squirrel detected at {timestamp}\n")

try:
    print("Starting detection...")
    while True:
        ret, frame = camera.read()
        if not ret:
            print("Failed to capture frame.")
            break

        # Detect objects
        if detect_objects(frame):
            print(f"Squirrel detected at {datetime.now()}")
            log_detection()  # Log the detection
            trigger_deterrent()
        else:
            print("No squirrel detected.")

except KeyboardInterrupt:
    print("Exiting...")
finally:
    camera.release()
    GPIO.cleanup()

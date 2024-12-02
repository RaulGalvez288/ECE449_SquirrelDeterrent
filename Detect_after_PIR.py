import os
import time
from datetime import datetime
import subprocess
import cv2

# Define directories and paths
output_dir = '/home/pi/Desktop/Sensing/Detection/images'
timestamp = datetime.now().strftime('%Y_%m_%d')
detection_dir = os.path.join(output_dir, timestamp)
yolov7_script = '/home/pi/Desktop/Sensing/yolov7/detect.py'  # Replace with the actual path to detect.py
yolov7_weights = '/home/pi/Desktop/Sensing/yolov7-tiny.pt'  # Replace with your YOLOv7 weights file
yolov7_data = '/home/pi/Desktop/Sensing/yolov7/data/coco.yaml'  # Replace with the YOLOv7 data configuration file
yolov7_img_size = 640  # YOLOv7 image size (e.g., 640)
secondary_script = '/home/pi/Desktop/Sensing/Run_all_deterrents.py'  # Path to secondary script

# Ensure the detection directory exists
os.makedirs(detection_dir, exist_ok=True)

def capture_image():
    """Captures an image using the USB camera and saves it to the detection directory."""
    cap = cv2.VideoCapture(0)  # Use the USB camera (usually ID 0)
    if not cap.isOpened():
        print("Error: Cannot access the camera.")
        return None
    
    ret, frame = cap.read()
    if ret:
        image_path = os.path.join(detection_dir, f"{datetime.now().strftime('%H%M%S')}.jpg")
        cv2.imwrite(image_path, frame)
        cap.release()
        return image_path
    else:
        print("Error: Failed to capture an image.")
        cap.release()
        return None

def run_yolov7(image_path):
    """Runs YOLOv7 detection on the given image."""
    output_path = os.path.join(detection_dir, 'yolov7_output')
    os.makedirs(output_path, exist_ok=True)
    
    command = [
        'python', yolov7_script,
        '--weights', yolov7_weights,
        '--conf', '0.25',
        '--img-size', str(yolov7_img_size),
        '--source', image_path,
        '--project', output_path,
        '--name', 'results',
        '--save-txt',
        '--exist-ok'
    ]
    subprocess.run(command)

def check_for_non_person_objects(txt_file):
    """Checks if 'person' label is absent in the detection results."""
    has_person = False
    with open(txt_file, 'r') as f:
        for line in f:
            label = line.strip().split()[0]  # Assuming label is the first item in each line
            if label == 'person':
                has_person = True
                break
    return not has_person

def process_detection_results():
    """Processes the YOLOv7 results to check for the presence of 'person'."""
    results_dir = os.path.join(detection_dir, 'yolov7_output', 'results', 'labels')
    if not os.path.exists(results_dir):
        print("No detection results found.")
        return

    for txt_file in os.listdir(results_dir):
        txt_file_path = os.path.join(results_dir, txt_file)
        if check_for_non_person_objects(txt_file_path):
            print("No 'person' detected. Running the secondary script...")
            subprocess.run(['python', secondary_script])

def main():
    """Main loop to capture, analyze, and respond."""
    while True:
        # Capture an image
        image_path = capture_image()
        if image_path:
            print(f"Captured image: {image_path}")
            
            # Run YOLOv7 detection
            run_yolov7(image_path)
            
            # Process detection results
            process_detection_results()
        
        # Wait for a few seconds before capturing the next image
        time.sleep(5)

if __name__ == "__main__":
    main()

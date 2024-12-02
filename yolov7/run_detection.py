import subprocess
import os
from datetime import datetime
import cv2  # OpenCV for capturing images
import time

start_time = time.time()

# Set the parameters
weights = '/home/pi/Desktop/Sensing/yolov7/yolov7-tiny.pt'
timestamp = datetime.now().strftime('%Y_%m_%d')
output_dir = f'/home/pi/Desktop/Sensing/Detection/images/{timestamp}'

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Function to capture an image using OpenCV (for USB cameras or Raspberry Pi Camera Module with OpenCV)
def capture_image():
    source_image = os.path.join(output_dir, f'{datetime.now().strftime("%H_%M_%S")}_captured.jpg')
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

# Function to run detection
def run_detection(source_image):
    # Get the current timestamp for naming the output file
    timestamp = datetime.now().strftime('%H_%M_%S')
    txt_file_path = os.path.join(output_dir, f'{timestamp}.txt')
    
    print(f"Running detection... Output: {txt_file_path}")
    
    # Reduce image size for faster processing
    command = [
        'python', 'detect.py',
        '--weights', weights,
        '--source', source_image,
        '--img-size', '416',  # Smaller image size for faster detection
        '--conf-thres', '0.2',
        '--device', 'cpu',  # Change to '0' if using GPU
        '--save-txt',
        '--save-conf',
        '--project', output_dir,  # Specify the project directory to save results
        '--name', f'{timestamp}',  # Specify the output name
    ]
    
    # Run the command
    subprocess.run(command)

# Capture a new image and save it to the current timestamped directory
source_image = capture_image()

mid_time = time.time()

# Run detection on the newly captured image
run_detection(source_image)

# Define animal labels
animal_labels = ["cat", "dog", "horse", "sheep", "cow", "bird", "elephant"]  # Add more animals as needed

# Parse the output text file to collect confidence scores and check for animals
txt_file = os.path.join(output_dir, f'{datetime.now().strftime("%H_%M_%S")}_1.txt')  # Use the same timestamp for the output file
confidence_scores = {}
animal_detected = False

if os.path.exists(txt_file):
    with open(txt_file, 'r') as f:
        for line in f:
            parts = line.strip().split()
            label = parts[0]
            conf = float(parts[1])  # Adjust this index based on your file structure
            if label not in confidence_scores:
                confidence_scores[label] = []
            confidence_scores[label].append(conf)

            # Check if the label is an animal and set the flag to True
            if label in animal_labels:
                animal_detected = True

# Calculate and print the average confidence for each label
stop_time = time.time()
print("MIDDLE TIME", mid_time - start_time)
print("FINAL TIME:", stop_time - start_time)
for label, scores in confidence_scores.items():
    avg_confidence = sum(scores) / len(scores) if scores else 0
    print(f"Average confidence for '{label}': {avg_confidence:.2f}")

# If an animal was detected, run the secondary script
if animal_detected:
    print("Animal detected! Running secondary script...")
    subprocess.run(["python", "/home/pi/Desktop/Sensing/Run_all_deterrents.py"])  # Replace with your secondary script
else:
    print("No animal detected.")

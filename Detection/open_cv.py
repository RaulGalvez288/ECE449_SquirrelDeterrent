import cv2
import RPi.GPIO as GPIO
import time
import os
import subprocess  # To run a secondary script

# PIR Sensor Setup
PIR_PIN = 17  # Replace with the GPIO pin you connected the PIR sensor to

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

# Load class names and model files
classNames = []
classFile = "/home/pi/Desktop/Object_Detection_Files/coco.names"
with open(classFile, "rt") as f:
    classNames = f.read().rstrip("\n").split("\n")

configPath = "/home/pi/Desktop/Object_Detection_Files/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
weightsPath = "/home/pi/Desktop/Object_Detection_Files/frozen_inference_graph.pb"

# Setup OpenCV DNN model
net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

# Object detection function
def getObjects(img, thres, nms, draw=True, objects=[]):
    classIds, confs, bbox = net.detect(img, confThreshold=thres, nmsThreshold=nms)
    if len(objects) == 0: objects = classNames
    objectInfo = []
    if len(classIds) != 0:
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
            className = classNames[classId - 1]
            if className in objects:
                objectInfo.append([box, className])
                if draw:
                    cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
                    cv2.putText(img, className.upper(), (box[0], box[1] - 10), 
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                    cv2.putText(img, f"{round(confidence * 100, 2)}%", 
                                (box[0], box[1] + 30), 
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
    return img, objectInfo

# Main logic
if __name__ == "__main__":
    cap = cv2.VideoCapture(0)  # Use the USB camera
    cap.set(3, 640)  # Width
    cap.set(4, 480)  # Height

    try:
        while True:
            if GPIO.input(PIR_PIN):  # Motion detected
                print("Motion detected!")
                success, img = cap.read()
                if success:
                    # Save the captured image
                    timestamp = time.strftime("%Y%m%d-%H%M%S")
                    day = time.strfttime("%m_%d_Y")
                    if not os.path.exists("/home/pi/Desktop/Sensing/Detection/images/{day}"):
                        os.makedirs("/home/pi/Desktop/Sensing/Detection/images/{day}")
                    imagePath = f"/home/pi/Desktop/Sensing/Dectection/images/{day}/{timestamp}.jpg"
                    cv2.imwrite(imagePath, img)

                    # Run object detection
                    result, objectInfo = getObjects(img, 0.45, 0.2)
                    print(objectInfo)  # Debugging purposes

                    # Check for "person"
                    person_detected = any(obj[1] == "person" for obj in objectInfo)
                    if not person_detected:
                        print("No person detected. Running secondary script...")
                        # Replace the below line with the path to your secondary script
                        subprocess.run(["python3", "/home/pi/Desktop/secondary_script.py"])
                    else:
                        print("Person detected. Skipping secondary script.")

                    # Show the detection result
                    cv2.imshow("Detection Output", img)
                    cv2.waitKey(1)

                # Small delay to prevent multiple triggers
                time.sleep(2)
    except KeyboardInterrupt:
        print("Exiting program...")
    finally:
        GPIO.cleanup()
        cap.release()
        cv2.destroyAllWindows()

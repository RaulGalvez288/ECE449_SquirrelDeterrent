import cv2

# Open the camera
cap = cv2.VideoCapture(0)  # '0' is usually the default USB camera

if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

# Capture a frame
ret, frame = cap.read()

if ret:
    # Save the image
    cv2.imwrite("photo.jpg", frame)
    print("Photo saved as photo.jpg")
else:
    print("Error: Could not capture an image.")

# Release the camera
cap.release()

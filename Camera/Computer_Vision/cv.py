import cv2

# Set the video source to your USB camera (usually /dev/video0)
video_source = 0  # Change this if you have multiple cameras

# Initialize video capture
cap = cv2.VideoCapture(video_source)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Display the frame
    cv2.imshow('Webcam', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close windows
cap.release()
cv2.destroyAllWindows()

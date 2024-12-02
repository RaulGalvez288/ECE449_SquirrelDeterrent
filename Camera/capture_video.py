import os
from datetime import datetime
from picamera2 import Picamera2
import time
from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput

def record_video(duration=3):
    # Initialize the camera
    picam2 = Picamera2()
    picam2.configure(picam2.create_video_configuration())
    picam2.start()

    # Generate the current date strings
    current_time = datetime.now()
    
    #Set up encoder and output
    encoder = H264Encoder(10000000)
    
    # Date in MMDDYY format
    date_str = current_time.strftime("%m_%d_%y")  # e.g., '101723' for October 17, 2023

    # Create a directory for today's date if it doesn't exist
    directory_path = os.path.expanduser(f"/home/pi/Desktop/Sensing/Camera/videos/{date_str}")
    os.makedirs(directory_path, exist_ok=True)

    # Time in HHMMSS format
    time_str = current_time.strftime("%H_%M_%S")  # Change ':' to '_' to avoid file name issues

    # Create the file path with date and time
    file_path = os.path.join(directory_path, f"{time_str}.h264")

    # Start recording video
    print(f"Recording video for {duration} seconds...")
    picam2.start_recording(encoder, output=file_path)

    time.sleep(duration)  # Record for the specified duration

    # Stop recording
    picam2.stop_recording()
    picam2.stop()

    print(f"Video recorded and saved as {file_path}")

if __name__ == "__main__":
    record_video()

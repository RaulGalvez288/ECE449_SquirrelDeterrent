import pygame
import time
import os

# Initialize Pygame mixer
pygame.mixer.init()
pygame.mixer.music.set_volume(1)
# Function to play audio
def play_audio(file_path):
    if os.path.isfile(file_path):
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        print(f"Playing: {file_path}")
        
        # Keep the script running while the audio is playing
        while pygame.mixer.music.get_busy():
            time.sleep(1)
    else:
        print(f"File not found: {file_path}")

# Specify the directory containing your audio files
audio_directory = "/home/pi/Desktop/Sensing/Sound/audios"

# Loop through all audio files in the directory
for filename in os.listdir(audio_directory):
    start_time = time.time()  # Record the start time
    while time.time() - start_time < 1:  # Run the loop for 4 seconds
        if filename.endswith(('.mp3', '.wav', '.ogg')):  # Add more extensions if needed
            file_path = os.path.join(audio_directory, filename)
            play_audio(file_path)

print("All audio files have been played.")

import pygame
import os
import random
import signal
import sys

# This sets the volume of the speakers based on a percentage
os.system("amixer set 'Master' 100%")

# Initialize Pygame mixer
pygame.mixer.init()

# Define a flag to control playback
stop_playback = False

# Signal handler to stop playback when Ctrl+C is pressed
def stop_signal_handler(sig, frame):
    global stop_playback
    print("\nPlayback stopped by user.")
    stop_playback = True
    pygame.mixer.music.stop()
    sys.exit(0)

# Register the signal handler for Ctrl+C (SIGINT)
signal.signal(signal.SIGINT, stop_signal_handler)

def play_audio_files_once(directory):
    try:
        # Get the list of audio files in the directory
        audio_files = [f for f in os.listdir(directory) if f.endswith(('.mp3', '.wav', '.ogg'))]

        # Shuffles the order that the files are played
        random.shuffle(audio_files)

        # Iterates through the files
        for audio_file in audio_files:
            file_path = os.path.join(directory, audio_file)
            try:
                pygame.mixer.music.load(file_path)
                pygame.mixer.music.play()
                print(f"Playing: {audio_file}")
                while pygame.mixer.music.get_busy():
                    pygame.time.wait(100)
                    
            except pygame.error as e:
                print(f"Error playing {audio_file}: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Play all audio files once
play_audio_files_once("/home/pi/Desktop/Sensing/Sound/audios")

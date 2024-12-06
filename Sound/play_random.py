import pygame
import os
import random
import signal
import sys

# Set the audio volume using amixer
os.system("amixer set 'Master' 100%")

# Initialize Pygame mixer
pygame.mixer.init()

# Define a flag to control playback
stop_playback = False

# Signal handler to stop playback when Ctrl+E is pressed
def stop_signal_handler(sig, frame):
    global stop_playback
    print("\nPlayback stopped by user.")
    stop_playback = True
    pygame.mixer.music.stop()
    sys.exit(0)

# Register the signal handler for Ctrl+C (SIGINT) and Ctrl+E (SIGINT)
signal.signal(signal.SIGINT, stop_signal_handler)

def play_audio_files(directory):
    global stop_playback
    try:
        # Get the list of audio files in the directory
        audio_files = [f for f in os.listdir(directory) if f.endswith(('.mp3', '.wav', '.ogg'))]
        
        if not audio_files:
            print("No audio files found in the directory.")
            return

        # Play all audio files sequentially
        for audio_file in audio_files:
            if stop_playback:
                return  # Exit the function if Ctrl+E was pressed
            
            file_path = os.path.join(directory, audio_file)
            try:
                pygame.mixer.music.load(file_path)
                pygame.mixer.music.play()
                print(f"Playing: {audio_file}")

                while pygame.mixer.music.get_busy():
                    if stop_playback:
                        return  # Exit if Ctrl+E was pressed
                    pygame.time.wait(100)
            except pygame.error as e:
                print(f"Error playing {audio_file}: {e}")
        
        # Play a random audio file after all have been played, if not interrupted
        if not stop_playback:
            random_file = random.choice(audio_files)
            file_path = os.path.join(directory, random_file)
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            print(f"Playing a random audio: {random_file}")

            while pygame.mixer.music.get_busy():
                if stop_playback:
                    return  # Exit if Ctrl+E was pressed
                pygame.time.wait(100)

    except Exception as e:
        print(f"An error occurred: {e}")

# Define the directory containing audio files
audio_directory = "/home/pi/Desktop/Sensing/Sound/audios"

# Play all audio files and then a random one
play_audio_files(audio_directory)

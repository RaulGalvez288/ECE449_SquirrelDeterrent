import subprocess
import time

def run_scripts():
    # Run all scripts simultaneously
    processes = []
    
    # Start test.py in the ./Light directory
    # processes.append(subprocess.Popen(["python3", "/home/pi/Desktop/Sensing/Light/Floodlight.py"]))
    # process.append(subprocess.Popen(["python3", "/home/pi/Desktop/Sensing/Camera/capture_image.py"]))
    # time.sleep(3)
    processes.append(subprocess.Popen(["python3", "/home/pi/Desktop/Sensing/Light/Deterrent.py"]))
    
    # Start play_random.py in the ./Sound directory
    processes.append(subprocess.Popen(["python3", "/home/pi/Desktop/Sensing/Sound/play_random.py"]))
    
    # Start test.py in the ./Motion directory
    processes.append(subprocess.Popen(["python3", "/home/pi/Desktop/Sensing/Motion/test.py"]))
    
    # Wait for all processes to complete
    for process in processes:
        process.wait()

if __name__ == "__main__":
    run_scripts()

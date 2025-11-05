import os
import time
from playsound import playsound

def alarm(seconds):
    time_elapsed = 0
    while time_elapsed < seconds:
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60
        print(f"\r{minutes_left:02d}:{seconds_left:02d}", end="")
        time.sleep(1)
        time_elapsed += 1

    print("\nTime’s up!")

    sound_path = os.path.join(os.path.dirname(__file__), "Alarm.mp3")
    print("Playing:", sound_path)

    try:
        playsound(sound_path)
    except Exception as e:
        print("Error playing sound:", e)

alarm(5)

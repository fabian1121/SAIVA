import pyautogui
from SpeakFunction import speak
from ListenFunction import *

def volume():
    speak("Do you want to increase or decrease the volume or mute?")
    command = TakeCommand().lower()
    if 'increase' in command:
        pyautogui.press("volumeup")
    elif 'decrease' in command:
        pyautogui.press("volumedown")
    elif 'mute' in command:
        pyautogui.press('volumemute')
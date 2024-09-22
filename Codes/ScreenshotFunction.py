import pyautogui
from ListenFunction import *
from SpeakFunction import speak

def screenshot():
    img = pyautogui.screenshot()
    speak("What should I name it?")
    filename = TakeCommand().lower()
    img.save("C:/Users/Fabian/OneDrive/Desktop/project/"+filename+".png")
    speak("Screenshot taken")
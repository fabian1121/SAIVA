import datetime
from SpeakFunction import speak

def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The time is")
    speak(Time)
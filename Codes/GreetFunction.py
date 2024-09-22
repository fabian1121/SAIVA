import datetime
from SpeakFunction import speak

user = "Fabian"

def greeting():
    hour = datetime.datetime.now().hour
    if hour>=3 and hour<12:
        speak("Good Morning "+user)
    elif hour>=12 and hour<18:
        speak("Good Afternoon "+user)
    else:
        speak("Good Evening "+user)
    speak("Welcome back, SAIVA at your Service")
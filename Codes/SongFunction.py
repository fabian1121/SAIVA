import pywhatkit
from SpeakFunction import speak
from ListenFunction import TakeCommand

def song():
    speak("Please tell me the name of the song you want to me to play?")
    command = TakeCommand()
    pywhatkit.playonyt(command)

song()
#evanescence
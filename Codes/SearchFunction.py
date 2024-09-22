import webbrowser as wb
from SpeakFunction import speak
from ListenFunction import *

def youtube():
    speak("What do you want me to search?")
    search = TakeCommand().lower()
    speak("Opening Youtube")
    wb.open('https://www.youtube.com/results?search_query='+search)

def google():
    speak("What do you want me to search?")
    search = TakeCommand().lower()
    speak("Opening Google")
    wb.open('https://www.google.com/search?q='+search)

def y1():
    speak("Opening Youtube")
    wb.open('https://www.youtube.com')

def g1():
    speak("Opening Google")
    wb.open('https://www.google.com')


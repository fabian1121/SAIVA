import wikipedia
from SpeakFunction import speak

def wiki(text):
    speak("Searching...")
    query = text.replace('wikipedia','')
    result = wikipedia.summary(query,sentences=3)
    speak("According to Wikipedia")
    #print(result)
    speak(result)
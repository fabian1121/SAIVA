import pyttsx3

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 175)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
#print(voices)

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

#message = "hi, my name is Johann, nice to meet you"
#message = "Fabian Gomes"
#speak(message)


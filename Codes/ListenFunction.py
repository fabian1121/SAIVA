import speech_recognition as sr
from SpeakFunction import speak

def TakeCommand():
    r = sr.Recognizer()
    m = sr.Microphone()
    with m:
        speak("Listening....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(m, duration=0.2)
        audio = r.listen(m)

    try:
        speak("Recognizing....")
        query = r.recognize_google(audio, language= 'en-US')
        #print(query)
        speak(query)
    
    except sr.UnknownValueError as e:
        print(e)
        speak("Please Repeat")
        return "None"
    return query
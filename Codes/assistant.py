import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb

engine = pyttsx3.init()
user = "Johann"


def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()
#speak("hello world")

def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The time is")
    speak(Time)
#time()

def date():
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    speak("Today's date is "+day+" "+month+" "+year)
    #speak(day)
    #speak(month)
    #speak(year)
#date()

def greeting():
    #speak(user)
    hour = datetime.datetime.now().hour
    print(hour)
    if hour>=3 and hour<12:
        speak("Good Morning "+ user)
    elif hour>=12 and hour<18:
        speak("Good Afternoon "+user)
    else:
        speak("Good Evening "+ user)
    speak("Welcome back")
#greeting()

def TakeCommand():
    r = sr.Recognizer()
    m = sr.Microphone()
    with m:
        speak("Listening....")
        r.pause_threshold = 1
        audio = r.listen(m)

    try:
        speak("Recognizing....")
        query = r.recognize_google(audio, language='en-US')
        #print(query)
        speak(query)
    
    except sr.UnknownValueError as e:
        print(e)
        speak("Please Repeat")
        return "None"
    return query
#TakeCommand()

def wiki(text):
    speak("Searching...")
    query = text.replace('wikipedia','')
    result = wikipedia.summary(query,sentences=3)
    speak("According to Wikipedia")
    #print(result)
    speak(result)

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    server.login('johannjose295@gmail.com', 'darling295')
    server.sendmail('johannjose295@gmail.com', to, content)
    server.close()

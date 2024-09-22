from GreetFunction import *
from ListenFunction import *
from TimeFunction import *
from DateFunction import *
from WikipediaFunction import *
from EmailFunction import *
from SpeakFunction import speak
from SearchFunction import *
from BatteryAndCPUFunction import *
from JokeFunction import *
from ScreenshotFunction import *
from NewsFunction import *
from WeatherFunction import *
from BrightnessFunction import *
from VolumeFunction import *


def get_audio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
		said = ""

		try:
		    said = r.recognize_google(audio)
		    
		except Exception as e:
		    print("Exception: " + str(e))

	return said


def wake():
    Wake = "hello"

    text = get_audio()

    #while True:
    #    text = get_audio()
    #    print(text)

    if text.count(Wake)>0:
            driver()

def cont():
    while True:
        wake()

def driver():
        greeting()

        while True:
                query = TakeCommand().lower()
                        
                if 'time' in query:
                    time()
                        
                if 'date' in query:
                    date()

                if 'goodbye' in query:
                    speak("Signing out")
                    cont()
                        
                if 'wikipedia' in query:
                    wiki(query)

                if 'email' in query:
                    emailOptions()

                if 'search on youtube' in query:
                    youtube()
                        
                if 'search on google' in query:
                    google()

                if 'cpu' in query:
                    cpu()

                if 'battery' in query:
                    battery()

                if 'joke' in query:
                    jokes()

                if 'screenshot' in query:
                    screenshot()

                if 'weather' in query:
                    weather()
                        
                if 'news' in query:
                    news()

                if 'brightness' in query:
                    brightness()

                if 'volume' in query:
                    volume()

                if 'open Google' in query:
                    g1()

                if 'open Youtube' in query:
                    y1()

if __name__ == '__main__':
    while True:
        wake()









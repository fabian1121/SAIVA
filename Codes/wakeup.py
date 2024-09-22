#import driver
import speech_recognition as sr
from gtts import gTTS


def get_audio():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
		said = ""

		try:
		    said = r.recognize_google(audio)
		    print(said)
		except Exception as e:
		    print("Exception: " + str(e))

	return said


#text = get_audio()
#Wake = "hello"

#while True:
#    text = get_audio()

#    if text.count(Wake)>0:
#        driver()
        
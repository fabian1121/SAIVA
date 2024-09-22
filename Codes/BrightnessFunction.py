import screen_brightness_control as bright
from SpeakFunction import speak
from ListenFunction import *

now = bright.get_brightness()


def current_brightness():
    speak("Brightness level is at "+str(now))

def increase_brightness():
    speak("By how much do you want me to increase by?")
    level = TakeCommand().lower()
    new_level = now + int(level)
    bright.set_brightness(new_level)
    speak("Brightness level increased to "+str(bright.get_brightness()))

def decrease_brightness():
    speak("By how much do you want me to decrease by?")
    level = TakeCommand().lower()
    new_level = now - int(level)
    bright.set_brightness(new_level)
    speak("Brightness level decreased to "+str(bright.get_brightness()))

def s_brightness():
    level = TakeCommand().lower()
    bright.set_brightness(level)
    speak("Brightness level set to "+str(bright.get_brightness(level)))

def brightness():
    speak("The current brightness value is "+str(now))
    speak("do you want to increase/decrease or set brightness?")
    control = TakeCommand().lower()
    #now = bright.get_brightness()
    if 'current' in control :
        current_brightness()
    elif 'increase' in control:
        increase_brightness()
    elif 'decrease' in control :
        decrease_brightness()
    elif 'set' in control:
        s_brightness()

#brightness()

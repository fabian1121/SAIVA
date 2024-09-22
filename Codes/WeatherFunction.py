from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from ListenFunction import *

def weather():
    api_key = "ad5bd44e9e623d36284a09a93aec80b2"
    owm = OWM(api_key=api_key)
    mgr = owm.weather_manager()

    speak("Please enter the city name")
    city = TakeCommand()

    observation = mgr.weather_at_place(city)
    w = observation.weather

    status = w.detailed_status
    humidity = str(w.humidity)
    temperature = str(w.temperature('celsius')['temp'])

    message = "The current forecast shows "+status+". The humidity is "+humidity+"%. The temperature is "+temperature+" Celsius."

    speak(message)

weather()
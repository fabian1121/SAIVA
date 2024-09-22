import psutil
from SpeakFunction import speak

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at "+usage+" percent")

def battery():
    battery = psutil.sensors_battery()
    speak("Battery is at "+ str(battery.percent)+" percent")


#cpu()
#battery()
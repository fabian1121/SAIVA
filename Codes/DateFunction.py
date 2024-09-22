import datetime
from SpeakFunction import speak

month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def date():
    year = str(datetime.datetime.now().year)
    month = datetime.datetime.now().month
    day = str(datetime.datetime.now().day)
    speak("Today's date is "+day+" "+month_names[month-1]+" "+year)

date()
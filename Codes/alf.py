import pyjokes
from ai import AI
from datetime import datetime


alf = AI()

def joke():
    funny = pyjokes.get_joke()
    # print(funny)
    alf.say(funny)

command = ""
alf.say("Hello")
while True and command != "goodbye":
    try:
        command = alf.listen()
        command = command.lower()
    except:
        print("oops there was an error")
        command = ""
    print("command was:", command)

    if command == "tell me a joke":
        joke()
        command = ""

    if command in ['good morning','good evening','good night','good afternoon']:
        now = datetime.now()
        hr = now.hour
        if hr <= 0 <=12:
            message = "Morning"
        if hr >=12 <= 17:
            message = "Afternoon"
        if hr >=17 <=21:
            message = "Evening"
        if hr > 21: message = "Night"

        message = "Good " + message + " Kevin"
        alf.say(message)
        
        
        joke()
        
    
  

alf.say("Goodbye!")


import os
from ListenFunction import *
from TimeFunction import *
from DateFunction import *
from datetime import *

def Notepad():

    print("tell me about it.....")
    print("Im ready to write...")

    input = TakeCommand()

    time = datetime.now().strftime("%H:%M")

    filename = str(time).replace(":","-") + "-note.txt"
    with open(filename,"w") as file:
        file.write(input)

    path_1 = "D:/test1/" + str(filename)

    path_2 = "D:/test1/five/notepad/" +str(filename)


    os.rename(path_1,path_2)
   # os.startfile(path_2)

Notepad()

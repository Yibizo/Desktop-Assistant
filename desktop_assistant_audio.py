import os, sys, pyttsx3
from playsound import playsound

engine = pyttsx3.init()
rate = 170
engine.setProperty('rate',rate)
volume = engine.getProperty('volume')
engine.setProperty('volume',0.8)

textString = ""
while True:
    file = open("desk_text.txt","r+")

    if os.stat("desk_text.txt").st_size != 0:
        textString = file.readline()
        engine.say(textString)
        engine.runAndWait()

    file.truncate(0)
    file.close()
import speech_recognition as sr
import winsound as ws
import webbrowser as wb
import os, sys, datetime, ctypes, time, pyttsx3
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from datetime import timezone,tzinfo,timedelta

engine = pyttsx3.init()
rate = 170
engine.setProperty('rate',rate)
volume = engine.getProperty('volume')
engine.setProperty('volume',0.8)

def say(text):
    engine.say(text)
    engine.runAndWait()

def google_search(search):
    voiceOutput = ""
    textListLen = len(textList)
    for i in range(textListLen-1):
        if i != 0:
            search += "+"
        search += textList[i+1]
        voiceOutput += textList[i+1]
        if i != textListLen-2:
            voiceOutput += " "
    action = "searching on"
    if command == "search":
        say(f"{action} google: {voiceOutput}")
    elif command == "youtube":
        say(f"{action} youtube: {voiceOutput}")
    elif command == "map":
        say(f"{action} google maps: {voiceOutput}")
    print(search)
    wb.open_new_tab(search)

def create_program(textList):
    lengthList = len(textList)
    if lengthList == 2:
        program = textList[1]
    else:
        program = ""
        for i in range(lengthList-1):
            program += textList[i+1]
            if i != lengthList-2:
                program += " "
    return program

def open_program(program):
    say(f"opening now")
    os.startfile(program)
    time.sleep(2)
    user32 = ctypes.WinDLL('user32')
    SW_MAXIMISE = 3
    hWnd = user32.GetForegroundWindow()
    user32.ShowWindow(hWnd, SW_MAXIMISE)

def get_datetime(date_time):
    currentDate = datetime.datetime.now()
    if date_time == 0:
        newDateTime = currentDate.strftime("%A, %d of %B of %Y")
    else:
        newDateTime = currentDate.strftime("%I:%M %p")
    print(f"It is {newDateTime}")
    say(f"It is {newDateTime}")

ops = {
    "+": lambda x,y: x+y,
    "-": lambda x,y: x-y,
    "*": lambda x,y: x*y,
    "/": lambda x,y: x/y
}

programs = {
    "documents": r"D:"
}

r = sr.Recognizer()
counter = 1

with sr.Microphone() as source:
    while True:
        print(f"Say initial command #{counter}: ")
        counter += 1
        audio = r.listen(source,phrase_time_limit=2.5)
        try:
            audioText = r.recognize_google(audio)
            text = audioText.lower()
            print(f"You said: {text}")
            if "computer" in text:
                print("in")
                say("Yes?")
                print("Say anything: ")
                audio = r.listen(source,phrase_time_limit=5)

                try:
                    audioText = r.recognize_google(audio)
                    text = audioText.lower()
                    print(f"You said: {text}")
                    file = open("desk_text.txt","a")
                    list = [text]
                    file.writelines(list)
                    file.close()

                    textList = text.split()

                    command = textList[0]

                    if command == "open" or command == "abrir":
                        program = create_program(textList)

                        if program in programs:
                            open_program(programs[program])

                    elif command == "search":
                        google_search("https://www.google.com/search?q=")

                    elif command == "map":
                        google_search("https://www.google.com/maps/search/")

                    elif command == "youtube":
                        if textList[1] == "subscriptions" and len(textList) == 2:
                            say("opening youtube subscriptions")
                            wb.open("https://www.youtube.com/feed/subscriptions")
                        else:
                            google_search("https://www.youtube.com/results?search_query=")

                    elif command == "math":
                        print(ops[textList[2]](float(textList[1]),float(textList[3])))
                    
                    elif text == "what day is it":
                        get_datetime(0)

                    elif text == "what time is it":
                        get_datetime(1)

                    elif text == "exit program":
                        break
                        
                except:
                    print("Could not recognize...")
            else:
                print("out")
        except:
            print("not recognized")
import speech_recognition as sr
import os
import winsound as ws
import webbrowser as wb
import datetime
import ctypes
import time
import pyttsx3
from datetime import timezone,tzinfo,timedelta

engine = pyttsx3.init()
rate = 150
engine.setProperty('rate',rate)

def say(text):
    engine.say(text)
    engine.runAndWait()
    engine.stop()

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

ops = {
    "+": lambda x,y: x+y,
    "-": lambda x,y: x-y,
    "*": lambda x,y: x*y,
    "/": lambda x,y: x/y
}

programs = {
    "discord": r"C:\Users\Yibizo\AppData\Local\Discord\app-0.0.307\Discord.exe",
    "steam": r"C:\Program Files (x86)\Steam\Steam.exe",
    "spotify": r"C:\Users\Yibizo\AppData\Roaming\Spotify\Spotify.exe",
    "osu": r"F:\Alternate Games\osu!\osu!.exe",
    "epic pen": r"C:\Program Files (x86)\Epic Pen\EpicPen.exe",
    "epic games": r"C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe",
    "bluestacks": r"C:\Program Files\BlueStacks\Bluestacks.exe",
    "downloads": r"C:\Users\Yibizo\Downloads",
    "documents": r"D:",
    "my games": r"F:\Alternate Games",
    "my website": "https://yibizo.github.io/"
}

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say anything: ")
    audio = r.listen(source,phrase_time_limit=5)

    try:
        audioText = r.recognize_google(audio)
        text = audioText.lower()
        print(f"You said: {text}")
        say(f"You said: {text}")

        textList = text.split()

        command = textList[0]
        print(command)

        if command == "open" or command == "abrir":
            lengthList = len(textList)
            if lengthList == 2:
                program = textList[1]
            else:
                program = ""
                for i in range(lengthList-1):
                    program += textList[i+1]
                    if i != lengthList-2:
                        program += " "

            if program in programs:
                say(f"opening now")
                os.startfile(programs[program])
                time.sleep(2)
                user32 = ctypes.WinDLL('user32')
                SW_MAXIMISE = 3
                hWnd = user32.GetForegroundWindow()
                user32.ShowWindow(hWnd, SW_MAXIMISE)

        #if text == "play audio":
            #ws.PlaySound("bruh",ws.SND_FILENAME)

        elif command == "search" or command == "buscar":
            google_search("https://www.google.com/search?q=")

        elif command == "map":
            google_search("https://www.google.com/maps/search/")

        elif command == "youtube":
            google_search("https://www.youtube.com/results?search_query=")

        elif command == "math":
            print(ops[textList[2]](float(textList[1]),float(textList[3])))
        
        elif text == "what day is it today":
            currentDate = datetime.datetime.now()
            date = currentDate.strftime("%A, %d of %B of %Y")
            print(f"It is currently {date}")
            say(f"It is currently {date}")

        elif text == "what time is it":
            currentDate = datetime.datetime.now()
            time = currentDate.strftime("%I:%M %p")
            print(f"It is {time}")
            say(f"It is {time}")
    except:
        print("Could not recognize...")
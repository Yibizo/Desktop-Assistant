from subprocess import *
import time, os, sys

os.system("attrib +h desk_text.txt")

file = open("desk_text.txt","r+")
file.truncate(0)
file.close()

Popen("python desktop_assistant_v3.py")
time.sleep(0.5)
Popen("python desktop_assistant_audio.py")
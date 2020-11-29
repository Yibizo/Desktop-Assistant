from subprocess import *
import time,os

os.system("attrib +h desk_text.txt")

Popen("python desktop_assistant_v3.py")
time.sleep(1)
Popen("python desktop_assistant_pygame_v3.py")
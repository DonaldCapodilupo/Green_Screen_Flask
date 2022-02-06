import playsound
import time
from pyautogui import hotkey
import os
import pygetwindow as gw

def countdown(t):
    while t:
        timefile = open("Counter.txt", "w")
        mins, secs = divmod(t, 60)
        if mins > 59:
            hours, mins = divmod(mins, 60)
        else:
            hours = 0
        timeformat = f"{hours:02d}:{mins:02d}:{secs:02d}"
        timefile.write(timeformat)
        timefile.close()
        time.sleep(1)
        t -= 1
    os.remove("Counter.txt")



# ]url = ex. "C:\\Users\\Don\\Documents\\Github Folder\\Green_Screen_Flask\\Audio\\Johnny B Goode.mp3"
def play_Music(url):
    playsound.playsound(url)





#def activate_Window()



win = gw.getWindowsWithTitle('OBS')[0]
win.maximize()
win.activate()

countdown(7)

hotkey('shift', '1')

hotkey('alt', '/')

play_Music("C:\\Users\\Don\\Documents\\Github Folder\\Green_Screen_Flask\\Audio\\Johnny B Goode.mp3")

hotkey('alt', '/')
hotkey('shift', '2')


win = gw.getWindowsWithTitle('Green_Screen_Flask')[0]
win.maximize()
win.activate()

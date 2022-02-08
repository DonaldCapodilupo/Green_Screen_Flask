#!/bin/bash
import time
from pyautogui import hotkey
import os
import pygetwindow as gw
from pygame import mixer
import pyautogui

#Dict = userInput: (Image, MP3, scene_hotkey, length)
dict_Of_Scenes = {
    "Beach":("Beach.jpg", "Johnny B Goode.mp3",1, 54),
    "Graveyard":("Graveyard.jpg", "Thriller.mp3",7, 47),
    "Disco":("Disco Background.mp4", "Funky Town.mp3", 9, 46),
    "Old West":("Old West Town.jpg", "Old Town Road.mp3", 5, 29),
    "Outer Space":("Space.png", "Rocketman.mp3", 3, 52),



}

def countdown(t):
    while t:
        time_File = open("Counter.txt", "w")
        minutes, secs = divmod(t, 60)
        if minutes > 59:
            hours, minutes = divmod(minutes, 60)
        else:
            hours = 0
        time_Format = f"{hours:02d}:{minutes:02d}:{secs:02d}"
        time_File.write(time_Format)
        time_File.close()
        time.sleep(1)
        t -= 1
    os.remove("Counter.txt")


def hide_All_Sources():
    list_Of_Sources_To_Hide = ["0" if hotkey_Num[2] == 9 else str(hotkey_Num[2] + 1)  for hotkey_Num in dict_Of_Scenes.values()]
    return list_Of_Sources_To_Hide

def record_Scene(scene_Image):
    win = gw.getWindowsWithTitle('OBS 27.1.3')[0]
    win.maximize()
    win.activate()

    time.sleep(.75)

    #Show scene

    pyautogui.moveTo(470, 520)
    pyautogui.click()

    for scene in hide_All_Sources():
        hotkey('shift', scene)


    hotkey('shift', str(dict_Of_Scenes[scene_Image][2]))

    countdown(7)
    time.sleep(.5)


    #record
    hotkey('alt', '/')

    mixer.init()
    mixer.music.load('Audio\\' + dict_Of_Scenes[scene_Image][1])
    mixer.music.play()
    time.sleep(dict_Of_Scenes[scene_Image][3])


    hotkey('alt', '/')

    if dict_Of_Scenes[scene_Image][2]+1 == 10:
        hotkey('shift', '0')
    elif dict_Of_Scenes[scene_Image][2] == "+":
        hotkey('shift', '-')
    else:
        hotkey('shift', str(dict_Of_Scenes[scene_Image][2]+1))

    win = gw.getWindowsWithTitle('Don Caps Green Screen Party App')[0]
    win.maximize()
    win.activate()


scenes = ["Beach", "Outer Space","Old West", "Mugshot", "Graveyard", "Disco"]




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
    "Disco":("Disco Backround.mp4", "Funky Town.mp3", 9, 46),
    "Old West":("Old West Town.jpg", "Old Town Road.mp3", 5, 29),
    "Outer Space":("Space.png", "Rocketman.mp3", 3, 52)


}

class ListDisplay:
    def __init__(self, listToDisplay):
        self.listToDisplay = listToDisplay

    def displayList(self, addExit=True):
        print("Which option would you like to choose")
        s = 1  # This is the counter to display in the output string.
        for i in self.listToDisplay:  # Loop through the menu options
            print(str(s) + ") " + i)  # Display all of the items in the list as a menu
            s += 1
        if addExit:
            print(str(s) + ") Exit" )
            s += 1
        userChoice = int(input(">"))  # Prompt the user to enter a number
        # Reruns the prompt if the user enters a number that is to big
        if userChoice == len(self.listToDisplay)+1:
            exit()
        while userChoice > len(self.listToDisplay):
            print("Invalid data. Please enter a valid number")
            print()
            print("Which option would you like to choose")
            s = 1  # This is the counter
            for i in self.listToDisplay:  # Loop through the menu options
                print(str(s) + ") " + i)  # Display all of the items in the list as a menu
                s += 1
            if addExit:
                print(str(s) + ") Exit")
                s += 1
            userChoice = int(input(">"))
            if userChoice == len(self.listToDisplay) + 1:
                exit()
        # Closes the program if the user selects "Exit"
        # At some point I would like it to step back one function
        if userChoice == (s - 1) and self.listToDisplay[-1] == "Exit":
            print("Exiting")
            exit()
        # Converts the users numerical entry into the string version of the option selected.
        userChoiceFINAL = self.listToDisplay[(int(userChoice) - 1)]
        # Return the variable
        return userChoiceFINAL

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
    else:
        hotkey('shift', str(dict_Of_Scenes[scene_Image][2]+1))

    win = gw.getWindowsWithTitle('Don Caps Green Screen Party App')[0]
    win.maximize()
    win.activate()


scenes = ["Beach", "Outer Space","Old West", "Mugshot", "Graveyard", "Disco"]

if __name__ == '__main__':
    hide_All_Sources()
    while True:
        user_Choice = ListDisplay(scenes).displayList()

        record_Scene(user_Choice)




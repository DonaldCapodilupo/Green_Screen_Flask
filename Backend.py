from playsound import   playsound
import time
from pyautogui import hotkey
import os
import pygetwindow as gw
from pygame import mixer

#Dict = userInput: (Image, MP3, scene_hotkey, length)
dict_Of_Scenes = {
    "Beach":("Beach.jpg", "Johnny B Goode.mp3",1, 54),
    "Graveyard":("Graveyard.jpg", "Thriller.mp3",7, 47)


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



# ]url = ex. "C:\\Users\\Don\\Documents\\Github Folder\\Green_Screen_Flask\\Audio\\Johnny B Goode.mp3"
def play_Music(url):
    playsound(url)


def record_Scene(scene_Image, song):






    win = gw.getWindowsWithTitle('OBS')[0]
    win.maximize()
    win.activate()



    countdown(7)

    hotkey('shift', str(dict_Of_Scenes[scene_Image][2]))

    hotkey('alt', '/')

    mixer.init()
    mixer.music.load('Audio\\' + dict_Of_Scenes[user_Choice][1])
    mixer.music.play()
    time.sleep(dict_Of_Scenes[scene_Image][3])

#play_Music("C:\\Users\\Don\\Documents\\Github Folder\\Green_Screen_Flask\\Audio\\Johnny B Goode.mp3")

    hotkey('alt', '/')

    hotkey('shift', str(dict_Of_Scenes[scene_Image][2]+1))


    win = gw.getWindowsWithTitle('Green_Screen_Flask')[0]
    win.maximize()
    win.activate()


scenes = ["Beach", "Outer Space","Old West", "Mugshot", "Graveyard"]

if __name__ == '__main__':
    while True:
        user_Choice = ListDisplay(scenes).displayList()

        record_Scene(user_Choice,dict_Of_Scenes[user_Choice])




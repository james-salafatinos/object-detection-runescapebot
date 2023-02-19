# write a program that takes in a portion of the screen and screesnhots it every .5 seconds
# and saves it to a folder

import pyautogui
import os
import time


def check_runelite_exists():
    if len(pyautogui.getWindowsWithTitle("Rune")) == 0:
        print("RuneLite is not open")
        exit()
    else:
        rl = pyautogui.getWindowsWithTitle("Rune")[0]
        pyautogui.getWindowsWithTitle("Rune")[0].restore()
        print("RuneLite is open at ", rl)
        return [rl.left, rl.top, rl.width, rl.height]


def data_set_creator(left, top, width, height):
    cwd = os.getcwd()
    if not (os.path.exists(cwd + "/images")):
        os.mkdir(cwd + "/images")
    os.chdir(cwd + "/images")

    for i in range(200):

        pyautogui.screenshot("image" + str(i) + ".png",
                             region=(left, top, width, height))
        time.sleep(1)


def main():
    rl = check_runelite_exists()

    data_set_creator(*rl)


main()

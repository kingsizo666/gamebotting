from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con

# initial sleep
time.sleep(2)

##
def click(x,y):
    """
    Clicks on a location on the screen

    :param x: x-coordinate of the location
    :param y: y-coordinate of the location
    """
    pyautogui.moveTo(x,y)
    pyautogui.mouseDown(button='left')
    time.sleep(0.1)
    pyautogui.mouseUp(button='left')

def textinput(s):
    """
    Enter the provided string char by char with
    random intervals between them

    :param s: string to be inputed
    """
    for char in s:
        pyautogui.write(char)
        time.sleep(random.uniform(0.03, 0.05))
    pyautogui.press('enter')

click(290,980)
textinput("/join battleon-9989")
time.sleep(2)
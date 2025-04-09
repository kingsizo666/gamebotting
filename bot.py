from pyautogui import *
import pyautogui
import time
import keyboard
import numpy as np
import random
import win32api, win32con

#Sleep
time.sleep(1)

#Move to location then click
pyautogui.moveTo(200,600)
time.sleep(1)
pyautogui.click()
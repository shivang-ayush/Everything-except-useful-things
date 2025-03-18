import pyautogui
import time
import random

while True:
    x = random.randint(0, 1920)
    y = random.randint(0, 1080)
    pyautogui.moveTo(x, y, duration=0.5)
    time.sleep(2)
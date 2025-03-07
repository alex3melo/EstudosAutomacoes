import pyautogui
from time import sleep

pyautogui.moveTo(1411,416,duration=2)
for i in range(50000):
    sleep(0.04)
    pyautogui.click()
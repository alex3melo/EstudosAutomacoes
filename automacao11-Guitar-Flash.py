import pyautogui
import keyboard
from time import sleep

pyautogui.click(1463,643, duration=1)
pyautogui.press('a')

#while keyboard.is_pressed('ctrl+space'):
#prePressionar 1 para parar execução 
while keyboard.is_pressed('1') == False:
    if(pyautogui.pixelMatchesColor(1286,818,(10,10,10))):
        pyautogui.press('a')
        sleep(0.03)
    if(pyautogui.pixelMatchesColor(1376,819,(255,0,0))):
        pyautogui.press('s')
        sleep(0.03)
    if(pyautogui.pixelMatchesColor(1466,817,(244,244,2))):
        pyautogui.press('j')
        sleep(0.03)
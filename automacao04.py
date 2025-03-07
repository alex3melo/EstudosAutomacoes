import pyautogui
from time import sleep

#chamar janela executar
pyautogui.hotkey('winleft', 'r')
#digitar o site
pyautogui.write("https://pt.wikipedia.org/wiki/Brasil")
pyautogui.press('enter')
sleep(2)
pyautogui.scroll(-2600)


import pyautogui
from time import sleep

def abrirSite(site):
    #chamar janela executar
    pyautogui.hotkey('winleft', 'r')
    #digitar o site
    pyautogui.write(site)
    pyautogui.press('enter')
    sleep(3)
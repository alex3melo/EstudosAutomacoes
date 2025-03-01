import pyautogui
import pyperclip
from time import sleep


#chamar janela executar
pyautogui.hotkey('winleft', 'r')
#digitar o site
pyperclip.copy("https://www.google.com/recaptcha/api2/demo?_gl=1*c76bq5*_ga*ODQ0ODI3NTkuMTc0MDE4ODA3MQ..*_ga_37GXT4VGQK*MTc0MDc5NjgwMi4xOS4xLjE3NDA4MDAxOTYuMC4wLjA.")
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')
sleep(2)

recaptcha = pyautogui.locateCenterOnScreen('botao-recaptcha.png')
pyautogui.click(recaptcha[0],recaptcha[1],duration=1)
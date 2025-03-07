import pyautogui
import webbrowser
from time import sleep

telefones = []

with open('fones.txt','r') as arquivo:
    for linha in arquivo:
        telefones.append(linha.split('\n')[0])
    print(telefones)

for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send/?phone={telefone}')
    sleep(10)
    pyautogui.typewrite('TESTE')
    sleep(3)
    pyautogui.press('enter')
    sleep(3)
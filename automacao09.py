import pyautogui
import webbrowser
from time import sleep

tempo = 1

webbrowser.open("https://cursoautomacao.netlify.app/")
sleep(tempo)

pyautogui.click(1470,247, duration=tempo)
pyautogui.scroll(-1000)

sleep(tempo)
#localizar botao proximo
botao_alerta = pyautogui.locateCenterOnScreen('botao-alerta.png')
caixa_nome = pyautogui.locateCenterOnScreen('botao-nome.png')
sleep(tempo)

pyautogui.click(caixa_nome[0], caixa_nome[1], duration=tempo)
sleep(tempo+2)

pyautogui.typewrite("Alex Martins")
pyautogui.click(botao_alerta[0], botao_alerta[1], duration=tempo/2)

sleep(tempo)
botao_ok = pyautogui.locateCenterOnScreen('botao-ok.png')
pyautogui.click(botao_ok[0], botao_ok[1], duration=tempo)

pyautogui.scroll(5000)
sleep(tempo)
pyautogui.scroll(-2200)

dow_excel = pyautogui.locateCenterOnScreen('botao-excel.png')
sleep(tempo)
pyautogui.click(dow_excel[0], dow_excel[1]+35, duration=tempo)
sleep(tempo)
pyautogui.press('enter')
sleep(tempo)

dow_pdf = pyautogui.locateCenterOnScreen('botao-PDF.png')
sleep(tempo)
pyautogui.click(dow_pdf[0], dow_pdf[1]+35, duration=tempo)
sleep(tempo)
pyautogui.press('enter')
sleep(tempo)

pyautogui.alert(text='VOCÊ TERMINOU', title='Automação Test')




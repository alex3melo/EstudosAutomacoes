import pyautogui
import pyperclip
from time import sleep

#Função para escrever com acento
def escrever(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')

#Abri janela executar
pyautogui.hotkey('winleft', 'r')
#chamar bloco de notas
pyautogui.typewrite("notepad")
pyautogui.hotkey('enter')

sleep(1)
escrever("Automação é Incrível!")

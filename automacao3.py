import pyautogui
import os

pasta = "D:\Documentos\Documents\Projetos Python\Automações\\arquivos"
lista = os.listdir(pasta)
qtd_arquivo = len(lista)

for i in range(qtd_arquivo):
    pyautogui.moveTo(1397,281,duration=0.5)
    pyautogui.dragTo(1483,849,button='left',duration=0.5)
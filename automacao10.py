import pyautogui
import webbrowser
from time import sleep

webbrowser.open_new('https://www.instagram.com')
sleep(5)

# login = pyautogui.locateCenterOnScreen('botao-nome-instagram.png')

#conta salva, por acesso sem senha
# pyautogui.click(login[0],login[1], duration=1)
# sleep(1)
# pyautogui.typewrite('alex3melo')
# sleep(1.1)
# senha = pyautogui.locateCenterOnScreen('senha-salva-instagram.png')
# pyautogui.click(senha[0],senha[1], duration=1)
# sleep(1)

# #senha pc
# pyautogui.typewrite('xx')
# sleep(1)
# entrar = pyautogui.locateCenterOnScreen('botao-entrar-instagram.png')
# pyautogui.click(entrar[0],entrar[1], duration=1)


localizar = pyautogui.locateCenterOnScreen('botao-localizar-instagram.png')
pyautogui.click(localizar[0],localizar[1], duration=1.1)
sleep(3)
pesquizar = pyautogui.locateCenterOnScreen('botao-pesquisar-instagram.png')
pyautogui.click(pesquizar[0],pesquizar[1], duration=1.1)
sleep(3)
pyautogui.typewrite('nike')

sleep(1.1)


nike = pyautogui.locateCenterOnScreen('botao-nike2-instagram.png')
pyautogui.click(nike[0],nike[1], duration=1.1)
sleep(1.2)

#pegar segunda imagem, pois a primeira esta definido como fixo
reels = pyautogui.locateCenterOnScreen('botao-reels2-instagram.png')
pyautogui.click(reels[0],reels[1]+200, duration=1.1)
sleep(2.3)

curtir = pyautogui.locateCenterOnScreen('botao-curtir-instagram.png')

if(curtir!=None):
    pyautogui.click(curtir[0],curtir[1], duration=1.1)

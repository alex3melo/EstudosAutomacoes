import pyautogui
import pyperclip
from time import sleep


#Função para escrever com caracteres especiais
def escrever(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')
    
#Função abrir bloco de notas e escrever dados
def programa(email, senha):
    #Abri janela executar
    pyautogui.hotkey('winleft', 'r')
    #chamar bloco de notas
    pyautogui.typewrite("notepad")
    pyautogui.hotkey('enter')
    sleep(1)

    print(email)
    print("")
    print(senha)
    escrever(email)
    pyautogui.hotkey('enter')
    escrever(senha)

#Pegar dados do usuário
email = pyautogui.prompt(text="Informe seu e-mail:", title="Dados de acesso")
senha = pyautogui.password(text="Informe sea senha:", title="Dados de acesso", mask='*')

#Verificar se não vazio
if email != "" and senha != "":
    programa(email, senha)
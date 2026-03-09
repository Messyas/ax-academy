import pyautogui
import time

print("Você tem 3s para se preparar")
time.sleep(4)

try:
    ponto = pyautogui.locateCenterOnScreen('calculadora.png', confidence=0.9)
    pyautogui.click(ponto)
    print('Cliquei no centro calculadora.')
except pyautogui.ImageNotFoundException:
    print('Não encontrei a calculadora na tela.')
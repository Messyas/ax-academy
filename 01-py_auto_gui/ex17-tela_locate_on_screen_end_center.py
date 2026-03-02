import pyautogui
import time

print("Você tem 3s para se preparar")
time.sleep(4)

try:
    box = pyautogui.locateOnScreen('calculadora.png', confidence=0.7)
    x, y = pyautogui.center(box)
    pyautogui.click(x, y)
    print('Cliquei na calculadora!')
except pyautogui.ImageNotFoundException:
    print('Nao achei a calculadora na tela.')
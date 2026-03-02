# Verifica se um ponto está dentro ou fora da tela

import pyautogui
import time

largura, altura = pyautogui.size()
print(pyautogui.onScreen(10, 10))
time.sleep(1)
print(pyautogui.onScreen(-10, 10))
time.sleep(1)
print(pyautogui.onScreen(largura + 2, altura + 2))
time.sleep(1)
print(pyautogui.onScreen(500, 500))
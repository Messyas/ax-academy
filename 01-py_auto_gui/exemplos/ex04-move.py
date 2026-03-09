# Faz movimentos do mouse relativos

import pyautogui

pyautogui.moveTo(800, 500, duration=2)
pyautogui.move(0, -200, duration=2)    # sobe 80
pyautogui.move(-200, 0, duration=2)    # esquerda 60
pyautogui.move(0, 200, duration=2)    # desce 100
pyautogui.move(200, 0, duration=2)    # direita 110
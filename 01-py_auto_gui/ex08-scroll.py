import pyautogui
import time

print("Você tem 3s para se preparar")
time.sleep(5)

pyautogui.moveTo(200, 540)
time.sleep(0.2)
pyautogui.scroll(-400)  # rolagem para baixo
time.sleep(2)
pyautogui.scroll(400)   # rolagem para cima
time.sleep(2)

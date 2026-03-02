import pyautogui
import time

print("Você tem 3s para se preparar")
time.sleep(3)

pyautogui.write('ola, isso foi digitado pelo bot', interval=0.2)
pyautogui.press('enter')
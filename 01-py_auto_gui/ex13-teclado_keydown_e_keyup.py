import pyautogui
import time

print("Você tem 3s para se preparar")
time.sleep(3)

pyautogui.moveTo(300, 360)
pyautogui.click()

pyautogui.keyDown('shift')
pyautogui.press(['left', 'left', 'left'])
pyautogui.keyUp('shift')
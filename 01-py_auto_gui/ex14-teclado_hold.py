import pyautogui
import time

print("Você tem 3s para se preparar")
time.sleep(4)

pyautogui.moveTo(300, 360)
pyautogui.click()
with pyautogui.hold('shift'):
    pyautogui.press(['left', 'left', 'left'])
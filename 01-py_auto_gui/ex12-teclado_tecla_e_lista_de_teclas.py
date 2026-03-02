import pyautogui
import time

print("Você tem 3s para se preparar")
time.sleep(3)

pyautogui.moveTo(520, 360)
pyautogui.click()
pyautogui.press(['tab','tab', 'tab','tab', 'tab'])
time.sleep(2)
pyautogui.write('Arraial do Cabo')
time.sleep(2)
pyautogui.press('F1')
time.sleep(2)

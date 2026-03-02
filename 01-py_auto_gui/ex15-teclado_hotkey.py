import pyautogui
import time

print("Você tem 3s para se preparar")
time.sleep(4)

pyautogui.moveTo(300, 360)
pyautogui.click()

pyautogui.hotkey('ctrl', 'a')  # selecionar tudo
time.sleep(2)
pyautogui.hotkey('ctrl', 'c')  # copiar
time.sleep(2)
pyautogui.press(['tab', 'tab', 'tab', 'tab'])
pyautogui.hotkey('ctrl', 'v')  # colar
time.sleep(4)

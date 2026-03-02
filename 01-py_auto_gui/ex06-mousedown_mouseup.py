import pyautogui
import time

print('Prepare-se em 3 segundos')
time.sleep(3)

pyautogui.moveTo(290, 360, duration=0.5)
pyautogui.mouseDown()                 # pressiona o mouse
pyautogui.move(250, 0, duration=0.5)  # arrasta segurando
pyautogui.mouseUp()
time.sleep(0.5)
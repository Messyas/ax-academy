#arrastar mouse
import pyautogui
import time

print('Prepare-se em 3 segundos')
time.sleep(4)

# arrasta de forma absoluta
pyautogui.moveTo(290, 360, duration=0.5)
pyautogui.click()
pyautogui.dragTo(430, 460, duration=1, button='right')

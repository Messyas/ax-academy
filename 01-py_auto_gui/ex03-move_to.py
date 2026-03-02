# move mouse lentamente

import pyautogui
import time

pyautogui.moveTo(500, 500)
pyautogui.moveTo(300, 800, duration=2)
time.sleep(1)
pyautogui.moveTo(600, 200, duration=2)

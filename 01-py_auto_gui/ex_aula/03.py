#ex 3 12 tabs

import pyautogui
import time
import webbrowser

webbrowser.open("http://localhost:8000")

pyautogui.click()

time.sleep(1)

pyautogui.press(['tab', 'tab', 'tab', 'tab', 'tab', 'tab', 'tab', 'tab', 'tab', 'tab', 'tab', 'tab', 'tab', 'enter'])

time.sleep(1)
pyautogui.write('campo 1')
time.sleep(1)

pyautogui.press("tab")
time.sleep(1)
pyautogui.write('campo 2')
time.sleep(1)

pyautogui.press("tab")
time.sleep(1)
pyautogui.write('notas hehehe')
time.sleep(1)

pyautogui.hotkey('shift', 'tab')
pyautogui.hotkey('shift', 'tab')
pyautogui.hotkey('shift', 'tab')
pyautogui.hotkey('enter')

pyautogui.press(['tab', 'tab', 'tab', 'tab', 'tab', 'tab', 'tab', 'tab', 'tab', 'tab'])

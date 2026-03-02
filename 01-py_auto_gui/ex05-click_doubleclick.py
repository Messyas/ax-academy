import pyautogui
import time

print('Posicione onde o mouse deve clicar em 3 segundos')
time.sleep(3)

pyautogui.click(430, 370)  # move e clica
time.sleep(2)
pyautogui.click(430, 460)  # move e clica
time.sleep(2)
pyautogui.click(430, 550)  # move e clica
time.sleep(2)
pyautogui.click(430, 550, button='right') # move e clique direito
time.sleep(2)
pyautogui.click(430, 600, button='right') # move e clique direito
time.sleep(2)

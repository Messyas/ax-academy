import pyautogui
import time

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.2

print("Você tem 3s para se preparar")
time.sleep(3)

pyautogui.moveTo(200, 400, duration=2)
time.sleep(1)
pyautogui.moveTo(500, 400, duration=4, tween=pyautogui.easeInQuad)
time.sleep(1)
pyautogui.moveTo(900, 400, duration=4, tween=pyautogui.easeOutQuad)
time.sleep(1)
pyautogui.moveTo(1200, 400, duration=4, tween=pyautogui.easeInBounce)
time.sleep(1)
pyautogui.moveTo(1500, 400, duration=2, tween=pyautogui.easeInElastic)
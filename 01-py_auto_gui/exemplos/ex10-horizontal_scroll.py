import pyautogui
import time

print("Scroll Horizontal: Você tem 3s para você colocar o foco na janela certa")
time.sleep(3)

pyautogui.hscroll(100)
time.sleep(1)
pyautogui.hscroll(-100)
time.sleep(1)

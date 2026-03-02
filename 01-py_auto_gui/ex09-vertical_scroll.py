import pyautogui
import time

print("Scroll Vertical: Você tem 3s para você colocar o foco na janela certa")
time.sleep(3)

pyautogui.vscroll(200)
time.sleep(1)
pyautogui.vscroll(-300)
time.sleep(1)

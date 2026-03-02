
import pyautogui
import time

print("Você tem 3s para se preparar")
time.sleep(3)

x, y = 430, 700
cor = pyautogui.pixel(x, y)  # cor vermelho
print('Cor em', x, y, ':', cor)

print(pyautogui.pixelMatchesColor(x, y, cor))
x, y = 655, 700
print(pyautogui.pixelMatchesColor(x, y, cor))
x, y = 790, 700
print(pyautogui.pixelMatchesColor(x, y, cor))
x, y = 980, 700
print(pyautogui.pixelMatchesColor(x, y, cor))
x, y = 1210, 700
print(pyautogui.pixelMatchesColor(x, y, cor))

import pyautogui
import time
import webbrowser

webbrowser.open("http://localhost:8000")

time.sleep(1)
pyautogui.press("tab")
time.sleep(1)
pyautogui.write('Messyas')
time.sleep(1)

pyautogui.press("tab")
time.sleep(1)
pyautogui.write('messyas@gmail.com')
time.sleep(1)

pyautogui.press("tab")
time.sleep(1)
pyautogui.write("702.242.526-27")
time.sleep(1)

pyautogui.press("tab")
time.sleep(1)
pyautogui.write('(92) 92424-2525')
time.sleep(1)

pyautogui.press("tab")
time.sleep(1)
pyautogui.write('Rua legal da silva ponto sei la')
time.sleep(1)

pyautogui.press("tab")
time.sleep(1)
pyautogui.write('Manaus')
time.sleep(1)

pyautogui.press("tab")
time.sleep(1)
pyautogui.write('Amazonas')
time.sleep(1)

pyautogui.press("tab")
time.sleep(1)
pyautogui.write('69037-490')
time.sleep(1)

#categoria
pyautogui.press("tab")
time.sleep(1)
pyautogui.press('down')
time.sleep(1)

pyautogui.press('tab')
time.sleep(1)
pyautogui.write('Texto aleatorio')
time.sleep(1)

#ex 2 - pulando

#voltando pro topo
pyautogui.hotkey('shift', 'tab')
pyautogui.hotkey('shift', 'tab')
pyautogui.hotkey('shift', 'tab')
pyautogui.hotkey('shift', 'tab')
pyautogui.hotkey('shift', 'tab')
pyautogui.hotkey('shift', 'tab')
pyautogui.hotkey('shift', 'tab')
pyautogui.hotkey('shift', 'tab')


time.sleep(1)
pyautogui.hotkey('ctrl', 'a')  # selecionar tudo
time.sleep(1)
pyautogui.hotkey('ctrl', 'c')  # copiar
time.sleep(1)


#tap 8 vezes
pyautogui.press(['tab', 'tab', 'tab', 'tab', 'tab', 'tab', 'tab', 'tab'])

pyautogui.press('enter')

pyautogui.hotkey('ctrl', 'v')  # colar
time.sleep(1)
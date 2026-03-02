import pyautogui
import time

print("Você tem 3s para se preparar")
time.sleep(4)

# Salvar a tela inteira em arquivo
pyautogui.screenshot('tela.png')
time.sleep(2)

# Retornar a imagem (sem salvar)
img = pyautogui.screenshot()
print(type(img))
time.sleep(2)

# Capturar só uma região (x, y, largura, altura)
pyautogui.screenshot('canto.png', region=(0, 0, 400, 300))

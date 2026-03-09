import pyautogui
import time

print("Você tem 3s para se preparar")
time.sleep(3)

def esperar_imagem(arquivo, timeout=10, confidence=0.9):
    inicio = time.time()
    while True:
        try:
            box = pyautogui.locateOnScreen(arquivo, confidence=confidence)
            return box
        except pyautogui.ImageNotFoundException:
            pass

        if time.time() - inicio > timeout:
            return None

        time.sleep(0.3)

box = esperar_imagem('enviar_form.png', timeout=8)
if box is None:
    print('Nao apareceu. Vou tirar screenshot e parar.')
    pyautogui.screenshot('erro_login.png')
else:
    pyautogui.click(pyautogui.center(box))
    print('Cliquei no login.')
import pyautogui
import time

print("Você tem 3s para se preparar")
time.sleep(3)

try:
    # pega todas as ocorrências
    boxes = list(pyautogui.locateAllOnScreen('icone.png', confidence=0.90, grayscale=True))
    print('Quantidade encontrada:', len(boxes))

    for box in boxes:
        x, y = pyautogui.center(box)
        pyautogui.click(x, y)
        time.sleep(0.5)
        pyautogui.press('esc')
        time.sleep(0.2)
except pyautogui.ImageNotFoundException:
    print('Não encontrei nenhuma ocorrência.')
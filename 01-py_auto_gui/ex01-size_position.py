# imprime a posição do mouse (várias vezes)

import pyautogui
import time

QTDE = 3
INTERVALO = 3

largura, altura = pyautogui.size()
print('Tela:', largura, 'x', altura)

time.sleep(INTERVALO)
i = 1
x, y = pyautogui.position()
print('Leitura', i, '-> Mouse em:', x, y)
while i < QTDE:
    print('Mova o mouse para outra posição em até 2s')
    time.sleep(INTERVALO)
    i += 1
    x, y = pyautogui.position()
    print('MessyasLeitura', i, '-> Mouse em:', x, y)
print('Fim.')
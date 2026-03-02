import pyautogui
import time

print("Você tem 3s para se preparar")
time.sleep(3)

pyautogui.alert(text='Vou iniciar o bot agora.', title='RPA', button='OK')
resp = pyautogui.confirm(text='Continuar?', title='RPA', buttons=['Sim', 'Nao'])
print('Resposta:', resp)
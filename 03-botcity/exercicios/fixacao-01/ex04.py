from botcity.core import DesktopBot
import time

bot = DesktopBot()

print("Posicione o Google sala de aula como tela de primeiro plano em até 5s")
time.sleep(5)

if bot.find(label="img", matching=0.9, waiting_time=10000):
    print("Elemento encontrado!")
    bot.screenshot("alvo.png")
else:
    print("Elemento não encontrado.")
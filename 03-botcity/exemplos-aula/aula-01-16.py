# encontrar elementos na tela

from botcity.core import DesktopBot
import time

bot = DesktopBot()

print("Posicione o Google como tela de primeiro plano em até 5s")
time.sleep(5)

if bot.find(label="sorte", matching=0.9, waiting_time=10000):
    bot.click()
time.sleep(2)

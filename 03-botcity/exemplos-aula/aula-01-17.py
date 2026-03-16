# encontrar elementos na tela

from botcity.core import DesktopBot
import time

bot = DesktopBot()

print("Posicione o Google como tela de primeiro plano em até 5s")
time.sleep(5)

bot.click_on(label="sorte")
time.sleep(2)

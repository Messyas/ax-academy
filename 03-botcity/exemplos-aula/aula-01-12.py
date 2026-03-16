from botcity.core import DesktopBot
import time

bot = DesktopBot()

print("Posicione o cursor do mouse em até 2s")
time.sleep(2)

# Lê a última posição conhecida do mouse
x = bot.get_last_x()
y = bot.get_last_y()

print("Posição do mouse:", x, y)
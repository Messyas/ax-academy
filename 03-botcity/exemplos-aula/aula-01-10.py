from botcity.core import DesktopBot
import time

bot = DesktopBot()

print("Posicione o cursor do mouse em até 5s")
time.sleep(5)

for _ in range(10):
    bot.type_down()
    time.sleep(0.5)

for _ in range(10):
    bot.type_right()
    time.sleep(0.1)

# Atalho Win + Shift + S no Windows (snapshot)
bot.type_keys(["win", "shift", "s"])
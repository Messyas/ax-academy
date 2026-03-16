# Teclas básicas


from botcity.core import DesktopBot
import time

bot = DesktopBot()

print("Posicione o cursor do mouse em até 5s")
time.sleep(5)

# Navega entre campos
bot.tab()
time.sleep(2)
bot.tab()
time.sleep(2)
bot.enter()
time.sleep(2)
bot.key_esc()


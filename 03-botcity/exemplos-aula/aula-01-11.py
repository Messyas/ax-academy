from botcity.core import DesktopBot
import time

bot = DesktopBot()

print("Posicione o cursor do mouse em até 5s")
time.sleep(5)

bot.control_a()
bot.control_c()
bot.type_down()
bot.control_v()

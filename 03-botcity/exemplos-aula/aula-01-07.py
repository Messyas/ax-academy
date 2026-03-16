# colar textos

from botcity.core import DesktopBot
import time

bot = DesktopBot()

print("Posicione o cursor do mouse em até 5s")
time.sleep(5)

# Cola o texto de uma vez no campo ativo
bot.paste("Texto colado rapidamente no campo.")
from botcity.core import DesktopBot
import time

bot = DesktopBot()

print("Posicione o cursor do mouse em até 2s")
time.sleep(2)

# Move o mouse para uma posição exata da tela
bot.mouse_move(x=1000, y=500)
# Clipboard

from botcity.core import DesktopBot
import time

bot = DesktopBot()

print("Posicione o cursor do mouse em até 5s")
time.sleep(5)

bot.control_a()
time.sleep(1)
bot.control_c()
time.sleep(1)

# Lê e exibe o texto copiado
texto = bot.get_clipboard()
print("Texto copiado:", texto)
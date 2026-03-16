# Clipboard
from botcity.core import DesktopBot
import time

bot = DesktopBot()

print("Posicione o cursor do mouse no editor em até 5s")
time.sleep(5)

# Coloca texto na área de transferência
bot.copy_to_clipboard("Texto vindo do BotCity")

# Cola no campo ativo
bot.control_v()

# Lê o conteúdo atual da área de transferência
conteudo = bot.get_clipboard()
print("Clipboard:", conteudo)
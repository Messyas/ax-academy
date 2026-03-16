
from botcity.core import DesktopBot
import time
# 1. abra o Bloco de Notas no Windows;

bot = DesktopBot()
# Abre o menu Iniciar do Windows
bot.type_windows()
# digitar notepad
# digitar notepad
bot.type_key("notepad")
time.sleep(1)
# Exemplo com Shift pressionado
bot.hold_shift()
bot.control_home()
bot.release_shift()
bot.sleep(1)
bot.enter()
time.sleep(1)
# 2. digite uma frase simples
bot.type_key("Texto simples todo dia toda hora")
time.sleep(1)
# 3. salve uma screenshot da tela;
bot.screenshot("screenshot.png")
time.sleep(1)
# 4. feche o aplicativo.
bot.alt_f4()
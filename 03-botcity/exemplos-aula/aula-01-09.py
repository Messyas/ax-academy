# Teclas

from botcity.core import DesktopBot
import time

bot = DesktopBot()

# Abre o menu Iniciar do Windows
bot.type_windows()

# digitar notepad
bot.type_key("notepad")
time.sleep(1)
# Exemplo com Shift pressionado
bot.hold_shift()
bot.control_home()
bot.release_shift()
time.sleep(1)

bot.enter()

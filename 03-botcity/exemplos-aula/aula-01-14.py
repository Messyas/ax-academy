from botcity.core import DesktopBot
import time

bot = DesktopBot()

# Clique esquerdo em uma coordenada
bot.click_at(x=273, y=294)
time.sleep(2)

# Clique direito em uma coordenada
bot.right_click_at(x=290, y=435)
time.sleep(2)

bot.key_esc()
time.sleep(2)

bot.click_at(x=329, y=222)
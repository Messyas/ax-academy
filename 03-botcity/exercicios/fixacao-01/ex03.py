from botcity.core import DesktopBot
import time

# 1. abra o Paint;
bot = DesktopBot()

bot.type_windows()

bot.type_key("paint")
time.sleep(1)
bot.enter()
# 2.espere o aplicativo carregar
time.sleep(1)
# 3. mova o mouse até a área de desenho
bot.mouse_move(x=1000, y=500)
# 4. pressione o botão do mouse
bot.mouse_down() #segura
# 5. desenhe uma linha horizontal;
bot.mouse_move(x=1200, y=700)
# 6. solte o botão do mouse;
bot.mouse_up() #solta
# 7. salve uma screenshot da tela.
bot.screenshot("screenshot.png")
time.sleep(1)
# 8. feche o aplicativo.
bot.alt_f4()
bot.type_right()
bot.enter()
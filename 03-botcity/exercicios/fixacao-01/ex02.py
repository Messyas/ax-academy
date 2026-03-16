from botcity.core import DesktopBot
import time

# 1. abra o Bloco de Notas;
bot = DesktopBot()

bot.type_windows()

bot.type_key("notepad")
time.sleep(1)

bot.hold_shift()
bot.control_home()
bot.release_shift()
bot.sleep(1)
bot.enter()
time.sleep(1)

# 2. digite três linhas de texto;
bot.type_key("linha 1")
time.sleep(1)
bot.enter()

bot.type_key("linha 2")
time.sleep(1)
bot.enter()

bot.type_key("linha 3")
time.sleep(1)
# 3. selecione todo o conteúdo;
bot.control_a()
# 4. copie para a área de transferência;
bot.control_c()
time.sleep(1)
# 5. leia o conteúdo do clipboard e exiba no terminal;
texto = bot.get_clipboard()
print(texto)
# 6. vá para o final do texto e cole o conteúdo copiado novamente;
bot.type_right()
bot.enter()
bot.control_v()
time.sleep(1)
# 7. salve uma screenshot;
bot.screenshot("screenshot.png")
time.sleep(1)
# 8. feche o aplicativo.
bot.alt_f4()
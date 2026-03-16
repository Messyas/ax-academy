from botcity.core import DesktopBot
import time

# 1. abra o Paint;
bot = DesktopBot()

bot.type_windows()

bot.type_key("calculadora")
time.sleep(1)
bot.enter()

bot.delete()

#calculos

bot.type_key("15 + 7 =")
time.sleep(1)
bot.screenshot("resultado_1.png")
time.sleep(1)
bot.delete()

bot.type_key("23 * 9 =")
time.sleep(1)
bot.screenshot("resultado_2.png")
time.sleep(1)
bot.delete()

bot.type_key("144 / 23 =")
time.sleep(1)
bot.screenshot("resultado_3.png")
time.sleep(1)
bot.delete()

bot.type_key("50 - 18 =")
time.sleep(1)
bot.screenshot("resultado_4.png")
time.sleep(1)

bot.screenshot("resultado_final.png")
time.sleep(1)
bot.alt_f4()


from webdriver_manager.chrome import ChromeDriverManager
from botcity.web import WebBot
#tem que baixar a lib pip install webdriver-manager e modificar o codigo pra abrir corretamente
bot = WebBot()
# Point the bot to the automatically downloaded driver
bot.driver_path = ChromeDriverManager().install()

bot.browse("https://www.google.com")
print(bot.driver.title)
bot.sleep(2000)
bot.stop_browser()
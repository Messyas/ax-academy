# Clicar no "Estou com Sorte"

from botcity.web import WebBot, Browser, By

bot = WebBot()
bot.browser = Browser.CHROME
bot.browse("https://www.google.com/")
bot.maximize_window()
bot.sleep(1000)

campo = bot.driver.find_element(By.NAME, 'btnI')

bot.sleep(2000)

bot.stop_browser()
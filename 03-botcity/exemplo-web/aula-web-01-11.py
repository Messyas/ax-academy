# screenshot

from botcity.web import WebBot
from botcity.web.browsers import Browser

bot = WebBot()

bot.browser = Browser.CHROME

bot.browse("https://quotes.toscrape.com")
bot.maximize_window()

bot.sleep(2000)

bot.driver.save_screenshot("pagina_quotes.png")

print("Screenshot salvo")
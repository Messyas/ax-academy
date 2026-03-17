# Extraindo links das páginas

from botcity.web import WebBot
from botcity.web.browsers import Browser

bot = WebBot()

bot.browser = Browser.CHROME

bot.browse("https://quotes.toscrape.com")
bot.maximize_window()

links = bot.driver.find_elements("tag name", "a")

print("Total de links:", len(links))

for l in links:
    print(l.text, l.get_attribute("href"))
from botcity.web import WebBot
from botcity.web.browsers import Browser

bot = WebBot()

bot.browser = Browser.CHROME

bot.browse("https://quotes.toscrape.com")

# seleciona todos os autores
autores = bot.driver.find_elements("css selector", ".author")

for a in autores:
    print(a.text)
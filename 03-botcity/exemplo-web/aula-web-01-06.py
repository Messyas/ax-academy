# coletar todas as citações exibidas na página.

from botcity.web import WebBot
from botcity.web.browsers import Browser

bot = WebBot()

bot.browser = Browser.CHROME

# abre o site
bot.browse("https://quotes.toscrape.com")

# encontra todas as citações
quotes = bot.driver.find_elements("class name", "quote")

print("Total de citações:", len(quotes))

for q in quotes:

    texto = q.find_element("class name", "text").text
    autor = q.find_element("class name", "author").text

    print("\nAutor:", autor)
    print("Citação:", texto)
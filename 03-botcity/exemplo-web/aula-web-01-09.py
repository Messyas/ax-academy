# Mostra os autores de duas páginas

from botcity.web import WebBot
from botcity.web.browsers import Browser

bot = WebBot()

bot.browser = Browser.CHROME

bot.browse("https://quotes.toscrape.com")

for i in range(2):

    quotes = bot.driver.find_elements("class name", "quote")

    print("Página", i + 1)

    for q in quotes:

        autor = q.find_element("class name", "author").text
        print(autor)

    # botão próxima página
    next_button = bot.driver.find_element("css selector", ".next a")

    next_button.click()

    bot.sleep(3000)
# Abrindo uma guia

from botcity.web import WebBot
from botcity.web.browsers import Browser

bot = WebBot()

bot.browser = Browser.CHROME

# abre o navegador e acessa o site
bot.browse("https://duckduckgo.com")
bot.wait(4000)

# Abrindo uma nova guia no navegador.
bot.create_tab("https://botcity.dev")
bot.wait(4000)

bot.stop_browser()


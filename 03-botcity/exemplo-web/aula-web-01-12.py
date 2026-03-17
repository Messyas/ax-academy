# preenchendo compo de um formulário

from botcity.web import WebBot
from botcity.web.browsers import Browser

bot = WebBot()

bot.browser = Browser.CHROME

bot.browse("https://httpbin.org/forms/post")
bot.maximize_window()

# localiza campo nome
campo_nome = bot.driver.find_element("name", "custname")

# preenche campo
campo_nome.send_keys("Maria Silva")

bot.sleep(5000)

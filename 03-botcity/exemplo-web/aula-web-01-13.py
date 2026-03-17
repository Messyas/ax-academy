# preenchendo compo de um formulário

from botcity.web import WebBot
from botcity.web.browsers import Browser

bot = WebBot()

bot.browser = Browser.CHROME

bot.browse("https://httpbin.org/forms/post")
bot.maximize_window()

# localiza campo pizza size
tamanho = bot.driver.find_element("css selector", "input[value='medium']")
tamanho.click()

bot.sleep(5000)

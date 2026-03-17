from botcity.web import WebBot
from botcity.web.browsers import Browser

bot = WebBot()

bot.browser = Browser.CHROME

bot.browse("https://quotes.toscrape.com")

# encontra botão Next
next_button = bot.driver.find_element("xpath", "//li[@class='next']/a")

bot.sleep(2000)

# clica no botão
next_button.click()

bot.sleep(2000)

print("Nova página carregada")
# Acessando elementos do DOM
# O objeto bot.driver do BotCity não é uma API própria do BotCity
# É um WebDriver do Selenium usado pelo BotCity

from botcity.web import WebBot, Browser, By

bot = WebBot()
bot.browser = Browser.CHROME
bot.browse("https://www.google.com")

bot.sleep(2000)

# usando NAME
campo = bot.driver.find_element(By.NAME, "q")
campo.send_keys("automação python")
bot.enter()
bot.sleep(2000)

bot.stop_browser()
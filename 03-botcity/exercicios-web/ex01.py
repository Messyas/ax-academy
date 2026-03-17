from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from botcity.web import WebBot
#tem que baixar a lib pip install webdriver-manager e modificar o codigo pra abrir corretamente
bot = WebBot()
# Faz o bot baixar automaticamente o driver que ele tem que usar
bot.driver_path = ChromeDriverManager().install()

bot.browse("https://httpbin.org/forms/post")
bot.sleep(1000)

bot.find_element(selector="custname", by=By.NAME).send_keys("Ana Souza")
bot.sleep(1000)
bot.find_element(selector="custtel", by=By.NAME).send_keys("92988887777")
bot.sleep(1000)
bot.find_element(selector="custemail", by=By.NAME).send_keys("ana@email.com")
bot.sleep(1000)

bot.tab()
bot.sleep(1000)
bot.type_down()
bot.sleep(1000)
bot.type_down()
bot.sleep(1000)

#caixas de marcar
bot.tab()
#marca bacon
bot.find_element(selector="input[value='bacon']", by=By.CSS_SELECTOR).click()
#marca cheese
bot.find_element(selector="input[value='cheese']", by=By.CSS_SELECTOR).click()

bot.sleep(1000)
#escreve comentario
bot.find_element(selector="comments", by=By.NAME).send_keys("Pedido criado automaticamente por RPA")

bot.sleep(2000)
bot.find_element(selector="button", by=By.CSS_SELECTOR).click()
bot.sleep(2000)

bot.driver.save_screenshot("prova_q1.png")
bot.stop_browser()


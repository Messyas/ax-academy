from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from botcity.web import WebBot
import pandas as pd
import random

#definindo e criando dataframe
tamanhos = ['Small', 'Medium', 'Large']
adicionais = ['bacon', 'cheese', 'onion', 'mushroom']

data = []
for i in range(1, 11):
    row = {
        'custname': f'Cliente {i}',
        'custtel': f'9298888{7770 + i}',
        'custemail': f'cliente{i}@email.com',
        'size': random.choice(tamanhos),
        'toppings': random.sample(adicionais, k=random.randint(1, len(adicionais))),
        'comment': f'Pedido {i} criado automaticamente por RPA'
    }
    data.append(row)

df_pedidos = pd.DataFrame(data)

bot = WebBot()
bot.driver_path = ChromeDriverManager().install()

for index, row in df_pedidos.iterrows():
    # recarrega a pagina para cada iteracao
    bot.browse('https://httpbin.org/forms/post')
    #Preenche os dados do usuario atual
    bot.find_element(selector='custname', by=By.NAME).send_keys(row['custname'])
    bot.find_element(selector='custtel', by=By.NAME).send_keys(row['custtel'])
    bot.find_element(selector='custemail', by=By.NAME).send_keys(row['custemail'])
    size_value = row['size'].lower()
    bot.find_element(selector=f"input[value='{size_value}']", by=By.CSS_SELECTOR).click()
    # Seleciona as caixas
    for topping in row['toppings']:
        bot.find_element(selector=f"input[value='{topping}']", by=By.CSS_SELECTOR).click()

    # preenche os comentarios
    bot.find_element(selector='comments', by=By.NAME).send_keys(row['comment'])
    # Envia
    bot.find_element(selector='button', by=By.CSS_SELECTOR).click()
    bot.sleep(1000)
    # salva prova
    printado = f'formulario_enviado_{index + 1}.png'
    bot.save_screenshot(printado)
    print(f'Formumalrio {index + 1} enviado e salvo como: {printado}')

bot.stop_browser()


import os
import time
from pathlib import Path
import base64
import pandas as pd

from botcity.web import WebBot, Browser, By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# configurações
INDEX_HTML = Path(r"C:\\Users\\\\Desktop\\botcity\\web\\index.html")
CSV_PATH = Path(r"C:\\Users\\\\Desktop\\botcity\\web\\cadastros_portal_fake_20.csv")
QTDE = 5
DELEY = 0.5

def carregar_usuarios(csv_path):
    df = pd.read_csv(csv_path, dtype=str)
    return df.to_dict(orient='records')

#configurar webbot do botcity
def iniciar_bot():
    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()
    bot.start_browser()
    return bot

def abrir_portal(bot, url_portal):
    url = "file://" + str(url_portal).replace("\\", "/")
    bot.browser.open(url)
    WebDriverWait(bot.driver, timeout=10).until(
        #expected conditions
        #vamos utulizar o selenium para verificar dentro da arvore do dom
        #quando o botao de novo cadastro tiver sido carregado, se for, é um sinal de que o portal foi carregado.
        ec.presence_of_element_located((By.CSS_SELECTOR, "#btnNovo"))
    )

def zerar_base(bot):
    bot.find_element("#btnClearAll", By.CSS_SELECTOR).click()
    bot.drive.switch_to.alert.accept()
    time.sleep(DELEY)

def b_cadastrar_usuario(bot, usuario):
    bot.find_element("btnNovo", By.CSS_SELECTOR).click()
    time.sleep(DELEY)

    for campo_id, coluna in [
        ("f_nome", "nome"),
        ("f_sobrenome", "sobrenome"),
        ("f_cpf", "cpf"),
        ("f_telefone", "telefone"),
        ("f_email", "email"),
        ("f_nascimento", "nascimento"),
        ("f_endereco", "endereco"),
        ("f_observacao", "observacao")
    ]:
        el = bot.find_element(f'#{campo_id}', By.CSS_SELECTOR)
        el.clear()
        el.send_keys(str(usuario['coluna']))

    Select(bot.find_element("#f_status", By.CSS_SELECTOR)).select_by_visible_text(usuario['status'])
    bot.find_element("brnSalvar", By.CSS_SELECTOR).click()
    time.sleep(DELEY)

def cadastro_todos(bot, usuarios, qtd):
    lista = usuarios[:qtd] if qtd else usuarios
    total = len(lista)

    for i, usuario in enumerate(lista, start=1):
        print(f"{i}/{total} {usuario['nome']} {usuario['sobrenome']}")
        b_cadastrar_usuario(bot, usuario)

    print(f'todos os {total} cadastros concluidos...')

def tirar_screenshot(bot, arquivo="evidencia.png"):
    result = bot.driver.execute_cdp_cmd("Page.captureScreenshot", {
        "format": "png",
        "captureBeyondViewPort": True,
    })

    with open(arquivo, "wb") as f:
        f.write(base64.b64decode(result['data']))

    print(f"Screenshot salvo em: {arquivo}")

def main():
    # 1. carregar o csv
    usuarios = carregar_usuarios(CSV_PATH)
    # 2. iniciar o bot
    bot = iniciar_bot()
    # 3. abrir portal
    try:
        abrir_portal(bot, INDEX_HTML)
        # 4. zerar o banco de dados
        zerar_base(bot)
        # 5. cadastrar todos os usuarios
        cadastro_todos(bot, usuarios, qtde=QTDE)
        # 6. tirar uma evidencia com um print screen
        tirar_screenshot(bot)
        time.sleep(3)
    finally:
        # 7. fechar o navegador
        bot.stop_browser()

if __name__ == "__main__":
    main()



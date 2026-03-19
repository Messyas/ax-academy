import os
import sys # vai ser utilizado dentro da instancia do botcity
import time
import base64

from botcity.web import WebBot, Browser, By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from dotenv import load_dotenv
from botcity.maestro import BotMaestroSDK, AutomationTaskFinishStatus

load_dotenv()

SERVER = os.getenv('MAESTRO_SERVER')
LOGIN = os.getenv('MAESTRO_LOGIN')
KEY = os.getenv('MAESTRO_KEY')
DATAPOOL = os.getenv('DATAPOOL_LABEL')
PORTAL_URL = os.getenv('PORTAL_URL')
DELEY = 0.5

def conectar_maestro():
    if len (sys.argv) > 1:
        maestro = BotMaestroSDK.from_sys_args()
        task_id = maestro.get_execution().task_id
    else:
        maestro = BotMaestroSDK()
        maestro.login(server=SERVER, login=LOGIN, key=KEY)
        task_id = None
    return maestro, task_id

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

def cadastro_todos(bot, datapool, task_id):
    ok, erros = 0, 0
    while datapool.has_next():
        item = datapool.next(task_id=task_id)
        if item is None:
            break
        usuario = item.values
        print(f"{ok+erros+1} {usuario['nome']} [{usuario['sobrenome']} sendo cadastrado...")
        try:
            b_cadastrar_usuario(bot, usuario)
            item.report_done()
            ok += 1
            print("    Ok")
        except Exception as e:
            print(f"     ERRO: {e}")
            erros += 1
            try:
                bot.find_element("#btnCancelar", By.CSS_SELECTOR).click()
            except Exception:
                pass
            item.report_error() #marca o dado e erro
        print(f"\nConcluido: {ok} OK | {erros} ERROS.")
        return ok, erros

def finalizar_task(maestro, task_id, ok, erros):
    if task_id:
        maestro.finish_task(
            task_id=task_id,
            status=AutomationTaskFinishStatus.SUCCESS if erros == 0 else AutomationTaskFinishStatus.PARTIALLY_COMPLETED,
            message=f"{ok} OK | {erros} ERROS."
        )

def tirar_screenshot(bot, arquivo="evidencia.png"):
    result = bot.driver.execute_cdp_cmd("Page.captureScreenshot", {
        "format": "png",
        "captureBeyondViewPort": True,
    })

    with open(arquivo, "wb") as f:
        f.write(base64.b64decode(result['data']))

    print(f"Screenshot salvo em: {arquivo}")

def main():
    maestro, task_id, = conectar_maestro()
    bot = iniciar_bot()
    try:
        abrir_portal(bot, PORTAL_URL)
        zerar_base(bot)
        datapool = maestro.get_datapool(label=DATAPOOL)
        ok, erros = cadastro_todos(bot, datapool, task_id)
        tirar_screenshot(bot)
        time.sleep(3)
    finally:
        bot.stop_browser()
        finalizar_task(maestro, task_id, ok, erros)

if __name__ == "__main__":
    main()



from botcity.web import WebBot, Browser, By
from webdriver_manager.chrome import ChromeDriverManager
from botcity.maestro import *
import csv

# Desabilitar erros se não estiver conectado ao Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    bot = WebBot()
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()
    bot.headless = False

    bot.browse("https://quotes.toscrape.com/")
    
    # Gerando CSV
    # newline='' é para evitar linhas em branco extras no Windows
    with open('citacoes.csv', mode='w', newline='', encoding='utf-8') as arquivo_csv:
        escritor = csv.writer(arquivo_csv, delimiter=';')
        # Escrevendo o cabeçalho
        escritor.writerow(['Pagina', 'Citacao'])

        pagina_atual = 1
        tem_proxima = True

        while tem_proxima:
            print(f"Processando página {pagina_atual}...")
            bot.wait(1000) # Espera simples para garantir o carregamento

            # 1. Captura todas as citações da página atual
            # pegar a lista completa de elements
            citacoes = bot.find_elements("div.quote span.text", By.CSS_SELECTOR)

            for citacao in citacoes:
                texto = citacao.text
                # Escreve no CSV: Número da página; Texto da citação
                escritor.writerow([pagina_atual, texto])

            # 2. Verifica se o botão "Next" existe
            botao_next = bot.find_element("li.next a", By.CSS_SELECTOR)

            if botao_next:
                botao_next.click()
                pagina_atual += 1
            else:
                print("Botão Next não encontrado. fim da execução do bot.")
                tem_proxima = False

    print("Processo finalizado.")
    bot.wait(2000)
    bot.stop_browser()

    # Finaliza a tarefa no Maestro (caso esteja rodando nele)
    if BotMaestroSDK.RAISE_NOT_CONNECTED:
        maestro.finish_task(
            task_id=execution.task_id,
            status=AutomationTaskFinishStatus.SUCCESS,
            message="Relatório de citações gerado."
        )

if __name__ == '__main__':
    main()
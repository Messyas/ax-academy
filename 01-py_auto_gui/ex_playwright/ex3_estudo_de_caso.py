# Importa a API síncrona do Playwright
from playwright.sync_api import sync_playwright


# Inicia o Playwright
with sync_playwright() as p:
    # Abre o Chromium com interface gráfica
    # slow_mo=500 adiciona 500ms de pausa entre cada ação
    # facilita visualizar cada passo em sala de aula
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()
    page.goto('https://www.selenium.dev/selenium/web/web-form.html')
    page.wait_for_load_state('domcontentloaded')

    # 1. Utilizando o Pandas, gere 10 conjuntos de dados sintéticos para os seguintes
    # campos: Nome, Senha, Descrição, Quantidade de imóveis (One, Two ou Three),
    # Cidade (San Francisco, New York, Seattle, Los Angeles, Chicago), Data (DD/MM/AAAA).
    # Coloque esses dados em um Dataframe.






    # Preenche o campo de texto simples pelo label "Text input"
    page.get_by_label('Text input').fill('Playwright RPA')

    # Preenche o campo de senha pelo label "Password"
    page.get_by_label('Password').fill('senha_secreta_123')

    # Preenche o campo textarea pelo label "Textarea"
    page.get_by_label('Textarea').fill('Este texto foi preenchido automaticamente pelo Playwright.')

    # Seleciona uma opção no dropdown pelo label "Dropdown (select)"
    # Seleciona pelo texto visível da opção
    page.get_by_label('Dropdown (select)').select_option('Two')

    # Marca o checkbox pelo label "Default checkbox"
    page.get_by_label('Default checkbox').check()

    # Seleciona o radio button pelo label "Default radio"
    page.get_by_label('Default radio').check()

    # Preenche o campo de data com uma data no formato correto
    # O campo aceita o formato MM/DD/YYYY
    page.get_by_label('Date picker').fill('2025-01-31')

    # Tira screenshot do formulário preenchido antes de enviar
    page.screenshot(path='formulario_preenchido.png')
    print('Screenshot do formulário preenchido salvo.')

    # Clica no botão de envio do formulário
    page.get_by_role('button', name='Submit').click()

    # Aguarda a página de confirmação carregar
    page.wait_for_load_state('domcontentloaded')

    # Captura a mensagem de confirmação exibida após o envio
    # O site retorna uma mensagem no elemento com id "message"
    mensagem = page.locator('#message').text_content()

    # Imprime a mensagem capturada
    print(f'Mensagem de retorno: {mensagem}')

    # Tira screenshot da página de confirmação como evidência
    page.screenshot(path='formulario_confirmacao.png')
    print('Screenshot da confirmação salvo.')

    # Fecha o browser
    browser.close()

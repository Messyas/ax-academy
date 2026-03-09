from playwright.sync_api import sync_playwright

def parte1():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        content = browser.new_context()
        page = content.new_page()

        page.goto('https://the-internet.herokuapp.com/inputs',
                  wait_until='domcontentloaded')

        # Localizar campo numerico
        campo_numero = page.locator("input[type='number']")
        campo_numero.click()

        # Digitar com deley
        campo_numero.press_sequentially("1000", delay=100)
        page.wait_for_timeout(1000)

        # Apagar os dois últimos dígitos (00) com Backspace
        campo_numero.press("Backspace")
        campo_numero.press("Backspace")
        page.wait_for_timeout(1000)

        # Adicionar 5 ao final
        campo_numero.press_sequentially("5")
        page.wait_for_timeout(1000)

        # Ctl + a
        campo_numero.press("Control+a")
        page.wait_for_timeout(1000)

        # Digitar 9999
        campo_numero.press_sequentially("9999", delay=100)

        # imprimir no terminal
        valor_final = campo_numero.input_value()
        print(f"O valor final do campo é: {valor_final}")

        content.close()
        browser.close()

def parte2():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        content = browser.new_context()
        page = content.new_page()

        #1
        page.goto('https://the-internet.herokuapp.com/tinymce',
                  wait_until='domcontentloaded')

        # 1. CONTORNO DO AVISO DE ASSINATURA:
        # Injetamos JavaScript para varrer a tela e deletar o banner de aviso (.tox-notification)
        page.evaluate("document.querySelectorAll('.tox-notification').forEach(el => el.remove());")

        # 2. O SEGREDO DO IFRAME:
        # Avisamos o Playwright que queremos interagir com o documento que está DENTRO do iframe
        editor_frame = page.frame_locator("iframe")

        # Agora buscamos o corpo do editor (body) focado APENAS dentro do iframe
        caixa_texto = editor_frame.locator("body#tinymce")

        # Clicamos para garantir que o cursor está piscando lá dentro
        caixa_texto.click()

        #2 Localizar o editor de texto rico (TinyMCE)
        mce = page.get_by_label("tynymce")

        #3 Limpar o conteúdo existente com Control+A seguido de Delete]
        mce.press("Control+a")
        mce.press("Delete")
        #4 Digitar o seguinte texto
        mce.press_sequentially("Playwright automatiza browsers com precisao.", delay=100)
        mce.press("Enter")
        mce.press_sequentially("RPA com Python e muito poderoso.", delay=100)
        mce.press("Enter")
        mce.press_sequentially("Aprenda automacao na pratica.", delay=100)

        page.wait_for_timeout(1000)

        #5 Usar Control+A para selecionar todo o texto
        mce.press("Control+a")

        #6 Usar Control+C para copiar
        mce.press("Control+c")

        #7 Navegar para o campo de texto simples que aparece abaixo do editor

        #8 Usar Control+V para colar o texto copiado
        mce.press("Control+v")

        #9 Tirar screenshot do resultado
        page.screenshot(path="screenshot_ex2_parte2.png")

        content.close()
        browser.close()


def main():
    #parte1()
    parte2()
    #usar o dontpad no lugar da api

if __name__ == '__main__':
    main()
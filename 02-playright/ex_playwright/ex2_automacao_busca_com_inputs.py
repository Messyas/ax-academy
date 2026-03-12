from playwright.sync_api import sync_playwright

def parte1():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        content = browser.new_context()
        page = content.new_page()

        page.goto(
            'https://the-internet.herokuapp.com/inputs',
            wait_until='domcontentloaded'
        )

        # Localizar campo numerico
        campo_numero = page.locator("input[type='number']")
        campo_numero.click()

        # Digitar com delay
        campo_numero.press_sequentially("1000", delay=100)
        page.wait_for_timeout(1000)

        # Apagar os dois últimos dígitos
        campo_numero.press("Backspace")
        campo_numero.press("Backspace")
        page.wait_for_timeout(1000)

        # Adicionar 5 ao final
        campo_numero.press_sequentially("5", delay=100)
        page.wait_for_timeout(1000)

        # Ctrl + A
        campo_numero.press("Control+A")
        page.wait_for_timeout(1000)

        # Digitar 9999
        campo_numero.press_sequentially("9999", delay=100)

        # Imprimir no terminal
        valor_final = campo_numero.input_value()
        print(f"O valor final do campo é: {valor_final}")

        content.close()
        browser.close()


def parte2():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto(
            "https://www.rapidtables.com/tools/notepad.html",
            wait_until="domcontentloaded"
        )

        # Fecha aviso inicial, se aparecer
        botao_close = page.get_by_text("Close")
        if botao_close.first.is_visible():
            botao_close.first.click()

        # Localiza a área principal de texto do notepad
        editor = page.locator("textarea").first
        editor.wait_for(state="visible")
        editor.click()

        # Limpa o conteúdo existente
        page.keyboard.press("Control+A")
        page.keyboard.press("Delete")

        texto = (
            "Playwright automatiza browsers com precisao.\n"
            "RPA com Python e muito poderoso.\n"
            "Aprenda automacao na pratica."
        )

        # Digita o texto no editor
        editor.press_sequentially(texto, delay=30)
        page.wait_for_timeout(1000)

        # Seleciona tudo e copia
        page.keyboard.press("Control+A")
        page.keyboard.press("Control+C")
        page.wait_for_timeout(500)

        # Cola no final do próprio texto
        page.keyboard.press("End")
        page.keyboard.press("Enter")
        page.keyboard.press("Control+V")
        page.wait_for_timeout(1000)

        page.screenshot(path="parte2.png", full_page=True)

        context.close()
        browser.close()


def main():
    parte1()
    parte2()

if __name__ == "__main__":
    main()
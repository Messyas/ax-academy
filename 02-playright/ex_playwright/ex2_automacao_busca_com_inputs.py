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
        context = browser.new_context()
        page = context.new_page()

        # usei esse site ja que o orinal nao funcionava
        page.goto("https://anotepad.com/", wait_until="load")

        titulo = page.get_by_role("textbox").first
        titulo.wait_for(state="visible")
        titulo.click()

        #limpa conteudo
        page.keyboard.press("Control+A")
        page.keyboard.press("Delete")

        texto = (
            "Playwright automatiza browsers com precisao. "
            "RPA com Python e muito poderoso. "
            "Aprenda automacao na pratica."
        )
        # digita tudo
        titulo.type(texto, delay=30)
        #copia
        page.keyboard.press("Control+A")
        page.keyboard.press("Control+C")

        #vai pro input de baixo
        page.keyboard.press("Tab")
        #copia
        page.keyboard.press("Control+V")
        #printa
        page.screenshot(path="parte2.png", full_page=True)

        context.close()
        browser.close()

def main():
    parte1()
    parte2()

if __name__ == "__main__":
    main()
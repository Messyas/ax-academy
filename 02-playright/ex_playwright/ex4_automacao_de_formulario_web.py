from playwright.sync_api import sync_playwright
from pathlib import Path
import os

def fazer_login(nome, senha):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        content = browser.new_context()
        page = content.new_page()

        page.goto('https://the-internet.herokuapp.com/login',
                  wait_until='domcontentloaded')

        campo_usuario = page.locator("#username")
        campo_senha = page.locator("#password")
        botao_login = page.locator("button[type='submit']")

        if campo_usuario.is_visible() and campo_usuario.is_enabled():
            campo_usuario.fill(nome)

        if campo_senha.is_visible() and campo_senha.is_enabled():
            campo_senha.type(senha, delay=80)

        botao_login.click()

        flash = page.locator("#flash")
        flash.wait_for(state="visible")
        response = flash.text_content().strip()
        print("Resposta: ", response)

        page.screenshot(path="etapa1_login.png")

def selec_config():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        content = browser.new_context()
        page = content.new_page()
        page.goto("https://the-internet.herokuapp.com/dropdown", wait_until='domcontentloaded')

        dropdown = page.locator("#dropdown")

        opcoes = dropdown.locator("option").all_text_contents()
        for i, opcao in enumerate(opcoes):
            print(f"{i}: {opcao.strip()}")

        dropdown.select_option(label="Option 1")
        page.screenshot(path="etapa2_dropdown_option1.png")

        dropdown.select_option(value="2")
        page.screenshot(path="etapa2_dropdown_option2.png")

def validar_permissoes():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        content = browser.new_context()
        page = content.new_page()
        page.goto('https://the-internet.herokuapp.com/checkboxes',
                  wait_until='domcontentloaded')

        checkboxes = page.locator("input[type='checkbox']")
        total_checkboxes = checkboxes.count()
        print("Quantidade de checkboxes:", total_checkboxes)

        for i in range(total_checkboxes):
            cb = checkboxes.nth(i)
            estado_atual = cb.is_checked()
            print(f"Checkbox {i + 1} antes:", estado_atual)

            if not estado_atual:
                cb.check()
                print(f"Checkbox {i + 1} foi marcado.")

        for i in range(total_checkboxes):
            cb = checkboxes.nth(i)
            print(f"Checkbox {i + 1} depois:", cb.is_checked())

        page.screenshot(path="etapa3_checkboxes.png")

def enviar_doc():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        content = browser.new_context()
        page = content.new_page()
        page.goto('https://the-internet.herokuapp.com/upload',
                  wait_until='domcontentloaded')

        caminho_arquivo = Path("upload_test.txt")
        caminho_arquivo.write_text(
            "Definitivamente um texto",
            encoding="utf-8"
        )
        print("Arquivo criado:", caminho_arquivo.resolve())

        input_upload = page.locator("#file-upload")
        botao_upload = page.locator("#file-submit")

        #define o arquivo no input
        input_upload.set_input_files(str(caminho_arquivo))

        botao_upload.click()

        nome_enviado = page.locator("#uploaded-files")
        nome_enviado.wait_for(state="visible")
        texto_arquivo = nome_enviado.text_content().strip()

        print("Arquivo: ", texto_arquivo)

        page.screenshot(path="etapa4_upload.png")

        if texto_arquivo == "upload_teste.txt":
            os.remove(caminho_arquivo)
            print("Arquivo removido")
        else:
            print("Arquivo removido")

        content.close()
        browser.close()

def main():
    nome = 'tomsmith'
    senha = 'SuperSecretPassword!'

    #Etapa 1
    fazer_login(nome, senha)
    #Etapa 2
    selec_config()
    #Etapa 3
    validar_permissoes()
    #Etapa 4
    enviar_doc()

if __name__ == '__main__':
    main()
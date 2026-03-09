# Exercício 1
# Automação de Login e Extração de Dados
#
# O site https://the-internet.herokuapp.com é uma plataforma criada especificamente para praticar automação. Você deverá criar um script que realize as seguintes tarefas:
#
# Parte 1 — Login

# Acessar a página de login em https://the-internet.herokuapp.com/login
# Localizar os campos de usuário e senha usando localizadores semânticos
# Preencher com as credenciais: usuário tomsmith e senha SuperSecretPassword!
# Clicar no botão de login
# Verificar se a mensagem de sucesso apareceu na tela
# Capturar e imprimir o texto dessa mensagem

# Parte 2 — Navegação e extração
#
# Após o login, acessar a página https://the-internet.herokuapp.com/checkboxes
# Verificar o estado atual de cada checkbox (marcado ou desmarcado)
# Inverter o estado de cada um — o que estava marcado desmarca, o que estava desmarcado marca
# Verificar e imprimir o novo estado de cada checkbox
# Tirar screenshot como evidência

from playwright.sync_api import sync_playwright

def fazer_login(nome, senha):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        content = browser.new_context()
        page = content.new_page()

        page.goto('https://the-internet.herokuapp.com/login',
                  wait_until='domcontentloaded')  # quando todo o conteudo da pag for carregado

        # Preenche o campo de usuário pelo placeholder
        page.get_by_label("Username").fill(nome)
        # Preenche a senha usando o rótulo (Label) visível na tela
        page.get_by_label("Password").fill(senha)
        # Clica no botão usando a função semântica de "papel" (Role)
        page.get_by_role("button", name="Login").click()

        success = page.locator('#flash')
        success.wait_for(state='visible')
        print(success.inner_text())

        page.screenshot(path='screenshot_p1.png')
        content.close()
        browser.close()

def verificar_checkbox():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        content = browser.new_context()
        page = content.new_page()
        page.goto('https://the-internet.herokuapp.com/checkboxes',
                  wait_until='domcontentloaded')  # quando todo o conteudo da pag for carregado

        #pegar todos os elementos
        boxes = page.get_by_role("checkbox").all()

        for _, c in enumerate(boxes):
            checked = c.is_checked()
            print(f"Caixa esta: {checked}")

            if checked:
                c.uncheck()
            else:
                c.check()

        page.screenshot(path='screenshot_p2.png')

def main():
    nome = 'tomsmith'
    senha = 'SuperSecretPassword!'

    fazer_login(nome, senha)
    verificar_checkbox()

if __name__ == '__main__':
    main()
from playwright.sync_api import sync_playwright
import pandas as pd
import numpy as np
from datetime import datetime

# 1) Gera dados
np.random.seed(42)

letras = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
cidades = np.array(["Manaus", "New York", "California", "Africa", "Papua nova guine"])
imoveis = np.array(["One", "Two", "Three"])
descricoes = np.array([
    "hahaha",
    "Buxada de bode",
    "ho ho ho",
    "Eu gosto de lasanha",
    "Busquem comer cimento: By ET Bilu"
])

nomes = [
    "".join(np.random.choice(letras, size=np.random.randint(5, 10)))
    for _ in range(10)
]

senhas = [
    "".join(np.random.choice(letras, size=np.random.randint(8, 13)))
    for _ in range(10)
]

datas = [
    f"{np.random.randint(1, 29):02d}/{np.random.randint(1, 13):02d}/{np.random.randint(2023, 2027)}"
    for _ in range(10)
]

df = pd.DataFrame({
    "Nome": nomes,
    "Senha": senhas,
    "Descricao": np.random.choice(descricoes, size=10),
    "Quantidade de imoveis": np.random.choice(imoveis, size=10),
    "Cidade": np.random.choice(cidades, size=10),
    "Data": datas
})

# 2) Automation hohoho
relatorio = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    for i in range(len(df)):
        page.goto("https://www.selenium.dev/selenium/web/web-form.html")
        page.wait_for_load_state("domcontentloaded")

        # pega a linha atual
        nome = df.loc[i, "Nome"]
        senha = df.loc[i, "Senha"]
        descricao = df.loc[i, "Descricao"]
        qtd_imoveis = df.loc[i, "Quantidade de imoveis"]
        cidade = df.loc[i, "Cidade"]
        data_br = df.loc[i, "Data"]

        # converte DD/MM/AAAA para YYYY-MM-DD pq é oq ta no campo do site
        data_formatada = datetime.strptime(data_br, "%d/%m/%Y").strftime("%Y-%m-%d")

        # preenche os campos pedidos
        page.get_by_label("Text input").fill(nome)
        page.get_by_label("Password").fill(senha)
        page.get_by_label("Textarea").fill(descricao)
        page.get_by_label("Dropdown (select)").select_option(qtd_imoveis)
        page.get_by_label("Dropdown (datalist)").fill(cidade)
        page.get_by_label("Date picker").fill(data_formatada)

        # screenshot
        page.screenshot(path=f"form_{i+1}.png")
        print(f"Screenshot form_{i+1}.png salvo.")

        # envia
        page.get_by_role("button", name="Submit").click()
        page.wait_for_load_state("domcontentloaded")

        # verifica mensagem
        mensagem = page.locator("#message").text_content()
        timestamp = datetime.now().strftime("%d%m%Y %H:%M:%S")

        if mensagem == "Received!":
            status = "sucesso"
            page.screenshot(path=f"form_preenchido_{i+1}.png")
            print(f"Screenshot form_preenchido_{i+1}.png salvo.")
        else:
            status = "Errrrrrrroooooouuuuuuuuuuuu"

        relatorio.append(f"{nome} | {status} | {timestamp}")
        print(f"{nome} -> {status} | {timestamp}")

    browser.close()

# 3) Gera relatorio
with open("relatorio.txt", "w", encoding="utf-8") as arquivo:
    for linha in relatorio:
        arquivo.write(linha + "\n")


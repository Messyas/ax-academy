import os
import asyncio
from datetime import datetime

import gspread
from dotenv import load_dotenv
from google.auth.aio.transport import aiohttp
from google.oauth2.service_account import Credentials
from playwright.async_api import async_playwright
from playwright.sync_api import Playwright

#GOOGLE_CREDENTIAL=C:\Users\Turma01\Documents\messyas\ax-lg\02-playright\bot_monitor_mercado_livre\credentials.json
#SHEET_NAME=teste-mercadolivre

load_dotenv()

PRODUTO = "malbec"
MAX_RESULTADOS = 10
PRECO_LIMITE = 450.00

CREDENTIALS_FILE = os.getenv('GOOGLE_CREDENTIALS')
SHEET_NAME = os.getenv('SHEET_NAME')

SELETOR_ITEM = 'li.ui-search-layout__item'
SELETOR_TITULO = '.poly-component__title-wrapper a'
SELETOR_LINK = SELETOR_TITULO
SELETOR_PRECO = '.andes-money-amount__fraction'

'''
1. Conectar com o google Docs
2. Salvar os datapools na planilha
3. scraper (raspagem) do mercado livre 
4. (opcional) gerar um relatorio de sucesso/erro
5. botar em producao (main)
'''

def conectar_planilha():
    scope = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive',
    ]

    cred = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=scope)
    client = gspread.authorize(cred)

    planilha = client.open(SHEET_NAME)
    aba = planilha.sheet1

    #cria um cabeçalho se a planilha estiver vazia
    if not aba.col_values(1):
        aba.append_row(
            ['Data/Hora', 'String de busca', 'Titulo',
             'Preco (R$)', 'Link', 'Oferta?'],
            value_input_option='USER_ENTERED'
        )
        print('Cabeçalho criado na planilha')
    return aba

def salvar_planilha(aba, resultados):
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    linhas = []

    for r in resultados:
        oferta = 'SIM' if r['preco'] and r['preco'] <= PRECO_LIMITE else 'NAO'
        linhas.append([
            agora,
            PRODUTO,
            r['titulo'],
            r['preco'],
            r['link'],
            oferta,
        ])

    aba.append_rows(linhas, value_input_option='USER_ENTERED')
    print(f'{len(linhas)} linhas adicionadas na planilha')

async def raspar_mercado_livre():
    url = f'https://lista.mercadolivre.com.br/{PRODUTO.replace(" ", "-")}'
    resultados = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        print(f"Acessando o mercado livre em busca de {PRODUTO}")

        await page.goto(url, wait_until="domcontentloaded", timeout=20000)
        await page.wait_for_selector(SELETOR_ITEM, timeout=3000)

        itens = await page.locator(SELETOR_ITEM).all()
        itens = itens[:MAX_RESULTADOS]
        print(f'{len(itens)} itens encontrados. Extraindo informações')

        for item in itens:
            try:
                el = item.locator(SELETOR_TITULO).first
                titulo = await el.inner_text(timeout=2000)
                link = await el.get_attribute('href', timeout=2000)
                link = link.split('?')[0]
            except Exception:
                titulo = 'nao tem'
                link = 'nao tem'

            try:
                preco = await item.locator(SELETOR_PRECO).first.inner_text(timeout=2000)
                preco = float(preco.replace('.', '').replace(',', '.'))
            except Exception:
                preco = None

            resultados.append({
                'titulo': titulo,
                'preco': preco,
                'link': link,
            })

        await browser.close()

    return resultados

async def main():
    #pegar os dados
    resultados = await raspar_mercado_livre()
    #conectar no google cloud
    print('Conectando ao Google Sheets...')
    aba = conectar_planilha()
    salvar_planilha(aba, resultados)
    print('Processo concluido...')

if __name__ == '__main__':
    asyncio.run(main())

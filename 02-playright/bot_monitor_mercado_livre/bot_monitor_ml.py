import os
import asyncio
from datetime import datetime

import gspread
from dotenv import load_dotenv
from google.oauth2.service_account import Credentials
from playwright.sync_api import Playwright

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


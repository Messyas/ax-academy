import pandas as pd
from pathlib import Path
from playwright.sync_api import sync_playwright
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Bot de Cadastro", description="API para cadastro em portal fake", version="1.0")

class RunRequest(BaseModel):
    headless: bool = False
    clean_base: bool = True
    csv_path: str
    portal_url: str

def open_portal(p):
    return Path(p).resolve().as_uri()

def carregar_dados(csv_path):
    df = pd.read_csv(csv_path).fillna('')
    #falta fazer o relatorio
  #  required = ['nome', 'sobrenome', 'cpf', 'email', 'telefone', 'nascimento', 'status', 'observacao', 'endereco']
    return df

# 0. abrir o portal 
# 1. zerar os registros
# 2. abrir o cadastro de novo
# 3. preencher os campos com os dados
# 4. salvar 
# 5. pausar
# 6. fechar o navegador

def zerar_base(page):
    page.once('dialog', lambda dialog: dialog.accept())
    page.click("#btnClearAll")
    page.wait_for_timeout(1000)

def cadastrar_lote(page, df):
    for _, r in df.iterrows():
        d = r.to_dict()
        page.click("#btnNovo")
        page.fill('#f_nome', str(d['nome']))
        page.fill('#f_sobrenome', str(d['sobrenome']))
        page.fill('#f_cpf', str(d['cpf']))
        page.fill('#f_email', str(d['email']))
        page.fill('#f_telefone', str(d['telefone']))
        page.fill('#f_nascimento', str(d['nascimento'])) 
         
        page.select_option('#f_status', str(d['status'].upper()))
        
        page.fill('#f_observacao', str(d['observacao']))
        page.fill('#f_endereco', str(d['endereco'])) 
        page.click("#btnSalvar")
        page.wait_for_timeout(300)

@app.post("/run")
def run(request: RunRequest):
    portal_url = open_portal(request.portal_url)
    df = carregar_dados(request.csv_path)
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=request.headless)
        content = browser.new_context()
        page = content.new_page()
        
        page.goto(portal_url)
        
        if request.clean_base:    
            zerar_base(page)
        
        cadastrar_lote(page, df)
        page.wait_for_timeout(5000)
        content.close()
        

    #run
    #ovecorn bot_service:app --host 127.0.0.q --port 8001
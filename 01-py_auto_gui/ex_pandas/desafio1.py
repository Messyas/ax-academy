# ### Altere o código do Exemplo 1 (mostrado em sala de aula) da seguinte forma:
# 1. Gere todas as fichas em um único arquivo.
# 2. Após abrir o notepad retire o time.sleep, mas verifique se o notepad já foi efetivamente aberto.
# 2. Dê o seguinte nome ao arquivo: "PyAutoGUI-Pandas-YYYYMMDD_HHMMSS"
# 3. Adicionar um novo campo Telefone à automação, de modo que ele seja
# lido da planilha e digitado no Bloco de Notas após o campo Cargo.
# Gere uma nova planilha clientes.xlsx adicionando a coluna Telefone.
# 4. Registre no relatório final (clientes_processados.xlsx) a data
# e hora exata em que cada ficha foi gerada, usando a biblioteca datetime.

import pyautogui
import pandas as pd
import time
import datetime
import os

PASTA_ATUAL = os.getcwd()
PLANILHA_ENTRADA = "clientes2.xlsx"
PLANILHA_SAIDA = "clientes_processados.xlsx"  # Voltei para o nome padrão do relatório
INTERVALO = 0.5

def ler_planilha(caminho):
    return pd.read_excel(caminho)

def abrir_bloco_de_notas():
    pyautogui.hotkey("win", "r")
    time.sleep(INTERVALO)
    pyautogui.typewrite("notepad", interval=0.05)
    pyautogui.press("enter")

    # 1. verificar se já abriu o notepad
    abriu = False
    while not abriu:
        titulo = pyautogui.getActiveWindowTitle()
        # Verifica se o título da janela ativa contém o nome do aplicativo
        if titulo and (
                "Notepad" in titulo or "Bloco de Notas" in titulo or "Sem título" in titulo or "Untitled" in titulo):
            abriu = True
        else:
            time.sleep(0.2)

def digitar_dados(nome, email, cargo, telefone):
    pyautogui.typewrite(f"Nome:  {nome}", interval=0.03)
    pyautogui.press("enter")
    pyautogui.typewrite(f"Email: {email}", interval=0.03)
    pyautogui.press("enter")
    pyautogui.typewrite(f"Cargo: {cargo}", interval=0.03)
    pyautogui.press("enter")
    pyautogui.typewrite(f"Telefone: {telefone}", interval=0.03)
    pyautogui.press("enter")
    pyautogui.press("enter")  # separar um clientes
    time.sleep(INTERVALO)

def salvar_e_fechar(nome_arquivo):
    pyautogui.hotkey("ctrl", "s")
    time.sleep(INTERVALO)
    # 3. Agora recebe o nome formatado dinamicamente
    caminho = os.path.join(PASTA_ATUAL, nome_arquivo)
    pyautogui.typewrite(caminho, interval=0.05)
    pyautogui.press("enter")
    time.sleep(INTERVALO)
    pyautogui.hotkey("alt", "f4")
    time.sleep(INTERVALO)

def exportar_relatorio(resultados, caminho):
    df_saida = pd.DataFrame(resultados)
    df_saida.to_excel(caminho, index=False)
    print(f"\nRelatório salvo em: {caminho}")

def main():
    df = ler_planilha(PLANILHA_ENTRADA)
    print("Colunas disponíveis no DataFrame:", df.columns.tolist())

    resultados = []

    abrir_bloco_de_notas()

    for index, row in df.iterrows():
        nome = str(row["Nome"])
        email = str(row["Email"])
        cargo = str(row["Cargo"])
        telefone = str(row["Telefone"])

        # Digita os dados na tela que já está aberta
        digitar_dados(nome, email, cargo, telefone)

        # Captura o datetime exato
        hora_geracao = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        resultados.append({
            "ID": index + 1,
            "Nome": nome,
            "Email": email,
            "Cargo": cargo,
            "Telefone": telefone,
            "Gerado_Em": hora_geracao,
            "Status": "Processado"
        })
        print(f"Ficha digitada para: {nome}")

    #Monta arquivo
    agora = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_arquivo_txt = f"PyAutoGUI-Pandas-{agora}.txt"

    # Salva e fecha o arquivo UMA ÚNICA VEZ, depois que todos foram digitados
    salvar_e_fechar(nome_arquivo_txt)

    # Gera o relatório no Excel
    exportar_relatorio(resultados, PLANILHA_SAIDA)


if __name__ == "__main__":
    main()
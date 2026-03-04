# precisa que esteja instalado a biblioteca openpyxl

import pyautogui
import pandas as pd
import time
import os

PASTA_ATUAL = os.getcwd()
PLANILHA_ENTRADA = "clientes-3.xlsx"
PLANILHA_SAIDA = "clientes_processados.xlsx"
INTERVALO = 0.5


# ─── ATIVIDADE 1: Ler clientes.xlsx
def ler_planilha(caminho):
    return pd.read_excel(caminho)


# ─── ATIVIDADE 2: Abrir Bloco de Notas
def abrir_bloco_de_notas():
    pyautogui.hotkey("win", "r")
    time.sleep(INTERVALO)
    pyautogui.typewrite("notepad", interval=0.05)
    pyautogui.press("enter")
    time.sleep(1)


# ─── ATIVIDADE 3: Digitar dados do cliente
def digitar_dados(nome, email, cargo):
    pyautogui.typewrite(f"Nome:  {nome}", interval=0.03)
    pyautogui.press("enter")
    pyautogui.typewrite(f"Email: {email}", interval=0.03)
    pyautogui.press("enter")
    pyautogui.typewrite(f"Cargo: {cargo}", interval=0.03)
    pyautogui.press("enter")
    time.sleep(INTERVALO)


# ─── ATIVIDADE 4: Salvar ficha_N.txt e fechar
def salvar_e_fechar(index):
    pyautogui.hotkey("ctrl", "s")
    time.sleep(INTERVALO)
    caminho = os.path.join(PASTA_ATUAL, f"ficha_{index + 1}.txt")
    pyautogui.typewrite(caminho, interval=0.05)
    pyautogui.press("enter")
    time.sleep(INTERVALO)
    pyautogui.hotkey("alt", "f4")
    time.sleep(INTERVALO)


# ─── ATIVIDADE 5: Exportar clientes_processados.xlsx
def exportar_relatorio(resultados, caminho):
    df_saida = pd.DataFrame(resultados)
    df_saida.to_excel(caminho, index=False)
    print(f"\nRelatório salvo em: {caminho}")


# ─── MAIN: fluxo principal
def main():
    df = ler_planilha(PLANILHA_ENTRADA)

    resultados = []

    for index, row in df.iterrows():
        nome  = str(row["Nome"])
        email = str(row["Email"])
        cargo = str(row["Cargo"])

        abrir_bloco_de_notas()
        digitar_dados(nome, email, cargo)
        salvar_e_fechar(index)

        resultados.append({
            "ID":     index + 1,
            "Nome":   nome,
            "Email":  email,
            "Cargo":  cargo,
            "Status": "Processado"
        })
        print(f"[OK] Linha {index + 1}: {nome}")

    exportar_relatorio(resultados, PLANILHA_SAIDA)


if __name__ == "__main__":
    main()

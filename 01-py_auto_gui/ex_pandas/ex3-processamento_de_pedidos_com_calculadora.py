# precisa que estejam instaladas as bibliotecas openpyxl e pyperclip

import pyautogui
import pandas as pd
import pyperclip
import time
import subprocess

# ─── CONFIGURAÇÃO
PLANILHA_PEDIDOS = "pedidos-3.xlsx"
RELATORIO_SAIDA  = "relatorio_pedidos.xlsx"
PAUSA            = 0.5


# ─── ATIVIDADE 1: Ler pedidos.xlsx
def ler_planilha(caminho):
    df = pd.read_excel(caminho)
    df.columns = df.columns.str.strip()
    return df


# ─── ATIVIDADE 2: Abrir calculadora
def abrir_calculadora():
    subprocess.Popen("calc")
    time.sleep(1.5)


# ─── ATIVIDADE 3: Fechar calculadora
def fechar_calculadora():
    pyautogui.hotkey("alt", "f4")
    time.sleep(0.5)


# ─── ATIVIDADE 4: Calcular total pela calculadora
def calcular_total(quantidade, preco_unit):
    abrir_calculadora()
    pyautogui.typewrite(str(quantidade), interval=0.05)
    pyautogui.press("*")
    pyautogui.typewrite(str(preco_unit), interval=0.05)
    pyautogui.press("=")
    time.sleep(PAUSA)
    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.3)
    fechar_calculadora()

    valor = pyperclip.paste()
    return float(valor.replace(",", "."))


# ─── ATIVIDADE 5: Aplicar desconto e classificar status
def processar_pedido(pedido_id, produto, qtd, preco, desconto_pct):
    total_bruto    = calcular_total(qtd, preco)
    valor_desconto = round(total_bruto * (desconto_pct / 100), 2)
    total_liquido  = round(total_bruto - valor_desconto, 2)
    status         = "Aprovado" if total_liquido <= 20000 else "Revisao"

    print(f"  Pedido {pedido_id}: R$ {total_liquido:.2f} -> {status}")

    return {
        "ID_Pedido":     pedido_id,
        "Produto":       produto,
        "Quantidade":    qtd,
        "Preco_Unit":    preco,
        "Desconto_%":    desconto_pct,
        "Total_Bruto":   total_bruto,
        "Valor_Desc":    valor_desconto,
        "Total_Liquido": total_liquido,
        "Status":        status
    }


# ─── ATIVIDADE 6: Exportar relatório
def exportar_relatorio(resultados, caminho):
    df_out      = pd.DataFrame(resultados)
    total_geral = df_out["Total_Liquido"].sum()
    df_out.to_excel(caminho, index=False)
    print(f"\nTotal Geral dos Pedidos: R$ {total_geral:.2f}")
    print(f"Relatório salvo em: {caminho}")


# ─── MAIN: fluxo principal
def main():
    df = ler_planilha(PLANILHA_PEDIDOS)

    resultados = []

    for _, row in df.iterrows():
        resultado = processar_pedido(
            pedido_id   = row["ID_Pedido"],
            produto     = row["Produto"],
            qtd         = int(row["Quantidade"]),
            preco       = float(row["Preco_Unitario"]),
            desconto_pct= float(row.get("Desconto_%", 0))
        )
        resultados.append(resultado)

    exportar_relatorio(resultados, RELATORIO_SAIDA)


if __name__ == "__main__":
    main()

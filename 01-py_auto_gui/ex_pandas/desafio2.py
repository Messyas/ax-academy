# Altere o código do Exemplo 2 (mostrado em sala de aula) da seguinte forma:
# Retire a leitura do arquivo Excel, mas gere um dataframe sintético
# (tome como base o que já foi apresentado em aulas anteriores)
#
# Adicionar uma coluna Categoria ao relatório final, classificando
# o pedido com base no valor do Total_Liquido, da seguinte forma:
# Até RS 1.000: "Pequeno"; De RS 1.001 a RS 20.000: "Médio";
# e Acima de RS 20.000: "Grande"
#
# Altere a função exportar_relatorio() para que, além de salvar
# o arquivo, exiba no console um resumo agrupado por status,
# mostrando a quantidade de pedidos e o total líquido de cada
# grupo. Dica: use groupby, len e sum.

import pyautogui
import pandas as pd
import pyperclip
import time
import subprocess
import random

# ─── CONFIGURAÇÃO
RELATORIO_SAIDA  = "relatorio_pedidos.xlsx"
PAUSA = 0.5

# Gera DataFrame Sintético
def gerar_dataframe_sintetico():
    dados = []
    for i in range(1, 5):
        dados.append({
            "ID_Pedido": f"PED-2026-{1000 + i}",
            "Produto": f"Produto {chr(64 + i)}",  # Gera Produto A, C, B...
            "Quantidade": random.randint(1, 15),
            "Preco_Unitario": round(random.uniform(50.0, 3000.0), 2),
            "Desconto_%": random.choice([0.0, 5.0, 10.0])
        })
    return pd.DataFrame(dados)

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

    # Classifica cada categoria de um pedido
    if total_liquido <= 1000:
        categoria = "Pequeno"
    elif total_liquido <= 20000:
        categoria = "Médio"
    else:
        categoria = "Grande"

    print(f"Pedido: {pedido_id}: R$:{total_liquido:.2f}; {status}; ({categoria}).")

    return {
        "ID_Pedido":     pedido_id,
        "Produto":       produto,
        "Quantidade":    qtd,
        "Preco_Unit":    preco,
        "Desconto_%":    desconto_pct,
        "Total_Bruto":   total_bruto,
        "Valor_Desc":    valor_desconto,
        "Total_Liquido": total_liquido,
        "Status":        status,
        "Categoria":     categoria #novo campo
    }


# ─── ATIVIDADE 6: Exportar relatório
def exportar_relatorio(resultados, caminho):
    df_out = pd.DataFrame(resultados)

    # Save to Excel
    df_out.to_excel(caminho, index=False)

    # Resumo agrupado por status
    print("\nResumo Agrupado por Status")
    resumo_status = df_out.groupby('Status').agg(
        Quantidade_Pedidos=('ID_Pedido', 'size'), #size pra contar qta de cada grupo
        Total_Liquido_Agrupado=('Total_Liquido', 'sum')
    ).reset_index()
    print(resumo_status.to_string(index=False))

    total_geral = df_out["Total_Liquido"].sum()
    print(f"\nTotal Geral dos Pedidos: R$: {total_geral:.2f}")
    print(f"Relatorio salvo em: {caminho}")


def main():
    df = gerar_dataframe_sintetico()

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


import pandas as pd

# Caminho da planilha
arquivo = r"C:\Users\W Junior\Desktop\Invest\Ações.xlsx"

# Nome da aba que você quer ler
aba = "Carteira Clear"

# Lendo a aba específica
df = pd.read_excel(arquivo, sheet_name=aba)

# Informe aqui os nomes das colunas da sua planilha
col_ticker = "Ticker"
col_quantidade = "Qtdade"
col_preco_compra = "Valor Compra"
col_preco_venda = "Valor Venda"

# Calcula o custo total e o valor de venda
df["CustoTotal"] = df[col_quantidade] * df[col_preco_compra]
df["ValorVenda"] = df[col_quantidade] * df[col_preco_venda]

# Lucro ou prejuízo por operação
df["Resultado"] = df["ValorVenda"] - df["CustoTotal"]

# Consolidado por ticker
consolidado = df.groupby(col_ticker)[["CustoTotal", "ValorVenda", "Resultado"]].sum()

# Mostra o resultado
print("Consolidado de Lucro/Prejuízo:")
print(consolidado)

# Resultado total da carteira
resultado_total = consolidado["Resultado"].sum()
print("\nResultado total da carteira:", resultado_total)

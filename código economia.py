import pandas as pd

import pandas as pd

# 1. Carregar a base pulando as primeiras linhas de título e ajustando o encoding
# O parâmetro 'skiprows=5' ignora os cabeçalhos duplos e pega a linha dos dados
# (se ainda pegar linhas de texto, ajuste o skiprows para 4 ou 6)
df = pd.read_csv("dados.csv", sep=";", encoding="latin1", skiprows=5, header=None)

# 2. Definir nomes claros e diretos para todas as 23 colunas
novas_colunas = [
    "Localidade",
    "Total_Medio", "Total_Mediano",
    "Homem_Medio", "Homem_Mediano",
    "Mulher_Medio", "Mulher_Mediano",
    "Branca_Medio", "Branca_Mediano",
    "Parda_Medio", "Parda_Mediano",
    "Preta_Medio", "Preta_Mediano",
    "Preta_Parda_Medio", "Preta_Parda_Mediano",
    "Homem_Branco_Medio", "Homem_Branco_Mediano",
    "Homem_Preto_Pardo_Medio", "Homem_Preto_Pardo_Mediano",
    "Mulher_Branca_Medio", "Mulher_Branca_Mediano",
    "Mulher_Preta_Parda_Medio", "Mulher_Preta_Parda_Mediano"
]

# Garantir que a quantidade de colunas bate com a tabela
if len(df.columns) == len(novas_colunas):
    df.columns = novas_colunas

# 3. Remover linhas totalmente vazias ou com notas de rodapé do IBGE
df = df.dropna(subset=["Localidade"])

# 4. Limpar e converter os valores das colunas numéricas de texto (str) para números (float)
colunas_numericas = df.columns[1:] # Pega da segunda coluna em diante

for col in colunas_numericas:
    # Remove espaços em branco (ex: "2 017" vira "2017") e substitui vírgula por ponto
    df[col] = df[col].astype(str).str.replace(" ", "").str.replace(",", ".")
    # Converte para número e transforma qualquer texto inválido em Nulo (NaN)
    df[col] = pd.to_numeric(df[col], errors="coerce")

# 5. Conferir o resultado final
print("--- PRIMEIRAS LINHAS DA BASE TRATADA ---")
print(df.head())

print("\n--- INFORMAÇÕES DOS TIPOS DE DADOS ---")
df.info()

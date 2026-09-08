import pandas as pd
import plotly.express as px
import streamlit as st

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Dashboard Economia - IBGE 2024",
    layout="wide"
)

st.title("📊 Dashboard de Rendimento Domiciliar per capita (IBGE 2024)")

# Tenta carregar o arquivo dados.csv localmente
try:
    df = pd.read_csv("dados.csv", sep=";", encoding="latin1", skiprows=5, header=None)

    # 1. Renomear as 23 colunas oficiais
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
    if len(df.columns) == len(novas_colunas):
        df.columns = novas_colunas

    # 2. Limpeza de notas de rodapé do IBGE e duplicatas
    df = df.dropna(subset=["Total_Medio"])
    df = df.drop_duplicates()

    # 3. Conversão das colunas de texto para números decimais (float)
    colunas_numericas = df.columns[1:]
    for col in colunas_numericas:
        df[col] = df[col].astype(str).str.replace(" ", "").str.replace(",", ".")
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # --- INDICADORES / MÉTRICAS PRINCIPAIS ---
    st.subheader("📌 Resumo Geral da Base")
    col1, col2, col3 = st.columns(3)
    col1.metric("Quantidade de Locais Analisados", df.shape[0])
    col2.metric("Total de Colunas", df.shape[1])
    
    # Pega o rendimento médio do Brasil (primeira linha)
    rendimento_brasil = df[df["Localidade"].str.strip() == "Brasil"]["Total_Medio"].values[0]
    col3.metric("Rendimento Médio Brasil", f"R$ {rendimento_brasil:,.2f}")

    st.markdown("---")

    # --- VISUALIZAÇÃO DA TABELA ---
    st.subheader("👀 Tabela de Dados Trata")
    st.dataframe(df, use_container_width=True)

    # --- GRÁFICO INTERATIVO ---
    st.subheader("📈 Comparativo: Homem Branco vs. Mulher Preta/Parda (Rendimento Médio)")
    
    # Filtra as primeiras 10 localidades para o gráfico ficar limpo
    fig = px.bar(
        df.head(10), 
        x="Localidade", 
        y=["Homem_Branco_Medio", "Mulher_Preta_Parda_Medio"],
        barmode="group",
        labels={"value": "Rendimento (R$)", "variable": "Categoria", "Localidade": "Estado/Região"},
        title="Diferença de Rendimento por Localidade (R$)"
    )
    st.plotly_chart(fig, use_container_width=True)

except FileNotFoundError:
    st.error("Erro: O arquivo 'dados.csv' não foi encontrado na mesma pasta do projeto.")
st.set_page_config(
    page_title="Dashboard Economia - Juan, Victor e Aquiles",
    page_icon="📊",
    layout="wide",
)
st.title("stream lit de juan victor e aquiles do 2CDD01")
st.title("📊 Dashboard de Rendimento Domiciliar per capita (IBGE 2024)")

# 1. Carregar os dados do arquivo CSV
try:
  df = pd.read_csv(
      "dados.csv", sep=";", encoding="latin1", skiprows=5, header=None
  )
except Exception as e:
  st.error(
      "❌ Não foi possível carregar o arquivo 'dados.csv'. Verifique se ele"
      " está na mesma pasta do app.py"
  )
  st.stop()

# 2. Manter apenas as 23 primeiras colunas do IBGE
df = df.iloc[:, :23]

# 3. Nomear todas as colunas
novas_colunas = [
    "Localidade",
    "Total_Medio",
    "Total_Mediano",
    "Homem_Medio",
    "Homem_Mediano",
    "Mulher_Medio",
    "Mulher_Mediano",
    "Branca_Medio",
    "Branca_Mediano",
    "Parda_Medio",
    "Parda_Mediano",
    "Preta_Medio",
    "Preta_Mediano",
    "Preta_Parda_Medio",
    "Preta_Parda_Mediano",
    "Homem_Branco_Medio",
    "Homem_Branco_Mediano",
    "Homem_Preto_Pardo_Medio",
    "Homem_Preto_Pardo_Mediano",
    "Mulher_Branca_Medio",
    "Mulher_Branca_Mediano",
    "Mulher_Preta_Parda_Medio",
    "Mulher_Preta_Parda_Mediano",
]
df.columns = novas_colunas

# 4. Limpeza de números (remove espaços e troca vírgula por ponto)
for col in df.columns[1:]:
  df[col] = (
      df[col]
      .astype(str)
      .str.replace(r"\s+", "", regex=True)
      .str.replace(",", ".")
  )
  df[col] = pd.to_numeric(df[col], errors="coerce")

df["Localidade"] = df["Localidade"].astype(str).str.strip()

# 5. Lista dos 27 Estados do Brasil
estados = [
    "Rondônia",
    "Acre",
    "Amazonas",
    "Roraima",
    "Pará",
    "Amapá",
    "Tocantins",
    "Maranhão",
    "Piauí",
    "Ceará",
    "Rio Grande do Norte",
    "Paraíba",
    "Pernambuco",
    "Alagoas",
    "Sergipe",
    "Bahia",
    "Minas Gerais",
    "Espírito Santo",
    "Rio de Janeiro",
    "São Paulo",
    "Paraná",
    "Santa Catarina",
    "Rio Grande do Sul",
    "Mato Grosso do Sul",
    "Mato Grosso",
    "Goiás",
    "Distrito Federal",
]

# 6. Filtrar apenas os estados e ordenar
df_estados = df[df["Localidade"].isin(estados)].drop_duplicates(
    subset=["Localidade"], keep="first"
)
df_estados_ordenado = df_estados.sort_values(by="Total_Medio", ascending=True)

# 7. Cartões de Destaque
menor_estado = df_estados_ordenado.iloc[0]
maior_estado = df_estados_ordenado.iloc[-1]

st.subheader("📌 Destaques")
col1, col2 = st.columns(2)
col1.metric(
    "Maior Rendimento Médio",
    f"{maior_estado['Localidade']}",
    f"R$ {maior_estado['Total_Medio']:,.2f}",
)
col2.metric(
    "Menor Rendimento Médio",
    f"{menor_estado['Localidade']}",
    f"R$ {menor_estado['Total_Medio']:,.2f}",
)

st.markdown("---")

# =========================================================
# GRÁFICO 1: RANKING GERAL DOS ESTADOS
# =========================================================
st.subheader("📈 1. Ranking do Rendimento Médio Geral por Estado")

fig1 = px.bar(
    df_estados_ordenado,
    x="Total_Medio",
    y="Localidade",
    orientation="h",
    labels={"Total_Medio": "Rendimento Médio (R$)", "Localidade": "Estado"},
    title="Rendimento Domiciliar per capita por Estado",
    height=600,
)

st.plotly_chart(fig1, use_container_width=True)

st.markdown("---")

# =========================================================
# GRÁFICO 2: COMPARATIVO POR GÊNERO E COR/RAÇA
# =========================================================
st.subheader("📊 2. Média de Rendimento por Gênero e Cor/Raça em cada Estado")

# Reorganizar dados em formato longo
df_etnias = df_estados.melt(
    id_vars=["Localidade"],
    value_vars=[
        "Homem_Branco_Medio",
        "Homem_Preto_Pardo_Medio",
        "Mulher_Branca_Medio",
        "Mulher_Preta_Parda_Medio",
    ],
    var_name="Perfil_Cod",
    value_name="Rendimento",
)

mapeamento = {
    "Homem_Branco_Medio": "Homem Branco",
    "Homem_Preto_Pardo_Medio": "Homem Preto/Pardo",
    "Mulher_Branca_Medio": "Mulher Branca",
    "Mulher_Preta_Parda_Medio": "Mulher Preta/Parda",
}
df_etnias["Perfil"] = df_etnias["Perfil_Cod"].map(mapeamento)

fig2 = px.bar(
    df_etnias,
    x="Localidade",
    y="Rendimento",
    color="Perfil",
    barmode="group",
    title="Rendimento Médio por Sexo e Cor/Raça nos 27 Estados",
    labels={"Localidade": "Estado", "Rendimento": "Rendimento Médio (R$)"},
    height=600,
)
fig2.update_layout(xaxis_tickangle=-45)

st.plotly_chart(fig2, use_container_width=True)

st.markdown("#### este dashboard ira apresentar: ")
st.markdown("""##### &nbsp;&nbsp;&nbsp;&nbsp; O gráfico apresenta a média do rendimento financeiro mensal por morador em cada um dos 27 estados do Brasil, dividindo as informações por grupos de gênero e cor/raça (homens brancos, homens pretos/pardos, mulheres brancas e mulheres pretas/pardas).
##### &nbsp;&nbsp;&nbsp;&nbsp; A ferramenta permite comparar lado a lado como os ganhos financeiros se distribuem entre esses diferentes perfis populacionais dentro de cada estado do país.
#####  &nbsp;&nbsp;&nbsp;&nbsp; Analisando os dados, observa-se uma disparidade constante em todas as Unidades da Federação: os maiores rendimentos médios estão concentrados no grupo de homens brancos, seguidos pelas mulheres brancas, enquanto os menores valores médios aparecem nos grupos de homens e mulheres pretos ou pardos. 
##### &nbsp;&nbsp;&nbsp;&nbsp; Além disso, nota-se uma variação regional expressiva, na qual os estados do Sul, Sudeste e o Distrito Federal registram valores médios superiores aos encontrados nos estados das regiões Norte e Nordeste, independentemente do perfil analisado.
"""
)
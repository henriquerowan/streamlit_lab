# --- Importe as bibliotecas de dados e streamlit
import numpy as np
import pandas as pd
import streamlit as st  

# --- Título da página
st.title('Retorno da empresa')

# --- Upload de arquivo CSV
st.subheader('📂 Upload de Arquivo CSV')
uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")
if uploaded_file is not None:
    try:
        df_uploaded = pd.read_csv(uploaded_file)
        st.success("Arquivo carregado com sucesso!")
        st.write("As 5 primeiras linhas do arquivo:")
        st.dataframe(df_uploaded.head(5))

        # --- Plotar o grágico de linha dos investimentos
        st.subheader('📈 Gráfico de Linha')
        df_investimento=df_uploaded[['TV','Radio','Newspaper']]
        st.line_chart(df_investimento)

        # --- Plotar o gráfico de barras do retorno
        st.subheader('📊 Gráfico de Barras')
        df_retorno=df_uploaded[['Sales']]
        st.bar_chart(df_retorno)
    except Exception as e:
        st.error(f"Erro ao ler o arquivo: {e}")

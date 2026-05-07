# --- Importar as bibliotecas para dados e gráficos
import numpy as np
import pandas as pd
import streamlit as st
#import matplotlib.pyplot as plt 

# --- Título da página
st.title('Aula 03 - Dados e Gráficos')

# --- Criar um cabeçalho
st.header('Gerando e Exibindo Dados Aleatórios')

# --- Gerar um DataFrame com dados aleatórios
data = np.random.randn(20, 3)  # 20 linhas e 3 colunas
df = pd.DataFrame(data, columns=['A', 'B', 'C'])    

# --- Exibir o DataFrame de forma interativa
st.subheader('DataFrame Gerado interativamente')
st.dataframe(df)




# --- Exemplo com upload de arquivo
st.subheader('📂 Upload de Arquivo CSV')
uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")
if uploaded_file is not None:
    # --- insira um try para ler o arquivo e exibir os dados
    try:
        df_uploaded = pd.read_csv(uploaded_file)
        # --- Criação de duas colunas
        col1, col2 = st.columns(2)

        # --- Gráfico de linha
        with col1:
            st.markdown('### 📈 Gráfico de Linha')
            st.line_chart(df_uploaded)

        # --- Gráfico de barras
        with col2:
            st.markdown('### 📊 Gráfico de Barras')
            st.bar_chart(df_uploaded)

    except Exception as e:
        st.error(f"Erro ao ler o arquivo: {e}")
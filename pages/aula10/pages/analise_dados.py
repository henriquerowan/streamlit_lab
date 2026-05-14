# --- Importar o Streamlit ---
import streamlit as st
import plotly.express as px
from utils.carregar_dados import carregar_dados 

def analise_dados():
    """Função responsável por exibir o conteúdo da página de análise de dados."""
    st.header('Análise de Dados')
    
    # Carregar os dados usando a função do módulo utils
    df = carregar_dados()
    
    st.subheader('Dados Carregados')
    st.dataframe(df)
    
    st.subheader('Gráfico de Barras')
    fig = px.bar(df, x='col_3', y='col_2', title='Gráfico de Dispersão')
    st.plotly_chart(fig)
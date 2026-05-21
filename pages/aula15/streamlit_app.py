# --- Importar o streamlit ---
import streamlit as st
import numpy as np  
import pandas as pd

# -- configurações da página ---
st.set_page_config(layout="wide", page_title="Aula 15 - DataEditor")

# --- Título ---
st.title("Aula 15 - DataEditor na prática")

dados = pd.DataFrame({
    "produtos": ["Notebook", "Smartphone", "Tablet", "Monitor", "Teclado", "Mouse", "Impressora", "Cadeira Gamer", "Mesa Escritório", "Fone de Ouvido"],
    "preco": [4500, 2800, 1800, 1200, 250, 120, 950, 1400, 900, 350],
    "quantidade": [12, 25, 18, 10, 45, 60, 8, 6, 4, 30],  
    "Ativo": [False, False, False, False, False, False, False, False, False, False]  

})

# --- Exibir o DataFrame editável ---
st.subheader("Tabela de Produtos")

# --- Editor de dados --- #
dados_editados = st.data_editor(
    dados,
    num_rows="dynamic",
    use_container_width=True,
    hide_index=True,

    column_config={

        "produtos": st.column_config.TextColumn(
            label="📦 Produto",
            max_chars=30,
            help="Nome do produto"
        ),

        "preco": st.column_config.NumberColumn(
            label="💰 Preço",
            min_value=0.0,
            format="R$ %.2f",
            help="Preço do produto"
        ),

        "quantidade": st.column_config.NumberColumn(
            label="📊 Quantidade",
            min_value=0,
            help="Quantidade em estoque"
        ),

        "Ativo": st.column_config.CheckboxColumn(
            label="✅ Ativo",
            help="Indica se o produto está ativo"
        )
    }
)


# --- Exibir os dados editados ---
st.subheader("Dados Editados")
st.dataframe(dados_editados)    

# --- Conversão do DataFrame para CSV --- #
st.subheader("Download dos Dados Editados")
csv = dados_editados.to_csv(index=False).encode('utf-8')
# --- Botão para o download do DataFrame atualizado --- #
st.download_button(
    label='Baixar dados editados (CSV)',
    data=csv,
    file_name='dados_editados.csv',
    mime='text/csv'
)
# --- Importar as bibliotecas de dados e streamlit --- #
import numpy as np
import pandas as pd
import streamlit as st

# --- Configuração da página --- #
st.set_page_config(
    layout='wide',
    page_title='Aula 14 - Abas no Streamlit'
)

# --- Título da página --- #
st.title('📚 Aula 14 - Abas no Streamlit')

# --- Criar as abas --- #
aba1, aba2, aba3 = st.tabs(
    ['📈 Gráficos', '📝 Formulário', '🗂️ Dados']
)

# ---------------------------------------------------------------- #
# --- ABA 1: GRÁFICOS -------------------------------------------- #
# ---------------------------------------------------------------- #

with aba1:

    st.header('📊 Gráficos')

    # --- Dados gráfico de linha --- #
    dados_linha = pd.DataFrame({
        'semana': ['S1', 'S2', 'S3', 'S4', 'S5'],
        'vendas': [100, 150, 100, 200, 250]
    }).set_index('semana')

    st.subheader('📈 Gráfico de Linhas')
    st.line_chart(dados_linha)

    # --- Dados gráfico de barras --- #
    dados_barra = pd.DataFrame({
        'produto': [
            'Notebook',
            'Smartphone',
            'Tablet',
            'Monitor'
        ],
        'vendas': [300, 500, 200, 400]
    }).set_index('produto')

    st.subheader('📊 Gráfico de Barras')
    st.bar_chart(dados_barra)

    # --- Dados gráfico de área --- #
    dados_area = pd.DataFrame(
        np.random.rand(20, 3),
        columns=['A', 'B', 'C']
    )

    st.subheader('🌊 Gráfico de Área')
    st.area_chart(dados_area)

with aba2:

    st.header('📝 Formulário')

    with st.form('formulario'):
        nome = st.text_input('Nome')
        email = st.text_input('Email')
        idade = st.number_input('Idade', min_value=0, max_value=120)
        submit = st.form_submit_button('Enviar')

    if submit:
        st.success(f'Formulário enviado! Nome: {nome}, Email: {email}, Idade: {idade}')

with aba3:

    st.header('🗂️ Visualização de Dados')

    st.write(
        '📊 Tabela e filtros simples para explorar os dados.'
    )

    # --- Criar um DataFrame de exemplo --- #
    dados = pd.DataFrame({
        'produto': [
            'Notebook',
            'Smartphone',
            'Tablet',
            'Monitor'
        ],

        'preco': [
            4500,
            2500,
            1500,
            1200
        ],

        'estoque': [
            10,
            20,
            15,
            5
        ]
    })

    # --- Slider de intervalo --- #
    filtro_preco = st.slider(
        '💰 Filtrar por faixa de preço',
        min_value=0,
        max_value=5000,
        value=(0, 5000)
    )

    # --- Filtrar DataFrame --- #
    dados_filtrados = dados[
        (dados['preco'] >= filtro_preco[0]) &
        (dados['preco'] <= filtro_preco[1])
    ]

    # --- Exibir dados --- #
    st.dataframe(dados_filtrados)
 
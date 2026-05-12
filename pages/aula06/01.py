# --- Importar streamlit and datetime  
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, time, timedelta    

# --- Título da página
st.title('Widgets Avançados de Entrada')

st.header('Seleção de opções com Multiselect')

# --- Caixa de seleção simples
option = st.selectbox(
    label='Selecione sua fruta favorita:',
    options=['', 'Maçã', 'Banana', 'Laranja', 'Uva', 'Abacaxi']
)
st.write(f'Você selecionou: {option}')

# --- Caixa de seleção múltipla
options = st.multiselect(
    label='Selecione suas frutas favoritas:',
    options=['Maçã', 'Banana', 'Laranja', 'Uva', 'Abacaxi'],
    placeholder='Escolha uma ou mais frutas'
)
st.write(f'Você selecionou: {options}')

# --- Exemplo de radio button
st.header('Seleção de opções com Radio Buttons')
radio_option = st.radio(
    label='Qual o seu gênero:',
    options=['Masculino', 'Feminino', 'Outro']
)
st.write(f'Você escolheu: {radio_option}') 

# --- Exemplo de widget de data
st.header('Data de nascimento')
date = st.date_input(
    label='Selecione uma data:',
    value=datetime.now().date(),
    min_value=datetime(1900, 1, 1).date(),
    max_value=datetime.now().date()
)
st.write(f'Você selecionou a data: {date}') 

# --- Exemplo de widget de hora
st.header('Hora de início')
hora_min = st.time_input(
    label='Selecione um horário:',
    value=time(hour=9, minute=0)
)
st.write(
    f'Você selecionou o horário: {hora_min.strftime("%H:%M")}'
)

# --- Caixa de seleção e botão de download
st.header('📥 Download de dados')

termos = st.checkbox('Aceito os termos e condições')

if termos:

    st.success('Obrigado por aceitar os termos!')

    # --- Abrir arquivo
    with open('dados_aleatorios.csv', 'rb') as file:

        st.download_button(
            label='📥 Baixar dados de exemplo',
            data=file,
            file_name='dados_aleatorios.csv',
            mime='text/csv'
        )

else:
    st.warning(
        'Você precisa aceitar os termos para baixar os dados.'
    )

# --- Formularios com st.form
st.header('Formulário de contato')
with st.form(key='contact_form'):
    name = st.text_input('Nome')
    email = st.text_input('Email')
    message = st.text_area('Mensagem')

    submit_button = st.form_submit_button(label='Enviar')
    if submit_button:
        st.success('Mensagem enviada com sucesso!')
        st.write(f'Nome: {name}')
        st.write(f'Email: {email}')
        st.write(f'Mensagem: {message}')    
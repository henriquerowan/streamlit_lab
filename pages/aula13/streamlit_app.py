# --- Importar as bibliotecas de dados e streamlit
import numpy as np
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

# --- Configuração da página do site --- #
st.set_page_config(layout='wide')

# --- Titulo da pagina
st.title('st.metric() na prática')

# --- Criar um conjunto de dados fictícios --- #
np.random.seed(42)

dados = pd.DataFrame({
    'mes': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
    'vendas_atual': np.random.randint(8000, 15000, 6),
    'vendas_anterior': np.random.randint(7000, 14000, 6)
})

# --- Calculo das metricas principais --- #
total_vendas_atual = dados['vendas_atual'].sum()
total_vendas_anterior = dados['vendas_anterior'].sum()
delta_vendas = total_vendas_atual - total_vendas_anterior
percentual_variacao = (delta_vendas / total_vendas_anterior) * 100

# --- Colocar as metricas na tela --- #
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label='Total Vendas Atual', value=f'R$ {total_vendas_atual:,.2f}', delta=f'R$ {delta_vendas:,.2f}')
with col2:
    st.metric(label='Variação (%)', value=f'{percentual_variacao:.2f}%', delta=f'{percentual_variacao:.2f}%')

media_mensal = dados['vendas_atual'].mean()
media_mensal_anterior = dados['vendas_anterior'].mean()
delta_media = media_mensal - media_mensal_anterior
percentual_variacao_media = (delta_media / media_mensal_anterior) * 100
with col3:
    st.metric(label='Média Mensal Atual', value=f'R$ {media_mensal:,.2f}', delta=f'R$ {delta_media:,.2f}')  

# --- Selecionar quais dados serao lidos na metrica
st.divider()
st.subheader('Seleção de dados para a métrica')
mes_selecionado = st.selectbox('Selecione o mês para exibir as métricas', dados['mes'])
linha_mes=dados[dados['mes']==mes_selecionado]
vendas_atual_mes = linha_mes['vendas_atual'].values[0]
vendas_anterior_mes = linha_mes['vendas_anterior'].values[0]
delta_mes = vendas_atual_mes - vendas_anterior_mes
percentual_variacao_mes = (delta_mes / vendas_anterior_mes) * 100

delta_formatado=''
if delta_mes < 0:
    delta_formatado = f'-R$ {delta_mes:,.2f}'
else:
    delta_formatado = f'R$ {delta_mes:,.2f}'

st.metric(label=f'Vendas em {mes_selecionado}', value=f'R$ {vendas_atual_mes:,.2f}', delta=delta_formatado) 

# --- Colocar graficos junto com as metricas
st.divider()
st.subheader('st.metrics() com graficos embutidos')

# --- gerador de numeros aleatorios para o grafico
gerador=rng(4)

# --- variacao dos dados
mudancas = list(gerador.standard_normal(20))

# --- Série acumulada da evolução do indicador
dados = [sum(mudancas[:i]) for i in range(len(mudancas))]

# --- Delta 
delta = round(dados[-1],  2)

 # --- Colocar as métricas com os graficos
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label='Indicador Atual', 
              value=10, 
              delta=f'{delta:.2f}',
              chart_data=dados,
              chart_type='line',
              border=True)

with col2:
    st.metric(label='Indicador area', 
              value=10, 
              delta=f'{delta:.2f}',
              chart_data=dados,
              chart_type='area',
              border=True)

with col3:
    st.metric(label='Indicador barra', 
              value=10, 
              delta=f'{delta:.2f}',
              chart_data=dados,
              chart_type='bar',
              border=True)
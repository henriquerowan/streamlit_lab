# --- Import streamlit
import streamlit as st 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns
import altair as alt
import plotly.express as px


# --- Título da página
st.title('Visualização de Dados avançada')


# --- Dados de exemplo
df = pd.DataFrame({
    'data': pd.to_datetime(pd.date_range(start='2025-01-01', periods=100)),
    'valor_a':np.random.rand(100).cumsum(),
    'valor_b':np.random.rand(100).cumsum()+10
})

# --- Exemplo com matplotlib
st.header('Gráfico com Matplotlib')
fig, ax = plt.subplots()
ax.plot(df['data'], df['valor_a'], label='Valor A')
ax.plot(df['data'], df['valor_b'], label='Valor B')
ax.set_title('Gráfico de Linhas')
ax.set_xlabel('Data')
ax.set_ylabel('Valor')
ax.legend()
st.pyplot(fig)

# --- Exemplo com Plotly
st.header('Gráfico com Plotly')
fig = px.line(df, x='data', y=['valor_a', 'valor_b'], title='Gráfico de Linhas')
st.plotly_chart(fig)

# --- Exemplo com Altair
st.header('Gráfico com Altair')
chart = alt.Chart(df).mark_line().encode(
    x='data',
    y='valor_a',
    color=alt.value('blue')
).properties(title='Valor A')
chart_b = alt.Chart(df).mark_line().encode(
    x='data',
    y='valor_b',
    color=alt.value('orange')
).properties(title='Valor B')
st.altair_chart(chart + chart_b, use_container_width=True)
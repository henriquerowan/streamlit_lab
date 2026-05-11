# --- Importar as bibliotecas
import time
import streamlit as st  

# --- Título da página 
st.title('Otimizando com caching')

@st.cache_data(ttl=10)
def simular_operacao_demorada(parametro):
    st.write('Simulando uma operação demorada para o parâmetro: {parametro}')
    time.sleep(3)  # Simula uma operação que demora 3 segundos
    return f'Resultado da operação demorada para {parametro}: {time.time()}'

# --- Simular o parametro
parametro =st.slider('Escolha um parâmetro', 0, 10, 5)

resultado = simular_operacao_demorada(parametro)
st.write(resultado)

# --- Botão para limpar o cache manualmente
if st.button('Limpar Cache'):
    st.cache_data.clear()
    st.write('Cache limpo!')
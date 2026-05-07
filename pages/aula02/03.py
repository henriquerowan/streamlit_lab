# --- Importe o streamlit
import streamlit as st

# --- Título da página
st.title('🧮 Calculadora')

# --- Entrada de números
num1 = st.number_input(
    label='Digite o primeiro número',
    value=0.0
)

num2 = st.number_input(
    label='Digite o segundo número',
    value=0.0
)

# --- Inicializa variáveis
resultado = None
operacao = ''

# --- Criação das colunas
col1, col2, col3, col4 = st.columns(4)

# --- Botões em colunas separadas
with col1:
    if st.button('➕ Soma'):
        resultado = num1 + num2
        operacao = 'Soma'

with col2:
    if st.button('➖ Subtração'):
        resultado = num1 - num2
        operacao = 'Subtração'

with col3:
    if st.button('✖️ Multiplicação'):
        resultado = num1 * num2
        operacao = 'Multiplicação'

with col4:
    if st.button('➗ Divisão'):
        operacao = 'Divisão'

        if num2 != 0:
            resultado = num1 / num2
        else:
            st.error('Erro: Divisão por zero não é permitida.')

# --- Exibir resultado
if resultado is not None:
    st.success(
        f'📌 Operação realizada: {operacao}\n\n'
        f'🧾 Resultado entre {num1} e {num2}: {resultado}'
    )
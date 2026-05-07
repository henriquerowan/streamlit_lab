# --- Importe o streamlit
import streamlit as st
# --- Título da página
st.title('Calculadora')
# --- Entrada de números
num1 = st.number_input(label='Digite o primeiro número', value=0.0)
num2 = st.number_input(label='Digite o segundo número', value=0.0)
# --- Operações matemáticas
operacao = st.selectbox(label='Selecione a operação', options=['+', '-', '*', '/'])
# --- Botão para calcular
if st.button('Calcular'):
    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            st.error('Erro: Divisão por zero não é permitida.')
            resultado = None
    # --- Exibir o resultado
    if resultado is not None:
        st.success(f'O resultado de {num1} {operacao} {num2} é: {resultado}')
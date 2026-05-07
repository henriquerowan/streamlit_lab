# --- Importar o streamlit --- #
import streamlit as st

# --- Título da página --- #
st.title("Minha Primeira Página")

# --- Cabeçalho --- #
st.header("Bem-vindo à minha primeira página no Streamlit!")

# --- subcabeçalho --- #
st.subheader("Este é um subcabeçalho")

# --- Texto --- #
st.write("Este é um texto simples para demonstrar o uso do Streamlit.")

# --- Markdown --- #
st.markdown("""
**Texto em negrito** e 
*texto em itálico* usando Markdown,
e até mesmo listas:
- Item 1
- Item 2
""")

# --- Exibir um texto --- #
st.text("Este é um texto exibido usando st.text()")
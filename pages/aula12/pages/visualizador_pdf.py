# --- Importar o Streamlit
import streamlit as st

# --- Configurações da página
st.set_page_config(page_title="Visualizador de PDF", page_icon="📄", layout="centered")

# --- Título da página
st.title("Visualizador de PDF")

# --- Campo para selecionar o arquivo PDF
pdf_file = st.file_uploader("Selecione um arquivo PDF para visualizar", type="pdf")
# --- Exibir o PDF selecionado
if pdf_file:
    st.write("Visualizando o PDF selecionado:")
    st.pdf(pdf_file, height=850)
else:
    st.warning("Por favor, selecione um arquivo PDF para visualizar.")  
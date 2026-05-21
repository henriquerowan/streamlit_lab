# --- Importar streamlit
import streamlit as st

from obter_pdfs import obter_pdfs
from juntar_pdf import juntar_pdfs

# --- Configurações da página
st.set_page_config(page_title="Juntar PDFs", page_icon="📄", layout='centered')

# --- Título da página
st.title("Juntar PDFs")

# --- Campo para selecionar o nome do arquivo final
nome_arquivo = st.text_input("Digite o nome do arquivo final (sem extensão):", "pdfs_merged")
# --- Botão para selecionar os arquivos PDF
pdfs = st.file_uploader("Selecione os arquivos PDF para juntar", type="pdf", accept_multiple_files=True)

# --- Criar as colunas para os botões
colunas = st.columns(5)

# --- Botão para juntar os PDFs
with colunas[2]:
    if st.button("Juntar PDFs"):
        if pdfs:
            # --- Obter os bytes dos PDFs selecionados
            pdf_bytes_list = obter_pdfs(pdfs)
            # --- Juntar os PDFs e obter os bytes do arquivo final
            pdf_final_bytes = juntar_pdfs(pdf_bytes_list)
            # --- Criar um link para download do arquivo final
            st.download_button(label="Download do PDF Final", data=pdf_final_bytes, file_name=f"{nome_arquivo}.pdf", mime="application/pdf")
        else:
            st.warning("Por favor, selecione pelo menos um arquivo PDF para juntar.")    

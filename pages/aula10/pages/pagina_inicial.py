# --- Importar o Streamlit ---
import streamlit as st

def pagina_inicial():
    """Função responsável por exibir o conteúdo da página inicial."""
    st.header('Bem-vindo à Página Inicial')
    st.write('Esta é a página inicial do aplicativo. Use a barra lateral para navegar entre as páginas.')
    st.info('Use a barra lateral para acessar a página de análise e visualizar os dados carregados.')
    

# --- Importar o Streamlit ---
import streamlit as st
from pages import pagina_inicial, analise_dados

# --- Titulo do site
#st.title('Aplicativo com multiplas páginas')

st.sidebar.title('Navegação')
page = st.sidebar.radio('Ir para:', ['Página Inicial', 'Análise'])


if page == 'Página Inicial':
    pagina_inicial.pagina_inicial()
elif page == 'Análise': 
    analise_dados.analise_dados()




# --- Importar o Streamlit
import streamlit as st 

# --- Criar um menu lateral para navegar entre as páginas
pg=st.navigation(
    [st.Page(title="Juntar PDFs", page="./pages/pdf_merger.py", default=True),
     st.Page(title="Visualizador de PDF", page="./pages/visualizador_pdf.py")]
)

pg.run()
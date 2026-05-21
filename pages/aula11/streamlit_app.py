# --- importar o streamlit
import streamlit as st

pg = st.navigation(
    [
        st.Page(
            page='./pages/home.py',
            title='Home',
            icon='🏠',
            default=True  # <- define como página inicial
        ),

        st.Page(
            page='./pages/pag2.py',
            title='Pagina 2',
            icon='📄'
        ),

        st.Page(
            page='./pages/pag3.py',
            title='Pagina 3',
            icon='📊'
        )
    ],
    position='top'
)

pg.run()
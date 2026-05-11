# --- importando streamlit
import streamlit as st 

# -- Importando Numpy
import numpy as np

st.header('Gerador de numero aleatório entre sessões')

if st.button('Gerar'):
    if 'numero_aleatorio' in st.session_state:
        st.session_state.numero_aleatorio_anterior = st.session_state.numero_aleatorio
        st.session_state.numero_aleatorio =np.nan
    st.session_state.numero_aleatorio = int(np.random.rand()*100)
    st.write(f'Sessão atual: {st.session_state.numero_aleatorio}')

# -- caching da sessão anterior
if 'numero_aleatorio_anterior' in st.session_state:
    st.write(f'Sessão anterior: {st.session_state.numero_aleatorio_anterior}')
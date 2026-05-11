# --- Importar o streamlit
import streamlit as st

# --- Título da página
st.title('Contador e Estado da Sessão')

# --- Criar um contador usando o estado da sessão
if 'contador' not in st.session_state:
    st.session_state.contador = 0

def incrementar_contador():
    st.session_state.contador += 1

# --- Criar um botão para incrementar o contador
if st.button('Incrementar'):
    incrementar_contador()

# --- Exibir o valor do contador
st.write(f'Valor do contador: {st.session_state.contador}')


# --- Exemplo de formulario que mantem o estado da sessão
st.header('Formulário com Estado da Sessão')
if 'nome' not in st.session_state:
    st.session_state.nome = ''

def atualizar_nome():
    st.session_state.nome = st.session_state.input_nome

# --- Criar um formulário
with st.form(key='form_nome'):
    st.text_input('Digite seu nome:', key='input_nome')
    st.form_submit_button('Atualizar Nome', on_click=atualizar_nome)

# --- Exibir o nome atual
st.write(f'Nome atual: {st.session_state.nome}')
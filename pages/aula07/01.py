# --- Importar streamlit and time
import streamlit as st
import time

# --- Configurações da página
st.set_page_config(
    page_title='Customização de  Layout',
    page_icon='🎨',
    layout='wide'
)

# --- Título da página
st.title('Customização de Layout')

# --- Explicação do site
st.markdown('''
Este site é um exemplo de como personalizar o layout e a aparência usando Streamlit.
''')

# --- Exemplo de st.status --- #
st.header('Mensagem de status')
with st.status('Preparando dados...', expanded=True) as status:
    st.write('Buscando dados da fonte...')
    time.sleep(2)
    st.write('Processando informações...')
    time.sleep(1)
    st.write('Gerando relatório final...')
    time.sleep(1)
    status.update(label='Dados carregados!', state='complete')
st.success('Processo concluído!')


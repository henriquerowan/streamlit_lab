# --- importar o streamlit
import streamlit as st  

# --- título da página
st.title('Elementos Interativos de Layout')

# --- Barra lateral
st.sidebar.header('Dados da aplicação')

nome = st.sidebar.text_input(label='Digite seu nome')
st.sidebar.write(f'Olá, {nome}! Bem-vindo(a) à aplicação!')


# --- Colunas para organizar o layout
col1, col2, col3 = st.columns(3)

with col1:
    st.header('🖱️ Interações simples')
    if st.button('Clique aqui'):
        st.success('Botão clicado!')

    valor_slider = st.slider(label='Escolha um valor', min_value=0, max_value=100, value=50)
    st.write(f'Valor selecionado: {valor_slider}')

with col2:
    st.header('🎨 Interações e imagens')
    st.info('Esta é uma mensagem informativa')
    st.image(
        'https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png',
        caption='Logo do Streamlit',
        #width=250,
        use_container_width=True
    )
    st.warning('Esta é uma mensagem de aviso', icon='⚠️')
    
    # --- Entrada de número e exibição do resultado ---
    st.header('🔢 Entrada de número')
    numero = st.number_input(label='Digite um número', value=0, min_value=0, max_value=100)
    st.write(f'Número digitado: {numero}')


with col3:
    st.header('⚡ Interações avançadas')
    opcoes = st.multiselect(label='Selecione suas frutas favoritas', options=['Maçã', 'Banana', 'Laranja', 'Uva'])
    st.write(f'Frutas selecionadas: {", ".join(opcoes)}')

    cor_favorita = st.color_picker(label='Escolha sua cor favorita')
    st.write(f'Cor selecionada: {cor_favorita}')
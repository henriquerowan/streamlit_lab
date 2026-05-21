# --- Importar o streamlit
import streamlit as st

# --- Configurações da página
st.set_page_config(layout='centered', page_title='Aula 16: st.dialog() e st.popover()', page_icon=':speech_balloon:')

# --- Título
st.title('Aula 16: st.dialog() e st.popover()')

# --- Botão que abre o diálogo
if st.button('Abrir Diálogo'):
    st.session_state.abrir_dialogo = True

@st.dialog('Confirmar Ação')
def dialog_confirmacao():
    # --- Texto explicativo dentro do dialog --- #
    st.write('Esta ação simula ima decisão importante dentro da aplicação')

    # --- Campo de entrada --- #
    nome = st.text_input('Digite seu nome para confirmar')

    # --- Botões de ação --- #
    colunas = st.columns(2)
    with colunas[0]:
        if st.button('Confirmar'):
            # --- Salvar na sessão o nome --- #
            if nome.strip() != '':
                st.session_state['nome'] = nome
            st.session_state.abrir_dialogo = False
            st.rerun()

    with colunas[1]:
        if st.button('Cancelar'):
            st.session_state.abrir_dialogo = False
            st.rerun()

# --- Controle para abrir o dialog
if st.session_state.get('abrir_dialogo', False):
    dialog_confirmacao()

# --- Colocar o nome salvo na sessão
if 'nome' in st.session_state:
    st.success(f'Olá, {st.session_state.nome}! A ação foi confirmada.')

st.divider()

# --- Botão que abre o popover
st.write('Aqui está o conteúdo principal da pagina.')
st.write('As configurações extras ficam ocultas no popover.')

# --- Popover para opções secundarias
with st.popover('Abrir configurações avançadas'):
    # --- Conteudo exibido apenas dentro do popover --- #
    st.write('Estas são as configurações avançadas da aplicação.')
    tema=st.selectbox('Escolha o tema da aplicação', ['Claro', 'Escuro', 'Sistema'])
    notificacoes=st.checkbox('Ativar notificações')
    
    # --- Salvar as escolhas na sessão --- #
    if st.button('Salvar Configurações'):
        st.session_state['tema'] = tema
        st.session_state['notificacoes'] = notificacoes
        st.success('Configurações salvas com sucesso!')

# --- Exibir as configurações salvas --- #
if 'tema' in st.session_state:
    st.info(f"Tema selecionado: {st.session_state.tema}")
if 'notificacoes' in st.session_state:
    st.info(f"Notificações ativadas: {'Sim' if st.session_state.notificacoes else 'Não'}")
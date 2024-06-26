import streamlit as st
from functions import hide_menu, redirect_with, verify_user, login, signup
from time import sleep
from database import User
from datetime import datetime

if 'wide_mode' in st.session_state:
    st.set_page_config(page_title='Home', layout=st.session_state.wide_mode)
else:
    st.set_page_config(page_title='Home', layout='centered')

hide_menu(st)
redirect_with(st)

st.title('O Castelo Organizado do Rei Queryon')
col1, col2 = st.columns([1, 2])

with col1:
    st.write('')
    st.markdown(
        """
        Em SQLandia, o sábio e valoroso Rei Queryon enfrentava um problema que tirava seu sono: a desorganização dos itens do castelo e do exército real. Tesouros estavam espalhados, registros dos cavaleiros eram confusos, e fazer consultas sobre qualquer informação era uma tarefa árdua.
        """
    )
with col2:
    st.image('assets/rei_tal.png', width=300)


st.markdown(
    """
    Um dia, o Rei Queryon convocou uma reunião com os conselheiros, expressando sua frustração.
    Nenhum conselheiro conseguiu oferecer uma solução prática. 
    Foi então que Sir Schema, um jovem aventureiro conhecido por sua habilidade com tecnologias modernas, se adiantou.
    
    Sir Schema propôs ao rei a criação de um banco de dados para organizar tudo de forma eficiente.
    O rei, inicialmente cético, ficou esperançoso ao ouvir a proposta, solicitando a criação imediata de um banco de dados.
    """
)
st.subheader('')
st.subheader('Entrar')
st.write(
    'Informe seu usuário, se ainda não tiver um, preencha o campo e clique em criar.'
)
user = st.text_input('Usuário:')

if st.button('Entrar!', disabled=False if user else True):
    if login(user):
        session = st.session_state.db.get_session()
        g_user = session.query(User).filter(User.name == user).first()
        g_user.updated_at = datetime.now()
        session.commit()
        session.close()
        st.switch_page('pages/select_step.py')
    else:
        st.error('Usuário não encontrado, tente novamente.')
        sleep(2)
        st.rerun()

if st.button('Criar', disabled=False if user else True):
    if verify_user(user):
        st.error('Usuário já existe, tente outro.')
        sleep(2)
        st.rerun()
    if signup(user):
        st.success('Usuário criado com sucesso!')
        sleep(2)
        if login(user):
            st.switch_page('pages/select_step.py')
        else:
            st.error('Erro ao logar, tente novamente.')
            sleep(2)
            st.rerun()

st.subheader('')

st.markdown(
    'Encontrou algum problema? [Reportar Bug](https://wa.me/+5511947229703)'
)

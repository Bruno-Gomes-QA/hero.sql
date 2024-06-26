import streamlit as st
from functions import hide_menu, redirect_with

if 'wide_mode' in st.session_state:
    st.set_page_config(page_title='Step', layout=st.session_state.wide_mode)
else:
    st.set_page_config(page_title='Step', layout='centered')

hide_menu(st)
redirect_with(st)

st.title(f'Bem vindo {st.session_state.username}!')
st.write('')
st.markdown(
    """
  Você pode escolher começar desde o começo da jornada, criando o banco de dados do zero, ou escolher qual habilidade deseja treinar.
  Se busca treinar querys SQL, clique em 'Seleção de Dados'. Mas se deseja começar a jornada, clique em 'Início'.
  """
)
st.subheader('')


if st.button('Início'):
    st.switch_page('pages/create_database.py')
if st.button('Criação de Tabelas'):
    st.switch_page('pages/create_titulos.py')
if st.button('Chave Estrangeira'):
    st.switch_page('pages/foreign_key.py')
if st.button('Seleção de Dados'):
    st.switch_page('pages/select.py')

st.subheader('')
st.markdown(
    'Encontrou algum problema? [Reportar Bug](https://wa.me/+5511947229703)'
)

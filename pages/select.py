import streamlit as st
from database import Database
from functions import hide_menu, redirect_with, create, insert, back_to_menu
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
castelo_user = os.getenv('CASTELO_USER')
castelo_password = os.getenv('CASTELO_PASSWORD')
host = os.getenv('MYSQL_HOST')
port = os.getenv('MYSQL_PORT')

if 'wide_mode' in st.session_state:
    st.set_page_config(page_title='Select', layout=st.session_state.wide_mode)
else:
    st.set_page_config(page_title='Select', layout='centered')


if 'db_castelo' not in st.session_state:
    st.session_state.db_castelo = Database(
        f'mysql+pymysql://{castelo_user}:{castelo_password}@{host}:{port}',
        'castelo',
    )
hide_menu(st)
redirect_with(st)
if 'wide_code_create' not in st.session_state:
    st.session_state.wide_code_create = True
if 'wide_code_insert' not in st.session_state:
    st.session_state.wide_code_insert = True

st.title('Relatório dos Soldados!')
st.subheader('')

st.markdown(
    """
    O rei precisa de um relatório dos soldados que são trabalhadores, sua data de nascimento e título.
    Construa a consulta SQL que retorne o nome do soldado, data de nascimento e título.
    """
)
st.write('')
st.info(
    'Para obter esse resultado será necessário usar a cláusula SELECT e JOIN.'
)
st.write('')

if not st.session_state.wide_code_insert:
    if st.button('Ocultar Insert'):
        st.session_state.wide_code_insert = True
        st.rerun()
    st.code(insert, language='sql'),
else:
    if st.button('Mostrar SQL de Inserção de Dados'):
        st.session_state.wide_code_insert = False
        st.rerun()

if not st.session_state.wide_code_create:
    if st.button('Ocultar Create'):
        st.session_state.wide_code_create = True
        st.rerun()
    st.code(create, language='sql'),
else:
    if st.button('Mostrar SQL de Criação do Banco de Dados'):
        st.session_state.wide_code_create = False
        st.rerun()

st.subheader('')

if 'code' not in st.session_state:
    st.session_state.code = ''

st.write('Digite a consulta SQL:')
st.session_state.code = st.text_area(
    'Code', height=200, value=st.session_state.code, label_visibility='hidden'
)
if st.button('Visualizar'):
    st.rerun()

st.write('Código SQL:')
st.write('')
st.write('')
st.code(st.session_state.code, language='sql')
if st.button('Executar'):
    try:
        result = st.session_state.db_castelo.execute_query(
            st.session_state.code
        )
        df = pd.DataFrame(result.fetchall(), columns=result.keys())

        st.dataframe(df)
        st.success('Consulta executada com sucesso!')
    except Exception as e:
        st.error(f'Erro ao executar a consulta: {str(e)}')

st.subheader('')
st.markdown(
    'Encontrou algum problema? [Reportar Bug](https://wa.me/+5511947229703)'
)

back_to_menu(st)

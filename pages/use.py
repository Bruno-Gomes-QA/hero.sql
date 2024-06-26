from time import sleep
import streamlit as st

from functions import hide_menu, redirect_with, back_to_menu

if 'wide_mode' in st.session_state:
    st.set_page_config(page_title='Use', layout=st.session_state.wide_mode)
else:
    st.set_page_config(page_title='Use', layout='centered')

hide_menu(st)
redirect_with(st)


if 'answer' not in st.session_state:
    st.session_state.answer = []
if 'tips' not in st.session_state:
    st.session_state.tips = [
        'DATABASE',
        'SET',
        'SELECT',
        'reinado',
        ';',
        'castelo',
        'USE',
    ]

st.title('Usando o banco de dados!')
st.subheader('')
st.markdown(
    """
    Agora que o banco de dados foi criado precisamos usá-lo para organizar os registros dos cavaleiros e dos tesouros do reino.
    Contrua a intrução SQL que selecione o banco de dados 'castelo'.
    """
)
st.subheader('')

col1, col2 = st.columns([1, 2])


def update_answer(value, index):
    for i, w in enumerate(st.session_state.answer):
        if w == value:
            st.session_state.answer.pop(i)
            return
    else:
        st.session_state.answer.append(value)


for i, tip in enumerate(st.session_state.tips):
    b_type = 'primary' if tip in st.session_state.answer else 'secondary'
    if col1.button(tip, key=i, type=b_type):
        update_answer(tip, i)
        st.rerun()

col1.subheader('')

answer = """"""
for w in st.session_state.answer:
    answer += w + ' '
col2.code(answer, language='sql')

expected_answer = ['USE', 'castelo', ';']

if col2.button('Executar'):
    if st.session_state.answer == expected_answer:
        col2.success('Sucesso! Vamos para a próxima etapa!')
        del st.session_state['answer']
        del st.session_state['tips']
        sleep(2)
        st.switch_page('pages/create_titulos.py')
    else:
        col2.error('Ops! Parece que algo deu errado.')
        if col2.button('Tentar novamente'):
            del st.session_state['answer']
            del st.session_state['tips']
            st.rerun()

col2.image('assets/cloud.png', use_column_width=True)

back_to_menu(st)

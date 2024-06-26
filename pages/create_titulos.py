from time import sleep
import streamlit as st
from functions import hide_menu, redirect_with, back_to_menu

if 'wide_mode' in st.session_state:
    st.set_page_config(
        page_title='Table Títulos', layout=st.session_state.wide_mode
    )
else:
    st.set_page_config(page_title='Table Títulos', layout='centered')

hide_menu(st)
redirect_with(st)

lines_info = [
    {
        'tips': [
            'SET',
            'tbl_titulos',
            'INSERT',
            'CREATE',
            ';',
            'tbl_titulo',
            '(',
            'TABLE',
        ],
        'expect_answer': ['CREATE', 'TABLE', 'tbl_titulos', '('],
    },
    {
        'tips': [
            'id_titulo',
            ';',
            'INT',
            'VARCHAR(255)',
            'PRIMARY',
            'AUTO_INCREMENT',
            'KEY',
            ',',
        ],
        'expect_answer': [
            'id_titulo',
            'INT',
            'PRIMARY',
            'KEY',
            'AUTO_INCREMENT',
            ',',
        ],
    },
    {
        'tips': [
            'nome_titulo',
            'VARCHAR(255)',
            'NOT',
            'NULL',
            ',',
            'VAR(255)',
            ';',
        ],
        'expect_answer': ['nome_titulo', 'VARCHAR(255)', 'NOT', 'NULL', ','],
    },
    {
        'tips': [
            'patente_titulo',
            'VARCHAR(255)',
            'NOT',
            'NULL',
            ',',
            'VAR(255)',
            ';',
        ],
        'expect_answer': [
            'patente_titulo',
            'VARCHAR(255)',
            'NOT',
            'NULL',
            ',',
        ],
    },
    {
        'tips': [')', ';'],
        'expect_answer': [')', ';'],
    },
    {
        'tips': [''],
        'expect_answer': [''],
    },
]


if 'current_line' not in st.session_state:
    st.session_state.current_line = 0
if 'answer' not in st.session_state:
    st.session_state.answer = []
if 'lines' not in st.session_state:
    st.session_state.lines = [''] * len(lines_info)


def update_answer(value):
    for i, w in enumerate(st.session_state.answer):
        if w == value:
            st.session_state.answer.pop(i)
            return
    else:
        st.session_state.answer.append(value)


st.title('Criando a tabela Títulos!')
st.write('')
st.markdown(
    """
    Cada soldado do reino Queryon possui um título que indica seu nível de experiência e habilidade.
    Para organizar essas informações, precisamos criar uma tabela chamada 'tbl_titulos' no banco de dados 'castelo'.
    Com as colunas de 'id_titulo', 'nome_titulo' e 'patente_titulo'. Nenhuma coluna pode ser nula.
    """
)
st.write('')
st.info(
    'Quando completar a linha corretamente as próximas dicas serão liberadas.'
)
st.write('')
col1, col2 = st.columns([1, 2])


# Criando as dicas
tips = lines_info[st.session_state.current_line]['tips']
for i, tip in enumerate(tips):
    b_type = 'primary' if tip in st.session_state.answer else 'secondary'
    if col1.button(tip, key=i, type=b_type):
        update_answer(tip)
        st.rerun()

# Verificando se a linha está correta
if (
    st.session_state.answer
    == lines_info[st.session_state.current_line]['expect_answer']
):
    # Adicionando resposta a linha atual
    st.session_state.lines[st.session_state.current_line] = ' '.join(
        st.session_state.answer
    )
    # Limpando a resposta e indo para próxima linha
    st.session_state.answer = []
    if st.session_state.current_line < len(lines_info):
        st.session_state.current_line += 1
    st.rerun()
else:
    # Adicionando resposta a linha atual
    st.session_state.lines[st.session_state.current_line] = ' '.join(
        st.session_state.answer
    )

l1, l2, l3, l4, l5, l6 = st.session_state.lines

answer = f"""
    {l1}
    {l2}
    {l3}
    {l4}
    {l5}
    {l6}
"""


col2.code(answer, language='sql', line_numbers=True)
if st.session_state.current_line == len(lines_info) - 1:
    if col2.button('Executar'):
        col2.success('Sucesso! Vamos para a próxima etapa!')
        sleep(2)
        del st.session_state['answer']
        del st.session_state['lines']
        del st.session_state['current_line']
        st.switch_page('pages/create_soldados.py')

col2.image('assets/patentes.png', use_column_width=True)
back_to_menu(st)
from time import sleep
import streamlit as st

from functions import hide_menu, redirect_with, back_to_menu

if 'wide_mode' in st.session_state:
    st.set_page_config(
        page_title='Table Soldados', layout=st.session_state.wide_mode
    )
else:
    st.set_page_config(page_title='Table Soldados', layout='centered')

hide_menu(st)
redirect_with(st)

lines_info = [
    {
        'tips': [
            'SET',
            'tbl_soldados',
            'INSERT',
            'CREATE',
            ';',
            'tbl_soldades',
            '(',
            'TABLE',
        ],
        'expect_answer': ['CREATE', 'TABLE', 'tbl_soldados', '('],
    },
    {
        'tips': [
            'id_soldado',
            ';',
            'INT',
            'VARCHAR(255)',
            'PRIMARY',
            'AUTO_INCREMENT',
            'KEY',
            ',',
        ],
        'expect_answer': [
            'id_soldado',
            'INT',
            'PRIMARY',
            'KEY',
            'AUTO_INCREMENT',
            ',',
        ],
    },
    {
        'tips': [
            'nome_soldado',
            'VARCHAR(255)',
            'NOT',
            'NULL',
            ',',
            'VAR(255)',
            ';',
        ],
        'expect_answer': ['nome_soldado', 'VARCHAR(255)', 'NOT', 'NULL', ','],
    },
    {
        'tips': [
            'nascimento_soldado',
            'DATA',
            'NOT',
            'NULL',
            ',',
            'DATE',
            ';',
        ],
        'expect_answer': ['nascimento_soldado', 'DATE', 'NOT', 'NULL', ','],
    },
    {
        'tips': [
            'altura_soldado',
            'DECIMAL(10,2)',
            'NOT',
            'NULL',
            ',',
            'INT',
            ';',
        ],
        'expect_answer': [
            'altura_soldado',
            'DECIMAL(10,2)',
            'NOT',
            'NULL',
            ',',
        ],
    },
    {
        'tips': [
            'fk_titulo',
            'FOREIGN',
            'NOT',
            'NULL',
            ',',
            'INT',
            ';',
            'KEY',
        ],
        'expect_answer': ['fk_titulo', 'INT', 'NOT', 'NULL', ','],
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


st.title('Criando a tabela Soldados!')
st.write('')

st.markdown(
    """
    Para o rei é imprescindível que os soldados do reino estejam bem organizados.
    Para organizar essas informações, precisamos criar uma tabela chamada 'tbl_soldados' no banco de dados 'castelo'.
    Com as colunas de 'id_soldado', 'nome_soldado', 'nascimento_soldado', 'altura_soldado', 'fk_titulo'. Nenhuma coluna pode ser nula.
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
    if st.session_state.current_line < len(lines_info):
        st.session_state.current_line += 1
        st.session_state.answer = []
    st.rerun()
else:
    # Adicionando resposta a linha atual
    st.session_state.lines[st.session_state.current_line] = ' '.join(
        st.session_state.answer
    )

l1, l2, l3, l4, l5, l6, l7, l8 = st.session_state.lines

answer = f"""
    {l1}
    {l2}
    {l3}
    {l4}
    {l5}
    {l6}
    {l7}
"""


col2.code(answer, language='sql', line_numbers=True)
if st.session_state.current_line == len(lines_info) - 1:
    if col2.button('Executar'):
        col2.success('Sucesso! Vamos para a próxima etapa!')
        sleep(2)
        del st.session_state['answer']
        del st.session_state['lines']
        del st.session_state['current_line']
        st.switch_page('pages/foreign_key.py')

col2.image('assets/patentes.png', use_column_width=True)

back_to_menu(st)

import streamlit as st


def clean_state():
    if 'first_line' in st.session_state:
        del st.session_state.first_line
    if 'answer' in st.session_state:
        del st.session_state.answer
    if 'lines' in st.session_state:
        del st.session_state.lines

import streamlit as st
from functions import hide_menu, redirect_with

try:
    st.set_page_config(
        page_title='Verify Progress', layout=st.session_state.wide_mode
    )
except:
    st.set_page_config(page_title='Verify Progress', layout='centered')

hide_menu(st)
redirect_with(st)

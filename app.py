import streamlit as st
from streamlit_js_eval import streamlit_js_eval
from database import Database, Base
from functions import get_width, hide_menu
from dotenv import load_dotenv
import os

load_dotenv()
user = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PASSWORD')
host = os.getenv('MYSQL_HOST')
port = os.getenv('MYSQL_PORT')
database = os.getenv('MYSQL_DATABASE')
st.set_page_config(page_title='Queryon', layout='centered')
get_width(st, streamlit_js_eval)
hide_menu(st)

if 'db' not in st.session_state:
    st.session_state.db = Database(
        f'mysql+pymysql://{user}:{password}@{host}:{port}', database
    )
    st.session_state.db.create_tables(Base)
if 'login' not in st.session_state:
    st.session_state.login = None
if 'username' not in st.session_state:
    st.session_state.username = None
if 'user_id' not in st.session_state:
    st.session_state.user_id = None

st.switch_page('pages/home.py')

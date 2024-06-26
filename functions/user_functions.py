import streamlit as st
import hashlib
from database import User


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def verify_user(username):
    session = st.session_state.db.get_session()
    user = session.query(User).filter_by(name=username).first()
    session.close()
    return user


def login(user):
    g_user = verify_user(user)
    if g_user:
        st.session_state.login = True
        st.session_state.username = g_user.name
        st.session_state.user_id = g_user.id
        return g_user
    else:
        return False


def signup(user):
    session = st.session_state.db.get_session()
    new_user = User(name=user)
    session.add(new_user)
    session.commit()
    session.close()
    return new_user

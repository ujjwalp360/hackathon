# login.py
import streamlit as st
from db import create_db_connection
from registration import complete_registration
from eligibility_check import show_eligibility_check

def login_user(username, password):
    db = create_db_connection()
    if db is None:
        st.error("Database connection failed.")
        return None
    cursor = db.cursor(dictionary=True)
    
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    
    cursor.close()
    db.close()
    
    return user

def check_registration(user_id):
    db = create_db_connection()
    if db is None:
        st.error("Database connection failed.")
        return False
    cursor = db.cursor()
    
    query = "SELECT * FROM user_info WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    info = cursor.fetchone()
    
    cursor.close()
    db.close()
    
    return bool(info)

def login_page():
    st.title("Login")
    
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button("Login")
    
    if submit_button:
        user = login_user(username, password)
        
        if user:
            st.success("Login successful!")
            # Set session state
            st.session_state['logged_in'] = True
            st.session_state['needs_registration'] = not check_registration(user['id'])
            st.session_state['user'] = user

        else:
            st.error("Invalid username or password.")

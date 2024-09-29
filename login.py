# login.py
import streamlit as st
from db import create_db_connection

# Login functionality
def login_user(username, password):
    db = create_db_connection()
    cursor = db.cursor(dictionary=True)
    
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    
    cursor.close()
    db.close()
    
    return user

def login_page():
    st.title("Login")

    # Using a Streamlit form to avoid auto-refresh
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        # Add a submit button to trigger form submission
        submit_button = st.form_submit_button("Submit")

    # If the submit button is pressed, process the login
    if submit_button:
        user = login_user(username, password)
        
        if user:
            st.success("Login successful!")
            return user
        else:
            st.error("Invalid username or password.")
            return None

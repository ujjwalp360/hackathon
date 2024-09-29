# login.py
import streamlit as st
from db import create_db_connection
from registration import complete_registration

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

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button("Submit")

    if submit_button:
        user = login_user(username, password)
        
        if user:
            st.success("Login successful!")
            if user['id'] not in get_user_info_ids():
                st.info("You haven't completed your registration.")
                if st.button("Complete Registration"):
                    complete_registration(user['id'])
            else:
                st.success("You are fully registered.")
                st.button("Check Eligibility")
        else:
            st.error("Invalid username or password.")

# login.py
import streamlit as st
from db import create_db_connection
from registration import complete_registration_page

# Function to verify user login
def verify_login(username, password):
    db = create_db_connection()
    cursor = db.cursor(dictionary=True)
    
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    
    cursor.close()
    db.close()
    
    return user

# Function to check if the user has completed registration
def check_registration_complete(user_id):
    db = create_db_connection()
    cursor = db.cursor()
    
    query = "SELECT COUNT(*) FROM user_info WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    registration_complete = cursor.fetchone()[0] > 0
    
    cursor.close()
    db.close()
    
    return registration_complete

# Main login page function
def login_page():
    st.title("Login")

    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if st.session_state['logged_in']:
        user = st.session_state['user']
        
        # Check if registration is complete for the logged-in user
        if not check_registration_complete(user['id']):
            st.write(f"Welcome, {user['username']}!")
            st.warning("You have not completed the registration. Please complete your registration to apply for the scholarship.")
            complete_registration_page()  # Show registration page if not complete
        else:
            st.success("Welcome back! Your registration is complete.")
            # User's personal dashboard or other features can be added here after login and registration
            st.write("Proceed to check eligibility or apply for the scholarship.")
    else:
        st.write("Please log in to continue.")
        
        # Login form
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            login_button = st.form_submit_button("Login")
        
        if login_button:
            user = verify_login(username, password)
            if user:
                st.session_state['logged_in'] = True
                st.session_state['user'] = user
                st.success(f"Login successful! Welcome, {user['username']}.")
                st.experimental_rerun()  # Refresh the page to show the registration status
            else:
                st.error("Invalid username or password. Please try again.")

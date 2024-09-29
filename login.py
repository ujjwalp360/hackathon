# login.py
import streamlit as st
from db import create_db_connection
from registration import complete_registration, get_user_info_ids

# Function to log in the user
def login_user(username, password):
    db = create_db_connection()
    cursor = db.cursor(dictionary=True)
    
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    
    cursor.close()
    db.close()
    
    return user

# Login page function
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

            # Check if user is registered
            user_info_ids = get_user_info_ids()
            if user['id'] not in user_info_ids:
                st.info("You haven't completed your registration.")
                if st.button("Complete Registration"):
                    complete_registration(user['id'])  # Redirect to registration
            else:
                st.success("You are fully registered.")
                if st.button("Check Eligibility"):
                    st.success("Redirecting to eligibility check...")
                    # Here, you can call the eligibility check function or redirect to its page.
                    # Example:
                    # show_eligibility_check(user['id'])  # Assuming this function checks eligibility
        else:
            st.error("Invalid username or password.")

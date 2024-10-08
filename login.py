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
def check_registration_complete(username):
    db = create_db_connection()
    cursor = db.cursor()
    
    query = "SELECT COUNT(*) FROM user_info WHERE username = %s"
    cursor.execute(query, (username,))
    registration_complete = cursor.fetchone()[0] > 0
    
    cursor.close()
    db.close()
    
    return registration_complete

# Main login page function
def login_page():
    st.title("Login")

    # Check if the user is logged in
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if st.session_state['logged_in']:
        username = st.session_state.get('username')  # Retrieve stored username
        
        if username:  # Ensure username is not None
            st.write(f"Welcome, {username}!")
        
            # Check if registration is complete for the logged-in user
            if st.session_state['needs_registration']:
                st.warning("You have not completed the registration. Please complete your registration to apply for the scholarship.")
                complete_registration_page()  # Load registration form
            else:
                st.success("Welcome back! Your registration is complete.")
                st.write("Proceed to check eligibility or apply for the scholarship.")
        else:
            st.error("Something went wrong with your session. Please log in again.")
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
                st.session_state['username'] = username  # Store username in session
                
                # Check if registration is already complete
                if check_registration_complete(username):
                    st.session_state['needs_registration'] = False
                else:
                    st.session_state['needs_registration'] = True

                st.success(f"Login successful! Welcome, {username}.")
                st.rerun()  # Refresh the page to show the registration status
            else:
                st.error("Invalid username or password. Please try again.")

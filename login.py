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

    # If user has logged in, redirect to registration or eligibility page
    if 'user' in st.session_state:
        show_post_login_page()
        return

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button("Login")

    if submit_button:
        user = login_user(username, password)
        
        if user:
            st.success("Login successful!")
            
            # Store user details in session_state
            st.session_state['user'] = user

            show_post_login_page()  # Show next steps after login
        else:
            st.error("Invalid username or password.")

# Function to show the post-login page (e.g., registration or eligibility)
def show_post_login_page():
    user = st.session_state['user']
    
    # Check if user is registered
    user_info_ids = get_user_info_ids()
    
    if user['id'] not in user_info_ids:
        st.info("You haven't completed your registration.")
        if st.button("Complete Registration"):
            complete_registration_page()  # Go to registration page
    else:
        st.success("You are fully registered.")
        if st.button("Check Eligibility"):
            st.success("Redirecting to eligibility check...")
            # Call the eligibility check function (not yet implemented)
            # show_eligibility_check(user['id'])

# Function to display the complete registration page
def complete_registration_page():
    st.title("Complete Registration")
    
    # Complete registration form
    with st.form("registration_form"):
        name = st.text_input("Full Name (as per Aadhaar)")
        aadhaar = st.text_input("Aadhaar Number")
        family_income = st.number_input("Family Income", min_value=0, step=1000)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        domicile = st.selectbox("Domicile State", ["Maharashtra", "Other"])
        category = st.selectbox("Category", ["Open", "OBC", "OBC-NCL", "SC", "ST"])
        enrollment_no = st.text_input("Enrollment Number")
        college_state = st.selectbox("College State", ["Maharashtra", "Other"])
        
        submit_button = st.form_submit_button("Submit")

    # Handle form submission
    if submit_button:
        st.success("Registration completed successfully!")
        # Save the registration details in the database (implement logic in registration.py)
        complete_registration(st.session_state['user']['id'], name, aadhaar, family_income, gender, domicile, category, enrollment_no, college_state)
        # Reset the session to reflect the updated registration
        st.session_state['user']['registration_complete'] = True
        st.success("You can now check your eligibility!")

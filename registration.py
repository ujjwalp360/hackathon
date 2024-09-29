# registration.py
import streamlit as st
from db import create_db_connection

# Function to save registration data in 'user_info' table
def complete_registration(user_id, name, aadhaar, family_income, gender, domicile, category, enrollment_no, college_state):
    db = create_db_connection()
    cursor = db.cursor()
    
    # Insert registration data into 'user_info' table, linking it with the user_id from 'users' table
    query = """
        INSERT INTO user_info (user_id, name, aadhaar, family_income, gender, domicile, category, enrollment_no, college_state)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (user_id, name, aadhaar, family_income, gender, domicile, category, enrollment_no, college_state))
    
    db.commit()
    cursor.close()
    db.close()

# Registration page function
def complete_registration_page():
    st.title("Complete Registration")
    
    # Ensure that user_id from session_state is used in registration
    user_id = st.session_state['user']['id']
    
    # Complete registration form
    with st.form("registration_form"):
        name = st.text_input("Full Name (as per Aadhaar)", key="name_input")
        aadhaar = st.text_input("Aadhaar Number", key="aadhaar_input")
        family_income = st.number_input("Family Income", min_value=0, step=1000, key="family_income_input")
        gender = st.selectbox("Gender", ["Male", "Female", "Other"], key="gender_select")
        
        domicile = st.radio("Do you have a domicile of Maharashtra?", ["Yes", "No"], key="domicile_radio")
        
        # If domicile is "No", display error and prevent registration
        if domicile == "No":
            st.error("You are not eligible for the scholarship as you do not have a domicile of Maharashtra.")
            return
        
        category = st.selectbox("Category", ["Open", "OBC", "OBC-NCL", "SC", "ST"], key="category_select")
        enrollment_no = st.text_input("Enrollment Number", key="enrollment_input")
        college_state = st.selectbox("College State", ["Maharashtra", "Other"], key="college_state_select")
        
        submit_button = st.form_submit_button("Submit", key="submit_button")

    if submit_button:
        # Debugging: Print values to ensure they are captured
        st.write("User ID:", user_id)
        st.write("Name:", name)
        st.write("Aadhaar:", aadhaar)
        st.write("Family Income:", family_income)
        st.write("Gender:", gender)
        st.write("Domicile:", domicile)
        st.write("Category:", category)
        st.write("Enrollment Number:", enrollment_no)
        st.write("College State:", college_state)

        # Ensure all required fields are filled
        if name and aadhaar and enrollment_no:
            # Pass all collected data to the complete_registration function
            complete_registration(user_id, name, aadhaar, family_income, gender, domicile, category, enrollment_no, college_state)
            st.session_state['user']['registration_complete'] = True
            st.success("Registration completed successfully! You can now check your eligibility.")
        else:
            st.error("Please fill out all required fields before submitting.")

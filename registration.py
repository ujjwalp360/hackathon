import streamlit as st
from db import create_db_connection

# Function to save registration data in 'user_info' table
def complete_registration(username, name, aadhaar, family_income, gender, domicile, category, enrollment_no, college_state):
    db = create_db_connection()
    cursor = db.cursor()
    
    # Insert registration data into 'user_info' table, linking it with the username from 'users' table
    query = """
        INSERT INTO user_info (username, name, aadhaar, family_income, gender, domicile_state, category, enrollment_no, college_state)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (username, name, aadhaar, family_income, gender, domicile, category, enrollment_no, college_state))
    
    db.commit()
    cursor.close()
    db.close()

# Registration page function
def complete_registration_page():
    st.title("Complete Registration")
    
    # Complete registration form
    with st.form("registration_form"):
        username=st.text_input("username")
        name = st.text_input("Full Name (as per Aadhaar)")
        aadhaar = st.text_input("Aadhaar Number")
        family_income = st.number_input("Family Income", min_value=0, step=1000)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        
        domicile = st.radio("Do you have a domicile of Maharashtra?", ["Yes", "No"])
        
        # If domicile is "No", display error and prevent registration
        if domicile == "No":
            st.error("You are not eligible for the scholarship as you do not have a domicile of Maharashtra.")
            return
        
        category = st.selectbox("Category", ["Open", "OBC", "OBC-NCL", "SC", "ST"])
        enrollment_no = st.text_input("Enrollment Number")
        college_state = st.selectbox("College State", ["Maharashtra", "Other"])
        button=st.form_submit_button("Submit")
    # Ensure all required fields are filled
        if button:
            if name and aadhaar and enrollment_no:
                # Pass all collected data to the complete_registration function
                complete_registration(username, name, aadhaar, family_income, gender, domicile, category, enrollment_no, college_state)
                st.success("Registration completed successfully! You can now check your eligibility.")
                st.rerun()  # Refresh page after registration
            else:
                st.error("Please fill out all required fields before submitting.")

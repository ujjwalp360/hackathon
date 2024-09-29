import streamlit as st
from db import create_db_connection

# Function to save registration data in 'user_info' table
def complete_registration(username, name, aadhaar, family_income, gender, domicile, category, enrollment_no, college_state):
    db = create_db_connection()
    cursor = db.cursor()
    
    query = """
        INSERT INTO user_info (username, name, aadhaar, family_income, gender, domicile_state, category, enrollment_no, college_state)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    try:
        cursor.execute(query, (username, name, aadhaar, family_income, gender, domicile, category, enrollment_no, college_state))
        db.commit()
        st.success("Registration data saved successfully!")
        
        # Update the registration status
        st.session_state['needs_registration'] = False
        
    except Exception as e:
        # Log the error to the console and show an error in the UI
        st.error(f"An error occurred while saving registration: {e}")
        print(f"Error: {e}")
    
    cursor.close()
    db.close()

# Registration page function
def complete_registration_page():
    st.title("Complete Registration")
    
    # Get username from session state
    username = st.session_state.get('username')
    if not username:
        st.error("Username not found. Please log in again.")
        return
    
    # Registration form
    with st.form("registration_form"):
        name = st.text_input("Full Name (as per Aadhaar)")
        aadhaar = st.text_input("Aadhaar Number")
        family_income = st.number_input("Family Income", min_value=0, step=10000)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        
        domicile = st.radio("Do you have a domicile of Maharashtra?", ["Yes", "No"])
        
        if domicile == "No":
            st.error("You are not eligible for the scholarship as you do not have a domicile of Maharashtra.")
            return
        
        category = st.selectbox("Category", ["Open", "OBC", "OBC-NCL", "SC", "ST"])
        enrollment_no = st.text_input("Enrollment Number")
        college_state = st.selectbox("College State", ["Maharashtra", "Other"])
        submit_button = st.form_submit_button("Submit")
    
        if submit_button:
            if name and aadhaar and enrollment_no:
                # Complete registration with the username from session
                complete_registration(username, name, aadhaar, family_income, gender, domicile, category, enrollment_no, college_state)
            else:
                st.error("Please fill out all required fields before submitting.")

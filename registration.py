# registration.py
import streamlit as st
from db import create_db_connection
from eligibility_check import show_eligibility_check

def complete_registration(user_id):
    st.title("Complete Registration")
    
    with st.form("registration_form"):
        aadhar = st.text_input("Aadhar Card Number")
        family_income = st.number_input("Family Income", min_value=0.0, step=1000.0)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        domicile_state = st.radio("Do you have a domicile of Maharashtra?", ["Yes", "No"])
        
        # If domicile is No, show an error and prevent further registration
        if domicile_state == "No":
            st.error("You are not eligible for the scholarship as you do not have a domicile of Maharashtra.")
            return  # Exit the registration page, since they can't apply
        
        # Proceed with the rest of the form if domicile is "Yes"
        category = st.selectbox("Category", ["Open", "OBC", "OBC-NCL", "SC", "ST"], key="category_select")
        enrollment_no = st.text_input("Enrollment Number", key="enrollment_input")
        college_state = st.selectbox("College State", ["Maharashtra", "Other"], key="college_state_select")
        
        submit_button = st.form_submit_button("Submit", key="submit_button")
    
    if submit_button:
        if domicile_state.lower() != "maharashtra":
            category = "Open"  # Automatically sets category to 'Open' for non-Maharashtra domicile
        
        db = create_db_connection()
        if db is None:
            st.error("Database connection failed.")
            return
        cursor = db.cursor()
        
        query = """
        INSERT INTO user_info (user_id, aadhar, family_income, gender, domicile_state, category, enrollment_no, college_state)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        try:
            cursor.execute(query, (user_id, aadhar, family_income, gender, domicile_state, category, enrollment_no, college_state))
            db.commit()
            st.success("Registration Complete!")
            st.session_state['needs_registration'] = False
        except Exception as e:
            st.error(f"An error occurred: {e}")
        finally:
            cursor.close()
            db.close()

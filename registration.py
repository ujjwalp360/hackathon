# registration.py
import streamlit as st
from db import create_db_connection

# Check if user info exists
def get_user_info_ids():
    db = create_db_connection()
    cursor = db.cursor()
    
    query = "SELECT user_id FROM user_info"
    cursor.execute(query)
    user_ids = [row[0] for row in cursor.fetchall()]
    
    cursor.close()
    db.close()
    return user_ids

# Complete Registration Page
def complete_registration(user_id):
    st.title("Complete Registration")

    aadhar = st.text_input("Aadhar Card Number")
    family_income = st.number_input("Family Income", min_value=0.0)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    domicile_state = st.text_input("Domicile State")
    category = st.selectbox("Category", ["Open", "OBC", "OBC-NCL", "SC", "ST"])
    enrollment_no = st.text_input("Enrollment Number")
    college_state = st.text_input("College State")

    if domicile_state != "Maharashtra":
        category = "Open"

    if st.button("Submit"):
        db = create_db_connection()
        cursor = db.cursor()
        
        query = """
        INSERT INTO user_info (user_id, aadhar, family_income, gender, domicile_state, category, enrollment_no, college_state)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (user_id, aadhar, family_income, gender, domicile_state, category, enrollment_no, college_state))
        db.commit()
        
        cursor.close()
        db.close()

        st.success(f"Registration Complete for user_id {user_id}!")

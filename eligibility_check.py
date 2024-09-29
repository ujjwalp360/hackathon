# eligibility_check.py
import streamlit as st
from db import create_db_connection

def get_user_info(user_id):
    db = create_db_connection()
    if db is None:
        st.error("Database connection failed.")
        return None
    cursor = db.cursor(dictionary=True)
    
    query = "SELECT * FROM user_info WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    user_info = cursor.fetchone()
    
    cursor.close()
    db.close()
    
    return user_info

def show_eligibility_check(user_id):
    st.title("Eligibility Check")
    
    user_info = get_user_info(user_id)
    if not user_info:
        st.error("User information not found.")
        return
    
    eligible = True
    st.write("**Eligibility Criteria:**")
    
    if user_info["family_income"] > 800000:
        st.write("- **Family Income** above ₹8 lakh: **Not Eligible**")
        eligible = False
    else:
        st.write("- **Family Income** below ₹8 lakh: **Eligible**")
    
    if user_info["domicile_state"].lower() != "maharashtra":
        st.write(f"- **Domicile State**: {user_info['domicile_state']} (Not Maharashtra): **Not Eligible**")
        eligible = Falsev
    else:
        st.write("- **Domicile State**: Maharashtra: **Eligible**")
    
    if user_info["college_state"].lower() != "maharashtra":
        st.write(f"- **College State**: {user_info['college_state']} (Not Maharashtra): **Not Eligible**")
        eligible = False
    else:
        st.write("- **College State**: Maharashtra: **Eligible**")
    
    if eligible:
        st.success("You are **eligible** for the scholarship!")
        st.write("**Document Requirements:**")
        st.write("- Income Certificate")
        st.write("- Domicile Certificate")
        
        if user_info["category"] != "Open":
            st.write("- Caste Certificate")
        
        with st.form("document_verification"):
            has_documents = st.checkbox("I have all required documents")
            submit_docs = st.form_submit_button("Apply for Scholarship")
        
        if submit_docs:
            if has_documents:
                # Here, you can add logic to handle the scholarship application
                st.success("Your scholarship application has been submitted successfully!")
            else:
                st.error("Please confirm that you have all required documents.")
    else:
        st.error("You are **not eligible** for the scholarship based on the provided information.")

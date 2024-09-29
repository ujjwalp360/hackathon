import streamlit as st
import mysql.connector

# MySQL Database connection
def create_db_connection():
    return mysql.connector.connect(
        host="ber9n6myvypxkq2zmnmt-mysql.services.clever-cloud.com",
        user="ubd29UcTDrAGhd4nvuhX",
        database="ber9n6myvypxkq2zmnmt"
    )

# Login functionality
def login_user(username, password):
    db = create_db_connection()
    cursor = db.cursor(dictionary=True)
    
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    
    cursor.close()
    db.close()
    
    return user

# Check if user has filled in registration details
def check_registration(user_id):
    db = create_db_connection()
    cursor = db.cursor(dictionary=True)
    
    query = "SELECT * FROM user_info WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    info = cursor.fetchone()
    
    cursor.close()
    db.close()
    
    return info

# Home Page
def home_page():
    st.title("Scholarship Program")
    st.write("Welcome to the Scholarship Program. Please log in to continue.")
    
    if st.button("Login"):
        login_page()

# Login Page
def login_page():
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Submit"):
        user = login_user(username, password)
        
        if user:
            st.success("Login successful!")
            user_info = check_registration(user["id"])
            
            if user_info:
                st.write("You have already completed registration.")
                # Show eligibility check option if already registered
                show_eligibility_check(user_info)
            else:
                st.warning("You need to complete your registration.")
                if st.button("Complete Registration"):
                    complete_registration(user["id"])
        else:
            st.error("Invalid username or password.")

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
        category = "Open"  # Automatically sets category to 'Open' for non-Maharashtra domicile

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

        st.success("Registration Complete!")
        st.write("You can now check your eligibility.")
        show_eligibility_check({
            "family_income": family_income,
            "domicile_state": domicile_state,
            "college_state": college_state
        })

# Eligibility Check Page
def show_eligibility_check(user_info):
    st.title("Eligibility Check")

    eligible = True
    st.write("Checking eligibility based on the following conditions:")
    
    if user_info["family_income"] > 800000:
        st.write("Income above 8 lakh: Not eligible")
        eligible = False
    else:
        st.write("Income below 8 lakh: Eligible")
    
    if user_info["domicile_state"] != "Maharashtra":
        st.write(f"Domicile not in Maharashtra ({user_info['domicile_state']}): Not eligible")
        eligible = False
    else:
        st.write("Domicile in Maharashtra: Eligible")
    
    if user_info["college_state"] != "Maharashtra":
        st.write(f"College not in Maharashtra ({user_info['college_state']}): Not eligible")
        eligible = False
    else:
        st.write("College in Maharashtra: Eligible")

    if eligible:
        st.success("You are eligible for the scholarship!")
        st.write("Document requirements:")
        st.write("- Income Certificate")
        st.write("- Domicile Certificate")
        
        if user_info["category"] != "Open":
            st.write("- Caste Certificate")
        
        if st.checkbox("I have all required documents"):
            if st.button("Apply for Scholarship"):
                st.success("Application submitted successfully!")
    else:
        st.error("You are not eligible for the scholarship.")

# Streamlit main app
if __name__ == "__main__":
    home_page()

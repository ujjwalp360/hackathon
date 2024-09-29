# main.py
import streamlit as st
from login import login_page
from registration import complete_registration
from eligibility_check import show_eligibility_check

# This function helps in page navigation
def main():
    st.sidebar.title("Navigation")
    choice = st.sidebar.selectbox("Choose Option", ["Home", "Login", "Register", "Eligibility Check"])

    if choice == "Home":
        st.title("Scholarship Program")
        st.write("Welcome to the Scholarship Program. Please log in to continue.")
    elif choice == "Login":
        user = login_page()
        if user:
            st.write("You are logged in.")
            if st.button("Complete Registration"):
                complete_registration(user["id"])
    elif choice == "Register":
        complete_registration()
    elif choice == "Eligibility Check":
        user_info = {"family_income": 600000, "domicile_state": "Maharashtra", "college_state": "Maharashtra", "category": "OBC"}
        show_eligibility_check(user_info)

if __name__ == "__main__":
    main()

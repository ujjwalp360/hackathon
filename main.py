import streamlit as st
from login import login_page
from registration import complete_registration
from eligibility_check import show_eligibility_check

def main():
    # Initialize session state variables if they don't exist
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
    if 'username' not in st.session_state:
        st.session_state['username'] = None
    if 'needs_registration' not in st.session_state:
        st.session_state['needs_registration'] = True

    # Sidebar Navigation
    st.sidebar.title("Navigation")
    menu = ["Home", "Login"]
    choice = st.sidebar.selectbox("Go to", menu)
    
    if choice == "Home":
        st.title("Scholarship Program")
        st.write("""Welcome to the Scholarship Program Website. Please log in to apply for scholarships.""")

    elif choice == "Login":
        if st.session_state['logged_in']:
            st.write("### You are already logged in.")
            if st.session_state['needs_registration']:
                st.info("You need to complete your registration to apply for scholarships.")
                if st.button("Complete Registration"):
                    complete_registration(st.session_state['username'])
            else:
                st.success("You have completed your registration.")
                if st.button("Check Eligibility"):
                    show_eligibility_check(st.session_state['username'])
            
            # Option to logout
            if st.button("Logout"):
                st.session_state['logged_in'] = False
                st.session_state['username

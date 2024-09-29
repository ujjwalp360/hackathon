import streamlit as st
from login import login_page
from registration import complete_registration_page
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
        st.write("Welcome to the Scholarship Program Website. Please log in to apply for scholarships.")

    elif choice == "Login":
        if st.session_state['logged_in']:
            username = st.session_state.get('username')
            if username:
                st.write(f"### Welcome, {username}!")
                if st.session_state['needs_registration']:
                    st.info("You need to complete your registration to apply for scholarships.")
                    if st.button("Complete Registration"):
                        complete_registration_page()
                else:
                    st.success("You have completed your registration.")
                    if st.button("Check Eligibility"):
                        show_eligibility_check(username)
            
            if st.button("Logout"):
                st.session_state['logged_in'] = False
                st.session_state['username'] = None
                st.session_state['needs_registration'] = True
                st.success("Logged out successfully.")
        else:
            login_page()

if __name__ == "__main__":
    main()

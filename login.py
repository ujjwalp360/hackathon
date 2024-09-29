def login_page():
    st.title("Login")

    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

    if st.session_state['logged_in']:
        username = st.session_state['username']
        
        # Check if registration is complete for the logged-in user
        if st.session_state['needs_registration']:
            st.write(f"Welcome, {username}!")
            st.warning("You have not completed the registration. Please complete your registration to apply for the scholarship.")
            complete_registration_page()  # Load the registration form
        else:
            st.success("Welcome back! Your registration is complete.")
            st.write("Proceed to check eligibility or apply for the scholarship.")
    else:
        st.write("Please log in to continue.")
        
        # Login form
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            login_button = st.form_submit_button("Login")
        
        if login_button:
            user = verify_login(username, password)
            if user:
                st.session_state['logged_in'] = True
                st.session_state['username'] = username  # Store username in session
                
                # Check if registration is already complete
                if check_registration_complete(username):
                    st.session_state['needs_registration'] = False
                else:
                    st.session_state['needs_registration'] = True

                st.success(f"Login successful! Welcome, {username}.")
                st.rerun()  # Refresh the page to show the registration status
            else:
                st.error("Invalid username or password. Please try again.")

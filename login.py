import streamlit as st

def login_page():
    st.title("Login Page")
    st.write("This is the login page.")
    
    # Button to go back to the home page
    if st.button("Go Back to Home"):
        # Navigates to the home page by updating the URL query parameters 
        # and then rerunning the script to reflect the changes.
        st.experimental_set_query_params(page="home")
        st.rerun()
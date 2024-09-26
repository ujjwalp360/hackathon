import streamlit as st

def login_page():
    st.title("Login Page")
    st.write("This is the login page.")
    
    # Button to go back to the home page
    if st.button("Go Back to Home"):
        # Update the URL to point to the home page
        st.experimental_set_query_params(page="home")
        st.rerun()

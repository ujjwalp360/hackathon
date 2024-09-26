import streamlit as st

def home_page():
    st.title("Home Page")
    st.write("Welcome to the Home Page!")
    
    # Button to navigate to the login page
    if st.button("Go to Login"):
        # Update the URL to point to the login page
        st.experimental_set_query_params(page="login")
        st.rerun()

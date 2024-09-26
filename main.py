import streamlit as st
from home import home_page  # Importing the home page logic
from login import login_page  # Importing the login page logic

# Get the current page from query parameters
query_params = st.experimental_get_query_params()
page = query_params.get("page", ["home"])[0]  # Default to "home"

# Render the appropriate page based on the URL query parameter
if page == "login":
    login_page()
else:
    home_page()

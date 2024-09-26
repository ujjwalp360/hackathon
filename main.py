import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Streamlit Navigation App")

# Function to show the home page
def home_page():
    st.title("Home Page")
    st.write("Welcome to the Home Page!")
    if st.button("Go to Login"):
        # Update the URL to point to the login page
        st.experimental_set_query_params(page="login")
        st.experimental_rerun()

# Function to show the login page
def login_page():
    st.title("Login Page")
    st.write("This is the login page.")
    if st.button("Go Back to Home"):
        # Update the URL to point to the home page
        st.experimental_set_query_params(page="home")
        st.experimental_rerun()

# Get the current page from query parameters
query_params = st.experimental_get_query_params()
page = query_params.get("page", ["home"])[0]  # Default to "home"

# Render the appropriate page based on the URL query parameter
if page == "login":
    login_page()
else:
    home_page()

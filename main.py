import streamlit as st
import streamlit as st

# Set page title
st.set_page_config(page_title="Multi-Page Streamlit App", page_icon=":house:")

# Function to show the home page
def home_page():
    st.title("Home Page")
    st.write("Welcome to the home page of the Streamlit app!")

# Function to show the about page
def about_page():
    st.title("About Page")
    st.write("This is the about page of the Streamlit app.")

# Dictionary mapping page names to functions
PAGES = {
    "Home": home_page,
    "About": about_page
}

# Get the query params from the URL
query_params = st.experimental_get_query_params()

# Extract page from the query params or default to "Home"
page = query_params.get("page", ["Home"])[0]

# Render the selected page
if page in PAGES:
    PAGES[page]()
else:
    st.error("Page not found!")

# Sidebar for navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

# Update the query params in the URL
st.experimental_set_query_params(page=selection)

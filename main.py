# main.py
import streamlit as st
from login import login_page

def main():
    st.sidebar.title("Navigation")
    choice = st.sidebar.selectbox("Choose Option", ["Home", "Login"])

    if choice == "Home":
        st.title("Scholarship Program")
        st.write("Welcome to the Scholarship Program. Please log in to continue.")
    elif choice == "Login":
        login_page()

if __name__ == "__main__":
    main()

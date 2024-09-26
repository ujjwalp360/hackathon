import streamlit as st
def loginPage():
    st.title("Login Page")
    if st.button("Go Back to Home"):
        st.experimental_get_query_params(page="home")
        st.rerun()

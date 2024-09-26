import streamlit as st
def homePage():
    st.title("home page")
    if st.button("login"):
       st.query_params(page="login")
       st.rerun()
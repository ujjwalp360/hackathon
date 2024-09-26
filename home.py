import streamlit as st
def homePage():
    st.title("home page")
    if st.button("login"):
       st.experimental_get_query_params(page="login")
       st.rerun()
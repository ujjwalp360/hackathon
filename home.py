import streamlit as st
def homePage():
    st.title("home page")
    if st.button("login"):
       st.session_state["page"]="login"
       st.rerun()
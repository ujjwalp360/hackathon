import streamlit as st

st.title("home page")
if st.button("login"):
    st.session_state["page"]="login"
    
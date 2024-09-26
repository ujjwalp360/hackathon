import streamlit as st
def loginPage():
    st.title("Login Page")
    if st.button("Go Back to Home"):
        st.session_state["page"] = "home"

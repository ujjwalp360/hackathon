import streamlit as st

st.title("Login Page")
st.write("Please enter your login details.")

# Button to go back to the home page
if st.button("Go Back to Home"):
    st.session_state["page"] = "home"
    st.rerun()

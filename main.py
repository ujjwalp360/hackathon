import streamlit as st
st.set_page_config(page_title="ujj",page_icon="💀")

def go_home():
    st.session_state["page"]="home"
def go_login():
    st.session_state["page"]="login"

if "page" not in st.session_state:
    st.session_state["page"]="home"

if st.session_state["page"]=="home":
    from home import homePage
    homePage()
    
elif st.session_state["page"]=="login":
    from login import loginPage
    loginPage()

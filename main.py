import streamlit as st
st.set_page_config(page_title="ujj",page_icon="💀")

query=st.query_params()
page=query.get("page",["home"])[0]

if page=="login":
    from login import loginPage
    loginPage()
elif page=="home":
    from home import homePage
    homePage()
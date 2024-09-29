# eligibility_check.py
import streamlit as st

# Eligibility Check Page
def show_eligibility_check(user_info):
    st.title("Eligibility Check")

    eligible = True
    st.write("Checking eligibility based on the following conditions:")
    
    if user_info["family_income"] > 800000:
        st.write("Income above 8 lakh: Not eligible")
        eligible = False
    else:
        st.write("Income below 8 lakh: Eligible")
    
    if user_info["domicile_state"] != "Maharashtra":
        st.write(f"Domicile not in Maharashtra ({user_info['domicile_state']}): Not eligible")
        eligible = False
    else:
        st.write("Domicile in Maharashtra: Eligible")
    
    if user_info["college_state"] != "Maharashtra":
        st.write(f"College not in Maharashtra ({user_info['college_state']}): Not eligible")
        eligible = False
    else:
        st.write("College in Maharashtra: Eligible")

    if eligible:
        st.success("You are eligible for the scholarship!")
        st.write("Document requirements:")
        st.write("- Income Certificate")
        st.write("- Domicile Certificate")
        
        if user_info["category"] != "Open":
            st.write("- Caste Certificate")
        
        if st.checkbox("I have all required documents"):
            if st.button("Apply for Scholarship"):
                st.success("Application submitted successfully!")
    else:
        st.error("You are not eligible for the scholarship.")

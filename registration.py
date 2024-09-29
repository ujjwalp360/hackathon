    if submit_button:
        st.success("Registration completed successfully!")
        # Save the registration details using user_id from session_state
            complete_registration(user_id, name=name, aadhaar=aadhaar, family_income=family_income, gender=gender, domicile=domicile, category=category, enrollment_no=enrollment_no, college_state=college_state)
        st.session_state['user']['registration_complete'] = True
        st.success("You can now check your eligibility!")

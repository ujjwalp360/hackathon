import streamlit as st
from db import create_db_connection

# Function to submit scholarship application details
def submit_scholarship_application(username, additional_details):
    db = create_db_connection()
    cursor = db.cursor()

    # Insert the scholarship application details into the 'scholarship_applications' table
    query = """
        INSERT INTO scholarship_applications (username, address, phone_number, bank_account_number, ifsc_code, documents_uploaded)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (username, additional_details['address'], additional_details['phone_number'], 
                           additional_details['bank_account_number'], additional_details['ifsc_code'], 
                           additional_details['documents_uploaded']))

    db.commit()
    cursor.close()
    db.close()

# Function to display the scholarship application page
def apply_for_scholarship(username):
    st.title("Scholarship Application Form")

    # Collect required details for the application
    with st.form("scholarship_form"):
        address = st.text_input("Address")
        phone_number = st.text_input("Phone Number")
        bank_account_number = st.text_input("Bank Account Number")
        ifsc_code = st.text_input("Bank IFSC Code")
        documents_uploaded = st.file_uploader("Upload Required Documents (ZIP or PDF)", type=["zip", "pdf"])

        submit_button = st.form_submit_button("Submit Application")

    if submit_button:
        # Validate user input
        if address and phone_number and bank_account_number and ifsc_code and documents_uploaded:
            # Save the file to a temporary location if needed
            file_path = f"uploads/{documents_uploaded.name}"
            with open(file_path, "wb") as f:
                f.write(documents_uploaded.getbuffer())

            # Submit application details
            submit_scholarship_application(username, {
                'address': address,
                'phone_number': phone_number,
                'bank_account_number': bank_account_number,
                'ifsc_code': ifsc_code,
                'documents_uploaded': documents_uploaded.name  # Store filename, adjust if necessary
            })
            st.success("Your scholarship application has been submitted successfully!")
        else:
            st.error("Please fill in all the required fields and upload the necessary documents.")

# Function to handle navigation from other pages
def scholarship_application_page():
    if 'username' in st.session_state:
        username = st.session_state['username']
        apply_for_scholarship(username)
    else:
        st.error("Please log in to apply for the scholarship.")

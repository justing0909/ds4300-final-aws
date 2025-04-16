from streamlit import st
import requests

def display_form():
    st.title("Data Submission Form")

    with st.form(key='data_form'):
        name = st.text_input("Name")
        email = st.text_input("Email")
        data = st.text_area("Data")
        
        submit_button = st.form_submit_button(label='Submit')

        if submit_button:
            if name and email and data:
                response = submit_data_to_lambda(name, email, data)
                if response.status_code == 200:
                    st.success("Data submitted successfully!")
                else:
                    st.error("Error submitting data.")
            else:
                st.error("Please fill out all fields.")

def submit_data_to_lambda(name, email, data):
    lambda_endpoint = "YOUR_LAMBDA_ENDPOINT"  # Replace with your Lambda endpoint
    payload = {
        "name": name,
        "email": email,
        "data": data
    }
    response = requests.post(lambda_endpoint, json=payload)
    return response
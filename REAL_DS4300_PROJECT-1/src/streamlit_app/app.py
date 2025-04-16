import streamlit as st
from src.streamlit_app.components.form import render_form
from src.streamlit_app.aws.lambda_invoker import invoke_lambda
from src.streamlit_app.utils.config import load_env_variables

def main():
    st.title("Data Submission Form")
    st.write("Please fill out the form below:")

    # Render the form for user input
    user_data = render_form()

    if st.button("Submit"):
        if user_data:
            # Invoke the Lambda function with the user data
            response = invoke_lambda(user_data)
            if response:
                st.success("Data submitted successfully!")
                st.json(response)
            else:
                st.error("Error submitting data. Please try again.")
        else:
            st.warning("Please fill out all fields in the form.")

if __name__ == "__main__":
    load_env_variables()
    main()
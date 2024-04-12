import streamlit as st

# Set the page title
st.set_page_config(page_title="Login Page")

"""
# Welcome to the Login Page!

Please enter your credentials below to login.
"""

# Creating a form for user login
with st.form("login_form"):
    # Input fields for the user to enter email and password
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    # Creating a submit button for the form
    submitted = st.form_submit_button("Login")
    
    # Actions to take upon form submission
    if submitted:
        if email and password:  # Check if fields are not empty
            st.success("Login successful!")
        else:
            st.error("Please enter both email and password.")

# Optional: You can include further instructions or information below the form
"""
### Need Help?
If you have any questions, please visit our [documentation](https://docs.streamlit.io) and [community forums](https://discuss.streamlit.io).
"""

import streamlit as st

# Set the page title
st.set_page_config(page_title="User Profile App")

# Initialize session state variables if they don't exist
if 'login_status' not in st.session_state:
    st.session_state['login_status'] = False
if 'show_details_form' not in st.session_state:
    st.session_state['show_details_form'] = False

# Function to display login form
def show_login_form():
    with st.form("login_form"):
        st.subheader("Please Login")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submitted_login = st.form_submit_button("Login")
        if submitted_login:
            if email and password:
                st.session_state['login_status'] = True
                st.session_state['show_details_form'] = True
            else:
                st.error("Please enter both email and password.")

# Function to display user details form
def show_details_form():
    with st.form("details_form"):
        st.subheader("Enter Your Details")
        education_level = st.selectbox("Education Level", ["High School", "Bachelor's", "Master's", "PhD"])
        work_experience_years = st.slider("Years of Work Experience", 0, 40, 5)
        current_role = st.text_input("Current Role")
        desired_role = st.text_input("Desired Role")
        industry = st.selectbox("Industry", ["Technology", "Healthcare", "Finance", "Education", "Other"])
        preferred_location = st.radio("Preferred Location", ['Remote', 'Hybrid', 'Offsite'])
        
        submitted_details = st.form_submit_button("Submit Details")
        if submitted_details:
            st.success("Details Submitted Successfully!")

# Main application logic
st.title("Welcome to the User Profile Application!")
if not st.session_state['login_status']:
    show_login_form()
elif st.session_state['show_details_form']:
    show_details_form()


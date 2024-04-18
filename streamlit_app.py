import streamlit as st

# Set the page title
st.set_page_config(page_title="User Profile App")

# Initialize session state variables if they don't exist
if 'login_status' not in st.session_state:
    st.session_state['login_status'] = False
if 'show_details_form' not in st.session_state:
    st.session_state['show_details_form'] = False
if 'is_new_user' not in st.session_state:
    st.session_state['is_new_user'] = False

# Function to display the option for the user to choose between login and registration
def choose_login_or_register():
    with st.container():
        st.subheader("Welcome! Please Login or Register")
        if st.button("Login"):
            st.session_state['is_new_user'] = False
        if st.button("Register"):
            st.session_state['is_new_user'] = True

# Function to display registration form
def show_registration_form():
    with st.form("registration_form"):
        st.subheader("Register New Account")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        register_submitted = st.form_submit_button("Register")
        
        if register_submitted:
            if email and password and password == confirm_password:
                # Here, add your code to register the user
                st.session_state['login_status'] = True
                st.session_state['show_details_form'] = True
            elif password != confirm_password:
                st.error("Passwords do not match.")
            else:
                st.error("Please fill in all fields.")

# Function to display login form
def show_login_form():
    with st.form("login_form"):
        st.subheader("Please Login")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submitted_login = st.form_submit_button("Login")
        if submitted_login:
            if email and password:
                # Here, add your code to validate the user
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
st.title("User Profile Application")
if not st.session_state['login_status']:
    if not st.session_state.get('is_new_user'):
        choose_login_or_register()
    elif st.session_state['is_new_user']:
        show_registration_form()
    else:
        show_login_form()
elif st.session_state['show_details_form']:
    show_details_form()

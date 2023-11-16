import streamlit as st
from mainGui import main_menu

def main():
    st.title("Registration and Login Page")

    # Ask the user whether they want to register or log in
    choice = st.radio("Choose an option:", ["Register", "Login"])

    if choice == "Register":
        register()
    elif choice == "Login":
        login()

def register():
    st.header("Registration")

    # Create input fields for registration
    username = st.text_input("Choose a username")
    password = st.text_input("Choose a password", type="password")
    confirm_password = st.text_input("Confirm password", type="password")

    register_button = st.button("Register")

    if register_button:
        # Validate registration inputs (You can replace this with your validation logic)
        if password == confirm_password:
            st.success("Registration successful for username: {}".format(username))
            # Simulate redirection by updating content
            st.markdown("***")
            # This will trigger the main_menu to be displayed
        else:
            st.error("Password and Confirm Password do not match. Please try again.")

def login():
    st.header("Login")

    # Create input fields for login
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Validate login inputs (You can replace this with your authentication logic)
        # For simplicity, we're using a hardcoded username and password
        if username == "user" and password == "pass":
            st.success("Logged in as {}".format(username))
            main_menu()
            # You can redirect to another page or perform additional actions after successful login
        else:
            st.error("Invalid username or password")

# def main_menu():
#     st.title("Main Menu")
    # Your main menu logic goes here

if __name__ == "__main__":
    main()

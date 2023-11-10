import streamlit as st
import time
import keyboard
import os
import psutil
from check_camera import check_camera
from Capture_Image import takeImages
from Train_Image import TrainImages
import Recognize

# Function to clear terminal screen
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Function to display title bar
def title_bar():
    clear_screen()
    st.title("Face Recognition Attendance System 🧑‍💼")

# Function to train images
def train_images():
    with st.spinner("Training images... Please wait."):
        TrainImages()
    st.success("Images Trained Successfully.")

# Function to recognize faces
def recognize_faces():
    Recognize.recognize_attendence()

# Main menu
def main_menu():
    title_bar()
    st.subheader("Welcome Menu")

    # Create a button for each option
    if st.button("Check Camera"):
        check_camera()

    # Button to trigger image capture
    if st.button("Capture Images"):
        takeImages()

    if st.button("Train Images"):
        train_images()

    if st.button("Recognize & Attendance"):
        recognize_faces()
    
    if st.button("Quit"):
        st.warning("Thank You For Using Our Services")
        st.warning("Shutting down the app...")
        time.sleep(4)
        # Close streamlit browser tab
        keyboard.press_and_release('ctrl+w')
        # Terminate streamlit python process
        pid = os.getpid()
        p = psutil.Process(pid)
        p.terminate()

# Main driver
if __name__ == "__main__":
    main_menu()



import csv
import cv2
import os
import streamlit as st
from PIL import Image

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

def takeImages():
    st.title("Capture Images")

    # Get user input for ID and name
    Id = st.text_input("Enter Your Id:")
    name = st.text_input("Enter Your Name:")

    # Create a button to trigger image capture
    start_capturing_button = st.button("Start Capturing")
    
    if start_capturing_button:
        st.warning("lessgo")
        if is_number(Id) and name.isalpha():
            cam = cv2.VideoCapture(0)
            harcascadePath = "haarcascade_frontalface_default.xml"
            detector = cv2.CascadeClassifier(harcascadePath)
            sampleNum = 0

            parent_dir = "TrainingImage"
            directory = os.path.join(parent_dir, Id)
            if not os.path.exists(directory):
                os.makedirs(directory)

            while True:
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (10, 159, 255), 2)
                    sampleNum = sampleNum + 1
                    cv2.imwrite(os.path.join(directory, name + "." + Id + '.' + str(sampleNum) + ".jpg"), gray[y:y + h, x:x + w])

                # Convert the image to PIL format for Streamlit
                pil_image = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
                st.image(pil_image, caption=f"Capturing Images for ID: {Id} Name: {name}", use_column_width=True)

                stop_capturing_button = st.button("Stop Capturing")
                if stop_capturing_button:
                    break

            cam.release()
            cv2.destroyAllWindows()

            res = f"Images Saved for ID: {Id} Name: {name}"
            st.success(res)

            header = ["Id", "Name"]
            row = [Id, name]

            if os.path.isfile("StudentDetails/StudentDetails.csv"):
                with open("StudentDetails/StudentDetails.csv", 'a+') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(j for j in row)
                csvFile.close()
            else:
                with open("StudentDetails/StudentDetails.csv", 'a+') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(i for i in header)
                    writer.writerow(j for j in row)
                csvFile.close()
        else:
            if not is_number(Id):
                st.warning("Enter Numeric ID")
            if not name.isalpha():
                st.warning("Enter Alphabetical Name")

# Test the function
# takeImages()

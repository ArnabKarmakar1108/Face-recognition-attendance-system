import datetime
import os
import time
import cv2
import pandas as pd
import streamlit as st

def recognize_attendence():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("./TrainingImageLabel/Trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)
    df = pd.read_csv("StudentDetails" + os.sep + "StudentDetails.csv")
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', 'Name', 'Date', 'Time']
    attendance_list = []

    # Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # set video width
    cam.set(4, 480)  # set video height

    # Define min window size to be recognized as a face
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    while True:
        _, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        attendance_file = "Attendance" + os.sep + "Attendance_" + str(datetime.date.today()) + ".csv"
        faces = faceCascade.detectMultiScale(gray, 1.2, 5, minSize=(int(minW), int(minH)),
                                             flags=cv2.CASCADE_SCALE_IMAGE)

        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (10, 159, 255), 2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])

            if conf < 100:
                aa = df.loc[df['Id'] == Id]['Name'].values
                confstr = "  {0}%".format(round(100 - conf))
                tt = str(Id) + "-" + aa
            else:
                Id = '  Unknown  '
                tt = str(Id)
                confstr = "  {0}%".format(round(100 - conf))

            if (100 - conf) > 55:
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = str(aa)[2:-2]
                attendance_list.append([Id, aa, date, timeStamp])

            tt = str(tt)[2:-2]
            if (100 - conf) > 55:
                tt = tt + " [Pass]"
                cv2.putText(im, str(tt), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            else:
                cv2.putText(im, str(tt), (x + 5, y - 5), font, 1, (255, 255, 255), 2)

            if (100 - conf) > 55:
                cv2.putText(im, str(confstr), (x + 5, y + h - 5), font, 1, (0, 255, 0), 1)
            elif (100 - conf) > 50:
                cv2.putText(im, str(confstr), (x + 5, y + h - 5), font, 1, (0, 255, 255), 1)
            else:
                cv2.putText(im, str(confstr), (x + 5, y + h - 5), font, 1, (0, 0, 255), 1)

        cv2.imshow('Attendance', im)
        if cv2.waitKey(1) == ord('q'):
            break

    attendance = pd.DataFrame(attendance_list, columns=col_names)
    attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
    print(attendance)

    if not os.path.isfile(attendance_file):
        attendance.to_csv(attendance_file, index=False)
    else:
        attendance.to_csv(attendance_file, mode='a', header=False, index=False)

    cam.release()
    cv2.destroyAllWindows()

    if len(attendance_list) > 0:
        last_record = attendance_list[-1]
        st.success(f"Attendance Successful for ID: {last_record[0]}, Name: {last_record[1]}")
    else:
        st.error("Attendance Couldn't Be Marked")

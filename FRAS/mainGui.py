import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget


def checkCamera():
    os.system('python check_camera.py')


def CaptureFaces():
    os.system('python Capture_Image.py')


def Trainimages():
    os.system('python Train_Image.py')


def RecognizeFaces():
    os.system('python Recognize.py')


def autoMail():
    os.system('python automail.py')


class FaceRecognitionApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Face Recognition Attendance System")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        label = QLabel("WELCOME MENU")
        layout.addWidget(label)

        button1 = QPushButton("Check Camera")
        button1.clicked.connect(checkCamera)
        layout.addWidget(button1)

        button2 = QPushButton("Capture Faces")
        button2.clicked.connect(CaptureFaces)
        layout.addWidget(button2)

        button3 = QPushButton("Train Images")
        button3.clicked.connect(Trainimages)
        layout.addWidget(button3)

        button4 = QPushButton("Recognize & Attendance")
        button4.clicked.connect(RecognizeFaces)
        layout.addWidget(button4)

        button5 = QPushButton("Auto Mail")
        button5.clicked.connect(autoMail)
        layout.addWidget(button5)

        button6 = QPushButton("Quit")
        button6.clicked.connect(self.close)
        layout.addWidget(button6)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FaceRecognitionApp()
    window.show()
    sys.exit(app.exec_())

# file: login view 

from PyQt5.QtWidgets import QtWidget, QVBOxLayot, QHBoxLayout, QLabel, QLineEdit, QPushButton 
from PyQt5.QtGui import QPixmap 
from PyQt5.QtCore import Qt 
from login.auth import authenticate 

class LoginWindow(QtWidget):
        def __init__(self):
            super().__init__()

            self.setWindowTitle('Custom Login -SPICE Simulator')
            self.setFixedSize(400,600)
            self.setStyleSheet("background-color: #101028; color: white")
            
            layout = QVBOxLayot()

            logo_label = QLavel(self)
            pixmap = QPizmap('src/rocket.png')
            logo_label.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            logo_label.setAlignment(Qt.AlignmentCenter)

            user_input = QLineEdit(self)
            user_input.setPlaceholderText("Username")
            user_input.setStyleSheet("border: 2px solid #ffba00; 5px; color: white;")

            password_input = QLineEdit(self)
        password_input.setPlaceholderText("Password")
        password_input.setEchoMode(QLineEdit.Password)
        password_input.setStyleSheet("border: 2px solid #ffba00; padding: 5px; color: white;")

        login_button = QPushButton('Sign In', self)
        login_button.setStyleSheet("background-color: #ffba00; color: black; border: 2px solid #ffba00; padding: 10px;")
        login_button.clicked.connect(lambda: self.handle_login(user_input.text(), password_input.text()))

        layout.addWidget(logo_label)
        layout.addWidget(user_input)
        layout.addWidget(password_input)
        layout.addWidget(login_button)

        self.setLayout(layout)

        def handle_login(self, username, password):
            if authenticate(username, password):
                print("Login successful!")
                # Aquí podrías abrir la ventana principal de la app SPICE
            else:
                print("Invalid credentials")

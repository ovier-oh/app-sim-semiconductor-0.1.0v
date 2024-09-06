import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import requests

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Custom Login - SPICE Simulator')
        self.setFixedSize(400, 500)
        self.setStyleSheet("background-color: #101028; color: white;")

        layout = QVBoxLayout()

        logo_label = QLabel(self)
        pixmap = QPixmap('graphx/rocket.png')
        logo_label.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        logo_label.setAlignment(Qt.AlignCenter)

        self.user_input = QLineEdit(self)
        self.user_input.setPlaceholderText("Username")
        self.user_input.setStyleSheet("border: 2px solid #ffba00; padding: 5px; color: white;")

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet("border: 2px solid #ffba00; padding: 5px; color: white;")

        login_button = QPushButton('Sign In', self)
        login_button.setStyleSheet("background-color: #ffba00; color: black; border: 2px solid #ffba00; padding: 10px;")
        login_button.clicked.connect(self.handle_login)

        layout.addWidget(logo_label)
        layout.addWidget(self.user_input)
        layout.addWidget(self.password_input)
        layout.addWidget(login_button)

        self.setLayout(layout)

    def handle_login(self):
        username = self.user_input.text()
        password = self.password_input.text()

        try:
            response = requests.post('http://127.0.0.1:5000/login', json={"username": username, "password": password})
            if response.status_code == 200:
                print("Login successful")
            else:
                print("Login failed: Invalid credentials")
        except requests.exceptions.RequestException as e:
            print(f"Error connecting to the server: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())

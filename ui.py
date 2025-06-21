from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMainWindow,
    QLineEdit, QMessageBox
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from database import register_user, validate_user


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setGeometry(400, 200, 300, 200)

        layout = QVBoxLayout()

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.handle_login)

        layout.addWidget(QLabel("Login"))
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if validate_user(username, password):
            QMessageBox.information(
                self, "Login Successful", f"Welcome, {username}")
            self.close()
        else:
            QMessageBox.warning(self, "Login Failed",
                                "Invalid username or password.")



class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Register")
        self.setGeometry(400, 200, 300, 250)

        layout = QVBoxLayout()

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Choose a Username")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Choose a Password")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.confirm_input = QLineEdit()
        self.confirm_input.setPlaceholderText("Confirm Password")
        self.confirm_input.setEchoMode(QLineEdit.Password)

        self.register_button = QPushButton("Register")
        self.register_button.clicked.connect(self.handle_register)

        layout.addWidget(QLabel("Register"))
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.confirm_input)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

        def handle_register(self):
            username = self.username_input.text()
            password = self.password_input.text()
            confirm = self.confirm_input.text()

            if not username or not password:
                QMessageBox.warning(self, "Error", "Please fill all fields.")
                return

            if password != confirm:
                QMessageBox.warning(self, "Error", "Passwords do not match.")
                return

            success = register_user(username, password)
            if success:
                QMessageBox.information(
                    self, "Success", f"User '{username}' registered successfully!")
                self.close()
            else:
                QMessageBox.warning(self, "Error", "Username already exists.")



class WelcomeScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Youth Skills & Market Alignment")
        self.setGeometry(300, 150, 600, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        title = QLabel("Youth Skills & Market Alignment")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)

        subtitle = QLabel(
            "Empowering youth with skills for today’s job market")
        subtitle.setAlignment(Qt.AlignCenter)

        self.login_button = QPushButton("Login")
        self.register_button = QPushButton("Register")
        self.guest_button = QPushButton("Continue as Guest")

        self.login_button.clicked.connect(self.open_login)
        self.register_button.clicked.connect(self.open_register)

        for btn in [self.login_button, self.register_button, self.guest_button]:
            btn.setFixedHeight(40)

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(30)
        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)
        layout.addWidget(self.guest_button)

        central_widget.setLayout(layout)

    def open_login(self):
        self.login_window = LoginWindow()
        self.login_window.show()

    def open_register(self):
        self.register_window = RegisterWindow()
        self.register_window.show()

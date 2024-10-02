import sys
from services.db import mydb
from main_page import StockApp
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QStackedWidget, QMessageBox

class LoginWidget(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        username_layout = QHBoxLayout()
        username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        username_layout.addWidget(username_label)
        username_layout.addWidget(self.username_input)

        password_layout = QHBoxLayout()
        password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        password_layout.addWidget(password_label)
        password_layout.addWidget(self.password_input)

        login_button = QPushButton("Login")
        login_button.clicked.connect(self.login)

        switch_to_register_button = QPushButton("Sign Up")
        switch_to_register_button.clicked.connect(self.switch_to_register)

        layout.addLayout(username_layout)
        layout.addLayout(password_layout)
        layout.addWidget(login_button)
        layout.addWidget(switch_to_register_button)

        self.setLayout(layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        print(username, password)
        
        try:
            mycursor = mydb.cursor()
            query = "SELECT password FROM users.users WHERE userName = %s"
            mycursor.execute(query, (username,))
            result = mycursor.fetchone()
            
            if result:
                correctPassword = result[0]
                if password == correctPassword:
                    print("User logged in successfully")
                    self.open_stock_app()
                else:
                    print("Incorrect password!")
                    self.show_alert("Incorrect Password", "The password you entered is incorrect. Please try again.")
            else:
                print("There is no such user...")
                self.show_alert("User Not Found", "No such user found. Please check the username and try again.")
                
        except Exception as e:
            print(f"A server error occurred while the user was logging in: {e}")
            self.show_alert("Login Error", "An error occurred while trying to log in. Please try again later.")

    def show_alert(self, title, message):
        alert = QMessageBox()
        alert.setWindowTitle(title)
        alert.setText(message)
        alert.setStandardButtons(QMessageBox.StandardButton.Ok)
        alert.exec()
    
    def open_stock_app(self):
        self.stock_app = StockApp()
        self.stock_app.show()
        self.close()

    def switch_to_register(self):
        self.stacked_widget.setCurrentIndex(1)

class RegisterWidget(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        username_layout = QHBoxLayout()
        username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        username_layout.addWidget(username_label)
        username_layout.addWidget(self.username_input)

        password_layout = QHBoxLayout()
        password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        password_layout.addWidget(password_label)
        password_layout.addWidget(self.password_input)

        confirm_password_layout = QHBoxLayout()
        confirm_password_label = QLabel("Repeat Password:")
        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setEchoMode(QLineEdit.EchoMode.Password)
        confirm_password_layout.addWidget(confirm_password_label)
        confirm_password_layout.addWidget(self.confirm_password_input)

        register_button = QPushButton("Sign Up")
        register_button.clicked.connect(self.register)

        switch_to_login_button = QPushButton("Login")
        switch_to_login_button.clicked.connect(self.switch_to_login)

        layout.addLayout(username_layout)
        layout.addLayout(password_layout)
        layout.addLayout(confirm_password_layout)
        layout.addWidget(register_button)
        layout.addWidget(switch_to_login_button)

        self.setLayout(layout)

    def register(self):
        username = self.username_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()
        
        if password != confirm_password:
            print("Error: Passwords do not match!")
            self.show_alert("Error", "Passwords do not match Please try again" )
        else:
            try:
                mycursor = mydb.cursor()
                sql = "INSERT INTO users.users (userName, password) VALUES (%s, %s)"
                val = ( username, password )
                mycursor.execute(sql, val)
                mydb.commit()
                print("User added to database.")
                self.open_stock_app()
            except:
                print("An error occurred while adding the user to the database")
                self.show_alert("Register Error", "An error occurred while trying to log in. Please try again later.")

    def show_alert(self, title, message):
        alert = QMessageBox()
        alert.setWindowTitle(title)
        alert.setText(message)
        alert.setStandardButtons(QMessageBox.StandardButton.Ok)
        alert.exec()
        
    def open_stock_app(self):
        self.stock_app = StockApp()
        self.stock_app.show()
        self.close()
    
    def switch_to_login(self):
        self.stacked_widget.setCurrentIndex(0)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.stacked_widget = QStackedWidget()
        
        login_widget = LoginWidget(self.stacked_widget)
        register_widget = RegisterWidget(self.stacked_widget)
        
        self.stacked_widget.addWidget(login_widget)
        self.stacked_widget.addWidget(register_widget)

        layout = QVBoxLayout()
        layout.addWidget(self.stacked_widget)
        self.setLayout(layout)

        self.setWindowTitle('Stock Market Tracker')
        self.setGeometry(300, 300, 300, 200)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
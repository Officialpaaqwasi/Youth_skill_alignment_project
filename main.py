import sys
from PyQt5.QtWidgets import QApplication
from ui import WelcomeScreen
from database import create_tables  # 👈


def main():
    create_tables()  # 👈 make sure database is set up
    app = QApplication(sys.argv)
    window = WelcomeScreen()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

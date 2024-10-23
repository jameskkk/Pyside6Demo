import sys
import PySide6.QtCore
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QLabel
from ui_main_window import Ui_MainWindow

class HBMainWindowManual:
    def __init__(self):
        loader = QUiLoader()
        self.ui = loader.load("main_window.ui")

class HBMainWindowAuto(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnOK.clicked.connect(self.say_ok)

    def say_ok(self):
        message_box = QMessageBox(self)
        message_box.setWindowTitle("MessageBox")
        message_box.setText("Enter OK and Cancel?")
        message_box.setIcon(QMessageBox.Information)
        message_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        
        response = message_box.exec()

        if response == QMessageBox.Ok:
            print("Enter OK!")
        else:
            print("Enter Cancel!")

if __name__ == "__main__":
    # Prints PySide6 version
    print(PySide6.__version__)

    # Prints the Qt version used to compile PySide6
    print(PySide6.QtCore.__version__)

    app = QApplication(sys.argv)
    # label = QLabel("Hello World!")
    # label.resize(640, 480)
    # label.show()

    # hb_window = HBMainWindowManual()
    # hb_window.ui.show()
    hb_window = HBMainWindowAuto()
    hb_window.show()
    app.exec()
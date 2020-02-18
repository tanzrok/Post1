from PyQt5 import QtCore, QtGui, QtWidgets
from Otkaz import Ui_Dialog
import sys

class Ot(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp=Ot()
    myapp.show()
    sys.exit(app.exec())
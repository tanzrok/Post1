from PyQt5 import QtCore, QtGui, QtWidgets
from usp import Ui_Dialog
import sys
import w32


class Uspeh(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.post=w32.Post()
        self.ui.label_3.setText('123')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp=Uspeh()
    myapp.show()
    sys.exit(app.exec())
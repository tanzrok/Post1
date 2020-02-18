import auth_up
import web3
import w32
import uspeh
import sys
import error_dt
import lich
from PyQt5 import QtCore, QtGui, QtWidgets

class Registr(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.reg)
        self.ui.pushButton.clicked.connect(self.login)
    def reg(self):
        fam = self.ui.lineEdit.text()
        name = self.ui.lineEdit_2.text()
        index = self.ui.lineEdit_4.text()
        adress = self.ui.lineEdit_3.text()
        password = self.ui.lineEdit_5.text()
        if self.w32.Post().reg(fam, name, index, adress, password):
            self.open=uspeh.Uspeh()
            self.open.show()
        else:
            self.open = error_dt.Erro()
            self.open.show()

    def login(self):
        user_adr=web3.Web3.toChecksumAddress(self.ui.lineEdit_6.text())
        passw=str(self.ui.lineEdit_7.text())
        if self.w32.Post().auth(user_adr, passw):
            self.open=lich.lich_k()
            self.open.show()
        else:
            self.open=error_dt.Erro()
            self.open.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp=Registr()
    myapp.show()
    sys.exit(app.exec())

from PyQt5 import QtCore, QtGui, QtWidgets
from auth import Ui_Dialog
import sys
import w32
import uspeh
import error_dt
import web3

class Auth(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.post=w32.Post()
        self.user=None
        self.passw=None
        self.ui.pushButton.clicked.connect(self.reg)
        #self.ui.pushButton_2.clicked.connect(self.login)
    def reg(self):
        fam = self.ui.lineEdit.text()
        name = self.ui.lineEdit_2.text()
        index = self.ui.lineEdit_4.text()
        adr = self.ui.lineEdit_3.text()
        password = self.ui.lineEdit_5.text()
        print(self.post.w3.eth.defaultAccount)
        try:
            user=self.post.reg(fam, name, adr, int(index), password)
            self.open=uspeh.Uspeh()
            self.open.show()
        except:
            self.open = error_dt.Erro()
            self.open.show()

    '''def login(self):
        user_adr=web3.Web3.toChecksumAddress(self.ui.lineEdit_6.text())
        passw=str(self.ui.lineEdit_7.text())
        if self.w32.Post().auth(user_adr, passw):
            self.open=lich.lich_k()
            self.open.show()
        else:
            self.open=error_dt.Erro()
            self.open.show()'''

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp=Auth()
    myapp.show()
    sys.exit(app.exec())
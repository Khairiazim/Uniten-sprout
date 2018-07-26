import sys
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets
from UI import login_insta
from dic import dicAcc

class Login_class(login_insta.Ui_Dialog_login,QtWidgets.QDialog):
    def __init__(self):
        # QtWidgets.QDialog.__init__(self)
        # uic.loadUi("UI/login_insta.ui",self)
        super(login_insta.Ui_Dialog_login, self).__init__() #import ui.py
        self.setupUi(self)

        ###############     GUI ACTION      #################
        self.pb_Login.clicked.connect(self.login)
        try:
            username = dicAcc.ACCOUNT_INSTA["username"]
            password = dicAcc.ACCOUNT_INSTA["password"]
            self.le_username.setText(username)
            self.le_password.setText(password)
        except:
            pass
    def login(self):
        username = str(self.le_username.text())
        password = str(self.le_password.text())

        dict = {'username':username, 'password':password}
        dicAcc.ACCOUNT_INSTA = dict
        self.close()

if __name__== "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Login = Login_class()#take from here put (self.) at front
    Login.show()#import this #class #untill here
    sys.exit(app.exec_())

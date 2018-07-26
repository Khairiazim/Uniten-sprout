import os
import sys

import requests
from PyQt5 import QtCore, QtWidgets
from PyQt5 import uic

import API_Util
from UI import license_windowes
import Software


class License_class(license_windowes.License_window_class,QtWidgets.QMainWindow):
    def __init__(self):
        # QtWidgets.QMainWindow.__init__(self)
        # uic.loadUi("UI/license_window.ui",self)
        super(license_windowes.License_window_class, self).__init__()
        self.setupUi(self)

        self.pb_apply.setEnabled(False)
        self.checkBox.stateChanged.connect(self.Enable_button)
        self.pb_renew.clicked.connect(self.renew_license)

    def renew_license(self):
        QtWidgets.QMessageBox.information(self,"Hi user","we will connect you to our renew page")
        #open renew web page


    def Enable_button(self,state):
        if state == QtCore.Qt.Checked:
            self.pb_apply.setEnabled(True)
            self.pb_apply.clicked.connect(self.Apply)
        else:
            self.pb_apply.setEnabled(False)

    def Apply(self):
        username = str(self.le_username.text())
        password = str(self.le_password.text())

        try:
            result = requests.post(API_Util.API_URL + "api/user/app_login", 
            data={  'username': username,
                    'password': password,
                    'pcname' : os.environ['COMPUTERNAME'],
                    'api_key': API_Util.API_KEY,
                    'mac_guid': API_Util.get_machine_guid()})
            result = result.json()

        except:
            # NO INTERNET CONNECTION
            QtWidgets.QMessageBox.information(self, "Hi user", "Cannot connect to the server. Please check your connection.")

        if result['status'] == 1:
            # LOGIN SUCCESS
            QtWidgets.QMessageBox.information(self, "Hi user", "Login Success.")
            self.open_software_ui()
            self.close()
        else:
            if result['code'] == 1:
                # WRONG USERNAME OR PASSWORD
                QtWidgets.QMessageBox.information(self, "Hi user", "Wrong username or password.")
            elif result['code'] == 2:
                # FREE ACCOUNT
                QtWidgets.QMessageBox.information(self, "Hi user", "Cannot use FREE account. Please upgrade your account.")
            elif result['code'] == 3:
                # FREE ACCOUNT
                QtWidgets.QMessageBox.information(self, "Hi user",
                    "You have reached your account login limit. Please log out from other PC.")


    def open_software_ui(self):
        self.Software = Software.Software_class()
        self.Software.show()

if __name__== "__main__":
    app = QtWidgets.QApplication(sys.argv)
    License = License_class()
    License.show()
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_insta.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_login(object):
    def setupUi(self, Dialog_login):
        Dialog_login.setObjectName("Dialog_login")
        Dialog_login.resize(306, 101)
        Dialog_login.setFocusPolicy(QtCore.Qt.WheelFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Icon/Bokehlicia-Captiva-Rocket.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog_login.setWindowIcon(icon)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Dialog_login)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_Username = QtWidgets.QLabel(Dialog_login)
        self.label_Username.setObjectName("label_Username")
        self.verticalLayout.addWidget(self.label_Username)
        self.label_Pass = QtWidgets.QLabel(Dialog_login)
        self.label_Pass.setObjectName("label_Pass")
        self.verticalLayout.addWidget(self.label_Pass)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.le_username = QtWidgets.QLineEdit(Dialog_login)
        self.le_username.setObjectName("le_username")
        self.verticalLayout_2.addWidget(self.le_username)
        self.le_password = QtWidgets.QLineEdit(Dialog_login)
        self.le_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_password.setObjectName("le_password")
        self.verticalLayout_2.addWidget(self.le_password)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pb_Cancel = QtWidgets.QPushButton(Dialog_login)
        self.pb_Cancel.setObjectName("pb_Cancel")
        self.horizontalLayout_2.addWidget(self.pb_Cancel)
        self.pb_Login = QtWidgets.QPushButton(Dialog_login)
        self.pb_Login.setObjectName("pb_Login")
        self.horizontalLayout_2.addWidget(self.pb_Login)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.label_Username.setBuddy(self.le_username)
        self.label_Pass.setBuddy(self.le_password)

        self.retranslateUi(Dialog_login)
        self.pb_Cancel.clicked.connect(self.le_password.clear)
        self.pb_Cancel.clicked.connect(self.le_username.clear)
        self.pb_Login.clicked.connect(Dialog_login.open)
        QtCore.QMetaObject.connectSlotsByName(Dialog_login)
        Dialog_login.setTabOrder(self.le_username, self.le_password)
        Dialog_login.setTabOrder(self.le_password, self.pb_Login)
        Dialog_login.setTabOrder(self.pb_Login, self.pb_Cancel)

    def retranslateUi(self, Dialog_login):
        _translate = QtCore.QCoreApplication.translate
        Dialog_login.setWindowTitle(_translate("Dialog_login", "Login"))
        self.label_Username.setText(_translate("Dialog_login", "Username"))
        self.label_Pass.setText(_translate("Dialog_login", "Password"))
        self.pb_Cancel.setText(_translate("Dialog_login", "Cancel"))
        self.pb_Login.setText(_translate("Dialog_login", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_login = QtWidgets.QDialog()
    ui = Ui_Dialog_login()
    ui.setupUi(Dialog_login)
    Dialog_login.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'unfollow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_Unfollow(object):
    def setupUi(self, Form_Unfollow):
        Form_Unfollow.setObjectName("Form_Unfollow")
        Form_Unfollow.resize(336, 99)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Icon/Bokehlicia-Captiva-Rocket.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form_Unfollow.setWindowIcon(icon)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form_Unfollow)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.rb_unnonfol = QtWidgets.QRadioButton(Form_Unfollow)
        self.rb_unnonfol.setObjectName("rb_unnonfol")
        self.verticalLayout.addWidget(self.rb_unnonfol)
        self.rb_unall = QtWidgets.QRadioButton(Form_Unfollow)
        self.rb_unall.setObjectName("rb_unall")
        self.verticalLayout.addWidget(self.rb_unall)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pb_cancel = QtWidgets.QPushButton(Form_Unfollow)
        self.pb_cancel.setObjectName("pb_cancel")
        self.horizontalLayout.addWidget(self.pb_cancel)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.pb_un_start = QtWidgets.QPushButton(Form_Unfollow)
        self.pb_un_start.setObjectName("pb_un_start")
        self.horizontalLayout.addWidget(self.pb_un_start)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Form_Unfollow)
        QtCore.QMetaObject.connectSlotsByName(Form_Unfollow)
        Form_Unfollow.setTabOrder(self.rb_unnonfol, self.rb_unall)
        Form_Unfollow.setTabOrder(self.rb_unall, self.pb_un_start)
        Form_Unfollow.setTabOrder(self.pb_un_start, self.pb_cancel)

    def retranslateUi(self, Form_Unfollow):
        _translate = QtCore.QCoreApplication.translate
        Form_Unfollow.setWindowTitle(_translate("Form_Unfollow", "Unfollow"))
        self.rb_unnonfol.setText(_translate("Form_Unfollow", "Unfollow non followers"))
        self.rb_unall.setText(_translate("Form_Unfollow", "Unfollow everyone"))
        self.pb_cancel.setText(_translate("Form_Unfollow", "Cancel"))
        self.pb_un_start.setText(_translate("Form_Unfollow", "Apply"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_Unfollow = QtWidgets.QWidget()
    ui = Ui_Form_Unfollow()
    ui.setupUi(Form_Unfollow)
    Form_Unfollow.show()
    sys.exit(app.exec_())


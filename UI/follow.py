# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'follow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_Follow(object):
    def setupUi(self, Form_Follow):
        Form_Follow.setObjectName("Form_Follow")
        Form_Follow.resize(327, 179)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Icon/Bokehlicia-Captiva-Rocket.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form_Follow.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form_Follow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(Form_Follow)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form_Follow)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Form_Follow)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pb_add = QtWidgets.QPushButton(Form_Follow)
        self.pb_add.setObjectName("pb_add")
        self.horizontalLayout.addWidget(self.pb_add)
        self.pb_delete = QtWidgets.QPushButton(Form_Follow)
        self.pb_delete.setObjectName("pb_delete")
        self.horizontalLayout.addWidget(self.pb_delete)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.listWidget = QtWidgets.QListWidget(Form_Follow)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pb_apply = QtWidgets.QPushButton(Form_Follow)
        self.pb_apply.setObjectName("pb_apply")
        self.horizontalLayout_2.addWidget(self.pb_apply)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form_Follow)
        QtCore.QMetaObject.connectSlotsByName(Form_Follow)

    def retranslateUi(self, Form_Follow):
        _translate = QtCore.QCoreApplication.translate
        Form_Follow.setWindowTitle(_translate("Form_Follow", "Follow"))
        self.comboBox.setItemText(0, _translate("Form_Follow", "Follow From Hashtag"))
        self.comboBox.setItemText(1, _translate("Form_Follow", "Follow Followers"))
        self.comboBox.setItemText(2, _translate("Form_Follow", "Follow Following"))
        self.comboBox.setItemText(3, _translate("Form_Follow", "Follow By Likes On Media"))
        self.label.setText(_translate("Form_Follow", "Hashtag"))
        self.lineEdit.setPlaceholderText(_translate("Form_Follow", "love"))
        self.pb_add.setText(_translate("Form_Follow", "Add"))
        self.pb_delete.setText(_translate("Form_Follow", "Delete"))
        self.pb_apply.setText(_translate("Form_Follow", "Apply"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_Follow = QtWidgets.QWidget()
    ui = Ui_Form_Follow()
    ui.setupUi(Form_Follow)
    Form_Follow.show()
    sys.exit(app.exec_())


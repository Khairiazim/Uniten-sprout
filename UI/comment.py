# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'comment.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_Comment(object):
    def setupUi(self, Form_Comment):
        Form_Comment.setObjectName("Form_Comment")
        Form_Comment.resize(513, 289)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Icon/Bokehlicia-Captiva-Rocket.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form_Comment.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form_Comment)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(Form_Comment)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form_Comment)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Form_Comment)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pb_add = QtWidgets.QPushButton(Form_Comment)
        self.pb_add.setObjectName("pb_add")
        self.horizontalLayout.addWidget(self.pb_add)
        self.pb_delete = QtWidgets.QPushButton(Form_Comment)
        self.pb_delete.setObjectName("pb_delete")
        self.horizontalLayout.addWidget(self.pb_delete)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.listWidget = QtWidgets.QListWidget(Form_Comment)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(Form_Comment)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(Form_Comment)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.pb_add2 = QtWidgets.QPushButton(Form_Comment)
        self.pb_add2.setObjectName("pb_add2")
        self.horizontalLayout_3.addWidget(self.pb_add2)
        self.pb_delete2 = QtWidgets.QPushButton(Form_Comment)
        self.pb_delete2.setObjectName("pb_delete2")
        self.horizontalLayout_3.addWidget(self.pb_delete2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.lw_comment = QtWidgets.QListWidget(Form_Comment)
        self.lw_comment.setObjectName("lw_comment")
        self.verticalLayout.addWidget(self.lw_comment)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pb_apply = QtWidgets.QPushButton(Form_Comment)
        self.pb_apply.setObjectName("pb_apply")
        self.horizontalLayout_2.addWidget(self.pb_apply)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form_Comment)
        QtCore.QMetaObject.connectSlotsByName(Form_Comment)

    def retranslateUi(self, Form_Comment):
        _translate = QtCore.QCoreApplication.translate
        Form_Comment.setWindowTitle(_translate("Form_Comment", "Comment"))
        self.comboBox.setItemText(0, _translate("Form_Comment", "Comment From Hashtag"))
        self.comboBox.setItemText(1, _translate("Form_Comment", "Comment Userlist"))
        self.comboBox.setItemText(2, _translate("Form_Comment", "Comment Your Timeline"))
        self.label.setText(_translate("Form_Comment", "Hashtag:"))
        self.lineEdit.setPlaceholderText(_translate("Form_Comment", "love"))
        self.pb_add.setText(_translate("Form_Comment", "Add"))
        self.pb_delete.setText(_translate("Form_Comment", "Delete"))
        self.label_2.setText(_translate("Form_Comment", "Comment:"))
        self.lineEdit_2.setPlaceholderText(_translate("Form_Comment", "Enter your comment"))
        self.pb_add2.setText(_translate("Form_Comment", "Add"))
        self.pb_delete2.setText(_translate("Form_Comment", "Delete"))
        self.pb_apply.setText(_translate("Form_Comment", "Apply"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_Comment = QtWidgets.QWidget()
    ui = Ui_Form_Comment()
    ui.setupUi(Form_Comment)
    Form_Comment.show()
    sys.exit(app.exec_())


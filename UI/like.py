# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'like.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_Like(object):
    def setupUi(self, Form_Like):
        Form_Like.setObjectName("Form_Like")
        Form_Like.resize(484, 179)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Icon/Bokehlicia-Captiva-Rocket.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form_Like.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form_Like)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(Form_Like)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_username = QtWidgets.QLabel(Form_Like)
        self.label_username.setObjectName("label_username")
        self.horizontalLayout.addWidget(self.label_username)
        self.le_hashtag = QtWidgets.QLineEdit(Form_Like)
        self.le_hashtag.setInputMethodHints(QtCore.Qt.ImhNone)
        self.le_hashtag.setInputMask("")
        self.le_hashtag.setText("")
        self.le_hashtag.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.le_hashtag.setObjectName("le_hashtag")
        self.horizontalLayout.addWidget(self.le_hashtag)
        self.pb_add = QtWidgets.QPushButton(Form_Like)
        self.pb_add.setObjectName("pb_add")
        self.horizontalLayout.addWidget(self.pb_add)
        self.pb_delete = QtWidgets.QPushButton(Form_Like)
        self.pb_delete.setObjectName("pb_delete")
        self.horizontalLayout.addWidget(self.pb_delete)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.listWidget = QtWidgets.QListWidget(Form_Like)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pb_apply = QtWidgets.QPushButton(Form_Like)
        self.pb_apply.setObjectName("pb_apply")
        self.horizontalLayout_2.addWidget(self.pb_apply)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form_Like)
        QtCore.QMetaObject.connectSlotsByName(Form_Like)
        Form_Like.setTabOrder(self.pb_add, self.pb_apply)
        Form_Like.setTabOrder(self.pb_apply, self.pb_delete)
        Form_Like.setTabOrder(self.pb_delete, self.comboBox)
        Form_Like.setTabOrder(self.comboBox, self.le_hashtag)
        Form_Like.setTabOrder(self.le_hashtag, self.listWidget)

    def retranslateUi(self, Form_Like):
        _translate = QtCore.QCoreApplication.translate
        Form_Like.setWindowTitle(_translate("Form_Like", "Like"))
        self.comboBox.setItemText(0, _translate("Form_Like", "Like from hashtag"))
        self.comboBox.setItemText(1, _translate("Form_Like", "Like followers"))
        self.comboBox.setItemText(2, _translate("Form_Like", "Like following"))
        self.comboBox.setItemText(3, _translate("Form_Like", "Like last media likers"))
        self.comboBox.setItemText(4, _translate("Form_Like", "Like your timeline"))
        self.label_username.setText(_translate("Form_Like", "Hashtag"))
        self.le_hashtag.setPlaceholderText(_translate("Form_Like", "love"))
        self.pb_add.setText(_translate("Form_Like", "Add"))
        self.pb_delete.setText(_translate("Form_Like", "Delete"))
        self.pb_apply.setText(_translate("Form_Like", "Apply"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_Like = QtWidgets.QWidget()
    ui = Ui_Form_Like()
    ui.setupUi(Form_Like)
    Form_Like.show()
    sys.exit(app.exec_())


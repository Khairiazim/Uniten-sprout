import sys
import os
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets

sys.path.append(os.path.join(sys.path[0], '../'))
from UI import like

like_job_file = "Private/like_job.txt"
like_random_file = "Private/like_random.txt"

class Like_class (like.Ui_Form_Like,QtWidgets.QDialog):
    def __init__(self):
        # QtWidgets.QDialog.__init__(self)
        # uic.loadUi("ui/like.ui",self)
        super(like.Ui_Form_Like, self).__init__() #import UI.py
        self.setupUi(self)

        ###########     GUI ACTION      ###################
        self.comboBox.currentIndexChanged.connect(self.check_cb)
        self.pb_add.clicked.connect(self.add_list)
        self.pb_delete.clicked.connect(self.del_list)
        self.pb_apply.clicked.connect(self.Apply)

    def check_cb(self):
        name = self.comboBox.currentText()
        if name == "Like from hashtag":
            self.label_username.setText("Hashtag")
            self.le_hashtag.setPlaceholderText("love")

        elif name == "Like followers":
            self.label_username.setText("Username")
            self.le_hashtag.setPlaceholderText("autopilot.co")

        elif name == "Like following":
            self.label_username.setText("Username")
            self.le_hashtag.setPlaceholderText("autopilot.co")

        elif name == "Like last media likers":
            self.label_username.setText("Username")
            self.le_hashtag.setPlaceholderText("autopilot.co")

        else:
            self.label_username.setText("Your Username Only")
            self.le_hashtag.setPlaceholderText("autopilot.co")

    def add_list(self):
        self.listWidget.addItem(self.le_hashtag.text())
        self.le_hashtag.setText("")
        self.le_hashtag.setFocus()

    def del_list(self):
        self.listWidget.takeItem(self.listWidget.currentRow())

    def clean_list(self):
        itemsTextList = [str(self.listWidget.item(i).text().strip()) for i in range(self.listWidget.count())]
        while '' in itemsTextList:
            itemsTextList.remove('')
        return itemsTextList

    # def current_list(self):


    def Apply(self):
        with open(like_job_file,"w") as wf:
            name = self.comboBox.currentText()
            if name == "Like from hashtag":
                wf.write(name)

            elif name == "Like followers":
                wf.write(name)

            elif name == "Like following":
                wf.write(name)

            elif name == "Like last media likers":
                wf.write(name)

            else:
                wf.write("Like your timeline")

        with open(like_random_file,"w") as wf:
            for i in self.clean_list():
                wf.write(i + "\n")
        self.close()

if __name__== "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Like = Like_class()
    Like.show()
    sys.exit(app.exec_())
import sys
import os
from PyQt5 import uic
from PyQt5 import QtCore, QtGui, QtWidgets

sys.path.append(os.path.join(sys.path[0], '../'))
from UI import limit_setting

class Limit_Setting_class (limit_setting.Ui_widget_Limit,QtWidgets.QDialog):
    def __init__(self):
        # QtWidgets.QDialog.__init__(self)
        # uic.loadUi("UI/limit_setting.ui",self)
        super(limit_setting.Ui_widget_Limit, self).__init__() #import ui.py
        self.setupUi(self)

        ###################        GUI ACTION       #################################
        self.pb_save.clicked.connect(self.save_limit)
        #self.pb_save.clicked.connect(self.showprint)  #example

    def save_limit(self):

        with open("Private/setting.txt", "w") as wf:
            #wf.write(str(like) + "\n") =  shortcut
            wf.write(str(self.sb_like.value()) + "\n")
            wf.write(str(self.sb_unlike.value()) + "\n")
            wf.write(str(self.sb_follow.value()) + "\n")
            wf.write(str(self.sb_unfollow.value()) + "\n")
            wf.write(str(self.sb_comment.value()) + "\n")
            wf.write(str(self.sb_liketolike.value()) + "\n")
            wf.write(str(self.sb_foltofol.value()) + "\n")
            wf.write(str(self.sb_min_foltofol.value()) + "\n")
            wf.write(str(self.sb_fingtofol.value()) + "\n")
            wf.write(str(self.sb_min_fingtofol.value()) + "\n")
            wf.write(str(self.sb_fertofing.value()) + "\n")
            wf.write(str(self.sb_fingtofer.value()) + "\n")
            wf.write(str(self.sb_min_media.value()) + "\n")
            wf.write(str(self.sb_like_delay.value()) + "\n")
            wf.write(str(self.sb_unlike_delay.value()) + "\n")
            wf.write(str(self.sb_follow_delay.value()) + "\n")
            wf.write(str(self.sb_unfollow_delay.value()) + "\n")
            wf.write(str(self.sb_comment_delay.value()) + "\n")
            wf.write(str(self.le_proxy.text()) or "None" + "\n")

            self.close()


if __name__== "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Limit_Setting = Limit_Setting_class()#take from here put (self.) at front
    Limit_Setting.show()#import this #class #untill here
    sys.exit(app.exec_())

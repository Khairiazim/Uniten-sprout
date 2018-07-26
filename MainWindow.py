#todo / schedule/ internet connection
#todo instabot.log at api.py / instabot started at bot.py
#todo set follow followers count limit
#generate random number at server send to apps
#both check

import os
import random
import shutil
import sys
import time
import threading
import errno

import requests

import API_Util

from PyQt5 import QtCore,QtGui, QtWidgets
from PyQt5 import uic
from tqdm import tqdm

#IMPORT INSTABOT
sys.path.append(os.path.join(sys.path[0], '../'))
from instabot import Bot
from UI import mainwindow

#IMPORT DIC
from dic import dicAcc

############ IMPORT QWIDGET / QDIALOG  #################
from Limit_Setting import Limit_Setting_class
from Login import Login_class
from Like import Like_class

############     WRITE FILE .TXT    ################
hashtag_file = "Private/hashtagsdb.txt"
users_file = "Private/usersdb.txt"
whitelist = "Private/whitelist.txt"
blacklist = "Private/blacklist.txt"
userlist = "Private/userlist.txt"
comment = "Private/comments.txt"
setting = "Private/setting.txt"
SECRET_FILE = "Private/secret.txt"

unfollow_job_file = "Private/unfollow_job.txt"
follow_job_file = "Private/follow_job.txt"
follow_random_file = "Private/follow_random.txt"
like_job_file = "Private/like_job.txt"
like_random_file = "Private/like_random.txt"
comment_job_file = "Private/comment_job.txt"
comment_file = "Private/comment.txt"
comment_usertag_file = "Private/comment_usertag.txt"

class workThread(QtCore.QThread):
    def __init__(self,parent=None):
        super(workThread,self).__init__(parent)

    def like_job(self):
        with open(like_job_file, "r") as rf:
            lines = rf.readlines()
            like_lines = str(lines[0].strip())

        with open(like_random_file, "r") as rff:
            usertag = [line.rstrip() for line in rff]

        if like_lines == "Like from hashtag":
            random_tag = random.choice(usertag)
            bot.like_hashtag(random_tag)

        elif like_lines == "Like followers":
            user_id = random.choice(usertag)
            bot.like_followers(user_id)

        elif like_lines == "Like following":
            user_id = random.choice(usertag)
            bot.like_following(user_id)

        elif like_lines == "Like last media likers":
            user_id = random.choice(usertag)
            medias = bot.get_user_medias(user_id, filtration=False)
            if len(medias):
                likers = bot.get_media_likers(medias[0])
                for liker in tqdm(likers):
                    bot.like_user(liker, amount=2, filtration=False)

        else:
            bot.like_timeline()

    def result_validation(self):
        try:
            result = requests.post(API_Util.API_URL + "api/user/check_validity/",
                                   data={'api_key': API_Util.API_KEY,
                                         'mac_guid': API_Util.get_machine_guid()})
            result = result.json()
            return result["status"]

        except:
            QtWidgets.QMessageBox.information(self, "Hi user","Cannot connect to the server. Please check your connection.")

    def run(self):
        print("workthread begin")

        # while self.result_validation(): #while result 1
        #     try:
        #         print("like")
        #         # Thread_like = threading.Thread(target=self.like_job())
        #         # Thread_like.start()
        #         # Thread_like.join()
        #         #
        #         self.result_validation()
        #     except:
        #         print("\n \n \n LIKE ERROR : NO LIKE ACTIVITIES \n \n \n")
        #         break

        QtWidgets.QMessageBox.warning(self, "Ooopps", "workthread stop")


class OutputWrapper(QtCore.QObject):
    """ to show all output in ui text edit"""
    outputWritten = QtCore.pyqtSignal(object, object)

    def __init__(self, parent, stdout=True):
        QtCore.QObject.__init__(self, parent)
        if stdout:
            self._stream = sys.stdout
            sys.stdout = self
        else:
            self._stream = sys.stderr
            sys.stderr = self
        self._stdout = stdout

    def write(self, text):
        self._stream.write(text)
        self.outputWritten.emit(text, self._stdout)

    def __getattr__(self, name):
        return getattr(self._stream, name)

    def __del__(self):
        try:
            if self._stdout:
                sys.stdout = self._stream
            else:
                sys.stderr = self._stream
        except AttributeError:
            pass

class MainWindow_class(mainwindow.Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        # QtWidgets.QMainWindow.__init__(self)
        # uic.loadUi("UI/mainwindow2.ui",self)
        super(mainwindow.Ui_MainWindow, self).__init__()#import ui.py
        self.setupUi(self)

        ################      BUTTON IN MAINWINDOW        ########################
        #self.pb_Start.clicked.connect(self.start_bot)
        self.pb_Start.clicked.connect(self.start_bot)
        self.pb_Stop.clicked.connect(self.enable_button)
        self.pb_Limit.clicked.connect(self.open_Limit_Setting)
        self.pb_Account.clicked.connect(self.open_Login)
        self.pb_Follow.clicked.connect(self.open_Follow)
        self.pb_Like.clicked.connect(self.open_Like)
        self.pb_Reset.clicked.connect(self.delete_all_txt) #todo
        self.pb_Dm.clicked.connect(self.open_coming_soon)
        self.actionLast_Activities.triggered.connect(self.server_Logout)#todo

        ########## workThread  #########
        self.workThread = workThread()

        ##########  show output in QTextEdit  #############
        stdout = OutputWrapper(self, True)
        stdout.outputWritten.connect(self.handleOutput)
        stderr = OutputWrapper(self, False)
        stderr.outputWritten.connect(self.handleOutput)


        QtCore.QCoreApplication.processEvents()
        # check package
        global package
        # package = API_Util.SESSION_DATA["acctype"].lower()
        package = "pro"
        print(package)

        if package == "personal":
            self.pb_Comment.setEnabled(False)
            self.pb_Dm.setEnabled(False)
            self.pb_Like.setEnabled(False)

        if package == "business":
            self.pb_Comment.setEnabled(False)
            self.pb_Dm.setEnabled(False)

        else:
            pass

    def disable_button(self):
        self.pb_Account.setEnabled(False)
        self.pb_Follow.setEnabled(False)
        self.pb_Comment.setEnabled(False)
        self.pb_Unfollow.setEnabled(False)
        self.pb_Dm.setEnabled(False)
        self.pb_Like.setEnabled(False)
        self.pb_Limit.setEnabled(False)
        self.pb_Reset.setEnabled(False)
        self.pb_Start.setEnabled(False)
        self.pb_blacklist.setEnabled(False)
        self.pb_whitelist.setEnabled(False)

    def enable_button(self):#todo
        try:
            self.workThread.terminate()

        except:
            print("workThread termination error")

        QtCore.QCoreApplication.processEvents()
        bot.logout()
        QtCore.QCoreApplication.processEvents()

        if package == "personal":
            self.pb_Account.setEnabled(True)
            self.pb_Follow.setEnabled(True)
            self.pb_Unfollow.setEnabled(True)
            self.pb_Limit.setEnabled(True)
            self.pb_Reset.setEnabled(True)
            self.pb_Start.setEnabled(True)
            self.pb_blacklist.setEnabled(True)
            self.pb_whitelist.setEnabled(True)

        if package == "business":
            self.pb_Account.setEnabled(True)
            self.pb_Follow.setEnabled(True)
            self.pb_Unfollow.setEnabled(True)
            self.pb_Like.setEnabled(True)
            self.pb_Limit.setEnabled(True)
            self.pb_Reset.setEnabled(True)
            self.pb_Start.setEnabled(True)
            self.pb_blacklist.setEnabled(True)
            self.pb_whitelist.setEnabled(True)

        else:
            self.pb_Account.setEnabled(True)
            self.pb_Follow.setEnabled(True)
            self.pb_Comment.setEnabled(True)
            self.pb_Unfollow.setEnabled(True)
            self.pb_Dm.setEnabled(True)
            self.pb_Like.setEnabled(True)
            self.pb_Limit.setEnabled(True)
            self.pb_Reset.setEnabled(True)
            self.pb_Start.setEnabled(True)
            self.pb_blacklist.setEnabled(True)
            self.pb_whitelist.setEnabled(True)

        QtCore.QCoreApplication.processEvents()

    def initial_checker(self):
        try:
            fh = open(hashtag_file, 'r')
            fh = open(users_file, 'r')
            fh = open(whitelist, 'r')
            fh = open(blacklist, 'r')
            #fh = open(comments, 'r')
            #fh = open(setting, 'r')

        except BaseException:
            fh = open(hashtag_file, 'w')
            fh = open(users_file, 'w')
            fh = open(whitelist, 'w')
            fh = open(blacklist, 'w')
            #fh = open(comments, 'w')
            #fh = open(setting, 'w')

    def start_bot(self):
        try:
            # self.initial_checker() #todo

            f = open(setting)
            lines = f.readlines()
            setting_0 = int(lines[0].strip())
            setting_1 = int(lines[1].strip())
            setting_2 = int(lines[2].strip())
            setting_3 = int(lines[3].strip())
            setting_4 = int(lines[4].strip())
            setting_5 = int(lines[5].strip())
            setting_6 = int(lines[6].strip())
            setting_7 = int(lines[7].strip())
            setting_8 = int(lines[8].strip())
            setting_9 = int(lines[9].strip())
            setting_10 = int(lines[10].strip())
            setting_11 = int(lines[11].strip())
            setting_12 = int(lines[12].strip())
            setting_13 = int(lines[13].strip())
            setting_14 = int(lines[14].strip())
            setting_15 = int(lines[15].strip())
            setting_16 = int(lines[16].strip())
            setting_17 = int(lines[17].strip())
            setting_18 = lines[18].strip()

            global bot
            bot = Bot(
                max_likes_per_day=setting_0,
                max_unlikes_per_day=setting_1,
                max_follows_per_day=setting_2,
                max_unfollows_per_day=setting_3,
                max_comments_per_day=setting_4,
                max_likes_to_like=setting_5,
                max_followers_to_follow=setting_6,
                min_followers_to_follow=setting_7,
                max_following_to_follow=setting_8,
                min_following_to_follow=setting_9,
                max_followers_to_following_ratio=setting_10,
                max_following_to_followers_ratio=setting_11,
                min_media_count_to_follow=setting_12,
                like_delay=setting_13,
                unlike_delay=setting_14,
                follow_delay=setting_15,
                unfollow_delay=setting_16,
                comment_delay=setting_17,
                #proxy=setting_18, todo
                whitelist=whitelist,
                blacklist=blacklist,
                comments_file=comment,
                stop_words=[
                    'order',
                    'shop',
                    'store',
                    'free',
                    'doodleartindonesia',
                    'doodle art indonesia',
                    'fullofdoodleart',
                    'commission',
                    'vector',
                    'karikatur',
                    'jasa',
                    'open'])

            print("Collecting data please wait ...........")
            QtCore.QCoreApplication.processEvents()
            self.disable_button()
            QtCore.QCoreApplication.processEvents()

            # username = dicAcc.ACCOUNT_INSTA["username"]
            # password = dicAcc.ACCOUNT_INSTA["password"]
            # bot.login(username=username, password=password)

            #########      WORK START HERE      ################
            QtCore.QCoreApplication.processEvents()
            self.workThread.start()
            QtCore.QCoreApplication.processEvents()

        except:
            QtWidgets.QMessageBox.warning(self, "Ooopps", "Please set your Account and Setting first")

    def server_Logout(self):
        QtCore.QCoreApplication.processEvents()
        # logout from server-> close
        try:
            requests.post(API_Util.API_URL + "api/user/app_logout/",
                          data={'api_key': API_Util.API_KEY,
                                'mac_guid': API_Util.get_machine_guid()})
            self.close()
        except:
            QtWidgets.QMessageBox.information(self, "Hi user",
                                              "Cannot connect to the server. Please check your connection.")

    def delete_all_txt(self):
        shutil.rmtree("Private")

    def handleOutput(self, text, stdout):
        self.textEdit.moveCursor(QtGui.QTextCursor.End)
        self.textEdit.insertPlainText(text)

    ############    OPEN QWIDGET / QDIALOG   #################
    def open_Limit_Setting(self):
        self.Limit_Setting = Limit_Setting_class()
        self.Limit_Setting.show()

    def open_Login(self):
        self.Login = Login_class()
        self.Login.show()

    def open_Follow(self):
        QtWidgets.QMessageBox.warning(self, "Ooopps", "Stay tuned")

    def open_Like(self):
        self.Like = Like_class()
        self.Like.show()

    def open_coming_soon(self):
        QtWidgets.QMessageBox.information(self,"Power Up","we will update this powerful tool soon ")

    def open_License_window(self):
        QtWidgets.QMessageBox.warning(self, "Ooopps", "Dont forget to leave your email")



if __name__== "__main__":
    try:
        os.makedirs("Private")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow_class()
    MainWindow.show()
    sys.exit(app.exec_())

import errno
import os
import sys
import requests
import API_Util
import License_window
import MainWindow

from PyQt5.QtCore import QSharedMemory
from PyQt5 import QtCore,QtGui, QtWidgets

from UI import software


class MemoryCondition:
    def __init__(self, key='memory_condition_key'):
        self._shm = QSharedMemory(key)
        if not self._shm.attach():
            if not self._shm.create(1):
                raise RuntimeError('error creating shared memory: %s' %
                                   self._shm.errorString())
        self.condition = False

    def __enter__(self):
        self._shm.lock()
        if self._shm.data()[0] == b'\x00':
            self.condition = True
            self._shm.data()[0] = b'\x01'
        self._shm.unlock()
        return self.condition

    def __exit__(self, exc_type, exc_value, traceback):
        if self.condition:
            self._shm.lock()
            self._shm.data()[0] = b'\x00'
            self._shm.unlock()

class Software_class(software.Ui_Dialog,QtWidgets.QDialog):
    def __init__(self):
        # QtWidgets.QDialog.__init__(self)
        # uic.loadUi("UI/software.ui",self)
        super(software.Ui_Dialog, self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.openMainwindow)
        self.check_session_api()

    def check_session_api(self):
        try:
            result = requests.post(API_Util.API_URL + "api/user/check_session/",
                                    data={  'api_key': API_Util.API_KEY,
                                            'mac_guid': API_Util.get_machine_guid()})
        except:
            QtWidgets.QMessageBox.information(self, "Hi user", "Cannot connect to the server. Please check your connection.")
        # print(API_Util.get_machine_guid())
        result = result.json()
        # print(result)
        if result['status'] == 1:
            API_Util.SESSION_DATA = result['user']

        else:
            QtWidgets.QMessageBox.information(self, "Hi user", "Your session not exist!")
            self.open_license_ui()
            sys.exit(app.exec())

    def open_license_ui(self):
        self.License = License_window.License_class()
        self.License.show()

    def openMainwindow(self):
        result = requests.post(API_Util.API_URL + "api/user/check_validity/",
                                    data={  'api_key': API_Util.API_KEY,
                                            'mac_guid': API_Util.get_machine_guid()})
        result = result.json()

        if result['status'] == 1:
            self.MainWindow = MainWindow.MainWindow_class()
            self.MainWindow.show()
        else:
            QtWidgets.QMessageBox.information(self, "Hi user", "Your account have expired!")

        self.close()

    def showMessage(self):
        QtWidgets.QMessageBox.warning(self, "Hi user", "Your app has been open")

if __name__== "__main__":
    try:
        os.makedirs("Private")
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    with MemoryCondition() as condition:
        if condition:
            app = QtWidgets.QApplication(sys.argv)
            Software = Software_class()
            Software.show()
            sys.exit(app.exec())
        else:
            app = QtWidgets.QApplication(sys.argv)
            Software = Software_class()
            Software.showMessage()
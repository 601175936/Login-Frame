from forgetpassword import *
from login import *
from mainwindow import *
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainForm(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    MainWindow = MainForm()

    # 忘记密码子窗口
    forget = QDialog()
    forget_ui = Ui_forgetpassword()
    forget_ui.setupUi(forget)
    forget.setWindowModality(Qt.ApplicationModal)

    # 注册子窗口
    login = QDialog()
    login_ui = Ui_login()
    login_ui.setupUi(login)
    login.setWindowModality(Qt.ApplicationModal)

    MainWindow.forgetpass.clicked.connect(forget.show)
    MainWindow.addtojilao.clicked.connect(login.show)


    MainWindow.show()

    sys.exit(app.exec_())


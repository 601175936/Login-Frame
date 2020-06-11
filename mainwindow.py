# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication
from forgetpassword import *
from login import *
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import time


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(250, 350)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())

        # 主窗口
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(250, 350))
        MainWindow.setMaximumSize(QtCore.QSize(250, 350))

        # 加载图片
        window_pale = QtGui.QPalette()
        window_pale.setBrush(MainWindow.backgroundRole(),
                             QtGui.QBrush(QtGui.QPixmap('bilidenglu.jpg')))
        MainWindow.setPalette(window_pale)

        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        # 登录按钮
        self.login = QtWidgets.QPushButton(self.centralWidget)
        self.login.setGeometry(QtCore.QRect(54, 220, 141, 41))
        self.login.setObjectName("login")
        self.login.clicked.connect(self.trynew)
        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.6)
        self.login.setGraphicsEffect(op)
        self.login.setAutoFillBackground(True)

        # 一起来搞基吧  label
        self.labelgaoji = QtWidgets.QLabel(self.centralWidget)
        self.labelgaoji.setGeometry(QtCore.QRect(86, 25, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.labelgaoji.setFont(font)
        self.labelgaoji.setObjectName("labelgaoji")

        # 提示label 密码错误等。。
        self.tishilabel = QtWidgets.QLabel(self.centralWidget)
        self.tishilabel.setGeometry(QtCore.QRect(70, 180, 121, 41))
        font1 = QtGui.QFont()
        self.tishilabel.setFont(font1)
        self.tishilabel.setObjectName('tishi')
        self.tishilabel.setVisible(False)

        # 忘记密码按键
        self.forgetpass = QtWidgets.QToolButton(self.centralWidget)
        self.forgetpass.setGeometry(QtCore.QRect(10, 290, 50, 20))
        self.forgetpass.setMinimumSize(QtCore.QSize(50, 20))
        self.forgetpass.setMaximumSize(QtCore.QSize(50, 20))
        self.forgetpass.setObjectName("forgetpass")
        self.forgetpass.clicked.connect(self.forshowall)
        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.6)
        self.forgetpass.setGraphicsEffect(op)
        self.forgetpass.setAutoFillBackground(True)

        # 注册按键
        self.addtojilao = QtWidgets.QToolButton(self.centralWidget)
        self.addtojilao.setGeometry(QtCore.QRect(190, 290, 50, 20))
        self.addtojilao.setMinimumSize(QtCore.QSize(50, 20))
        self.addtojilao.setMaximumSize(QtCore.QSize(50, 20))
        self.addtojilao.setObjectName("addtojilao")
        self.addtojilao.clicked.connect(self.loginshowall)
        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.6)
        self.addtojilao.setGraphicsEffect(op)
        self.addtojilao.setAutoFillBackground(True)

        # 用户名——文本框
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(22, 94, 201, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.textEdited.connect(self.Gettextyonghu)
        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.6)
        self.lineEdit_2.setGraphicsEffect(op)
        self.lineEdit_2.setAutoFillBackground(True)

        # 密码 —— 文本框
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 150, 200, 40))
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setCursorPosition(0)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.textEdited.connect(self.Gettextmima)
        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.5)
        self.lineEdit.setGraphicsEffect(op)
        self.lineEdit.setAutoFillBackground(True)

        # 菜单栏
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 250, 22))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.actionFunction = QtWidgets.QAction(MainWindow)
        self.actionFunction.setObjectName("actionFunction")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menu.addAction(self.actionFunction)
        self.menu.addAction(self.actionAbout)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "搞基"))
        self.login.setText(_translate("MainWindow", "开始你的搞基之旅"))
        self.login.setShortcut(_translate("MainWindow", "Return"))
        self.labelgaoji.setText(_translate("MainWindow", "来搞基吧！"))
        self.labelgaoji.setStyleSheet('color: rgb(210, 230, 230)')
        self.tishilabel.setText(_translate('MainWindow', 'tishi'))
        self.forgetpass.setText(_translate("MainWindow", "忘记密码"))
        self.addtojilao.setText(_translate("MainWindow", "加入基佬"))
        self.addtojilao.setShortcut(_translate('MainWindow', 'Meta+A'))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "搞基通行码"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "基佬用户名"))
        self.menu.setTitle(_translate("MainWindow", "搞基指南"))
        self.actionFunction.setText(_translate("MainWindow", "Function"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

    # 获得用户名
    def Gettextyonghu(self):
        self.get_yonghu_text = self.lineEdit_2.text()
        self.tishilabel.hide()

    # 获得密码
    def Gettextmima(self):
        self.get_mima_text = self.lineEdit.text()
        self.tishilabel.hide()

    # 点击注册按钮后的函数
    def loginshowall(self):
        login.show()
        login_ui.tishilabel.hide()

    # 点击忘记密码后的函数
    def forshowall(self):
        forget.show()
        forget_ui.tishilabel.hide()
        forget_ui.frame.setVisible(False)
        forget_ui.y1.show()
        forget_ui.y1.clear()

    # 点击开启旅程后的函数
    def trynew(self):
        try:
            filename = 'user_password.json'
            f = open(filename)
            line = f.readline()
            while line:
                ling = eval(line)
                if self.get_yonghu_text in ling.keys() and self.get_yonghu_text != '':
                    if self.get_mima_text == ling[self.get_yonghu_text]:
                        self.open_new_main()
                        break
                    else:
                        self.tip_error()
                        break
                line = f.readline()
            if line == '':
                self.tip_error()
            f.close()
        except:
            self.tip_error()

    # 提示用户名或密码错误
    def tip_error(self):
        self.tishilabel.hide()
        self.tishilabel.setText('用户名或密码错误！')
        self.tishilabel.show()

    # 打开主页面
    def open_new_main(self):
        time.sleep(0.3)
        login.show()
        MainWindow.close()



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


    MainWindow.show()

    sys.exit(app.exec_())


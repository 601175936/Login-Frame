# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import json
import operator
import io
import time


class Ui_login(object):
    def setupUi(self, login):
        self.login = login
        login.setObjectName("login")
        login.setWindowModality(QtCore.Qt.ApplicationModal)
        login.resize(300, 300)
        login.setMinimumSize(QtCore.QSize(300, 300))
        login.setMaximumSize(QtCore.QSize(300, 300))

        self.centralWidget = QtWidgets.QWidget(login)
        self.centralWidget.setObjectName("centralWidget")

        # 大标题 欢迎加入。。
        self.labe = QtWidgets.QLabel(login)
        self.labe.setGeometry(QtCore.QRect(80, 30, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.labe.setFont(font)
        self.labe.setObjectName("labe")

        self.layoutWidget = QtWidgets.QWidget(login)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 230, 228, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # 取消键
        self.delete_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.delete_2.setObjectName("delete_2")
        self.horizontalLayout.addWidget(self.delete_2)

        # 确定键
        self.ok = QtWidgets.QPushButton(self.layoutWidget)
        self.ok.setObjectName("ok")
        self.horizontalLayout.addWidget(self.ok)
        self.ok.clicked.connect(self.newt)

        # 提示标签 密码不一致等
        self.tishilabel = QtWidgets.QLabel(login)
        self.tishilabel.setGeometry(QtCore.QRect(80, 200, 151, 20))
        font1 = QtGui.QFont()
        self.tishilabel.setFont(font1)
        self.tishilabel.setObjectName('tishi')
        self.tishilabel.setVisible(False)

        self.layoutWidget_2 = QtWidgets.QWidget(login)
        self.layoutWidget_2.setGeometry(QtCore.QRect(42, 94, 221, 101))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        # 用户名标签
        self.yonghum = QtWidgets.QLabel(self.layoutWidget_2)
        self.yonghum.setObjectName("yonghum")
        self.gridLayout.addWidget(self.yonghum, 0, 0, 1, 1)
        # 用户名--文本框
        self.y1 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.y1.setObjectName("y1")
        self.y1.textEdited.connect(self.get_username)
        self.y1.setInputMethodHints(QtCore.Qt.ImhNoPredictiveText |
                                    QtCore.Qt.ImhLowercaseOnly | QtCore.Qt.ImhUppercaseOnly)
        self.gridLayout.addWidget(self.y1, 0, 1, 1, 1)

        # 密码标签
        self.mima = QtWidgets.QLabel(self.layoutWidget_2)
        self.mima.setObjectName("mima")
        self.gridLayout.addWidget(self.mima, 1, 0, 1, 1)

        # 密码文本框
        self.y2 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.y2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.y2.setObjectName("y2")
        self.y2.textEdited.connect(self.get_password1)
        self.y2.setInputMethodHints(QtCore.Qt.ImhNoPredictiveText |
                                    QtCore.Qt.ImhLowercaseOnly | QtCore.Qt.ImhUppercaseOnly)
        self.gridLayout.addWidget(self.y2, 1, 1, 1, 1)

        # 确认密码标签
        self.querebn = QtWidgets.QLabel(self.layoutWidget_2)
        self.querebn.setObjectName("querebn")
        self.gridLayout.addWidget(self.querebn, 2, 0, 1, 1)
        # 密码2文本框
        self.y3 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.y3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.y3.setObjectName("y3")
        self.y3.textEdited.connect(self.get_password2)
        self.gridLayout.addWidget(self.y3, 2, 1, 1, 1)
        self.y3.setInputMethodHints(QtCore.Qt.ImhNoPredictiveText |
                                    QtCore.Qt.ImhLowercaseOnly | QtCore.Qt.ImhUppercaseOnly)

        self.retranslateUi(login)
        self.delete_2.clicked.connect(self.closeup)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Dialog"))
        self.labe.setText(_translate("login", "欢迎你加入我们"))
        self.delete_2.setText(_translate("login", "取消"))
        self.ok.setText(_translate("login", "确认"))
        self.ok.setShortcut(_translate("login", "Return"))
        self.yonghum.setText(_translate("login", "搞基用户名："))
        self.mima.setText(_translate("login", "搞基通行码："))
        self.querebn.setText(_translate("login", "再次确认："))

    # 取消键函数
    def closeup(self):
        self.y1.clear()
        self.y2.clear()
        self.y3.clear()
        self.login.close()

    # 获得用户名
    def get_username(self):
        self.username = self.y1.text()
        self.tishilabel.hide()

    # 获得密码1
    def get_password1(self):
        self.password1 = self.y2.text()
        self.tishilabel.hide()

    # 获得密码2
    def get_password2(self):
        self.password2 = self.y3.text()
        self.tishilabel.hide()

    # 确定键函数
    def newt(self):
        try:
            filename = 'user_password.json'
            if self.password2 == self.password1 and self.password2 != '' and self.username != '':
                d = {self.username: self.password1}

                with open(filename, 'r') as f:
                    lines = f.readline()
                    while lines:
                        line = eval(lines)
                        if self.username in line.keys():
                            break
                        lines = f.readline()
                    if lines == '':
                        f.close()
                        with open(filename, 'a+') as f1:
                            f1.write(str(d) + '\n')

                    else:
                        self.user_already_exist()
            else:
                self.password_not_same()
        except AttributeError:
            pass

    # 密码不一致提示
    def password_not_same(self):
        self.tishilabel.hide()
        self.tishilabel.setText('两次输入的密码不一致！')
        self.tishilabel.show()

    # 用户已经存在
    def user_already_exist(self):
        self.tishilabel.hide()
        self.tishilabel.setText('该基佬已经存在！')
        self.tishilabel.show()

    # 注册成功后操作
    def sign_in_success(self):
        self.username = ''
        self.password1 = ''
        self.password2 = ''
        self.y1.clear()
        self.y2.clear()
        self.y3.clear()
        self.login.close()


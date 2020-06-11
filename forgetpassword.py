# Form implementation generated from reading ui file 'forgetpassword.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
# import os
# import  re

class Ui_forgetpassword(object):
    def setupUi(self, forgetpassword):
        self.forget = forgetpassword
        forgetpassword.setObjectName("forgetpassword")
        forgetpassword.resize(400, 300)
        forgetpassword.setMinimumSize(QtCore.QSize(400, 300))
        forgetpassword.setMaximumSize(QtCore.QSize(400, 300))

        # 大标签 别担心。。
        self.biaoti = QtWidgets.QLabel(forgetpassword)
        self.biaoti.setGeometry(QtCore.QRect(40, 60, 321, 20))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.biaoti.setFont(font)
        self.biaoti.setObjectName("biaoti")

        # 取消键
        self.ac = QtWidgets.QPushButton(forgetpassword)
        self.ac.setGeometry(QtCore.QRect(30, 220, 113, 32))
        self.ac.setObjectName("ac")

        # 确定键 输入用户名
        self.ok = QtWidgets.QPushButton(forgetpassword)
        self.ok.setGeometry(QtCore.QRect(250, 220, 113, 32))
        self.ok.setObjectName("ok")

        # 确定键 修改密码
        self.ok1 = QtWidgets.QPushButton(forgetpassword)
        self.ok1.setGeometry(QtCore.QRect(250, 220, 113, 32))
        self.ok1.setObjectName("ok1")
        self.ok1.setVisible(False)

        self.frame = QtWidgets.QFrame(forgetpassword)
        self.frame.setGeometry(QtCore.QRect(40, 80, 321, 141))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.frame.setVisible(False)

        # 密码1
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(60, 30, 200, 30))
        self.lineEdit.setMinimumSize(QtCore.QSize(200, 30))
        self.lineEdit.setMaximumSize(QtCore.QSize(200, 30))
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.textEdited.connect(self.get_password1)
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhNoPredictiveText | QtCore.Qt.ImhLowercaseOnly | QtCore.Qt.ImhUppercaseOnly)

        # 密码2
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 80, 200, 30))
        self.lineEdit_2.setMinimumSize(QtCore.QSize(200, 30))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(200, 30))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.textEdited.connect(self.get_password2)
        self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhNoPredictiveText | QtCore.Qt.ImhLowercaseOnly | QtCore.Qt.ImhUppercaseOnly)

        # 提示版
        self.tishilabel = QtWidgets.QLabel(forgetpassword)
        self.tishilabel.setGeometry(QtCore.QRect(130, 200, 141, 16))
        font1 = QtGui.QFont()
        self.tishilabel.setFont(font1)
        self.tishilabel.setObjectName('tishi')
        self.tishilabel.setVisible(False)

        # 用户名
        self.y1 = QtWidgets.QLineEdit(forgetpassword)
        self.y1.setGeometry(QtCore.QRect(51, 125, 291, 41))
        self.y1.setObjectName("y1")
        self.y1.textEdited.connect(self.get_yonghu)
        self.y1.setInputMethodHints(QtCore.Qt.ImhNoPredictiveText | QtCore.Qt.ImhLowercaseOnly | QtCore.Qt.ImhUppercaseOnly)

        # 按键函数
        self.retranslateUi(forgetpassword)
        self.ac.clicked.connect(forgetpassword.close)
        self.ok.clicked.connect(self.chonghui)
        self.ok1.clicked.connect(self.chonghui1)

        QtCore.QMetaObject.connectSlotsByName(forgetpassword)

    # 第一次ok
    def chonghui(self):

        filename = 'user_password.json'
        f = open(filename)
        try:
            line = f.readline()
            if self.username == '':
                pass
            else:
                while line:
                    ling = eval(line)
                    if self.username in ling.keys():
                        self.y1.clear()
                        self.frame.show()
                        self.y1.hide()
                        self.ok.hide()
                        self.tishilabel.hide()
                        self.ok1.show()
                        break
                    line = f.readline()

                if line == '':
                    self.tishilabel.hide()
                    self.tishilabel.setText('不存在该基佬！')
                    self.tishilabel.show()
                f.close()
        except:
            pass

    # 第二次 ok
    def chonghui1(self):
        try:
            if self.password1 == self.password2 and self.password2 != '':
                p1 = 'user_password.json'
                p2 = 'user_password1.json'

                f1 = open(p1, 'r+')
                f2 = open(p2, 'w+')
                line = f1.readline()
                while line:
                    ling = eval(line)
                    if self.username in ling.keys():
                        ling[self.username] = self.password2
                        rop = str(ling)
                        print(rop)
                        f2.write(rop+'\n')
                    else:
                        f2.write(line)
                    line = f1.readline()

                f1.close()
                f2.close()

                read = open(p2, 'r')
                write = open(p1, 'w')
                r = read.read()
                write.write(r)
                read.close()
                write.close()

                self.lineEdit.clear()
                self.lineEdit_2.clear()
                self.username = ''
                self.password2 = ''
                self.password1 = ''
                self.ok1.hide()
                self.ok.show()
                self.frame.hide()
                self.forget.close()

            elif self.password1 != self.password2 or not self.password2:
                self.tishilabel.setVisible(False)
                self.tishilabel.setText('两次输入的密码不一致！')
                self.tishilabel.show()
        except:
            pass

    # 获得用户名
    def get_yonghu(self):
        self.username = self.y1.text()

    # 获得密码1
    def get_password1(self):
        self.password1 = self.lineEdit.text()

    # 获得密码2
    def get_password2(self):
        self.password2 = self.lineEdit_2.text()

    def retranslateUi(self, forgetpassword):
        _translate = QtCore.QCoreApplication.translate
        forgetpassword.setWindowTitle(_translate("forgetpassword", "Dialog"))
        self.biaoti.setText(_translate("forgetpassword", "别担心！基佬是不会忘记他的密码的！"))
        self.ac.setText(_translate("forgetpassword", "取消"))
        self.ok.setText(_translate("forgetpassword", "确定"))
        self.ok1.setText(_translate("forgetpassword", "确定"))
        self.ok.setShortcut(_translate('forgetpassword', 'Return'))
        self.ok1.setShortcut(_translate('forgetpassword', 'Return'))

        self.lineEdit.setPlaceholderText(_translate("forgetpassword", "搞基密码"))
        self.lineEdit_2.setPlaceholderText(_translate("forgetpassword", "再次确认"))
        self.y1.setPlaceholderText(_translate("forgetpassword", "基佬用户名"))



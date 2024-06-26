# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 2.0 55 Regular")
        Form.setFont(font)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setStyleSheet("border-radius:15px;\n"
"background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_5.setStyleSheet("image:url(static/imgs/close.png);")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_7.addWidget(self.pushButton_5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.widget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.page)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(18)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.page)
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 2.0 55 Regular")
        font.setPointSize(60)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 170, 127);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.page)
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 2.0 55 Regular")
        font.setPointSize(15)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-radius:15px;\n"
"background-color: rgb(160, 160, 160);\n"
"padding:5px; ")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.page)
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 2.0 55 Regular")
        font.setPointSize(15)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("border-radius:15px;\n"
"background-color: rgb(160, 160, 160);\n"
"padding:5px; ")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(80)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox = QtWidgets.QCheckBox(parent=self.page)
        self.checkBox.setChecked(True)
        self.checkBox.setAutoExclusive(True)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(parent=self.page)
        self.checkBox_2.setAutoExclusive(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_2.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(parent=self.page)
        self.checkBox_3.setAutoExclusive(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_2.addWidget(self.checkBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(100)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(parent=self.page)
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 2.0 55 Regular")
        font.setPointSize(25)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    border-radius:15px;\n"
"    background-color: rgb(85, 170, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 221, 162);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(0, 90, 66);\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.page)
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 2.0 55 Regular")
        font.setPointSize(25)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    border-radius:15px;\n"
"    background-color: rgb(170, 170, 170);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 170, 127);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_9.addLayout(self.verticalLayout_2)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.page_2)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(18)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(parent=self.page_2)
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 2.0 55 Regular")
        font.setPointSize(60)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 170, 127);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.page_2)
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 2.0 55 Regular")
        font.setPointSize(15)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("border-radius:15px;\n"
"padding:5px;\n"
"background-color: rgb(160, 160, 160);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_4.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.page_2)
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 2.0 55 Regular")
        font.setPointSize(15)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("border-radius:15px;\n"
"padding:5px;\n"
"background-color: rgb(160, 160, 160);")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_4.addWidget(self.lineEdit_4)
        self.lineEdit_9 = QtWidgets.QLineEdit(parent=self.page_2)
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 2.0 55 Regular")
        font.setPointSize(15)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setStyleSheet("border-radius:15px;\n"
"padding:5px;\n"
"background-color: rgb(160, 160, 160);")
        self.lineEdit_9.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_4.addWidget(self.lineEdit_9)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(100)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.page_2)
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 2.0 55 Regular")
        font.setPointSize(25)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    border-radius:15px;\n"
"    background-color: rgb(170, 170, 170);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 170, 127);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_6.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.page_2)
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 2.0 55 Regular")
        font.setPointSize(25)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    border-radius:15px;\n"
"    background-color: rgb(85, 170, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 221, 162);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(0, 90, 66);\n"
"}\n"
"\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_6.addWidget(self.pushButton_4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem8)
        self.horizontalLayout_10.addLayout(self.verticalLayout_3)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.page_3)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_6.addItem(spacerItem9)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem10)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(18)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_3 = QtWidgets.QLabel(parent=self.page_3)
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 2.0 55 Regular")
        font.setPointSize(90)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 170, 127);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.page_3)
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 2.0 55 Regular")
        font.setPointSize(15)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("border-radius:15px;\n"
"padding:5px;\n"
"background-color: rgb(160, 160, 160);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_7.addWidget(self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=self.page_3)
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 2.0 55 Regular")
        font.setPointSize(15)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("border-radius:15px;\n"
"padding:5px;\n"
"background-color: rgb(160, 160, 160);")
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_7.addWidget(self.lineEdit_6)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setSpacing(100)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.page_3)
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 2.0 55 Regular")
        font.setPointSize(25)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"    border-radius:15px;\n"
"    background-color: rgb(85, 170, 0);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 221, 162);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(0, 90, 66);\n"
"}\n"
"\n"
"")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_12.addWidget(self.pushButton_7)
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.page_3)
        font = QtGui.QFont()
        font.setFamily("阿里巴巴普惠体 2.0 55 Regular")
        font.setPointSize(25)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"    border-radius:15px;\n"
"    background-color: rgb(170, 170, 170);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 170, 127);\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_12.addWidget(self.pushButton_6)
        self.verticalLayout_7.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_11.addLayout(self.verticalLayout_7)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem11)
        self.verticalLayout_6.addLayout(self.horizontalLayout_11)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_6.addItem(spacerItem12)
        self.horizontalLayout_13.addLayout(self.verticalLayout_6)
        self.stackedWidget.addWidget(self.page_3)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout_8.addLayout(self.verticalLayout_5)
        self.horizontalLayout_5.addWidget(self.widget)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        self.pushButton.clicked.connect(Form.login) # type: ignore
        self.pushButton_2.clicked.connect(Form.open_register_page) # type: ignore
        self.pushButton_3.clicked.connect(Form.open_login_page) # type: ignore
        self.pushButton_4.clicked.connect(Form.register) # type: ignore
        self.pushButton_5.clicked.connect(Form.close_window) # type: ignore
        self.pushButton_7.clicked.connect(Form.add_school) # type: ignore
        self.pushButton_6.clicked.connect(Form.close) # type: ignore
        self.lineEdit_6.returnPressed.connect(Form.add_school) # type: ignore
        self.lineEdit_2.returnPressed.connect(Form.login) # type: ignore
        self.lineEdit_9.returnPressed.connect(Form.register) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "教务管理系统"))
        self.label.setText(_translate("Form", "教务管理系统"))
        self.lineEdit.setPlaceholderText(_translate("Form", "账号"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "密码"))
        self.checkBox.setText(_translate("Form", "学生登录"))
        self.checkBox_2.setText(_translate("Form", "教师登录"))
        self.checkBox_3.setText(_translate("Form", "管理员登录"))
        self.pushButton.setText(_translate("Form", "登录"))
        self.pushButton_2.setText(_translate("Form", "注册"))
        self.label_2.setText(_translate("Form", "管理员注册"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "账号"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "密码"))
        self.lineEdit_9.setPlaceholderText(_translate("Form", "确认密码"))
        self.pushButton_3.setText(_translate("Form", "登录"))
        self.pushButton_4.setText(_translate("Form", "注册"))
        self.label_3.setText(_translate("Form", "创建机构"))
        self.lineEdit_5.setPlaceholderText(_translate("Form", "机构名称"))
        self.lineEdit_6.setPlaceholderText(_translate("Form", "机构地址"))
        self.pushButton_7.setText(_translate("Form", "创建"))
        self.pushButton_6.setText(_translate("Form", "返回"))

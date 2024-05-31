"""
用户视图层
"""
import logging
import sys
from PyQt6.QtWidgets import QWidget, QApplication, QMessageBox
from PyQt6.QtCore import Qt
from lib import common
from conf import settings
from insterface import admin_interface, common_interface, student_interface
from ui.login import Ui_Form as LoginUiMixin


test_logger = logging.getLogger("视图层")


class LoginWindow(QWidget, LoginUiMixin):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)   # 隐藏边框
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)  # 背景透明
        self.setupUi(self)
        self.admin_is_here = False  # 默认没有管理员

    def get_user_type(self):
        check_box = self.checkBox.isChecked()
        check_box2 = self.checkBox_2.isChecked()
        check_box3 = self.checkBox_3.isChecked()
        user_type_dic = {"Student": check_box, "Teacher": check_box2, "Admin": check_box3}
        for user_type in user_type_dic:
            if user_type_dic[user_type]:
                return user_type

    # 登录功能
    def login(self):
        # 获取用户名和密码，以及用户类型
        username = self.lineEdit.text().strip()
        password = self.lineEdit_2.text().strip()
        user_type = self.get_user_type()

        # 对账号密码做简单判断
        # 不能为空
        if not username or not password:
            QMessageBox.warning(self, "提示", "用户名或密码不能为空！")
            return

        # 调用登录接口
        # 对密码进行加密
        encrypted_password = common.sha256_encrypt(password)
        common_interface.login_interface(username, encrypted_password, user_type)

    def open_register_page(self):
        self.stackedWidget.setCurrentIndex(1)
        self.lineEdit_3.setFocus()
        # 判断是否有管理员
        flag, msg = common_interface.admin_is_exists_interface()
        # 如果存在管理员，将注册页面改为学员注册
        if flag:
            self.label_2.setText("学员注册")
            self.admin_is_here = True

    def open_login_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def register(self):
        username = self.lineEdit_3.text().strip()
        password = self.lineEdit_4.text().strip()
        check_password = self.lineEdit_9.text().strip()

        # 简单的密码判断
        # 确认密码是否一致
        if password != check_password:
            QMessageBox.about(self, "警告", "两次输入密码不一致！")
            return

        # 密码加密
        encrypted_password = common.sha256_encrypt(password)

        # 调用注册接口注册
        # 判断是否存在管理员，调用不同接口
        if self.admin_is_here:
            flag, msg = student_interface.student_register_interface(
                username, encrypted_password
            )
        else:
            flag, msg = admin_interface.admin_register_interface(
                username, encrypted_password
            )
        QMessageBox.about(self, "提示", msg)

        # 注册失败
        if not flag:
            return

        # 注册成功，跳转登录页面
        self.open_login_page()
        # 清空注册框
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_9.clear()
        # 自动填入用户名，密码框聚焦
        self.lineEdit.setText(username)
        self.lineEdit_2.setFocus()

    def close_window(self):
        self.close()


def run():
    app = QApplication(sys.argv)
    login_window = LoginWindow()

    login_window.show()
    sys.exit(app.exec())

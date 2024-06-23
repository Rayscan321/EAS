"""
用户视图层
"""

import logging
import sys
from PyQt6.QtWidgets import QWidget, QApplication, QMessageBox
from PyQt6.QtCore import Qt
from lib import common
from conf import settings
from interface import admin_interface, common_interface, student_interface
from ui.login import Ui_Form as LoginUiMixin
from ui.home import Ui_Form as HomeUiMixin


test_logger = logging.getLogger("视图层")


class LoginWindow(QWidget, LoginUiMixin):
    def __init__(self):
        super().__init__()
        self.home_window = None
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)  # 隐藏边框
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)  # 背景透明
        self.setupUi(self)
        self.admin_is_here = False  # 默认没有管理员
        self.init_login_window()

        self.user_type = None
        self.login_name = None

    # 初始化登录窗口
    def init_login_window(self):
        self.lineEdit.setText(settings.LOGIN_USERNAME)
        user_type_dic = {
            "Student": self.checkBox,
            "Teacher": self.checkBox_2,
            "Admin": self.checkBox_3,
        }
        user_type_dic.get(settings.LOGIN_TYPE).setChecked(True)

    # 创建学校功能
    def add_school(self):
        # 获取用户输入的数据
        school_name = self.lineEdit_5.text().strip()
        school_address = self.lineEdit_6.text().strip()

        # 简单逻辑判断
        if not school_name or not school_address:
            QMessageBox.warning(self, "警告", "学校名称或地址不能为空！")
            return

        # 调用创建学校接口
        flag, msg = admin_interface.add_school_interface(
            school_name, school_address, self.login_name
        )
        QMessageBox.about(self, "提示", msg)
        # 如果学校添加失败
        if not flag:
            return
        # 学校添加成功，进入主页
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()

    # 进入主页
    def go_home_page(self, user_type):
        self.close()
        # 实例化一个主页的窗口对象
        self.home_window = HomeWindow(user_type)
        self.home_window.show()

    # 获取用户类型
    def get_user_type(self):
        check_box = self.checkBox.isChecked()
        check_box2 = self.checkBox_2.isChecked()
        check_box3 = self.checkBox_3.isChecked()
        user_type_dic = {
            "Student": check_box,
            "Teacher": check_box2,
            "Admin": check_box3,
        }
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
        flag, msg = common_interface.login_interface(
            username, encrypted_password, user_type
        )
        if not flag:
            QMessageBox.warning(self, "登录失败", msg)
            return
        # 登录成功
        test_logger.info(f"{username}登录成功")
        settings.config.set("USER", "LOGIN_USERNAME", username)
        settings.config.set("USER", "LOGIN_TYPE", user_type)
        with open(settings.CONFIG_PATH, "w", encoding="utf-8-sig") as f:
            settings.config.write(f)

        # 登录成功，判断是否有学校
        flag, msg = common_interface.check_obj_is_exists("School")
        if not flag:
            # 如果没有学校的时候，是管理员登录，跳转到创建学校页面
            if user_type == "Admin":
                self.stackedWidget.setCurrentIndex(2)
            else:
                # 没有学校也不是管理员登录
                QMessageBox.warning(self, "警告", "当前不存在学校，请联系管理员添加学校！")

            # 记录用户名和用户类型
            self.login_name = username
            self.user_type = user_type
            return

        # 跳转到主页
        self.go_home_page(user_type)

    def open_register_page(self):
        self.stackedWidget.setCurrentIndex(1)
        self.lineEdit_3.setFocus()
        # 判断是否有管理员
        flag, msg = common_interface.check_obj_is_exists("Admin")
        # 如果存在管理员，将注册页面改为学员注册
        if flag:
            self.label_2.setText("学员注册")
            self.admin_is_here = True

    def open_login_page(self):
        self.stackedWidget.setCurrentIndex(0)
        self.lineEdit.setFocus()

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


class HomeWindow(QWidget, HomeUiMixin):
    def __init__(self, user_type):
        super().__init__()
        self.setupUi(self)

        self.home_window_init(user_type)
        self.open_home_page()

    # 主页数据初始化
    def home_window_init(self, user_type):
        if user_type == "Admin":
            self.admin_init()
        elif user_type == "Teacher":
            self.teacher_init()
        elif user_type == "Student":
            self.student_init()

    # 数据初始化
    def init_data(self):
        self.pushButton_2.hide()
        self.pushButton_4.hide()
        self.pushButton_5.hide()
        self.pushButton_3.setText("查看课程")

    # 学生初始化
    def student_init(self):
        self.init_data()
        self.pushButton_6.hide()
        self.pushButton_26.hide()

    # 管理员初始化
    def admin_init(self):
        self.stackedWidget_3.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(1)

    # 老师初始化
    def teacher_init(self):
        self.init_data()
        self.stackedWidget_3.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(0)
        self.pushButton_26.hide()

    # 切换学校功能
    def change_school(self):
        pass

    # 打开主页功能
    def open_home_page(self):
        self.stackedWidget.setCurrentIndex(0)

    # 打开学员管理页
    def open_stu_list_page(self):
        self.stackedWidget.setCurrentIndex(1)

    # 打开课程列表功能
    def open_course_list_page(self):
        self.stackedWidget.setCurrentIndex(2)

    # 打开设置功能
    def open_setting_page(self):
        self.stackedWidget.setCurrentIndex(5)

    # 打开财务中心功能
    def open_money_page(self):
        self.stackedWidget.setCurrentIndex(4)

    # 老师列表功能
    def open_teacher_list_page(self):
        self.stackedWidget.setCurrentIndex(3)

    # 登出功能
    def login_out(self):
        pass


def run():
    app = QApplication(sys.argv)
    login_window = LoginWindow()

    login_window.show()
    sys.exit(app.exec())

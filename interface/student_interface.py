"""
学生接口
"""

import os
import logging
from conf import settings
from db.models import Student

student_logger = logging.getLogger("student")


def student_register_interface(username, password):
    # 查询学生是否存在
    student_dir = os.path.join(settings.DB_DIR, "Student", username)
    if os.path.exists(student_dir):
        return False, f"用户{username}已存在！"
    # 学生不存在开始注册
    # 实例化学生类，类自动保存
    student = Student(username, password)
    msg = f"{username}注册成功！"
    student_logger.info(msg)
    return True, msg

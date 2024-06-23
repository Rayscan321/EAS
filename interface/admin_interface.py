"""
管理员接口
"""

import logging
from db.models import Admin, School

admin_logger = logging.getLogger("admin")


# 注册接口
def admin_register_interface(username, password):
    # 实例化管理员类，类自动保存
    admin = Admin(username, password)
    msg = f"{username}注册成功"
    admin_logger.info(msg)
    return True, msg


# 添加学校接口
def add_school_interface(school_name, school_addr, admin_name):
    # TODO:判断学校是否存在
    school_obj = School.select(school_name)
    if school_obj:
        return False, f"学校{school_name}已存在！"

    # 由管理员创建对象
    admin_obj = Admin.select(admin_name)
    admin_obj.add_school(school_name, school_addr)
    admin_logger.info(f"{admin_name}添加学校：{school_name}成功！")
    return True, f"学校：{school_name}添加成功！"


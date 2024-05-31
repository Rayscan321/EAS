"""
管理员接口
"""
from db.models import Admin


# 注册接口
def admin_register_interface(username, password):
    # 实例化管理员类，类自动保存
    admin = Admin(username, password)

    return True, f"{username}注册成功！"

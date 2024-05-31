# 公共接口
import os
import logging
from conf import settings
from db import models


# 管理员存在接口
def admin_is_exists_interface():
    # 获取管理员文件夹路径
    admin_dir = os.path.join(settings.DB_DIR, 'admin')
    # 判断文件夹是否存在
    if os.path.exists(admin_dir) and os.listdir(admin_dir):
        return True, '管理员已存在！'

    return False, '管理员不存在！'


# 登录接口
def login_interface(username, password, user_type):
    # 获取用户数据
    cls = getattr(models, user_type)
    obj = cls.select(username)
    # 判断用户是否存在
    if not obj:
        return False, '用户不存在！'
    # 判断密码是否正确
    if obj.password != password:
        return False, '密码错误！'
    # 判断用户是否被锁定
    # 判断对象是否有锁定标记
    is_locked = getattr(obj, 'is_locked', False)
    if is_locked:
        return False, '用户已被锁定，请联系管理员解锁！'
    # 返回登录成功
    return True, '登录成功！'


if __name__ == '__main__':
    pass

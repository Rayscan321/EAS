"""
数据处理
"""
import os
import pickle
from conf import settings


# 保存数据
def save_object(obj: object):
    # 获取保存对象文件夹的路径
    class_name = obj.__class__.__name__
    obj_dir = os.path.join(settings.DB_DIR, class_name)
    # 判断文件夹是否存在
    if not os.path.exists(obj_dir):
        os.mkdir(obj_dir)
    # 获得保存对象的路径
    obj_path = os.path.join(obj_dir, obj.username)
    with open(obj_path, 'wb') as f:
        pickle.dump(obj, f)


# 读取数据
def select_data(cls, username):
    # 拼接出查询路径
    obj_path = os.path.join(settings.DB_DIR, cls.__name__, username)

    # 判断文件是否存在
    if not os.path.exists(obj_path):
        return
    # 读取文件
    with open(obj_path, 'rb') as f:
        obj = pickle.load(f)
        return obj

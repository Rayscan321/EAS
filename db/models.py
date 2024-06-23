# 存放类
import datetime
from db import db_handler


class Base:
    def __init__(self, username):
        self.username = username
        self.create_time = datetime.datetime.now()
        # 自动保存
        self.save()

    def save(self):
        db_handler.save_object(self)

    @classmethod
    def select(cls, username):
        obj = db_handler.select_data(cls, username)
        return obj


class Admin(Base):
    def __init__(self, username, password):
        self.password = password

        # 累计付费人次
        self.pay_count = 0
        # 今日营收
        self.today_income = {}
        # 累计营收
        self.total_income = 0
        # 流水
        self.flow = []
        '''
            [time, course_name, money, "收入"],
            [time, teacher_name, money, "支出"],
        '''
        super().__init__(username)

    def add_school(self, school_name, school_addr):
        # 调用学校类，实例化学校对象
        school = School(school_name, school_addr)


class Teacher(Base):
    pass


class Student(Base):
    def __init__(self, username, password):
        self.password = password
        self.locked = False

        self.course_list = []
        self.learned_course_list = []

        super().__init__(username)


class Course(Base):
    pass


class School(Base):
    def __init__(self, school_name, school_addr):
        self.school_addr = school_addr
        self.course_list = []
        super().__init__(school_name)

# -*- coding:utf-8 -*-
#  Author:aling
class School():
    def __init__(self, ID, school_name, school_addr, school_tel):
        '''
        :param school_name: 学校名称
        :param school_addr: 学校地址
        :param school_tel: 服务电话
        '''
        self.ID = ID
        self.School_Name = school_name
        self.School_Addr = school_addr
        self.School_Tel = school_tel

    def add_course(self, ID, course_name, course_period, course_cost, School):
        result = Course( ID, course_name, course_period, course_cost, School)
        return result

class Course():
    def __init__(self, ID, course_name, course_period, course_cost, School):
        '''
        :param ID:课程ID
        :param course_name:课程名称
        :param course_period:课程周期
        :param course_cost:课程费用
        :param School:开课学校
        '''
        self.ID = ID
        self.Course_name = course_name
        self.Course_period = course_period
        self.Course_cost = course_cost
        self.Course_School = School

class Teacher():
    def __init__(self, ID, teacher_name, teacher_sex, teacher_addr, teacher_age, teacher_tel, teacher_salary, School):
        self.ID =ID
        self.Teacher_name = teacher_name
        self.Teacher_sex = teacher_sex
        self.Teacher_addr = teacher_addr
        self.Teacher_age = teacher_age
        self.Teacher_tell = teacher_tel
        self.Teacher_salary = teacher_salary
        self.Teach_Schoo = School   #老师所属学校
        # self.Teach_Cour = Course   #老师所教科目

class Student():
    def __init__(self, ID, stu_name, stu_sex, stu_addr, stu_age, stu_tel):
        self.Stu_name = stu_name
        self.Stu_sex = stu_sex
        self.Stu_addr = stu_addr
        self.Stu_age = stu_age
        self.Stu_tel = stu_tel
        self.ID = ID
        self.Stu_school = School
        self.Stu_Cour = Course  #学生所学课程
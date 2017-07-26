# -*- coding:utf-8 -*-
#  Author:aling
class School():
    def __init__(self,school_id,school_name,school_addr,school_tel):
        '''
        :param school_name: 学校名称
        :param school_addr: 学校地址
        :param school_tel: 服务电话
        '''
        self.School_Name = school_name
        self.School_Addr = school_addr
        self.School_Tel = school_tel
        self.School_ID = school_id

class Course():
    '''
    课程
    '''
    def __init__(self,course_id,course_name,course_cost):
        self.Course_name = course_name
        self.Course_cost = course_cost
        self.Course_ID = course_id

class Teacher():
    def __init__(self,teacher_id,teacher_name,teacher_sex,teacher_addr,teacher_age,teacher_tel,teacher_salary):
        self.Teacher_name = teacher_name
        self.Teacher_sex = teacher_sex
        self.Teacher_addr = teacher_addr
        self.Teacher_age = teacher_age
        self.Teacher_tell = teacher_tel
        self.Teacher_salary = teacher_salary
        self.Teacher_ID =teacher_id
        self.Teach_Schoo = School   #老师所属学校
        self.Teach_Cour = Course   #老师所教科目

class Student():
    def __init__(self,stu_id,stu_name,stu_sex,stu_addr,stu_age,stu_tel):
        self.Stu_name = stu_name
        self.Stu_sex = stu_sex
        self.Stu_addr = stu_addr
        self.Stu_age = stu_age
        self.Stu_tel = stu_tel
        self.Stu_ID = stu_id
        self.Stu_school = School
        self.Stu_Cour = Course  #学生所学课程
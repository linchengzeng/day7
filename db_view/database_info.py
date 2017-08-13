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

    def add_course(ID, course_name, course_period, course_cost, School):
        result = Course( ID, course_name, course_period, course_cost, School)
        return result

    def add_classes(ID, class_name, class_school, class_course, class_teacher):
        result = Classes(ID, class_name, class_school, class_course, class_teacher)
        return result

class Classes():
    def __init__(self, ID, class_name,  School, Course, Teacher):
        '''
        :param ID:班级ID
        :param class_name:班级名称
        :param School:班级所属学校
        :param Course:班级关联课程
        :param Teacher:班级关联老师
        '''
        self.ID = ID
        self.Class_Name = class_name
        self.Class_School = School
        self.Class_Course = Course
        self.Class_Teacher = Teacher

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
        '''
        :param ID: 教师ID（唯一）
        :param teacher_name: 教师名称
        :param teacher_sex: 教师性别
        :param teacher_addr: 教师地址
        :param teacher_age: 教师年龄
        :param teacher_tel: 教师电话
        :param teacher_salary: 教师工资
        :param School: 教师所属学校
        '''
        self.ID =ID
        self.Teacher_name = teacher_name
        self.Teacher_sex = teacher_sex
        self.Teacher_addr = teacher_addr
        self.Teacher_age = teacher_age
        self.Teacher_tell = teacher_tel
        self.Teacher_salary = teacher_salary
        self.Teacher_School = School   #老师所属学校
        # self.Teach_Cour = Course   #老师所教科目

class Student():
    def __init__(self, ID, stu_name, stu_sex, stu_addr, stu_age, stu_tel):
        '''
        :param ID:学生ID
        :param stu_name:学生姓名
        :param stu_sex:学生性别
        :param stu_addr:学生地址
        :param stu_age:学生年龄
        :param stu_tel:学生电话
        :param School:学生所在学校
        :param Course:学生所学课程
        '''
        self.ID = ID
        self.Stu_name = stu_name
        self.Stu_sex = stu_sex
        self.Stu_addr = stu_addr
        self.Stu_age = stu_age
        self.Stu_tel = stu_tel
        self.Stu_school = School
        self.Stu_Cour = Course  #学生所学课程
# -*- coding:utf-8 -*-
#  Author:aling
from db_view import database_info,db_operator
from information_operator import search_infomation
import manage_master,style,main_master

class Add_info(object):

    def add_obj(obj_table):
        print()
        result = None
        if obj_table == 'school_manage':
            print('\n请输入以下内容：学校ID、学校名称、学校地址、服务电话')
            school_id = input('学校ID（唯一）：')
            school_name = input('学校名称：')
            school_addr = input('学校地址：')
            school_tel = input('服务电话：')
            add_school = database_info.School(school_id,school_name, school_addr, school_tel)
            result = db_operator.operator_db.add_obj_to_db(add_school, obj_table)

        elif obj_table == 'teacher_manage':
            print('\033[31;1m\n请先输入教师所属学校的ID，再输入教师的其他信息！\033[0m')
            school_id = input('请输入学校ID：')
            school_obj = search_infomation.Search_info.search_id_in_table(school_id, 'school_manage')
            if school_obj == 'fail':
                print('您输入的学校ID有误，请查询后再操作！')
                return main_master.manage_view
            else:
                print(school_obj.ID)
                print(school_obj.School_Name)
            print('\033[31;1m请输入以下内容：教师ID、教师姓名、性别、住址、年龄、联系电话、月薪\033[0m')
            teacher_id = input('教师ID：')
            teacher_name = input('教师姓名：')
            teacher_sex = input('性别：')
            teacher_addr = input('住址：')
            teacher_age = input('年龄：')
            teacher_tel = input('联系电话：')
            teacher_salary = input('月薪：')
            add_teacher = database_info.Teacher(teacher_id, teacher_name, teacher_sex, teacher_addr, teacher_age,
                                               teacher_tel, teacher_salary, school_obj)
            result = db_operator.operator_db.add_obj_to_db(add_teacher, obj_table)
        elif obj_table == 'course_manage':
            print('add_infomation:添加课程信息 line 42')
        elif obj_table == 'student_manage':
            print('请输入以下内容：学生ID、学生姓名、性别、住址、年龄、联系电话')
            stu_id = input('学生ID：')
            stu_name = input('学生姓名：')
            stu_sex = input('性别：')
            stu_addr = input('住址：')
            stu_age = input('年龄：')
            stu_tel = input('联系电话：')
            stu_balance = 0
            add_stu = database_info.Student(stu_id, stu_name, stu_sex, stu_addr, stu_age, stu_tel, stu_balance)
            result = db_operator.operator_db.add_obj_to_db(add_stu, obj_table)
        if result is not None:
            print('\033[31;1m此%s已存在,请检查后重新输入。\033[0m' % style.menu_dict[obj_table])
            print()
            manage_master.manage_info(obj_table)
        else:
            print('\033[31;1m添加成功!\033[0m')
            manage_master.manage_info(obj_table)

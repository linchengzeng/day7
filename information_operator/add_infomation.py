# -*- coding:utf-8 -*-
#  Author:aling
from db_view import database_info,db_operator
import manage_master

class Add_info(object):

    menu_dict = {
        'school_manage': '学校',
        'teacher_manage': '讲师',
        'student_manage': '学生'
    }

    def add_obj(obj_db):
        print()
        if obj_db == 'school_manage':
            print('请输入以下内容：学校ID、学校名称、学校地址、服务电话')
            school_id = input('学校ID（唯一）：')
            school_name = input('学校名称：')
            school_addr = input('学校地址：')
            school_tel = input('服务电话：')
            add_school = database_info.School(school_id,school_name, school_addr, school_tel)
            result = db_operator.operator_db.add_obj_to_db(add_school, obj_db)

        elif obj_db == 'teacher_manage':
            print('请输入以下内容：教师ID、教师姓名、性别、住址、年龄、联系电话')
            teacher_id = input()
            teacher_name = input()
            teacher_sex = input()
            teacher_addr = input()
            teacher_age = input()
            teacher_tel = input()
            teacher_salary = input()

        elif obj_db == 'student_manage':
            print('请输入以下内容：学生ID、学生姓名、性别、住址、年龄、联系电话')
            stu_id = input()
            stu_name = input()
            stu_sex = input()
            stu_addr = input()
            stu_age = input()
            stu_tel = input()
        if not result:
            print('\033[31;1m此%s已存在,请检查后重新输入。\033[0m'%Add_info.menu_dict[obj_db])
            print()

            manage_master.manage_info(obj_db)
        else:
            print('添加成功!')
            manage_master.manage_info(obj_db)

# -*- coding:utf-8 -*-
#  Author:aling
from db_view import database_info
from db_view import db_operator


def add_obj(object):
    if object == 'school_manage':
        print('请输入以下内容：学校名称、学校地址、服务电话')
        school_name = input('学校名称：')
        school_addr = input('学校地址：')
        school_tel = input('服务电话：')
        add_school = database_info.School(school_name, school_addr, school_tel)
        db_operator.add_obj(add_school)
    elif object == 'teacher_manage':
        print('请输入以下内容：学生姓名、性别、住址、年龄、联系电话')
        teacher_name = input()
        teacher_sex = input()
        teacher_addr = input()
        teacher_age = input()
        teacher_tel = input()
        teacher_salary = input()

    elif object == 'student_manage':
        print('请输入以下内容：学生姓名、性别、住址、年龄、联系电话')
        stu_name = input()
        stu_sex = input()
        stu_addr = input()
        stu_age = input()
        stu_tel = input()


def editor_obj(object):
    print('修改',object)

def dele_obj(object):
    print('删除', object)

def search_obj(object):
    print('查询', object)


menu_dict = {
    'school_manage':'学校',
    'teacher_manage':'讲师',
    'student_manage':'学生'
}

option_menu_desc = {
    '1：添加':'add_obj',
    '2：修改':'editor_obj',
    '3：删除':'dele_obj',
    '4：查询':'search_obj'
}

option_menu_dict = {
    '1':add_obj,
    '2':editor_obj,
    '3':dele_obj,
    '4':search_obj
}


def manage_info(user_select_menu):
    print('用户选择管理：%s管理'%menu_dict[user_select_menu])
    for sub_menu in option_menu_desc.keys():
        print('%s%s'%(sub_menu,menu_dict[user_select_menu]))
    option_select = input('\033[31;1m请选择您需要的操作>>：\033[0m')
    if option_select in option_menu_dict:
        option_menu_dict[option_select](user_select_menu)


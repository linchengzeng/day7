# -*- coding:utf-8 -*-
#  Author:aling
from information_operator import add_infomation,editor_infomation




def dele_obj(object):
    print('删除', object)

def search_obj(object):
    print('查询', object)

def last(object):
    print('返回上级操作')

menu_dict = {
    'school_manage':'学校',
    'teacher_manage':'讲师',
    'student_manage':'学生'
}

option_menu_desc = {
    '1：添加':'add_obj',
    '2：修改':'editor_obj',
    '3：删除':'dele_obj',
    '4：查询':'search_obj',
    '5：返回上级操作':'last'
}

option_menu_dict = {
    '1':add_infomation.Add_info.add_obj,
    '2':editor_infomation.Editor_info.editor_obj,
    '3':dele_obj,
    '4':search_obj,
    '5':last
}


def manage_info(user_select_menu):
    print()
    print('\033[30;1m您现在操作的是%s管理选项\033[0m'%menu_dict[user_select_menu])
    for sub_menu in option_menu_desc.keys():
        print('%s%s'%(sub_menu,menu_dict[user_select_menu]))
    print()
    option_select = input('\033[31;1m请选择您需要的操作>>：\033[0m')
    if option_select in option_menu_dict:
        option_menu_dict[option_select](user_select_menu)


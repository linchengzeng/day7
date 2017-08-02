# -*- coding:utf-8 -*-
#  Author:aling

menu = u'''
    1：学员视图
    2：讲师视图
    3：管理视图
    4：退出
'''

role_desc_dict = {
    'school_manage':'学校',
    'teacher_manage':'讲师',
    'student_manage':'学生'
}

menu_desc = u'''
   1：学校管理
   2：讲师管理
   3：学生管理
   4：返回上级菜单
   '''

option_menu_desc_dict = {
    '1：添加':'add_obj',
    '2：修改':'editor_obj',
    '3：删除':'dele_obj',
    '4：查询':'search_obj',
    '5：返回上级操作':'last'
}

menu_num_dict = {
        '1': 'school_manage',
        '2': 'teacher_manage',
        '3': 'student_manage',
        '4': 'logout'
    }

school_menu_desc = u'''
    1:学校名称
    2:学校地址
    3:联系电话
'''

school_attr = {
    '1':'School_Name',
    '2':'School_Addr',
    '3':'School_Tel'
}


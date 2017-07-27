# -*- coding:utf-8 -*-
#  Author:aling
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
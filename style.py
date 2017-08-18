# -*- coding:utf-8 -*-
#  Author:aling

import main_master

menu = u'''
    1：学员视图
    2：讲师视图
    3：管理视图
    4：退出
'''

user_view_menu_desc = u'''
    1：个人信息管理
    2：课程管理
'''

user_view_menu = {
    '1': 'u_info_manage',
    '2': 'c_info_manage',
}

menu_dict = {
        'school_manage': '学校',
        'classes_manage': '班级',
        'teacher_manage': '讲师',
        'course_manage': '课程',
        'student_manage': '学生',
    }

menu_desc = u'''
   1：学校管理
   2：班级管理
   3：讲师管理
   4：课程管理
   5：学生管理
   6：返回上级菜单
   '''

option_menu_desc_dict = {
    '1：添加': 'add_obj',
    '2：修改': 'editor_obj',
    '3：删除': 'dele_obj',
    '4：查询': 'search_obj',
    '5：返回上级操作': 'last'
}

menu_num_dict = {
        '1': 'school_manage',
        '2': 'classes_manage',
        '3': 'teacher_manage',
        '4': 'course_manage',
        '5': 'student_manage',
        '6': 'logout'
    }


school_attr = {
    '1': 'School_Name',
    '2': 'School_Addr',
    '3': 'School_Tel'
}

course_attr = {
    '1':'Course_Name',
    '2':'Course_Period',
    '3':'Course_Cost'
}

teacher_arrt = {
    '1': 'Teacher_name',
    '2': 'Teacher_sex',
    '3': 'Teacher_addr',
    '4': 'Teacher_age',
    '5': 'Teacher_tell',
    '6': 'Teacher_salary',
    '7': 'Teacher_School'
}

classes_arrt = {
    '1': 'Class_Name',
    '2': 'Class_School',
    '3': 'Class_Course',
    '4': 'Class_Teacher'
}
student_arrt = {
    '1': 'Stu_name',
    '2': 'Stu_sex',
    '3': 'Stu_addr',
    '4': 'Stu_age,',
    '5': 'Stu_tel',
    '6': 'Stu_school',
    '7': 'Stu_Class',
    '8': 'Stu_Balance'
}

school_menu_arrt = u'''
    1:学校名称
    2:学校地址
    3:联系电话
'''

course_menu_arrt = u'''
    1:课程名称
    2:课程周期
    3:课程费用
'''

teacher_menu_arrt = u'''
    1：教师名称
    2：教师性别
    3：教师地址
    4：教师年龄
    5：教师电话
    6：教师工资
    7：教师所属学校
'''

classes_arrt_menu = u'''
    1：班级名称
    2：班级所属学校
    3：班级所授课程
    4：班级任课老师
'''

student_arrt_menu = u'''
    1：学生姓名
    2：学生性别
    3：联系地址
    4：学生年龄
    5：联系电话
    6：所在学校
    7：所在班级
    8：余额
'''
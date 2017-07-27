# -*- coding:utf-8 -*-
#  Author:aling

import setting
from db_view import db_operator


BASE_PATH = setting.BASE_PATH

class Editor_info():

    menu_dict = {
        'school_manage': '学校',
        'teacher_manage': '讲师',
        'student_manage': '学生'
    }

    def editor_obj(obj_table):
        print('修改', Editor_info.menu_dict[obj_table])
        edit_obj_id = input('\033[31;1m请输入您需要修改的%s的ID>>：\033[0m'%Editor_info.menu_dict[obj_table])
        result = db_operator.operator_db.search_db(edit_obj_id,obj_table)
        if result == 'fail':
            print('无法找到此信息，请确认后重新修改！')
        else:
            for line in result:
                print('学校ID（唯一）：%s'%line.School_ID)
                print('学校名称：%s'%line.School_Name)
                print('学校地址：%s'%line.School_Addr)
                print('联系电话：%s'%line.School_Tel)
                print('*******************')
            input('请输入您需要修改的')


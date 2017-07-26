# -*- coding:utf-8 -*-
#  Author:aling

import setting

BASE_PATH = setting.BASE_PATH

class Editor_info():

    menu_dict = {
        'school_manage': '学校',
        'teacher_manage': '讲师',
        'student_manage': '学生'
    }

    def editor_obj(obj_val):
        print('修改', Editor_info.menu_dict[obj_val])
        edit_obj_id = input('\033[31;1m请输入您需要修改的%s的ID>>：\033[0m'%Editor_info.menu_dict[obj_val])

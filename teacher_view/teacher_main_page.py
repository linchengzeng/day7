# -*- coding:utf-8 -*-
#  Author:aling



from information_operator.update_obj_infomation import Uptate_info
from information_operator.edit_obj_infomation import Editor_info
from information_operator.add_infomation import Add_obj_info
from teacher_view.update_teach_course import Update_teach_course_info
import style,main_master
class Teacher_info_manage(object):

    def teacher_info_main_page(self,user_data, *args,**kwargs):
        user_menu = {
            '1': Teacher_info_manage.teacher_edit_pwd,
            '2': Teacher_info_manage.teacher_u_info_manage,
            '3': Teacher_info_manage.teacher_c_info_manage,
            '4': Teacher_info_manage.teacher_logout
        }
        while True:
            print(style.user_view_menu_desc)
            user_select_menu = input('\033[31;1m请选择您需要的操作>>：\033[0m')
            if user_select_menu in style.user_view_menu:
                user_menu[user_select_menu](self, user_data['account_data'], 'teacher_manage')
            else:
                print('您选择的不在我提供的服务范围内，请重新选择！')

    def teacher_edit_pwd(self, teacher_obj, db_table):
        old_pwd = input('\033[31;1m请输入您的原密码>>：\033[0m')
        new_pwd = input('\033[31;1m请输入您的新密码>>：\033[0m')
        # if teacher_obj.Teacher_pwd == old_pwd:
        update_obj = Uptate_info()
        result = update_obj.update_teacher_info(teacher_obj, teacher_obj.ID, 'Teacher_pwd', new_pwd, db_table)
        if result:
            print('\033[30;1m更新成功！\033[0m')

    # 更新用户信息
    def teacher_u_info_manage(self, user_data, db_table):
        edit_obj = Editor_info()
        result = edit_obj.edit_teacher_info(db_table, self)
        # 更新缓存中登录后的信息
        self['account_data'] = result
        return result

    # 更新教师授课信息
    def teacher_c_info_manage(self, user_data, db_table):
        print('teacher_main_page.py line 30')
        teacher_course_manage_menu = {
            '1': Teacher_info_manage.add_user_course,
            '2': Teacher_info_manage.search_user_course,
            '3': Teacher_info_manage.logout,
        }
        while True:
            print(style.teacher_course_menu_desc)
            user_course_operator = input('\033[31;1m请输入您需要的操作>>：\033[0m')
            # 用户课程操作
            if user_course_operator in style.user_course_menu:
                result = teacher_course_manage_menu[user_course_operator](self, user_data, 'classes_manage')
            else:
                print('您的选择不在我们的服务范围，请重新选择！')
            return result

    # 添加课程信息
    def add_user_course(self, user_data, db_table, *args, **kwargs):
        print('teacher_main_page.py in line 61')
        print('\033[30;1m教师的课程添加即为班级的开设，请悉知！\033[0m')
        add_classes = Add_obj_info()
        add_classes.add_classes(db_table)

    # 修改课程信息
    def search_user_course(self, user_data, db_table, *args, **kwargs):
        print('teacher_main_page.py in line 64')
        print('\033[30;1m教师的课程修改即为班级的修改，请悉知！\033[0m')
        update_class_obj = Update_teach_course_info()
        update_class_obj.update_t_c_info(user_data)

    def logout(self, user_data, *args, **kwargs):
        return Teacher_info_manage.teacher_info_main_page(self, user_data, *args, **kwargs)

    def teacher_logout(self, user_data, db_table):
        main_master.user_data['account_data'] = None
        main_master.user_data['is_authenticated'] = False
        return main_master.main_page()





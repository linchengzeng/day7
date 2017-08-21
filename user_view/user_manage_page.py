# -*- coding:utf-8 -*-
#  Author:aling

from information_operator import edit_obj_infomation,update_obj_infomation
import style,main_master

class User_info_manage():

    def user_main_page(user_data, *args,**kwargs):

        user_menu = {
            '1': User_info_manage.edit_pwd,
            '2': User_info_manage.u_info_manage,
            '3': User_info_manage.c_info_manage,
            '4': User_info_manage.last
        }

        while True:
            print('\033[30;1m您现在所在的位置是：学生管理视图\033[0m')
            print(style.user_view_menu_desc)
            user_select_menu = input('\033[31;1m请选择您需要的操作>>：\033[0m')
            if user_select_menu in style.user_view_menu:
                result = user_menu[user_select_menu](user_data['account_data'], 'student_manage')
                user_data['account_data'] = result
            else:
                print('您选择的不在我提供的服务范围内，请重新选择！')

    def edit_pwd(self,obj_table):
        old_pwd = input('\033[31;1m请输入您的原密码>>：\033[0m')
        new_pwd = input('\033[31;1m请输入您的新密码>>：\033[0m')
        if self.Pwd == old_pwd:
            result = update_obj_infomation.uptate_info.update_student_obj(obj_table, 'Pwd', new_pwd, self)
        if result:
            print('\033[30;1m更新成功！\033[0m')

    # 个人信息修改
    def u_info_manage(self, obj_table):
        result = edit_obj_infomation.Editor_info.edit_student_obj(obj_table, self)
        return result

    # 课程管理修改
    def c_info_manage(self, obj_table):
        print('user_manage_page.py line 30')
        user_course = {
            '1': User_info_manage.add_user_course,
            '2': User_info_manage.search_user_course,
            '3': User_info_manage.last,
        }
        while True:
            print(style.user_course_menu_desc)
            user_course_operator = input('\033[31;1m请输入您需要的操作>>：\033[0m')
            if user_course_operator in style.user_course_menu:
                result = user_course[user_course_operator](self)
            else:
                print('您的选择不在我们的服务范围，请重新选择！')
            return result

    def add_user_course(self):
        pass

    def search_user_course(self):
        pass

    def last(self,obj_table):
        return main_master.main_page()




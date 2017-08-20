# -*- coding:utf-8 -*-
#  Author:aling

from information_operator import edit_obj_infomation
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
                result = user_menu[user_select_menu](user_data['account_data'],'student_manage')
                user_data['account_data'] = result
            else:
                print('您选择的不在我提供的服务范围内，请重新选择！')

    def edit_pwd(self):
        print(self.Pwd)

    def u_info_manage(self, obj_table):
        result = edit_obj_infomation.Editor_info.edit_student_obj(obj_table, self)
        return result



    def c_info_manage(self):
        print('user_manage_page.py line 30')

    def last(self,obj_table):
        return main_master.main_page()




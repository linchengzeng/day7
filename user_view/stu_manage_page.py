# -*- coding:utf-8 -*-
#  Author:aling

from information_operator.edit_obj_infomation import Editor_info
from information_operator.update_obj_infomation import Uptate_info
from information_operator.search_infomation import Search_info
import style,main_master

class User_info_manage(object):

    def user_main_page(self,user_data, *args,**kwargs):
        user_menu = {
            '1': User_info_manage.edit_pwd,
            '2': User_info_manage.u_info_manage,
            '3': User_info_manage.c_info_manage,
            '4': User_info_manage.logout
        }

        while True:
            print('\033[30;1m您现在所在的位置是：学生管理视图\033[0m')
            print(style.user_view_menu_desc)
            user_select_menu = input('\033[31;1m请选择您需要的操作>>：\033[0m')
            if user_select_menu in style.user_view_menu:
                user_menu[user_select_menu](user_data['account_data'], 'student_manage')
            else:
                print('您选择的不在我提供的服务范围内，请重新选择！')

    def edit_pwd(self,obj_table):
        old_pwd = input('\033[31;1m请输入您的原密码>>：\033[0m')
        new_pwd = input('\033[31;1m请输入您的新密码>>：\033[0m')
        if self.Pwd == old_pwd:
            update_obj = Uptate_info()
            result = update_obj.update_student_obj(obj_table, 'Pwd', new_pwd, self)
        if result:
            print('\033[30;1m更新成功！\033[0m')

    # 个人信息修改
    def u_info_manage(self, obj_table):
        edit_obj = Editor_info()
        result = edit_obj.edit_student_obj(obj_table, self)
        # 更新缓存中登录后的信息
        self['account_data'] = result
        return result

    # 课程管理修改
    def c_info_manage(self, obj_table):
        print('stu_manage_page.py line 30')
        user_course = {
            '1': User_info_manage.add_user_course,
            '2': User_info_manage.search_user_course,
            '3': User_info_manage.logout,
        }
        while True:
            print(style.user_course_menu_desc)
            user_course_operator = input('\033[31;1m请输入您需要的操作>>：\033[0m')
            # 用户课程操作
            if user_course_operator in style.user_course_menu:
                result = user_course[user_course_operator](self, 'user_course_manage', 'course_manage')
            else:
                print('您的选择不在我们的服务范围，请重新选择！')
            return result

    def add_user_course(self, db_table, buy_obj):
        print('\033[30;1m买课容易，学习不易，且学且珍惜！\033[0m')
        from information_operator import add_infomation
        add_infomation.Add_obj_info.add_buy_course(self, db_table, buy_obj)

    def search_user_course(self, db_table, *args, **kwargs):
        print('stu_manage_page.py line 62')
        search_obj = Search_info()
        search_user_buy_course_result = search_obj.search_all_obj(db_table)
        print('\033[30;1m您购买的课程如下\033[0m')
        for line in search_user_buy_course_result:
            if line[0].ID == self.ID:
                print('课程名称：%s' % line[1].Course_name)
                print('课程学时：%s' % line[1].Course_period)
                print('购买时间：%s' % line[2])
        return "stu_manage_page.py line 79"



    def logout(self, obj_table, *args, **kwargs):
        main_master.user_data['account_data'] = None
        main_master.user_data['is_authenticated'] = False
        return main_master.main_page()




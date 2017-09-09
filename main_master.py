# -*- coding:utf-8 -*-
#  Author:aling
import style
from information_operator.auth_info import Auth_user_info
from user_view.stu_manage_page import User_info_manage
from teacher_view.teacher_main_page import Teacher_info_manage
from user_view import manage_page

user_data = {
    'account_id': None,
    'is_authenticated': False,
    'account_data': None
}

# ##认证装饰器
def authentication(auth_val):
    def out_wapper(func):
        def wapper(*args,**kwargs):
            retry_count = 0
            user_auth = Auth_user_info()
            while user_data['is_authenticated'] is not True and retry_count < 3:
                uid = input('请输入您的ID>>：').strip()
                pwd = input('请输入您的密码>>：').strip()
                if auth_val == 'student_view':

                    auth_result = user_auth.auth_login_info(uid, pwd, 'student_manage')
                    if auth_result:
                        user_data['account_id'] = uid
                        user_data['is_authenticated'] = True
                        user_data['account_data'] = auth_result
                        print('欢迎\033[31;1m%s\033[0m回来' % user_data['account_data'].Stu_name)
                        func(args, kwargs)
                    else:
                        print('\033[30;1mID或密码错误，请重新输入!\033[0m')
                elif auth_val == 'teacher_view':
                    auth_result = user_auth.auth_login_info(uid, pwd, 'teacher_manage')
                    if auth_result:
                        user_data['account_id'] = uid
                        user_data['is_authenticated'] = True
                        user_data['account_data'] = auth_result
                        print('欢迎\033[31;1m%s\033[0m回来' % user_data['account_data'].Teacher_name)
                        func(args, kwargs)
                    else:
                        print('\033[30;1mID或密码错误，请重新输入!\033[0m')
                elif auth_val =='manage_view':
                    print('实现认证装饰manage_view')
                    func(args, kwargs)
                elif auth_val == 'classes_view':
                    print('实现认证装饰classes_view')
                    func(args, kwargs)
                retry_count += 1
            main_page(args, kwargs)
        return wapper
    return out_wapper

@authentication(auth_val  = 'student_view')
def student_view(*args,**kwargs):
    user_info_page = User_info_manage()
    user_info_page.user_main_page(user_data, args, kwargs)


@authentication(auth_val = 'teacher_view')
def teacher_view(*args,**kwargs):
    teacher_page = Teacher_info_manage()
    teacher_page.teacher_info_main_page(user_data, args, kwargs)

'''
管理视图函数
'''
@authentication(auth_val = 'manage_view')
def manage_view(self, *args,**kwargs):
    while True:
        print('\033[30;1m\n您现在所在位置：管理视图\033[0m')
        print(style.menu_desc)
        user_select_menu = input('\033[31;1m请输入您需要进入的管理界面>>：\033[0m')
        if user_select_menu in style.menu_num_dict:
            if user_select_menu == '6':
                return main_page()
            manage_page.manage_info(self, style.menu_num_dict[user_select_menu])

def logout():
    print('本次使用结束，欢迎您再次使用本系统!')
    exit()

def main_page(*args, **kwargs):
    print(style.menu)

    menu_dict = {
        '1': student_view,
        '2': teacher_view,
        '3': manage_view,
        '4': logout
    }
    user_select_menu = input('\033[31;1m请输入您需要进入的视图>>:\033[0m')
    if user_select_menu in menu_dict:
        menu_dict[user_select_menu]()
    else:
        print('您选择的不在我提供的服务范围内，请重新选择！')
        return main_page(args,**kwargs)


# -*- coding:utf-8 -*-
#  Author:aling
import style
from information_operator import auth_info
from user_view import user_manage_page, manage_page

user_data = {
    'account_id':None,
    'is_authenticated':False,
    'account_data':None
}

# ##认证装饰器
def authentication(auth_val):
    def out_wapper(func):
        def wapper(*args,**kwargs):
            retry_count = 0
            while user_data['is_authenticated'] is not True and retry_count < 3:
                uid = input('请输入您的ID>>：').strip()
                pwd = input('请输入您的密码>>：').strip()
                if auth_val == 'student_view':
                    auth_result = auth_info.Auth_user_info.auth_login_info(uid, pwd, 'student_manage')
                    if auth_result:
                        user_data['account_id'] = uid
                        user_data['is_authenticated'] = True
                        user_data['account_data'] = auth_result
                        func(args, kwargs)
                    else:
                        print('\033[31;1m用户名或密码错误\033[0m')
                        retry_count += 1
                elif auth_val == 'teacher_view':
                    uid = input('请输入您的ID>>：')
                    pwd = input('请输入您的密码>>：')
                    auth_result = auth_info.Auth_user_info.auth_login_info(uid, pwd, 'teacher_manage')
                    if auth_info == 'Success':
                        func(args, kwargs)
                    else:
                        print('\033[31;1m用户名或密码错误\033[0m')
                        main_page(args, kwargs)
                elif auth_val =='manage_view':
                    print('实现认证装饰manage_view')
                    func(args, kwargs)
                elif auth_val == 'classes_view':
                    print('实现认证装饰classes_view')
                    func(args, kwargs)
            else:
                print('用户名或密码错误，请联系查询后再操作！')
            main_page(args, kwargs)
        return wapper
    return out_wapper

@authentication(auth_val  = 'student_view')
def student_view(*args,**kwargs):
    print('欢迎%s回来' % user_data['account_data'].Stu_name)
    while True:
        print('\033[30;1m您现在所在的位置是：学生管理视图\033[0m')
        print(style.user_view_menu_desc)
        user_select_menu = input('\033[31;1m请选择您需要的操作>>：\033[0m')
        if user_select_menu in style.user_view_menu:
            user_manage_page.User_info_manage.user_main_page(user_data['account_data'])
        else:
            print('您选择的不在我提供的服务范围内，请重新选择！')
            return student_view(args,kwargs)

@authentication(auth_val = 'teacher_view')
def teacher_view(*args,**kwargs):
    pass

# @authentication(auth_val = 'classes_view')
# def classes_manage(args,kwargs):
#     pass

'''
管理视图函数
'''
@authentication(auth_val = 'manage_view')
def manage_view(*args,**kwargs):
    while True:
        print('\033[30;1m\n您现在所在位置：管理视图\033[0m')
        print(style.menu_desc)
        user_select_menu = input('\033[31;1m请输入您需要进入的管理界面>>：\033[0m')
        if user_select_menu in style.menu_num_dict:
            if user_select_menu == '6':
                return main_page()
            manage_page.manage_info(style.menu_num_dict[user_select_menu])

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


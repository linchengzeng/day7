# -*- coding:utf-8 -*-
#  Author:aling
import manage_master,style

user_data = {
    'username':'',
    'is_authenticated':''
}

# ##认证装饰器
def authentication(auth_val):
    def out_wapper(func):
        def wapper(*args,**kwargs):
            if auth_val == 'student_view':
                print('实现认证装饰student_view')
                func(args, kwargs)
            elif auth_val == 'teacher_view':
                print('实现认证装饰teacher_view')
                func(args, kwargs)
            elif auth_val =='manage_view':
                print('实现认证装饰manage_view')
                func(args, kwargs)
            elif auth_val == 'classes_view':
                print('实现认证装饰classes_view')
                func(args, kwargs)
        return wapper
    return out_wapper

@authentication(auth_val  = 'student_view')
def student_view(*args,**kwargs):
    print('欢迎%s回来' % user_data['username'])
    while True:
        print('\033[30;1m您现在所在的位置是：学生管理视图\033[0m')
        print(style.user_view_menu_desc)
        user_select_menu = input('请选择您需要的操作>>：')
        if user_select_menu in style.user_view_menu:
            pass
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
            manage_master.manage_info(style.menu_num_dict[user_select_menu])

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


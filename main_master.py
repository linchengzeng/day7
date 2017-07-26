# -*- coding:utf-8 -*-
#  Author:aling
import manage_master

user_data = {
    'username':'',
    'is_authenticated':''
}



###认证装饰器
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
        return wapper
    return out_wapper




@authentication(auth_val  = 'student_view')
def student_view(args,kwargs):
    pass

@authentication(auth_val = 'teacher_view')
def teacher_view(args,kwargs):
    pass


'''
管理视图函数
'''
@authentication(auth_val = 'manage_view')
def manage_view(args,kwargs):
    menu = u'''
    1：学校管理
    2：讲师管理
    3：学生管理
    4：返回上级菜单
    '''
    menu_dict = {
        '1': 'school_manage',
        '2': 'teacher_manage',
        '3': 'student_manage',
        '4': logout
    }
    print(menu)
    user_select_menu = input('\033[31;1m请输入您需要进入的管理界面>>:\033[0m')
    if user_select_menu in menu_dict:
        manage_master.manage_info(menu_dict[user_select_menu])


def logout():
    print('本次使用结束，欢迎您再次使用本系统!')
    exit()

menu = u'''
    1：学员视图
    2：讲师视图
    3：管理视图
    4：退出
'''

menu_dict = {
    '1': student_view,
    '2': teacher_view,
    '3': manage_view,
    '4': logout
}

print(menu)

user_select_menu = input('\033[31;1m请输入您需要进入的视图>>:\033[0m')
if user_select_menu in menu_dict:
    menu_dict[user_select_menu]()
else:
    print('您选择的不在我提供的服务范围内，请重新选择！')

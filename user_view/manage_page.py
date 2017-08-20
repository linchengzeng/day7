# -*- coding:utf-8 -*-
#  Author:aling
from information_operator import add_infomation, edit_obj_infomation, dele_infomation, search_infomation
import style

def last(object):
    print('返回上级操作')

option_menu_dict = {
    '1': add_infomation.Add_info.add_obj,
    '2': edit_obj_infomation.Editor_info.edit_obj_info,
    '3': dele_infomation.Dele_obj_info.dele_id_in_obj,
    '4': search_infomation.Search_info.search_all_obj,
    '5': last
}


def manage_info(user_select_menu):
    '''
    :param user_select_menu: 用户要操作的表格
    :return:
    '''
    print()
    print('\033[30;1m您现在操作的是%s管理选项\033[0m'%style.menu_dict[user_select_menu])
    # 遍历选项卡（操作菜单）
    for sub_menu in style.option_menu_desc_dict.keys():
        print('%s%s'%(sub_menu,style.menu_dict[user_select_menu]))
    print()
    # 用户选的是添加、修改、删除、查询、返回上级等操作
    option_select = input('\033[31;1m请选择您需要的操作>>：\033[0m')
    if option_select in option_menu_dict:
        option_menu_dict[option_select](user_select_menu)

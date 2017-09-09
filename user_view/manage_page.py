# -*- coding:utf-8 -*-
#  Author:aling
from information_operator import add_infomation
from information_operator.edit_obj_infomation import Editor_info
from information_operator.dele_infomation import Dele_obj_info
from information_operator.search_infomation import Search_info
import style


class Main_page(object):
    def manage_info(self, user_select_menu):
        add_obj_info = add_infomation.Add_obj_info()
        edit_obj_info = Editor_info()
        del_obj_info = Dele_obj_info()
        sear_obj_info = Search_info()
        option_menu_dict = {
            '1': add_obj_info.add_obj,
            '2': edit_obj_info.edit_obj_info,
            '3': del_obj_info.dele_id_in_obj,
            '4': sear_obj_info.search_all_obj,
            '5': Main_page.last
        }
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
            option_menu_dict[option_select]( user_select_menu)


    def last(self):
        print('返回上级操作')

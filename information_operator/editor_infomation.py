# -*- coding:utf-8 -*-
#  Author:aling


from db_view import db_operator,database_info
from information_operator import public_search

import setting,style


BASE_PATH = setting.BASE_PATH

class Editor_info():
    # 更新学校名称
    def editor_school_name(obj,school_id,new_name,obj_table):
        #读取所有信息
        all_obj_info = public_search.Public_search_all.search_obj_all(obj_table)
        for line in all_obj_info:
            #判断是本次需要修改的信息ID时进行删除
            if school_id == line.School_ID:
                all_obj_info.remove(line)
        #新建一个新的对象，并将新的值写入新对象
        new_obj = database_info.School(obj.School_ID,new_name,obj.School_Addr,obj.School_Tel)
        #将更新后的对象添加到原来的数据库表中
        all_obj_info.append(new_obj)
        #数据持久化到文件中
        db_operator.operator_db.fulsh_db(all_obj_info,obj_table)

    # 更新学校地址
    def editor_school_addr(obj,school_id,new_addr,obj_table):
        obj.School_Addr = new_addr

    # 更新学校电话
    def editor_school_tel(self,new_tel):
        self.School_Tel = new_tel

    edit_school_attr ={
        '1': editor_school_name,
        '2': editor_school_addr,
        '3': editor_school_tel
    }

    # 更新学校信息
    def editor_school_obj(obj_table):
        print('修改%s操作'% style.role_desc_dict[obj_table])
        edit_obj_id = input('\033[31;1m请输入您需要修改的%s的ID>>：\033[0m'%style.role_desc_dict[obj_table])
        result = db_operator.operator_db.search_id_in_db(edit_obj_id, obj_table)
        if result == 'fail':
            print('无法找到此信息，请确认后重新修改！')
        else:
            for line in result:
                print('***修改前的原始信息***')
                print('学校ID（唯一）：%s'%line.School_ID)
                print('学校名称：%s'%line.School_Name)
                print('学校地址：%s'%line.School_Addr)
                print('联系电话：%s'%line.School_Tel)
                print('*******************')
                obj_info = line
            print(style.school_menu_desc)
            edit_attr = input('\033[31;1m请输入您需要修改的信息\033[0m')
            if edit_attr in style.school_attr:
                new_val = input('\033[31;1m请输入新值>>：\033[0m')
                Editor_info.edit_school_attr[edit_attr](obj_info,obj_info.School_ID,new_val,obj_table)



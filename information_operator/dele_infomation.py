# -*- coding:utf-8 -*-
#  Author:aling

from information_operator import public_search
from db_view import db_operator
import main_master, time


class Dele_school_info():

    def dele_school_obj(obj_table):
        # 用于标记对象存在数据库中
        del_obj_id_flag = True
        # 读取所有信息
        all_obj_info = public_search.Public_search_all.search_obj_all(obj_table)
        del_obj_id = input('\033[31;1m请输入您要删除的学校ID>>：\033[0m')
        try:
            for line in all_obj_info:
                # 判断是本次需要修改的信息ID时进行删除
                if del_obj_id == line.ID:
                    all_obj_info.remove(line)
                    # time.sleep(0.6)是装饰用，无任何实际意义
                    time.sleep(0.6)
                    print('\033[31;1m删除成功！\033[0m')
                    # 使用pickle方式将数据持久化到文件中
                    db_operator.operator_db.fulsh_db(all_obj_info, obj_table)
                    # time.sleep(0.6)是装饰用，无任何实际意义
                    time.sleep(0.6)
                    print('\033[31;1m数据更新成功！\033[0m')
                    del_obj_id_flag = False
                    break
            if del_obj_id_flag:
                print('\033[31;1m无法删除数据对象或对象不存在，请查询后再操作！\033[0m')
        except:
            print('\033[31;1m无法删除数据对象或对象不存在，请查询后再操作！\033[0m')
        return main_master.manage_view
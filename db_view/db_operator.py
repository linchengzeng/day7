# -*- coding:utf-8 -*-
#  Author:aling
import pickle

def add_obj(object):
    obj_in_db = False
    try:
        with open('./db_files/schools.db', 'rb+') as old_fp:
            old_text = pickle.load(old_fp)

        for line in old_text:
            #名称和地址一至表示同一所学校
            if object.School_Addr == line.School_Addr and object.School_Name == line.School_Name:
                obj_in_db = True
                print('数据对象已存在')
                break
        if not obj_in_db:
            with open('./db_files/schools.db','wb') as new_fp:
                old_text.append(object)
                pickle.dump(old_text,new_fp)
    except EOFError:
        print('这是空文件导致需要执行此处')
        with open('./db_files/schools.db', 'wb') as new_fp:
            pickle.dump([object], new_fp)

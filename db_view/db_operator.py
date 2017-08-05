# -*- coding:utf-8 -*-
#  Author:aling
import pickle,setting

BASE_PATH = setting.BASE_PATH

class operator_db(object):
    def add_obj_to_db(obj_val, obj_db_table):
        db_file = BASE_PATH + '\db_files\\' + obj_db_table + '.db'
        try:
            with open(db_file, 'rb+') as table_obj:
                old_text = pickle.load(table_obj)
            for line in old_text:
                #ID存在表示信息已存在
                if obj_val.ID == line.ID:
                    # print('数据对象已存在')
                    return False
            with open(db_file,'wb') as new_fp:
                old_text.append(obj_val)
                pickle.dump(old_text,new_fp)
            return True
        except (EOFError,FileNotFoundError):
            print('这是空文件导致需要执行此处')
            with open(db_file, 'wb') as new_fp:
                pickle.dump([obj_val], new_fp)
            return True

    def search_id_in_db(obj_id, obj_db_table):
        db_file = BASE_PATH + '\db_files\\' + obj_db_table + '.db'
        with open(db_file, 'rb+') as table_obj:
            table_info = pickle.load(table_obj)
        result = None
        for line in table_info:
            # ID存在表示信息已存在
            if obj_id == line.ID:
                print('查到数据对象')
                result = line
        if result is None:
            return 'fail'
        else:
            return result

    def search_all_table(obj_db_table):
        db_file = BASE_PATH + '\db_files\\' + obj_db_table + '.db'
        with open(db_file, 'rb+') as table_obj:
            table_info = pickle.load(table_obj)
        result = []
        for line in table_info:
            result.append(line)
        if len(result) != 0:
            return result
        else:
            return 'fail'

    def fulsh_db(obj_val_all, obj_db_table):
        db_file = BASE_PATH + '\db_files\\' + obj_db_table + '.db'
        with open(db_file, 'wb') as new_fp:
            pickle.dump(obj_val_all,new_fp)


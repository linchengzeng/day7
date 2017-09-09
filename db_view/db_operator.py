# -*- coding:utf-8 -*-
#  Author:aling
import pickle,setting

BASE_PATH = setting.BASE_PATH

class Operator_db(object):
    def add_obj_to_db(self, obj_val, obj_db_table):
        db_file = BASE_PATH + '\db_files\\' + obj_db_table + '.db'
        try:
            with open(db_file, 'rb+') as table_obj:
                old_text = pickle.load(table_obj)
            with open(db_file,'wb') as new_fp:
                old_text.append(obj_val)
                pickle.dump(old_text,new_fp)
            return 'Success'
        except (EOFError,FileNotFoundError):
            # print('这是空文件导致需要执行此处')
            with open(db_file, 'wb') as new_fp:
                pickle.dump([obj_val], new_fp)
            return 'Success'

    def search_id_in_db(self, obj_id, obj_db_table):
        db_file = BASE_PATH + '\db_files\\' + obj_db_table + '.db'
        try:
            with open(db_file, 'rb+') as table_obj:
                table_info = pickle.load(table_obj)
            result = None
            for line in table_info:
                # ID存在表示信息已存在
                if obj_id == line.ID:
                    # print('查到数据对象')
                    result = line
        except (EOFError,FileNotFoundError):
            # print('这是空文件导致需要执行此处')
            return None
        return result

    def search_all_obj(self, obj_db_table):
        db_file = BASE_PATH + '\db_files\\' + obj_db_table + '.db'
        try:
            with open(db_file, 'rb+') as table_obj:
                table_info = pickle.load(table_obj)
        except:
            return 'Fail'
        if len(table_info) != 0:
            return table_info
        else:
            return 'Fail'

    def fulsh_db(self, obj_val_all, obj_db_table):
        db_file = BASE_PATH + '\db_files\\' + obj_db_table + '.db'
        with open(db_file, 'wb') as new_fp:
            pickle.dump(obj_val_all,new_fp)



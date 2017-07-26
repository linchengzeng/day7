# -*- coding:utf-8 -*-
#  Author:aling
import pickle,setting

BASE_PATH = setting.BASE_PATH

class operator_db(object):
    def add_obj(obj_val,obj_db):
        db_file = BASE_PATH + '\db_files\\' + obj_db + '.db'
        try:
            with open(db_file, 'rb+') as old_fp:
                old_text = pickle.load(old_fp)
            for line in old_text:
                #名称和地址一至表示同一所学校
                if obj_val.School_Addr == line.School_Addr and obj_val.School_Name == line.School_Name:
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
        # except FileNotFoundError:
        #     print('这是数据库文件不存在导致需要执行此处')
        #     with open(db_file, 'wb') as new_fp:
        #         pickle.dump([obj_val], new_fp)
        #     return True

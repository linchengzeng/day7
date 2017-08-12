# -*- coding:utf-8 -*-
#  Author:aling
import setting,pickle

BASE_PATH = setting.BASE_PATH

class Public_search_all():

    def search_obj_all(obj_in_table):
        db_file = BASE_PATH + '\db_files\\' + obj_in_table + '.db'
        with open(db_file, 'rb+') as table_obj:
            old_text = pickle.load(table_obj)
        return old_text
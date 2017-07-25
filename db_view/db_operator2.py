# -*- coding:utf-8 -*-
#  Author:aling
import pickle

def add_obj(object):
    line_info = False
    data_obj = [object]

    try:
        with open('./db_files/temp.file', 'wb+') as tp:
            pickle.dump(data_obj, tp)
            tp.write(b'\n')

        with open('./db_files/schools.db', 'rb+') as fp, \
                open('./db_files/temp.file', 'rb+') as tp:
            print(tp.readlines())
            print(fp.readlines())
            if tp.readlines() in fp.readlines():
                line_info = True
                print('您添加的信息已存在')
            else:
                with open('./db_files/schools.db', 'ab+') as fp:
                    pickle.dump(data_obj, fp)
                    fp.write(b'\n')
    except EOFError:
        if not line_info:
            print('空文件')
            with open('./db_files/schools.db', 'ab+') as fp:
                pickle.dump(data_obj, fp)
                fp.write(b'\n')


# -*- coding:utf-8 -*-
#  Author:aling
import setting
from db_view import db_operator
BASE_FILE = setting.BASE_PATH

class Search_info():

    def search_obj(obj_id,obj_db_table):
        '''
        :param obj_id:数据ID
        :param obj_db_table:表名
        :return:
        '''
        sql = 'select * from ' + obj_db_table + 'where School_ID = ' + obj_id
        print(sql)
        result = db_operator.operator_db.search_id_in_db(obj_id, obj_db_table)
        print(result)



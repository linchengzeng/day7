# -*- coding:utf-8 -*-
#  Author:aling
import setting
from db_view import db_operator
BASE_FILE = setting.BASE_PATH

class Search_info():

    def search_obj_info(obj_id,obj_db_table):
        '''
        :param obj_id:数据ID
        :param obj_db_table:表名
        :return:
        '''
        sql = 'select * from ' + obj_db_table + 'where School_ID = ' + obj_id
        print(sql)
        result = db_operator.operator_db.search_id_in_db(sql)
        print(result)


    def search_all_obj(obj_db_table):
        '''
        :param obj_id:数据ID
        :param obj_db_table:表名
        :return:
        '''
        obj_list = db_operator.operator_db.search_all_table(obj_db_table)
        if obj_list == 'fail':
            print('查谗失败或数据为空！请联系管理员！')
        else:
            for obj_info in obj_list:
                print(obj_info)

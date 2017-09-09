# -*- coding:utf-8 -*-
#  Author:aling
from db_view.db_operator import Operator_db
import setting

BASE_PATH = setting.BASE_PATH

class Auth_user_info(object):

    def auth_login_info(self, user_id, user_pwd, obj_in_table):
        search_obj = Operator_db()
        search_result = search_obj.search_id_in_db(user_id, obj_in_table)
        if search_result:
            if obj_in_table == 'studeng_manage':
                if search_result.Pwd == user_pwd:
                    return search_result
            elif obj_in_table == 'teacher_manage':
                if search_result.Teacher_pwd == None:
                    return search_result
        else:
            print('\033[31;1m用户ID或密码错误\033[0m')
            return None

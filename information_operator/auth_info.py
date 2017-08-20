# -*- coding:utf-8 -*-
#  Author:aling
from db_view import db_operator
import setting

BASE_PATH = setting.BASE_PATH

class Auth_user_info():

    def auth_login_info(user_id, user_pwd, obj_in_table):
        search_result = db_operator.operator_db.search_id_in_db(user_id, obj_in_table)
        if search_result:
            if search_result.Pwd == user_pwd:
                return search_result
        else:
            print('\033[31;1m用户ID或密码错误\033[0m')
            return None

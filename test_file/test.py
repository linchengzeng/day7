# -*- coding:utf-8 -*-
#  Author:aling
from  day7.db_view import db_operator
from  day7.db_view import database_info

school_obj = database_info.School('python学院','北京','010-84563333')
db_operator.add_obj(school_obj)
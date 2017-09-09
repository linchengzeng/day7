# -*- coding:utf-8 -*-
#  Author:aling
import pickle,os,sys

# 将项目目录加入系统环境变量
BASE_PATH = os.path.dirname(__file__)
SUPER_PATH = os.path.dirname(BASE_PATH)
sys.path.append(os.path.dirname(SUPER_PATH))
class Search_info(object):

    def search_all_obj(self,db_table):
        db_file = 'd:\\python\\demo\\day7\\db_files\\student_manage.db'
        with open(db_file, 'rb+') as table_obj:
            table_info = pickle.load(table_obj)
        for student_obj_info in table_info:
            print('************************')
            print('学生ID（唯一）：%s' % student_obj_info.ID)
            print('密码：%s' % student_obj_info.Pwd)
            print('姓名：%s' % student_obj_info.Stu_name)
            print('性别：%s' % student_obj_info.Stu_sex)
            print('住址：%s' % student_obj_info.Stu_addr)
            print('年龄：%s' % student_obj_info.Stu_age)
            print('联系电话：%s' % student_obj_info.Stu_tel)
            print('所在学校：%s' % student_obj_info.Stu_school.School_Name)
            print('所在班级：%s' % student_obj_info.Stu_Class.Class_Name)

abc = Search_info()
print(abc.search_all_obj('student_manage'))
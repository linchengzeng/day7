# -*- coding:utf-8 -*-
#  Author:aling
import setting
from db_view import db_operator
BASE_FILE = setting.BASE_PATH

class Search_info():

    def search_id_in_table(obj_id, obj_db_table):
        '''
        :param obj_id:数据ID
        :param obj_db_table:表名
        :return:
        '''
        # sql = 'select * from ' + obj_db_table + 'where School_ID = ' + obj_id
        # print(sql)
        result = db_operator.operator_db.search_id_in_db(obj_id, obj_db_table)
        return result


    def search_all_obj(db_table):
        '''
        :param obj_id:数据ID
        :param db_table:表名
        :return:
        '''
        search_obj_list = db_operator.operator_db.search_all_table(db_table)
        if search_obj_list == 'fail':
            print('查谗失败或数据为空！请联系管理员！')
        else:
            print('********查询结果*********')
            if db_table == 'school_manage':
                for school_obj_info in search_obj_list:
                    print('************************')
                    print('学校ID（唯一）：%s' % school_obj_info.ID)
                    print('学校名称：%s' % school_obj_info.School_Name)
                    print('学校地址：%s' % school_obj_info.School_Addr)
                    print('联系电话：%s' % school_obj_info.School_Tel)
            elif db_table == 'teacher_manage':
                for teacher_obj_info in search_obj_list:
                    print('************************')
                    print('教师ID（唯一）：%s' % teacher_obj_info.ID)
                    print('姓名：%s' % teacher_obj_info.Teacher_name)
                    print('性别：%s' % teacher_obj_info.Teacher_sex)
                    print('地址：%s' % teacher_obj_info.Teacher_addr)
                    print('年龄：%s' % teacher_obj_info.Teacher_age)
                    print('联系电话：%s' % teacher_obj_info.Teacher_tell)
                    print('工资：%s' % teacher_obj_info.Teacher_salary)
                    print('所属学校：%s' % teacher_obj_info.Teacher_School.School_Name)
            elif db_table == 'course_manage':
                for course_obj_info in search_obj_list:
                    print('************************')
                    print('课程ID（唯一）：%s' % course_obj_info.ID)
                    print('课程名称：%s' % course_obj_info.Course_name)
                    print('课程周期：%s' % course_obj_info.Course_period)
                    print('课程费用：%s' % course_obj_info.Course_cost)
                    print('开课地址：%s' % course_obj_info.Course_School.School_Addr)
                    print('联系电话：%s' % course_obj_info.Course_School.School_Tel)
            elif db_table == 'student_manage':
                for student_obj_info in search_obj_list:
                    print('************************')
                    print('学生ID（唯一）：' % student_obj_info.ID)
                    print('姓名：' % student_obj_info.Stu_name)
                    print('性别：' % student_obj_info.Stu_sex)
                    print('住址：' % student_obj_info.Stu_addr)
                    print('年龄：' % student_obj_info.Stu_age)
                    print('联系电话：' % student_obj_info.Stu_tel)
                    print('所在学校：' % student_obj_info.Stu_school.School_Name)
                    # print('所学课程：' % student_obj_info.Stu_Cour.)
            print('**********查询结束**********')
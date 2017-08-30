# -*- coding:utf-8 -*-
#  Author:aling
import setting
from db_view import db_operator
BASE_FILE = setting.BASE_PATH

class Search_info():

    def search_all_obj(db_table):
        '''
        :param obj_id:数据ID
        :param db_table:表名
        :return:
        '''
        search_obj_list = db_operator.operator_db.search_all_obj(db_table)
        if search_obj_list == 'Fail':
            print('查询失败或数据为空！请联系管理员！')
        else:
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
                    print('学生ID（唯一）：%s' % student_obj_info.ID)
                    print('姓名：%s' % student_obj_info.Stu_name)
                    print('性别：%s' % student_obj_info.Stu_sex)
                    print('住址：%s' % student_obj_info.Stu_addr)
                    print('年龄：%s' % student_obj_info.Stu_age)
                    print('联系电话：%s' % student_obj_info.Stu_tel)
                    print('所在学校：%s' % student_obj_info.Stu_school.School_Name)
                    print('所在班级：%s' % student_obj_info.Stu_Class.Class_Name)
            elif db_table == 'classes_manage':
                for classes_obj_info in search_obj_list:
                    print('************************')
                    print('班级ID（唯一）：%s' % classes_obj_info.ID)
                    print('班级名称：%s' % classes_obj_info.Class_Name)
                    print('所教课程：%s' % classes_obj_info.Class_Course.Course_name)
                    print('任课讲师：%s' % classes_obj_info.Class_Teacher.Teacher_name)
            elif db_table == 'user_course_manage':
                return search_obj_list

    def search_id(obj_id, obj_db_table):
        search_db_result = db_operator.operator_db.search_id_in_db(obj_id, obj_db_table)
        return search_db_result
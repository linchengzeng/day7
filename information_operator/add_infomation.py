# -*- coding:utf-8 -*-
#  Author:aling
from db_view import database_info,db_operator
from information_operator import search_infomation
import manage_master,style,main_master

class Add_info(object):

    def add_obj(obj_table):
        print()
        result = None
        if obj_table == 'school_manage':
            result = Add_info.add_school_obj(obj_table)
        elif obj_table == 'teacher_manage':
            result = Add_info.add_teacher_obj(obj_table)
        elif obj_table == 'course_manage':
            result = Add_info.add_course_obj(obj_table)
        elif obj_table == 'student_manage':
            result = Add_info.add_student_obj(obj_table)
        elif obj_table == 'classes_manage':
            result = Add_info.add_classes(obj_table)
        if result == 'Fail':
            print('\033[31;1m此%s已存在,请检查后重新输入。 add_infomation.py line in 24\033[0m' % style.menu_dict[obj_table])
            print()
            manage_master.manage_info(obj_table)
        elif result == 'Success':
            print('\033[31;1m添加成功!\033[0m')
            manage_master.manage_info(obj_table)

    # 添加学校信息
    def add_school_obj(obj_table):
        print('\n请输入以下内容：学校ID、学校名称、学校地址、服务电话')
        school_id = input('学校ID（唯一）：')
        search_school_id_result = search_infomation.Search_info.search_id_in_table(school_id, obj_table)
        if search_school_id_result != 'Fail':
            print('\033[31;1m此学校ID已存在，请查询后再操作！\033[0m')
            return main_master.manage_view
        school_name = input('学校名称：')
        school_addr = input('学校地址：')
        school_tel = input('服务电话：')
        add_school = database_info.School(school_id, school_name, school_addr, school_tel)
        result = db_operator.operator_db.add_obj_to_db(add_school, obj_table)
        return result

    ###添加课程信息
    def add_course_obj(obj_table):
        print('add_infomation:添加课程信息 line 43')
        print('\033[30;1m\n请先输入课程所属\033[0m\033[31;1m学校的ID\033[0m\033[30;1m，再输入课程的其他信息！\033[0m')
        school_id = input('请输入学校ID：')
        school_obj = search_infomation.Search_info.search_id_in_table(school_id, 'school_manage')
        if school_obj == 'Fail':
            print('您输入的学校ID有误，请查询后再操作！')
            return main_master.manage_view
        else:
            print('您将在\033[31;1m%s\033[0m下添加课程信息' % school_obj.School_Name)
        print('请输入以下课程信息：课程ID、课程名称、课程周期、课程价格')
        course_id = input('课程ID(唯一)：')
        search_course_id_result = search_infomation.Search_info.search_id_in_table(course_id, obj_table)
        if search_course_id_result != 'Fail':
            print('\033[31;1m此课程ID已存在，请查询后再操作！\033[0m')
            return main_master.manage_view
        course_name = input('课程名称：')
        course_period = input('课程周期：')
        course_cost = input('课程价格：')
        # 通过学校添加课程
        course_obj = database_info.School.add_course(course_id, course_name, course_period, course_cost, school_obj)
        result = db_operator.operator_db.add_obj_to_db(course_obj, obj_table)
        return result

    # 添加班级信息
    def add_classes(obj_table):
        print('this is add_infomation.py in line 72')
        print('\n\033[30;1m请先输入班级所属\033[0m\033[31;1m学校的ID\033[0m\033[30;1m、'
              '授课\033[0m\033[31;1m教师的ID\033[0m\033[30;1m，再输入其他相关信息！\033[0m')
        school_id = input('请输入学校ID：')
        school_obj = search_infomation.Search_info.search_id_in_table(school_id, 'school_manage')
        if school_obj == 'Fail':
            print('您输入的学校ID有误，请查询后再操作！')
            return main_master.manage_view



    # 添加教师信息
    def add_teacher_obj(obj_table):
        print('\n\033[30;1m请先输入教师所属\033[0m\033[31;1m学校的ID\033[0m\033[30;1m，再输入教师的其他信息！\033[0m')
        school_id = input('请输入学校ID：')
        school_obj = search_infomation.Search_info.search_id_in_table(school_id, 'school_manage')
        if school_obj == 'Fail':
            print('您输入的学校ID有误，请查询后再操作！')
            return main_master.manage_view
        else:
            print(school_obj.School_Name)
        print('\033[31;1m请输入以下内容：教师ID、教师姓名、性别、住址、年龄、联系电话、月薪\033[0m')
        teacher_id = input('教师ID(唯一)：')
        search_teacher_id_result = search_infomation.Search_info.search_id_in_table(teacher_id, obj_table)
        if search_teacher_id_result != 'Fail':
            print('\033[31;1m此教师ID已存在，请查询后再操作！\033[0m')
            return main_master.manage_view
        teacher_name = input('教师姓名：')
        teacher_sex = input('性别：')
        teacher_addr = input('住址：')
        teacher_age = input('年龄：')
        teacher_tel = input('联系电话：')
        teacher_salary = input('月薪：')
        add_teacher = database_info.Teacher(teacher_id, teacher_name, teacher_sex, teacher_addr, teacher_age,
                                            teacher_tel, teacher_salary, school_obj)
        result = db_operator.operator_db.add_obj_to_db(add_teacher, obj_table)
        return result

    # 添加学生信息
    def add_student_obj(obj_table):
        print('请输入以下内容：学生ID、学生姓名、性别、住址、年龄、联系电话')
        stu_id = input('学生ID：')
        stu_name = input('学生姓名：')
        stu_sex = input('性别：')
        stu_addr = input('住址：')
        stu_age = input('年龄：')
        stu_tel = input('联系电话：')
        stu_balance = 0
        add_stu = database_info.Student(stu_id, stu_name, stu_sex, stu_addr, stu_age, stu_tel, stu_balance)
        result = db_operator.operator_db.add_obj_to_db(add_stu, obj_table)
        return result
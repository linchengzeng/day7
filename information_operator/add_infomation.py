# -*- coding:utf-8 -*-
#  Author:aling
import main_master, style, time, datetime
from db_view import database_info
from db_view.db_operator import Operator_db
from user_view.manage_page import Main_page
from information_operator.search_infomation import Search_info


class Add_obj_info(object):

    def add_obj(self, obj_table):
        result = None
        manage_main_page = Main_page()
        if obj_table == 'school_manage':
            result = Add_obj_info.add_school_obj(self, obj_table)
        elif obj_table == 'teacher_manage':
            result = Add_obj_info.add_teacher_obj(self, obj_table)
        elif obj_table == 'course_manage':
            result = Add_obj_info.add_course_obj(self, obj_table)
        elif obj_table == 'student_manage':
            result = Add_obj_info.add_student_obj(self, obj_table)
        elif obj_table == 'classes_manage':
            result = Add_obj_info.add_classes(self, obj_table)

        if result == 'Fail':
            print('\033[31;1m此%s已存在,请检查后重新输入。 \033[0m' % style.menu_dict[obj_table])
            print()
            return manage_main_page.manage_info(obj_table)
        elif result == 'Success':
            print('\033[31;1m添加成功!\033[0m')
            return manage_main_page.manage_info(obj_table)

    # 添加学校信息
    def add_school_obj(self, obj_table):
        search_obj = Search_info()
        data_operator = Operator_db()
        print('\n请输入以下内容：学校ID、学校名称、学校地址、服务'
              '电话')
        school_id = input('学校ID（唯一）：')
        search_school_id_result = search_obj.search_id(school_id, obj_table)
        if search_school_id_result is not None:
            print('\033[31;1m此学校ID已存在，请查询后再操作！\033[0m')
            return main_master.manage_view
        school_name = input('学校名称：')
        school_addr = input('学校地址：')
        school_tel = input('服务电话：')
        add_school = database_info.School(school_id, school_name, school_addr, school_tel)
        result = data_operator.add_obj_to_db(add_school, obj_table)
        return result

    ###添加课程信息
    def add_course_obj(self, obj_table):
        search_obj = Search_info()
        data_operator = Operator_db()
        # print('add_infomation:添加课程信息 line 43')
        print('\033[30;1m\n请先输入课程所属\033[0m\033[31;1m学校的ID\033[0m\033[30;1m，再输入课程的其他信息！\033[0m')
        school_id = input('请输入学校ID：')
        school_obj = search_obj.search_id(school_id, 'school_manage')
        if school_obj == 'Fail':
            print('您输入的学校ID有误，请查询后再操作！')
            return main_master.manage_view
        else:
            print('您将在\033[31;1m%s\033[0m下添加课程信息' % school_obj.School_Name)
        print('请输入以下课程信息：课程ID、课程名称、课程周期、课程价格')
        course_id = input('课程ID(唯一)：')
        search_course_id_result = search_obj.search_id(course_id, obj_table)
        if search_course_id_result:
            print('\033[31;1m此课程ID已存在，请查询后再操作！\033[0m')
            return main_master.manage_view
        course_name = input('课程名称：')
        course_period = input('课程周期：')
        course_cost = input('课程价格：')
        # 通过学校添加课程
        course_obj = database_info.School.add_course(course_id, course_name, course_period, course_cost, school_obj)
        result = data_operator.add_obj_to_db(course_obj, obj_table)
        return result

    # 添加班级信息
    def add_classes(self, obj_table):
        search_obj = Search_info()
        data_operator = Operator_db()
        # print('this is add_infomation.py in line 72')
        print('\n\033[30;1m请先输入班级所属\033[0m'
              '\033[31;1m学校的ID、授课教师的ID、所学课程ID\033[0m'
              '\033[30;1m，再输入其他相关信息！\033[0m')
        school_id = input('请输入学校ID：')
        school_obj = search_obj.search_id(school_id, 'school_manage')
        if school_obj is None:
            print('您输入的学校ID有误，请查询后再操作！')
            return main_master.manage_view
        teacher_id = input('请输入任课教师的ID：')
        teacher_obj = search_obj.search_id(teacher_id, 'teacher_manage')
        if teacher_obj is None:
            print('您输入的教师ID有误，请查询后再操作！')
            return main_master.manage_view
        course_id = input('请输入所教课程的ID：')
        course_obj = search_obj.search_id(course_id, 'course_manage')
        if course_obj is None:
            print('您输入的课程ID有误，请查询后再操作！')
            return main_master.manage_view
        print('您现在选择的学校是：%s，选择的任课教师是：%s，所授课程是：%s'
              % (school_obj.School_Name, teacher_obj.Teacher_name, course_obj.Course_name))
        print('请输入以下班级信息：班级ID（唯一）、班级名称')
        classes_id = input('班级ID（唯一）：')
        search_classes_id = search_obj.search_id(classes_id, 'classes_manage')
        if search_classes_id is not None:
            print('\033[30;1m您输入的班级ID已存在，请查询后再操作！\033[0m')
            return main_master.manage_view
        classes_name = input('班级名称：')
        classes_obj = database_info.School.add_classes(classes_id, classes_name, school_obj, course_obj, teacher_obj)
        result = data_operator.add_obj_to_db(classes_obj, 'classes_manage')
        return result

    # 添加教师信息
    def add_teacher_obj(self, obj_table):
        search_obj = Search_info()
        data_operator = Operator_db()
        print('\n\033[30;1m请先输入教师所属\033[0m\033[31;1m学校的ID\033[0m\033[30;1m，再输入教师的其他信息！\033[0m')
        school_id = input('请输入学校ID：')
        school_obj = search_obj.search_id(school_id, 'school_manage')
        if school_obj == 'Fail':
            print('您输入的学校ID有误，请查询后再操作！')
            return main_master.manage_view
        else:
            print(school_obj.School_Name)
        print('\033[31;1m请输入以下内容：教师ID、教师姓名、性别、住址、年龄、联系电话、月薪\033[0m')
        teacher_id = input('教师ID(唯一)：')
        search_teacher_id_result = search_obj.search_id(teacher_id, obj_table)
        if search_teacher_id_result is None:
            teacher_pwd = ''
            teacher_name = input('教师姓名：')
            teacher_sex = input('性别：')
            teacher_addr = input('住址：')
            teacher_age = input('年龄：')
            teacher_tel = input('联系电话：')
            super_manage = '0'
            teacher_salary = input('月薪：')
            add_teacher = database_info.Teacher(teacher_id, teacher_pwd, teacher_name, teacher_sex, teacher_addr, teacher_age,
                                                teacher_tel, super_manage, teacher_salary, school_obj)
            result = data_operator.add_obj_to_db(add_teacher, obj_table)
        else:
            print('\033[31;1m此教师ID已存在，请查询后再操作！\033[0m')
            return main_master.manage_view
        return result

    # 添加学生信息
    def add_student_obj(self,obj_table):
        search_obj = Search_info()
        data_operator = Operator_db()
        print('创建学员时需先选择学校、关联班级后再添加学员信息！')
        school_id = input('请输入学员所在学校：')
        school_obj = search_obj.search_id(school_id, 'school_manage')
        if school_obj == 'Fail':
            print('您输入的学校ID有误，请查询后再操作！')
            return main_master.manage_view
        classes_id = input('请输入班级ID：')
        classes_obj =search_obj.search_id(classes_id, 'classes_manage')
        if classes_obj == 'Fail':
            print()
        print('请输入以下内容：学员ID（唯一）、姓名、性别、住址、年龄、联系电话')
        stu_id = input('学员ID：')
        pwd = ''
        stu_name = input('姓名：')
        stu_sex = input('性别：')
        stu_addr = input('住址：')
        stu_age = input('年龄：')
        stu_tel = input('联系电话：')
        stu_balance = 0
        add_stu = database_info.Student(stu_id, pwd, stu_name, stu_sex, stu_addr, stu_age, stu_tel, school_obj,
                                        classes_obj, stu_balance)
        result = data_operator.add_obj_to_db(add_stu, obj_table)
        return result

    # 添加购买课程信息
    def add_buy_course(self, db_table, buy_obj):
        print('************目前所开课程有************')
        search_obj = Search_info()
        data_operator = Operator_db()
        search_obj.search_all_obj(buy_obj)
        user_buy_course_id = input('\033[31;1m请输入您需要购买的课程ID：\033[0m')
        # 获取课程对象
        course_obj = search_obj.search_id(user_buy_course_id, buy_obj)
        if course_obj:
            obj_val = [self, course_obj, datetime.date.fromtimestamp(time.time())]
            # print('add_infomation.py line 168')
            data_operator.add_obj_to_db(obj_val, db_table)
            print('\033[30;1m报名成功。\033[0m')
        else:
            print('\033[30;1m您输入的课程ID不存在，请查询后再操作！\033[0m')

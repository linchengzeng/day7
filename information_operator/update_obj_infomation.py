# -*- coding:utf-8 -*-
#  Author:aling


from db_view import database_info
from db_view.db_operator import Operator_db
import setting

BASE_PATH = setting.BASE_PATH

class Uptate_info(object):

    # 执行更新学校信息操作
    def update_school_info(self, obj, ID, obj_rank, new_val, obj_table):
        # 读取所有信息
        search_obj = Operator_db()
        all_obj_info = search_obj.search_all_obj(obj_table)
        for line in all_obj_info:
            # 判断是本次需要修改的信息ID时进行删除
            if ID == line.ID:
                all_obj_info.remove(line)
        # 新建一个新的对象，并将新的值写入新对象
        if obj_rank == 'School_Name':
            #改名称
            new_obj = database_info.School(obj.ID, new_val, obj.School_Addr, obj.School_Tel)
        elif obj_rank =='School_Addr':
            #改地址
            new_obj = database_info.School(obj.ID, obj.School_Name, new_val,  obj.School_Tel)
        elif obj_rank == 'School_Tel':
            #改电话
            new_obj = database_info.School(obj.ID, obj.School_Name, obj.School_Addr, new_val)
        #将更新后的对象添加到原来的数据库表中
        all_obj_info.append(new_obj)
        #数据持久化到文件中
        search_obj.fulsh_db(all_obj_info, obj_table)
        return new_obj

    # 执行更新课程信息
    def update_course_info(self, obj_info, rank_name, new_val, obj_table):
        search_obj = Operator_db()
        # 读取所有信息
        all_obj_info = search_obj.search_all_obj( obj_table)
        for line in all_obj_info:
            # 判断是本次需要修改的信息ID时进行删除
            if obj_info.ID == line.ID:
                all_obj_info.remove(line)
        # 新建一个新的对象，并将新的值写入新对象
        if rank_name == 'Course_Name':
            # 改课程名称
            new_obj = database_info.Course(obj_info.ID, new_val, obj_info.Course_period, obj_info.Course_cost, obj_info.Course_School)
        elif rank_name == 'Course_Period':
            # 改地址
            new_obj = database_info.Course(obj_info.ID, obj_info.Course_name, new_val, obj_info.Course_cost, obj_info.Course_School)
        elif rank_name == 'Course_Cost':
            # 改电话
            new_obj = database_info.Course(obj_info.ID, obj_info.Course_name, obj_info.Course_period, new_val, obj_info.Course_School)
        # 将更新后的对象添加到原来的数据库表中
        all_obj_info.append(new_obj)
        # 数据持久化到文件中
        search_obj.fulsh_db(all_obj_info, obj_table)
        return new_obj

    # 执行更新课程信息
    def updata_classes_info(self, obj_info, rank_name, new_val, obj_table):
        search_obj = Operator_db()
        # 读取所有信息
        all_obj_info = search_obj.search_all_obj(obj_table)
        for line in all_obj_info:
            # 判断是本次需要修改的信息ID时进行删除
            if obj_info.ID == line.ID:
                all_obj_info.remove(line)
        # 新建一个新的对象，并将新的值写入新对象
        if rank_name == 'Class_Name':
            # 改班级名称
            new_obj = database_info.Classes(obj_info.ID, new_val, obj_info.Class_School, obj_info.Class_Course,
                                           obj_info.Class_Teacher)
        elif rank_name == 'Class_School':
            # 改班级所属学校
            # new_obj = database_info.Classes(obj_info.ID, obj_info.Course_name, new_val, obj_info.Course_cost,
            #                                obj_info.Course_School)
            print('\033[30;1m暂未开放此功能！\033[0m')
            new_obj = obj_info
        elif rank_name == 'Course_Cost':
            # 改电话
            # new_obj = database_info.Classes(obj_info.ID, obj_info.Course_name, obj_info.Course_period, new_val,
            #                                obj_info.Course_School)
            print('\033[30;1m暂未开放此功能！\033[0m')
            new_obj = obj_info
        # 将更新后的对象添加到原来的数据库表中
        all_obj_info.append(new_obj)
        # 数据持久化到文件中
        search_obj.fulsh_db(all_obj_info, obj_table)
        return new_obj


    # 执行更新教师信息
    def update_teacher_info(self, obj_info, ID, rank_name, new_val, obj_table):
        search_obj = Operator_db()
        # 读取所有信息
        all_obj_info = search_obj.search_all_obj(obj_table)
        for line in all_obj_info:
            # 判断是本次需要修改的信息ID时进行删除
            if ID == line.ID:
                all_obj_info.remove(line)
        # 新建一个新的对象，并将新的值写入新对象
        if rank_name == 'Teacher_name':
            # 改教师名称
            new_obj = database_info.Teacher(obj_info.ID, obj_info.Teacher_pwd, new_val, obj_info.Teacher_sex,
                                            obj_info.Teacher_addr, obj_info.Teacher_age, obj_info.Teacher_tell,
                                            obj_info.Super_manage, obj_info.Teacher_salary,  obj_info.Teacher_School)
        elif rank_name == 'Teacher_sex':
            # 更改性别
            new_obj = database_info.Teacher(obj_info.ID, obj_info.Teacher_pwd, obj_info.Teacher_name, new_val,
                                            obj_info.Teacher_addr, obj_info.Teacher_age, obj_info.Teacher_tell,
                                            obj_info.Super_manage, obj_info.Teacher_salary, obj_info.Teacher_School)
        elif rank_name == 'Teacher_addr':
            # 改地址
            new_obj = database_info.Teacher(obj_info.ID, obj_info.Teacher_pwd, obj_info.Teacher_name,
                                            obj_info.Teacher_sex, new_val, obj_info.Teacher_age, obj_info.Teacher_tell,
                                            obj_info.Super_manage, obj_info.Teacher_salary,  obj_info.Teacher_School)
        elif rank_name == 'Teacher_age':
            # 改年龄
            new_obj = database_info.Teacher(obj_info.ID, obj_info.Teacher_pwd, obj_info.Teacher_name,
                                            obj_info.Teacher_sex,  obj_info.Teacher_addr, new_val, obj_info.Teacher_tell,
                                            obj_info.Super_manage, obj_info.Teacher_salary, obj_info.Teacher_School)
        elif rank_name == 'Teacher_tell':
            # 改电话
            new_obj = database_info.Teacher(obj_info.ID, obj_info.Teacher_pwd, obj_info.Teacher_name,
                                            obj_info.Teacher_sex, obj_info.Teacher_addr, obj_info.Teacher_age, new_val,
                                            obj_info.Super_manage, obj_info.Teacher_salary, obj_info.Teacher_School)
        elif rank_name == 'Super_manage':
            # 更改超级管理权限
            new_obj = database_info.Teacher(obj_info.ID, obj_info.Teacher_pwd, obj_info.Teacher_name,
                                            obj_info.Teacher_sex, obj_info.Teacher_addr, obj_info.Teacher_age,
                                            obj_info.Teacher_tell,new_val, obj_info.Teacher_salary, obj_info.Teacher_School)
        elif rank_name == 'Teacher_salary':
            # 改工资
            new_obj = database_info.Teacher(obj_info.ID, obj_info.Teacher_pwd, obj_info.Teacher_name,
                                            obj_info.Teacher_sex, obj_info.Teacher_addr, obj_info.Teacher_age,
                                            obj_info.Teacher_tell, obj_info.Super_manage, new_val, obj_info.Teacher_School)
        elif rank_name == 'Teach_School':
            # 改学校
            new_obj = database_info.Teacher(obj_info.ID, obj_info.Teacher_pwd, obj_info.Teacher_name, obj_info.Teacher_sex,
                                            obj_info.Teacher_addr, obj_info.Teacher_age, obj_info.Teacher_tell,
                                            obj_info.Super_manage, obj_info.Teacher_salary, new_val)
        elif rank_name == 'Teacher_pwd':
            # 改密码
            new_obj = database_info.Teacher(obj_info.ID,new_val,obj_info.Teacher_name, obj_info.Teacher_sex,
                                            obj_info.Teacher_addr, obj_info.Teacher_age, obj_info.Teacher_tell,
                                            obj_info.Super_manage, obj_info.Teacher_salary, obj_info.Teacher_School)
        elif rank_name == 'Teacher_Super_manage':
            # 改权限
            new_obj = database_info.Teacher(obj_info.ID, obj_info.Teacher_pwd, obj_info.Teacher_name,
                                            obj_info.Teacher_sex, obj_info.Teacher_addr, obj_info.Teacher_age,
                                            obj_info.Teacher_tell, new_val, obj_info.Teacher_salary,
                                            obj_info.Teacher_School)
        # 将更新后的对象添加到原来的数据库表中
        all_obj_info.append(new_obj)
        # 数据持久化到文件中
        search_obj.fulsh_db(all_obj_info, obj_table)
        return new_obj

    # 更新学生信息
    def update_student_obj(self, obj_table, rank_name, new_val, obj_info):
        search_obj = Operator_db()
        # 读取所有信息
        all_obj_info = search_obj.search_all_obj(obj_table)
        for line in all_obj_info:
            # 判断是本次需要修改的信息ID时进行删除
            if obj_info.ID == line.ID:
                all_obj_info.remove(line)
        if rank_name == 'Pwd':
            new_obj = database_info.Student(obj_info.ID, new_val, obj_info.Stu_name, obj_info.Stu_sex, obj_info.Stu_addr,
                                            obj_info.Stu_age, obj_info.Stu_tel,
                                            obj_info.Stu_school, obj_info.Stu_Class, obj_info.Stu_Balance)
        elif rank_name == 'Stu_name':
            new_obj = database_info.Student(obj_info.ID, obj_info.Pwd, new_val, obj_info.Stu_sex, obj_info.Stu_addr,
                                            obj_info.Stu_age, obj_info.Stu_tel,
                                            obj_info.Stu_school, obj_info.Stu_Class, obj_info.Stu_Balance)
        elif rank_name == 'Stu_sex':
            new_obj = database_info.Student(obj_info.ID, obj_info.Pwd, obj_info.Stu_name, new_val, obj_info.Stu_addr,
                                            obj_info.Stu_age, obj_info.Stu_tel,
                                            obj_info.Stu_school, obj_info.Stu_Class, obj_info.Stu_Balance)
        elif rank_name == 'Stu_addr':
            new_obj = database_info.Student(obj_info.ID, obj_info.Pwd, obj_info.Stu_name, obj_info.Stu_sex, new_val,
                                            obj_info.Stu_age, obj_info.Stu_tel,
                                            obj_info.Stu_school, obj_info.Stu_Class, obj_info.Stu_Balance)
        elif rank_name == 'Stu_age':
            new_obj = database_info.Student(obj_info.ID, obj_info.Pwd, obj_info.Stu_name, obj_info.Stu_sex,
                                            obj_info.Stu_addr, new_val, obj_info.Stu_tel,
                                            obj_info.Stu_school, obj_info.Stu_Class, obj_info.Stu_Balance)
        elif rank_name == 'Stu_tel':
            new_obj = database_info.Student(obj_info.ID, obj_info.Pwd, obj_info.Stu_name, obj_info.Stu_sex,
                                            obj_info.Stu_addr,obj_info.Stu_age, new_val,
                                            obj_info.Stu_school, obj_info.Stu_Class, obj_info.Stu_Balance)
        elif rank_name == 'Stu_school':
            new_obj = database_info.Student(obj_info.ID, obj_info.Pwd, obj_info.Stu_name, obj_info.Stu_sex,
                                            obj_info.Stu_addr, obj_info.Stu_age, obj_info.Stu_tel,
                                            new_val, obj_info.Stu_Class, obj_info.Stu_Balance)
        elif rank_name == 'Stu_Class':
            new_obj = database_info.Student(obj_info.ID, obj_info.Pwd, obj_info.Stu_name, obj_info.Stu_sex,
                                            obj_info.Stu_addr, obj_info.Stu_age, obj_info.Stu_tel, obj_info.stu_balance,
                                            obj_info.Stu_school, new_val, obj_info.Stu_Balance)
        elif rank_name == 'Stu_Balance':
            new_obj = database_info.Student(obj_info.ID, obj_info.Pwd, obj_info.Stu_name, obj_info.Stu_sex,
                                            obj_info.Stu_addr, obj_info.Stu_age, obj_info.Stu_tel,
                                            obj_info.Stu_school, obj_info.Stu_Class, new_val)
        # 将更新后的对象添加到原来的数据库表中
        all_obj_info.append(new_obj)
        # 数据持久化到文件中
        search_obj.fulsh_db(all_obj_info, obj_table)
        return new_obj
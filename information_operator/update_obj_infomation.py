# -*- coding:utf-8 -*-
#  Author:aling


from db_view import db_operator,database_info
from information_operator import auth_info

import setting,style,main_master,time

BASE_PATH = setting.BASE_PATH

class uptate_info():
    '''

    # 更新前后的学校信息
    def editor_school_obj(obj_table):
        print('修改%s操作'% style.menu_dict[obj_table])
        edit_obj_id = input('\033[31;1m请输入您需要修改的%s的ID>>：\033[0m'%style.menu_dict[obj_table])
        # 查询此ID是否存在
        obj_info = db_operator.operator_db.search_id_in_db(edit_obj_id, obj_table)
        if obj_info == 'Fail':
            print('无法找到此信息，请确认后重新修改！')
        else:
            # 输出原始信息
            print('学校ID（唯一）：%s'%obj_info.ID)
            print('学校名称：%s'%obj_info.School_Name)
            print('学校地址：%s'%obj_info.School_Addr)
            print('联系电话：%s'%obj_info.School_Tel)
            print('*******************')
            print(style.school_menu_arrt)
            update_attr = input('\033[31;1m请输入您需要修改的信息\033[0m')
            if update_attr in style.school_attr:
                new_val = input('\033[31;1m请输入新值>>：\033[0m')
                rank_val = style.school_attr[update_attr]
                try:
                    # 执行更新学校信息操作
                    new_obj_info = uptate_info.update_school_info(obj_table, obj_info.ID, rank_val, new_val, obj_info)
                    # 输出更新后的信息
                    print('》》》》更新完成，更新后的信息为》》》》')
                    print('学校ID（唯一）：%s' % new_obj_info.ID)
                    print('学校名称：%s' % new_obj_info.School_Name)
                    print('学校地址：%s' % new_obj_info.School_Addr)
                    print('联系电话：%s' % new_obj_info.School_Tel)
                    print('*******************')
                except:
                    print('系统异常，更新信息失败，请联系管理员！')
        return main_master.manage_view

    # 更新前后的课程信息
    def editor_course_obj(obj_table):
        print('修改%s操作'% style.menu_dict[obj_table])
        # 查询此ID是否存在
        edit_obj_id = input('\033[31;1m请输入您需要修改的%s的ID>>：\033[0m'%style.menu_dict[obj_table])
        obj_info = db_operator.operator_db.search_id_in_db(edit_obj_id, obj_table)
        if obj_info == 'Fail':
            print('无法找到此信息，请确认后重新修改！')
        else:
            # 输出原始信息
            print('课程ID（唯一）：%s'%obj_info.ID)
            print('课程名称：%s'%obj_info.Course_name)
            print('课程周期：%s'%obj_info.Course_period)
            print('课程费用：%s'%obj_info.Course_cost)
            print('********课程额外信息**********')
            print('开课地址：%s' % obj_info.Course_School.School_Addr)
            print('联系电话：%s' % obj_info.Course_School.School_Tel)
            print(style.course_menu_arrt)
            update_attr = input('\033[31;1m请输入您需要修改的信息\033[0m')
            if update_attr in style.course_attr:
                new_val = input('\033[31;1m请输入新值>>：\033[0m')
                rank_name = style.course_attr[update_attr]
                try:
                    # 执行更新操作
                    new_course_info = uptate_info.update_course_info(obj_table, obj_info.ID, rank_name, new_val,
                                                                     obj_info)
                    # 输出更新后的信息
                    print('》》》》更新完成，更新后的信息为》》》》')
                    print('课程ID（唯一）：%s' % new_course_info.ID)
                    print('课程名称：%s' % new_course_info.Course_name)
                    print('课程周期：%s' % new_course_info.Course_period)
                    print('课程费用：%s' % new_course_info.Course_cost)
                    print('********课程额外信息**********')
                    print('开课地址：%s' % new_course_info.Course_School.School_Addr)
                    print('联系电话：%s' % new_course_info.Course_School.School_Tel)
                except EOFError:
                    print('系统异常，更新信息失败，请联系管理员！')
        return main_master.manage_view

    # 更新前后的教师信息
    def edit_teacher_info(obj_table):
        print('\033[30;1m您现在操作的是修改%s信息\033[0m'% style.menu_dict[obj_table])
        edit_obj_id = input('\033[31;1m请输入您需要修改的%s的ID>>：\033[0m' % style.menu_dict[obj_table])
        # 查询此ID是否存在
        old_obj_info = db_operator.operator_db.search_id_in_db(edit_obj_id, obj_table)

        if old_obj_info == 'Fail':
            print('无法找到此信息，请确认后重新修改！')
        else:
            # 输出原始信息
            print('\033[30;1m******讲师原始信息******\033[0m')
            print('教师ID（唯一）：%s' % old_obj_info.ID)
            print('教师名称：%s' % old_obj_info.Teacher_name)
            print('教师性别：%s' % old_obj_info.Teacher_sex)
            print('教师地址：%s' % old_obj_info.Teacher_addr)
            print('教师年龄：%s' % old_obj_info.Teacher_age)
            print('教师电话：%s' % old_obj_info.Teacher_tell)
            print('教师工资：%s' % old_obj_info.Teacher_salary)
            print('教师所属学校：%s' % old_obj_info.Teacher_School.School_Name)
            print('*********************')
            print('\033[30;1m修改菜单选项\033[0m')
            print(style.teacher_menu_arrt)
            update_attr = input('\033[31;1m请选择您需要修改的信息>>：\033[0m')
            if update_attr in style.teacher_arrt:
                if update_attr == '7':
                    print('修改教师所属学校 update_obj_infomation.py line 126')
                    new_school_id = input('请输入新的学校ID')
                    new_val = db_operator.operator_db.search_id_in_db(new_school_id, 'school_manage')
                    if new_val == 'Fail':
                        print('\033[30;1m没有找到学校ID，请查询后再操作！\033[0m')
                        return main_master.manage_view
                else:
                    new_val = input('\033[31;1m请输入新值>>：\033[0m')
                    rank_name = style.teacher_arrt[update_attr]
                # 执行更新操作
                try:
                    new_teacher_info = uptate_info.update_teacher_info(old_obj_info, old_obj_info.ID, rank_name,
                                                                       new_val, obj_table)
                    # 输出更新后的信息
                    print('\033[30;1m更新中，请稍侯！！！\033[0m')
                    time.sleep(1)
                    print('\033[30;1m》》》》更新完成，更新后的信息为》》》》\033[0m')
                    print('教师ID（唯一）：%s' % new_teacher_info.ID)
                    print('教师名称：%s' % new_teacher_info.Teacher_name)
                    print('教师性别：%s' % new_teacher_info.Teacher_sex)
                    print('教师地址：%s' % new_teacher_info.Teacher_addr)
                    print('教师年龄：%s' % new_teacher_info.Teacher_age)
                    print('教师电话：%s' % new_teacher_info.Teacher_tell)
                    print('教师工资：%s' % new_teacher_info.Teacher_salary)
                    print('教师所属学校：%s' % new_teacher_info.Teacher_School.School_Name)
                except EOFError:
                    print('系统异常，更新信息失败，请联系管理员！')
        return main_master.manage_view

'''
    # 执行更新学校信息操作
    def update_school_info(obj_table, obj_rank, new_val, obj_info):
        # 读取所有信息
        all_obj_info = db_operator.operator_db.search_all_table(obj_table)
        for line in all_obj_info:
            # 判断是本次需要修改的信息ID时进行删除
            if obj_info.ID == line.ID:
                all_obj_info.remove(line)
        # 新建一个新的对象，并将新的值写入新对象
        if obj_rank == 'School_Name':
            # 改名称
            new_obj = database_info.School(obj_info.ID, new_val, obj_info.School_Addr, obj_info.School_Tel)
        elif obj_rank == 'School_Addr':
            # 改地址
            new_obj = database_info.School(obj_info.ID, obj_info.School_Name, new_val,  obj_info.School_Tel)
        elif obj_rank == 'School_Tel':
            # 改电话
            new_obj = database_info.School(obj_info.ID, obj_info.School_Name, obj_info.School_Addr, new_val)
        # 将更新后的对象添加到原来的数据库表中
        all_obj_info.append(new_obj)
        # 数据持久化到文件中
        db_operator.operator_db.fulsh_db(all_obj_info,obj_table)
        return new_obj

    # 执行更新课程信息
    def update_course_info(obj_table, rank_name, new_val, obj_info):
        # 读取所有信息
        all_obj_info = db_operator.operator_db.search_all_table(obj_table)
        for line in all_obj_info:
            # 判断是本次需要修改的信息ID时进行删除
            if obj_info.ID == line.ID:
                all_obj_info.remove(line)
        # 新建一个新的对象，并将新的值写入新对象
        if rank_name == 'Course_Name':
            # 改课程名称
            new_obj = database_info.Course(obj_info.ID, new_val, obj_info.Course_period, obj_info.Course_cost,
                                           obj_info.Course_School)
        elif rank_name == 'Course_Period':
            # 改地址
            new_obj = database_info.Course(obj_info.ID, obj_info.Course_name, new_val, obj_info.Course_cost,
                                           obj_info.Course_School)
        elif rank_name == 'Course_Cost':
            # 改电话
            new_obj = database_info.Course(obj_info.ID, obj_info.Course_name, obj_info.Course_period, new_val,
                                           obj_info.Course_School)
        # 将更新后的对象添加到原来的数据库表中
        all_obj_info.append(new_obj)
        # 数据持久化到文件中
        db_operator.operator_db.fulsh_db(all_obj_info, obj_table)
        return new_obj

    # 执行更新教师信息
    def update_teacher_info(obj_table, rank_name, new_val, obj_info):
        # 读取所有信息
        all_obj_info = db_operator.operator_db.search_all_table(obj_table)
        for line in all_obj_info:
            # 判断是本次需要修改的信息ID时进行删除
            if obj_info.ID == line.ID:
                all_obj_info.remove(line)
        # 新建一个新的对象，并将新的值写入新对象
        if rank_name == 'Teacher_name':
            # 改教师名称
            new_obj = database_info.Teacher(obj_info.ID,new_val, obj_info.Teacher_name, obj_info.Teacher_addr,
                                            obj_info.Teacher_age, obj_info.Teacher_tell, obj_info.Teacher_salary,
                                            obj_info.Teacher_School)
        elif rank_name == 'Teacher_sex':
            # 更改性别
            new_obj = database_info.Teacher(obj_info.ID, obj_info.Teacher_name,new_val, obj_info.Teacher_addr,
                                            obj_info.Teacher_age, obj_info.Teacher_tell, obj_info.Teacher_salary,
                                            obj_info.Teacher_School)
        elif rank_name == 'Teacher_addr':
            # 改地址
            new_obj = database_info.Teacher(obj_info.ID, obj_info.Teacher_name, obj_info.Teacher_sex,new_val,
                                            obj_info.Teacher_age, obj_info.Teacher_tell, obj_info.Teacher_salary,
                                            obj_info.Teacher_School)
        elif rank_name == 'Teacher_age':
            # 改年龄
            new_obj = database_info.Teacher(obj_info.ID, obj_info.Teacher_name, obj_info.Teacher_sex,
                                            obj_info.Teacher_addr, new_val, obj_info.Teacher_tell,
                                            obj_info.Teacher_salary, obj_info.Teacher_School)
        elif rank_name == 'Teacher_tell':
            # 改电话
            new_obj = database_info.Teacher(obj_info.ID, obj_info.Teacher_name, obj_info.Teacher_sex,
                                            obj_info.Teacher_addr, obj_info.Teacher_age,new_val, obj_info.Teacher_salary
                                            , obj_info.Teacher_School)
        elif rank_name == 'Teacher_salary':
            # 改工资
            new_obj = database_info.Teacher(obj_info.ID, obj_info.Teacher_name, obj_info.Teacher_sex,
                                            obj_info.Teacher_addr,obj_info.Teacher_age, obj_info.Teacher_tell,new_val,
                                            obj_info.Teacher_School)
        elif rank_name == 'Teacher_School':
            # 改学校
            new_obj = database_info.Teacher(obj_info.ID, obj_info.Teacher_name, obj_info.Teacher_sex,
                                            obj_info.Teacher_addr, obj_info.Teacher_age, obj_info.Teacher_tell,
                                            obj_info.Teacher_salary,new_val)
        # 将更新后的对象添加到原来的数据库表中
        all_obj_info.append(new_obj)
        # 数据持久化到文件中
        db_operator.operator_db.fulsh_db(all_obj_info, obj_table)
        return new_obj

    # 更新班级信息
    def updata_classes_info(obj_table, rank_name, new_val, obj_info):
        # 读取所有信息
        all_obj_info = db_operator.operator_db.search_all_table(obj_table)
        for line in all_obj_info:
            # 判断是本次需要修改的信息ID时进行删除
            if obj_info.ID == line.ID:
                all_obj_info.remove(line)
                # 新建一个新的对象，并将新的值写入新对象
        if rank_name == 'Class_Name':
            # 修改班级名称
            new_obj = database_info.Classes(obj_info.ID, new_val, obj_info.Class_School, obj_info.Class_Course,
                                            obj_info.Class_Teacher)
        elif rank_name == 'Class_School':
            # 修改班级所属学校
            new_obj = database_info.Classes(obj_info.ID, obj_info.Class_Name, new_val, obj_info.Class_Course,
                                            obj_info.Class_Teacher)
        elif rank_name == 'Class_Course':
            # 修改班级所授课程
            new_obj = database_info.Classes(obj_info.ID, obj_info.Class_Name, obj_info.Class_School, new_val,
                                            obj_info.Class_Teacher)
        elif rank_name == 'Class_Teacher':
            # 修改班级授课教师
            new_obj = database_info.Classes(obj_info.ID, obj_info.Class_Name, obj_info.Class_School,
                                            obj_info.Class_Course, new_val)
        # 将更新后的对象添加到原来的数据库表中
        all_obj_info.append(new_obj)
        # 数据持久化到文件中
        db_operator.operator_db.fulsh_db(all_obj_info, obj_table)
        return new_obj

    # 更新学生信息
    def update_student_obj(obj_table, rank_name, new_val, obj_info):
        # 读取所有信息
        all_obj_info = db_operator.operator_db.search_all_table(obj_table)
        for line in all_obj_info:
            if line.ID == obj_info.ID:
                all_obj_info.remove(line)
        if rank_name == 'Stu_name':
            new_obj = database_info.Student(obj_info.ID, new_val, obj_info.Stu_sex, obj_info.Stu_addr,
                                            obj_info.Stu_age, obj_info.Stu_tel, obj_info.Stu_school,
                                            obj_info.Stu_Class, obj_info.Stu_Balance)
        elif rank_name == 'Stu_sex':
            new_obj = database_info.Student(obj_info.ID, obj_info.Stu_name, new_val, obj_info.Stu_addr,
                                            obj_info.Stu_age, obj_info.Stu_tel,
                                            obj_info.Stu_school, obj_info.Stu_Class, obj_info.Stu_Balance)
        elif rank_name == 'Stu_addr':
            new_obj = database_info.Student(obj_info.ID, obj_info.Stu_name, obj_info.Stu_sex, new_val,
                                            obj_info.Stu_age, obj_info.Stu_tel,
                                            obj_info.Stu_school, obj_info.Stu_Class, obj_info.Stu_Balance)
        elif rank_name == 'Stu_age':
            new_obj = database_info.Student(obj_info.ID, obj_info.Stu_name, obj_info.Stu_sex, obj_info.Stu_addr,
                                            new_val, obj_info.Stu_tel,
                                            obj_info.Stu_school, obj_info.Stu_Class, obj_info.Stu_Balance)
        elif rank_name == 'Stu_tel':
            new_obj = database_info.Student(obj_info.ID, obj_info.Stu_name, obj_info.Stu_sex, obj_info.Stu_addr,
                                            obj_info.Stu_age, new_val,
                                            obj_info.Stu_school, obj_info.Stu_Class, obj_info.Stu_Balance)
        elif rank_name == 'Stu_school':
            new_obj = database_info.Student(obj_info.ID, obj_info.Stu_name, obj_info.Stu_sex, obj_info.Stu_addr,
                                            obj_info.Stu_age, obj_info.Stu_tel,
                                            new_val, obj_info.Stu_Class, obj_info.Stu_Balance)
        elif rank_name == 'Stu_Class':
            new_obj = database_info.Student(obj_info.ID, obj_info.Stu_name, obj_info.Stu_sex, obj_info.Stu_addr,
                                            obj_info.Stu_age, obj_info.Stu_tel,
                                            obj_info.Stu_school, new_val, obj_info.Stu_Balance)
        elif rank_name == 'Stu_Balance':
            new_obj = database_info.Student(obj_info.ID, obj_info.Stu_name, obj_info.Stu_sex, obj_info.Stu_addr,
                                            obj_info.Stu_age, obj_info.Stu_tel,
                                            obj_info.Stu_school, obj_info.Stu_Class, new_val)
        # 将更新后的对象添加到原来的数据库表中
        all_obj_info.append(new_obj)
        # 数据持久化到文件中
        db_operator.operator_db.fulsh_db(all_obj_info, obj_table)
        return new_obj


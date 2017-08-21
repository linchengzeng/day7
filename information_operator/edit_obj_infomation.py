# -*- coding:utf-8 -*-
#  Author:aling
# 更新前后的学校信息
from db_view import db_operator
from information_operator import update_obj_infomation
import style, main_master, time

class Editor_info():

    def edit_obj_info(obj_table):
        print('\033[30;1m您现在操作的是修改%s信息\033[0m' % style.menu_dict[obj_table])
        edit_obj_id = input('\033[31;1m请输入您需要修改的%s的ID>>：\033[0m' % style.menu_dict[obj_table])
        # 查询此ID是否存在
        old_obj_info = db_operator.operator_db.search_id_in_db(edit_obj_id, obj_table)
        if old_obj_info == 'Fail':
            print('无法找到此信息，请确认后重新修改！')
        else:
            if obj_table == 'school_manage':
                Editor_info.editor_school_obj(obj_table, old_obj_info)
            elif obj_table == 'teacher_manage':
                Editor_info.edit_teacher_info(obj_table, old_obj_info)
            elif obj_table == 'course_manage':
                Editor_info.editor_course_obj(obj_table, old_obj_info)
            elif obj_table == 'student_manage':
                Editor_info.edit_student_obj(obj_table, old_obj_info)
            elif obj_table == 'classes_manage':
                Editor_info.editor_classes_info(obj_table, old_obj_info)
        return main_master.manage_view

    def editor_school_obj(obj_table, obj_info):
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
                new_obj_info = update_obj_infomation.uptate_info.update_school_info(obj_table, rank_val, new_val, obj_info)
                # 输出更新后的信息
                print('》》》》更新完成，更新后的信息为》》》》')
                print('学校ID（唯一）：%s' % new_obj_info.ID)
                print('学校名称：%s' % new_obj_info.School_Name)
                print('学校地址：%s' % new_obj_info.School_Addr)
                print('联系电话：%s' % new_obj_info.School_Tel)
                print('*******************')
            except:
                print('系统异常，更新信息失败，请联系管理员！')

    # 更新前后的课程信息
    def editor_course_obj(obj_table, obj_info):
        # 输出原始信息
        print('课程ID（唯一）：%s'%obj_info.ID)
        print('课程名称：%s'%obj_info.Course_name)
        print('课程周期：%s'%obj_info.Course_period)
        print('课程费用：%s'%obj_info.Course_cost)
        print('********课程额外信息**********')
        print('开课地址：%s' % obj_info.Course_School.School_Addr)
        print('联系电话：%s' % obj_info.Course_School.School_Tel)
        print(style.course_menu_arrt_desc)
        update_attr = input('\033[31;1m请输入您需要修改的信息\033[0m')
        if update_attr in style.course_attr:
            new_val = input('\033[31;1m请输入新值>>：\033[0m')
            rank_name = style.course_attr[update_attr]
            try:
                # 执行更新操作
                new_course_info = update_obj_infomation.uptate_info.update_course_info(obj_table,
                                                                                       rank_name, new_val, obj_info)
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

    # 更新前后的教师信息
    def edit_teacher_info(obj_table, old_obj_info):
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
        print(style.teacher_menu_desc)
        update_attr = input('\033[31;1m请选择您需要修改的信息>>：\033[0m')
        if update_attr in style.teacher_arrt:
            if update_attr == '7':
                print('修改教师所属学校 update_obj_infomation.py line 120')
                new_school_id = input('请输入新的学校ID>>：')
                new_val = db_operator.operator_db.search_id_in_db(new_school_id, 'school_manage')
                if new_val == 'Fail':
                    print('\033[30;1m没有找到学校ID，请查询后再操作！\033[0m')
                    return None
            else:
                new_val = input('\033[31;1m请输入新值>>：\033[0m')
            # 执行更新操作
            try:
                rank_name = style.teacher_arrt[update_attr]
                print('\033[30;1m更新中，请稍侯！！！\033[0m')
                new_teacher_info = update_obj_infomation.uptate_info.update_teacher_info(obj_table, rank_name,
                                                                                         new_val, old_obj_info)
                # 输出更新后的信息
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

    def editor_classes_info(obj_table, old_obj_info):
        print('\033[30;1m您现在操作的是修改%s信息\033[0m' % style.menu_dict[obj_table])
        edit_obj_id = input('\033[31;1m请输入您需要修改的%s的ID>>：\033[0m' % style.menu_dict[obj_table])
        # 查询此ID是否存在
        old_obj_info = db_operator.operator_db.search_id_in_db(edit_obj_id, obj_table)

        if old_obj_info == 'Fail':
            print('无法找到此信息，请确认后重新修改！')
        else:
            # 输出原始信息
            print('\033[30;1m******班级原始信息******\033[0m')
            print('班级ID（唯一）：%s' % old_obj_info.ID)
            print('班级名称：%s' % old_obj_info.Class_Name)
            print('所教课程：%s' % old_obj_info.Class_Course.Course_name)
            print('任课讲师：%s' % old_obj_info.Class_Teacher.Teacher_name)
            print('班级所属学校：%s' % old_obj_info.Class_School.School_Name)
            print('*********************')
            print('\033[30;1m修改菜单选项\033[0m')
            print(style.classes_menu_desc)
            update_attr = input('\033[31;1m请选择您需要修改的信息>>：\033[0m')
            if update_attr in style.classes_arrt:
                # 修改班级名称
                if update_attr == '1':
                    new_val = input('请输入新的班级名称')
                # 修改班级所属学校ID
                elif update_attr == '2':
                    new_school_id = input('请输入新的学校ID>>：')
                    new_val = db_operator.operator_db.search_id_in_db(new_school_id, 'school_manage')
                    if new_val == 'Fail':
                        print('\033[30;1m没有找到新的学校ID，请查询后再操作！\033[0m')
                        return main_master.manage_view
                # 修改班级所学课程
                elif update_attr == '3':
                    new_course_id = input('请输入新的课程ID>>：')
                    new_val = db_operator.operator_db.search_id_in_db(new_course_id, 'course_manage')
                    if new_val == 'Fail':
                        print('\033[30;1m没有找到新的课程ID，请查询后再操作！\033[0m')
                        return main_master.manage_view
                # 修改班级授课教师
                elif update_attr == '4':
                    new_teacher_id = input('请输入新的授课教师ID>>：')
                    new_val = db_operator.operator_db.search_id_in_db(new_teacher_id, 'teacher_manage')
                    if new_val == 'Fail':
                        print('\033[30;1m没有找到新的授课教师ID，请查询后再操作！\033[0m')
                        return main_master.manage_view
                try:
                    rank_name = style.classes_arrt[update_attr]
                    print('\033[30;1m更新中，请稍侯！！！\033[0m')
                    new_classes_info = update_obj_infomation.uptate_info.updata_classes_info(obj_table, rank_name, new_val, old_obj_info)
                    # 输出更新后的信息
                    time.sleep(1)
                    print('\033[30;1m》》》》更新完成，更新后的信息为》》》》\033[0m')
                    print('班级ID（唯一）：%s' % new_classes_info.ID)
                    print('班级名称：%s' % new_classes_info.Class_Name)
                    print('所教课程：%s' % new_classes_info.Class_Course.Course_name)
                    print('任课讲师：%s' % new_classes_info.Class_Teacher.Teacher_name)
                    print('班级所属学校：%s' % new_classes_info.Class_School.School_Name)
                    print('*********************')
                except EOFError:
                    print('系统异常，更新信息失败，请联系管理员！')
        return main_master.manage_view
    # 更新学生信息
    def edit_student_obj(obj_table, old_obj_info):
         # 输出原始信息
         print('\033[30;1m******学生原始信息******\033[0m')
         print('学生ID（唯一)：%s' % old_obj_info.ID)
         print('姓名：%s' % old_obj_info.Stu_name)
         print('性别：%s' % old_obj_info.Stu_sex)
         print('地址：%s' % old_obj_info.Stu_addr)
         print('年龄：%s' % old_obj_info.Stu_age)
         print('电话：%s' % old_obj_info.Stu_tel)
         print('所在学校：%s' % old_obj_info.Stu_school.School_Name)
         print('所在班级：%s' % old_obj_info.Stu_Class.Class_Name)
         print('余额：%s' % old_obj_info.Stu_Balance)
         print('*********************')
         print(style.student_menu_desc)
         update_attr = input('\033[31;1m请选择您需要修改的信息>>：\033[0m')
         if update_attr in style.student_arrt:
             rank_name = style.student_arrt[update_attr]
             new_val = input('请输入新值>>：')
             if update_attr == '6':
                 new_val = db_operator.operator_db.search_id_in_db(new_val, 'school_manage')
             elif update_attr == '7':
                 new_val = db_operator.operator_db.search_id_in_db(new_val, 'classes_manage')
             # if new_val == 'Fail':
             #     print('无法找到对象！请查询后再操作！')
             #     return None
             try:
                 print('更新中，请稍侯！！！')
                 time.sleep(1)
                 new_student_obj = update_obj_infomation.uptate_info.update_student_obj(obj_table, rank_name, new_val, old_obj_info)
                 print('更新完成，以下为更新后的信息')
                 print('学生ID（唯一)：%s' % new_student_obj.ID)
                 print('姓名：%s' % new_student_obj.Stu_name)
                 print('性别：%s' % new_student_obj.Stu_sex)
                 print('地址：%s' % new_student_obj.Stu_addr)
                 print('年龄：%s' % new_student_obj.Stu_age)
                 print('电话：%s' % new_student_obj.Stu_tel)
                 print('所在学校：%s' % new_student_obj.Stu_school.School_Name)
                 print('所在班级：%s' % new_student_obj.Stu_Class.Class_Name)
                 print('余额：%s' % new_student_obj.Stu_Balance)
                 print('*********************')
                 return new_student_obj
             except:
                 print('更新出错，请联系管理员！！！')
                 return None


